# coding=utf-8
import urllib.request
import datetime
from time import sleep
from random import random

if __name__ == "__main__":
    i = 0
    while i<=10000:
        try:
            url_image = urllib.request.urlopen("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()")
            file_image = open(datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg",'wb')
            file_image.write(url_image.read())
            file_image.close()
        except Exception:
            print("exception occurs")
        sleep(120*random())
        i=i+1
