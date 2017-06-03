# coding=utf-8
import urllib.request
import datetime
from time import sleep
from random import random

while 1==1:
    urllib.request.urlretrieve("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()",
                           datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg")
    sleep(60*random.random())