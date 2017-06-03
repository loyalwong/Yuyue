# coding=utf-8
import urllib.request
import datetime
from time import sleep
from random import random

itera = 1
while itera <= 10000:
    urllib.request.urlretrieve("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()",
                           datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg")
    sleep(120*random.random())
    itera = itera+1