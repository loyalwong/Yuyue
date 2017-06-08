# coding=utf-8
import urllib.request
import datetime
from time import sleep
from random import random

if __name__ == "__main__":
    i = 0
    while i<=10000:
        try:
            urllib.request.urlretrieve("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()",datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg")
        except Exception:
            continue
        sleep(120*random())
        i=i+1
