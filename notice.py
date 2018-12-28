#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import requests
# import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def send_message(message,robot_token):

    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot_token
    HEADERS = {
    "Content-Type": "application/json ;charset=utf-8 "
    }
    String_textMsg = {\
    "msgtype": "text",\
    "text": {"content": message}
    }

    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    return res.text

message = "各位注意~周五了！下下周三版本封需求了！"
message2 = "各位注意~周三了！请提测下周版本的内容！"
token01 = "8afe026f4cf367854da2f81959f8ad4dd55739ad5f01f9abf1355754a8d24ee1"

while True :
    nowTime = time.localtime(time.time())
    # print nowTime
    if (nowTime.tm_wday==4) & (nowTime.tm_hour == 15 ) & (nowTime.tm_min == 0 ) & (nowTime.tm_sec == 0) :
        send_message(message, token01)
        time.sleep(120)
    if (nowTime.tm_wday==2) & (nowTime.tm_hour == 15 ) & (nowTime.tm_min == 0 ) & (nowTime.tm_sec == 0) :
        send_message(message2, token01)
        time.sleep(120)

