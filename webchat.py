#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import itchat
'''群发带好友昵称的祝福词。'''


def qunfa(chatroomName, text):
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    if chatrooms is None:
        print("没有此群：" + chatroomName)
    else:
        room = itchat.update_chatroom(chatrooms[0]['UserName'])
        for i in room['MemberList']:
            i = itchat.search_friends(userName=i['UserName'])
            itchat.send(text %(i['DisplayName'] or i['NickName']), i['UserName'])
            time.sleep(.5)


itchat.auto_login()
qunfa('test', '祝 %s 小年快乐')