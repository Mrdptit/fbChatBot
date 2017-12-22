# -*- coding: UTF-8 -*-
#!/usr/bin/python
arrImageLink = [
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/2b775bcfe53f39cc88b820c532df1502.jpg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/download.jpeg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/med_1466487727_image.jpg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/1.jpeg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/Bb88N5lIUAA51Ux.jpg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/images.jpeg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/large.jpg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/pinterest2.jpeg',
    '/Users/dat/Documents/GitHub/fbChatBot/dataimage/23376322_1185590898251082_8043789806909211565_n.jpeg'
]
arrstickerID = [
    '499670976782072',
    '499671100115393',
    '499671060115397',
    '499670970115406',
    '499670943448742',
    '499671046782065',
    '499671003448736',
    '499671086782061',
    '499671206782049',
    '499671133448723',
    '499671140115389',
    '499671166782053',
    '499671073448729',
    '499670936782076',
    '499671153448721',
    '499671080115395',
    '499671106782059'

    
    ]
emoij = "😀 😃 😄 😁 😆 😅 😂 🤣 😊 😇 🙂 🙃 😉 😌 😍 😘 😗 😙 😚 😋 😜 😝 😛 🤑 🤗 🤓 😎 🤡 🤠😈 👿 👹 👺 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾 👐 🙌 👏 🙏 🤝 👍 👎 👊 ✊ 🤛 🤜 🤞 ✌️ 🤘 👌 👈 👉 👆 👇 ☝️ ✋ 🤚 🖐 🖖 👋 🤙 💪 🖕 ✍️ 🤳 💅 🖖 💄 💋 👄 👅 👂 👃 👣 👁 👀 🗣 👤 👥 ❤️ 💓 💓 💘 💙 💔 💕 💖 💝 😀 😁 😂 🤣 😃 😄 😅 😆 😙 😗 😘 😍 😎 😋 😊 😉 😚 🙂 🤗 🤔 😐 🤐 😮 😥 😣 🤗 😏 🙄 😶 😑 😯 😪 😫 😴 😌 😛 😜 🤐 😲 🤑 🙃 😕 😔 😓 😒 ☹️ 🙁 😖 😞 😕 🙃 🤑 😢 😰 🤥 🤡 😰 😭 😡 😵 😳"
arrEmoji = emoij.split()
def replace(content):
    content = content.replace("sim ","Dat")
    content = content.replace("simsim ","Dat")
    content = content.replace("simi ","Dat")
    content = content.replace("Simi ","Dat")
    content = content.replace("địt ","beep")
    content = content.replace("diss","beep")
    content = content.replace("điss","beep")
    content = content.replace("lồn ","beep")
    content = content.replace("loz","beep")
    content = content.replace("lồn","beep")
    return content
def check_type(data={}):
    data = data['delta']["attachments"][0]
    if "mercury" not in data:
        return "Messtext"
    else:
        data = data['delta']["attachments"][0]["mercury"]
        try:
            if "blob_attachment" in data:
                data = data["blob_attachment"]
                type = str(data["__typename"])
                return type
            if "extensible_attachment" in data:
                data = data["extensible_attachment"]
                return data["story_attachment"]["target"]["__typename"]
            pass
        except Exception as e:
            raise e