from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
user_id2 = os.environ["USER_ID2"]
template_id = os.environ["TEMPLATE_ID"]
template_water = os.environ["TEMPLATE_WATER"]


def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)

data = {}
res = wm.send_template(user_id, template_water,data)
res = wm.send_template(user_id2, template_water,data)
print(res)
