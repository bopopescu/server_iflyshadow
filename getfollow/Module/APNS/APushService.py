# -*- coding: utf-8 -*-
__author__ = 'sharp'

# {"aps":{"alert":"测试信息","sound":"default"}}
# {"aps":{"alert":{"action-loc-key":"Open","body":"Hello, world!"},"badge":2,"sound":"default"}}

from apnsclient import *
# 可以使用Session对象来维持连接池
# device_token 86969fbcd6f0914166e3fded2f3fb38c5215e9547ccc6cef3199d3b42cbac8bf
session = Session()
con = session.get_connection("push_sandbox", cert_file="final_aps_development.pem")
# 发送推送和得到反馈
# def __init__(self, tokens, alert=None, badge=None, sound=None, content_available=None,
# expiry=None, payload=None, priority=DEFAULT_PRIORITY, extra=None,
# **extra_kwargs):
# message = Message(["86969fbcd6f0914166e3fded2f3fb38c5215e9547ccc6cef3199d3b42cbac8bf"],
# alert={"action-loc-key": "Open", "body": "Hello, world 测试信息!"}, badge=1,
# sound="default")
message = Message(["86969fbcd6f0914166e3fded2f3fb38c5215e9547ccc6cef3199d3b42cbac8bf"], payload='''
{
  "aps": {
    "alert": {
      "title": "Game Request",
      "body": "Acme message received from Johnny Appleseed",
      "action-loc-key": "VIEW",
      "actions": [
        {
          "id": "delete",
          "title": "Delete"
        },
        {
          "id": "reply-to",
          "loc-key": "REPLYTO",
          "loc-args": [
            "Jane"
          ]
        }
      ]
    },
    "badge": 1,
    "sound": "default"
  },
  "acme-account": "jane.appleseed@apple.com",
  "acme-message": "message123456"
}''')
# Send the message.
srv = APNs(con)
try:
    res = srv.send(message)
except:
    print "Can't connect to APNs, looks like network is down"
else:
    # Check failures. Check codes in APNs reference docs.
    for token, reason in res.failed.items():
        code, errmsg = reason
        # according to APNs protocol the token reported here
        # is garbage (invalid or empty), stop using and remove it.
        print "Device failed: {0}, reason: {1}".format(token, errmsg)

    # Check failures not related to devices.
    for code, errmsg in res.errors:
        print "Error: {}".format(errmsg)

    # Check if there are tokens that can be retried
    if res.needs_retry():
        # repeat with retry_message or reschedule your task
        retry_message = res.retry()
    print "sent success"