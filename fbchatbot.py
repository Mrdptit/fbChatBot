# -*- coding: UTF-8 -*-
#!/usr/bin/python
from fbchat import Client,log
from fbchat.models import *
import urllib
import json
import config
import data
import random
BlockUser = [];
class EchoBot(Client):
    
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        self.markAsDelivered(author_id, thread_id) 
        self.markAsRead(author_id) 
        print msg
        
        if author_id != self.uid:
                if message_object.text == "Chat With Dat":
                    BlockUser.append(thread_id)
                if message_object.text == "Chat With Bot":
                    BlockUser.remove(thread_id)
                if thread_id in BlockUser:
                    return
                if thread_id == "100004048426982" or thread_id == "100010657146335" or thread_id == "100009855423845":
                    return
                if (thread_type.name == "USER" or thread_id == "1397966703611326"):
                    if  message_object.text is not None:
                        print "text"
                        link  = 'http://api.simsimi.com/request.p?key=bb18d9b6-e162-4e26-820b-fe9657924d9e&lc=vn&ft=11.0&text='+message_object.text.encode('utf-8')
                        response = urllib.urlopen(link)
                        json1 = json.loads(response.read())
                        print json1
                        if json1["result"] == 100:
                            messtesst = json1["response"].encode('utf-8')
                        else:
                            i = random.randint(0,len(data.arrEmoji)-1)
                            messtesst = data.arrEmoji[i]
                            print data.arrEmoji
                        messtesst = messtesst.replace("sim","Dat")
                        messtesst = messtesst.replace("simsim","Dat")
                        messtesst = messtesst.replace("simi","Dat")            
                        messtesst = messtesst.replace("Simi","Dat")
                        messtesst = messtesst.replace("địt ","beep")
                        messtesst = messtesst.replace("diss","beep")
                        messtesst = messtesst.replace("điss","beep")
                        messtesst = messtesst.replace("lồn","beep")
                        messtesst = messtesst.replace("loz","beep")
                        messtesst = messtesst.replace("lồn","beep")
                        log.info("Message from {} in {} ({}) with: {}!".format(author_id, thread_id, thread_type.name, message_object.text.encode('utf-8')))
                        # print thread_type.name
                        self.sendMessage(messtesst, thread_id=thread_id, thread_type=thread_type)
                        pass
                    else:
                        dictemp = msg['delta']["attachments"][0]["mercury"]
                        try:
                            if dictemp["sticker_attachment"]:
                                print "stcker"
                                i = random.randint(0,len(data.arrstickerID)-1)
                                self.send(Message(sticker=Sticker(data.arrstickerID[i])), thread_id=thread_id, thread_type=thread_type)
                                return
                        except KeyError:
                            pass
                        try:
                            if dictemp["blob_attachment"]:
                                print "image"
                                i = random.randint(0,len(data.arrImageLink)-1)
                                client.sendLocalImage(data.arrImageLink[i], message=Message(text='hehe'), thread_id=thread_id, thread_type=thread_type)
                                return
                                pass
                        except KeyError:
                            pass
                        self.sendMessage(messtesst, thread_id=thread_id, thread_type=thread_type)
                        pass
            
client = EchoBot(config.email,config.password)
client.listen()