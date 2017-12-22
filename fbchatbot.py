# -*- coding: UTF-8 -*-
#!/usr/bin/python
from fbchat import Client,log
from fbchat.models import *
import urllib
import json
import config
import data
import random
BlockUser = ["100004048426982","100010657146335","100009855423845","100004253857983"];
Success = ["1397966703611326","1668089616544648","1511863552230200"]
Key_stop = ['i love dat','-stop','i love you']
Key_restart = ['-restart','i hate you','i hate Dat']
GuileUser = [];
myId = "100007687420052"
guide = """
====================
<= Đây là Bot chat của Đạt =>
+Tạm dừng Bot chat: "I Love Dat" or "-stop"
+Khởi động lại Bot chat: "I Hate Dat" or "-restart"
+Hiện hướng dẫn chat: "-help" or "Help"
+Xoá thành viên  chat: "-rm" +Tag User
+Tra dự báo thời tiết chat : "-wt" + tên khu vực
"""
GIF_TYPE = "MessageAnimatedImage"
IMG_TYPE = "MessageImage"
URL_EXTENTION = "ExternalUrl"
FILE_TYPE = "MessageFile"
TEXT_TYPE = "Messtext"
FEMALE = "female_singular"
MALE = "male_singular"

class EchoBot(Client):
    
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        # self.markAsDelivered(author_id, thread_id)
        # self.markAsRead(author_id)
        # self.setTypingStatus
        print thread_type
        user = client.fetchUserInfo(author_id)[author_id]
        print user.gender
        if message_object.text is not None:
            print("{} send message to {}: {}".format(user.first_name.encode("utf-8"),thread_id,message_object.text.encode('utf-8')))
            if "-rm" in message_object.text and thread_type.name == "GROUP":
                print "ID"
                print message_object.mentions[0].thread_id
                uid = message_object.mentions[0].thread_id
                client.removeUserFromGroup(user_id = uid,thread_id=thread_id)
                return

            if message_object.text.lower() in Key_stop:
                if message_object.text == "-stop":
                    self.sendMessage(" Bot đã dừng", thread_id=thread_id, thread_type=thread_type)
                else:
                    if user.gender == FEMALE:
                        self.sendMessage("Yêu "+user.first_name.encode("utf-8")+" Ahihi", thread_id=thread_id, thread_type=thread_type)
                    else:
                        self.sendMessage(user.name.encode("utf-8")+" tao không gay nhé", thread_id=thread_id, thread_type=thread_type)
                BlockUser.append(thread_id)
                if thread_id in Success:
                    Success.remove(thread_id)
                return
            if message_object.text.lower() in Key_restart:
                if message_object.text == "-restart":
                    self.sendMessage("Đã khởi động lại bot", thread_id=thread_id, thread_type=thread_type)
                else:
                    self.sendMessage("Đạt ghét "+user.first_name.encode("utf-8")+" rồi đấy", thread_id=thread_id, thread_type=thread_type)
                if thread_id in BlockUser:
                    BlockUser.remove(thread_id)
                else:
                    Success.append(thread_id)
                return

        if author_id != self.uid:
            if  message_object.text is not None:
                #dự báo thời tiết
                if "-wt" in message_object.text:
                    WT = "====================="
                    message_object.text = message_object.text.replace("-wt","")
                    WT = WT+"\nBạn vừa tra cứu thời tiết ở "+message_object.text.encode("utf-8")
                    link  = 'https://api.trolyfacebook.com/thoitiet/?noidung={{%s}}'%(message_object.text.encode('utf-8'))
                    print link
                    response = urllib.urlopen(link)
                    json1 = json.loads(response.read())
                    arr = json1["messages"]
                    for i in arr:
                        if i != arr[0]:
                            WT = WT + "\n" +i['text'].encode('utf-8')
                    WT = WT +"\n====================="
                    print WT
                    self.sendMessage(WT, thread_id=thread_id, thread_type=thread_type)
                    return
                #remove member
            if thread_id in BlockUser:
                print "Block"
                return
            if (thread_type.name == "USER" or thread_id in Success):
                if  message_object.text is not None:
                    link  = 'http://api.simsimi.com/request.p?key=bb18d9b6-e162-4e26-820b-fe9657924d9e&lc=vn&ft=11.0&text='+message_object.text.encode('utf-8')
                    response = urllib.urlopen(link)
                    json1 = json.loads(response.read())
                    # print json1
                    if json1["result"] == 100:
                        messtesst = json1["response"].encode('utf-8')
                    else:
                        i = random.randint(0,len(data.arrEmoji)-1)
                        messtesst = data.arrEmoji[i]
                        print data.arrEmoji
                    messtesst = data.replace(messtesst)
                    if thread_id in GuileUser:
                        messtesst = messtesst
                    else:
                        messtesst = messtesst + guide
                        GuileUser.append(thread_id)
                    # log.info("Message from {} in {} ({}) with: {}!".format(author_id, thread_id, thread_type.name, message_object.text.encode('utf-8')))
                    # print thread_type.name
                    self.sendMessage(messtesst, thread_id=thread_id, thread_type=thread_type)
                    pass
                else:
                    type_mess = data.check_type(msg)
                    log.debug(type_mess)
                    try:
                        if message_object.sticker is not None:
                            # print "stcker"
                            i = random.randint(0,len(data.arrstickerID)-1)
                            self.send(Message(sticker=Sticker(data.arrstickerID[i])), thread_id=thread_id, thread_type=thread_type)
                            return
                    except KeyError:
                        pass
                    try:
                        if type_mess == IMG_TYPE:
                            # print "image"
                            i = random.randint(0,len(data.arrImageLink)-1)
                            client.sendLocalImage(data.arrImageLink[i], message=Message(text='hehe'), thread_id=thread_id, thread_type=thread_type)
                            return
                        elif type_mess == GIF_TYPE:
                            client.sendRemoteImage('https://media.giphy.com/media/lGAfVlN0gat4A/giphy.gif', message=Message(text='Heyyyyy!!!'), thread_id=thread_id, thread_type=thread_type)
                            return
                            pass
                        else:
                            client.sendRemoteImage('https://media.giphy.com/media/lGAfVlN0gat4A/giphy.gif', message=Message(text='Heyyyyy!!!'), thread_id=thread_id, thread_type=thread_type)
                            pass
                    except KeyError:
                        pass
                    self.sendMessage(messtesst, thread_id=thread_id, thread_type=thread_type)
                    pass
    def onColorChange(self, author_id, new_color, thread_id, thread_type, **kwargs):
        # if old_thread_id == thread_id and old_color != new_color:
        log.info("{} changed the thread color. It will be changed back".format(author_id))
        # self.changeThreadColor(old_color, thread_id=thread_id)

    def onEmojiChange(self, author_id, new_emoji, thread_id, thread_type, **kwargs):
        # if old_thread_id == thread_id and new_emoji != old_emoji:
        log.info("{} changed the thread emoji. It will be changed back".format(author_id))
        # self.changeThreadEmoji(old_emoji, thread_id=thread_id)

    def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
        log.info("{} got added".format(added_ids))
        
        # if added_ids != self.uid:
        for added_id in added_ids:
            user = client.fetchUserInfo(added_id)[added_id]
            if added_id != client.uid:
                client.sendMessage("Xin chào @{}".format(user.name.encode('utf-8')),thread_id=thread_id,thread_type=ThreadType.GROUP)
            else:
                client.sendMessage("Xin chào mọi người",thread_id=thread_id,thread_type=ThreadType.GROUP)
        

    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        # No point in trying to add ourself
        # if old_thread_id == thread_id and removed_id != self.uid and author_id != self.uid:
        log.info("{} got removed. They will be re-added".format(removed_id))
        # self.addUsersToGroup(removed_id, thread_id=thread_id)

    def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kwargs):
        # if old_thread_id == thread_id and old_title != new_title:
        log.info("{} changed the thread title. It will be changed back".format(author_id))
        # self.changeThreadTitle(old_title, thread_id=thread_id, thread_type=thread_type)

    def onNicknameChange(self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs):
        # if old_thread_id == thread_id and changed_for in old_nicknames and old_nicknames[changed_for] != new_nickname:
        log.info("{} changed {}'s' nickname. It will be changed back".format(author_id, changed_for))
            # self.changeNickname(old_nicknames[changed_for], changed_for, thread_id=thread_id, thread_type=thread_type)
# Change this to your group id
old_thread_id = '1234567890'

# Change these to match your liking
old_color = ThreadColor.MESSENGER_BLUE
old_emoji = '👍'
old_title = 'Old group chat name'
old_nicknames = {
    '12345678901': "User nr. 1's nickname",
    '12345678902': "User nr. 2's nickname",
    '12345678903': "User nr. 3's nickname",
    '12345678904': "User nr. 4's nickname"
}
client = EchoBot(config.email,config.password)
client.listen()
