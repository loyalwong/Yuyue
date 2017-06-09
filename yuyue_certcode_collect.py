# coding=utf-8
import urllib.request
import datetime
import time
import random

if __name__ == "__main__":
    i = 0
    while i<=10000:
        try:
            url_image = urllib.request.urlopen("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()")
            filename = "./data/" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            file_image = open(filename,'wb')
            file_image.write(url_image.read())
            file_image.close()
        except Exception:
            print("exception occurs")
        time.sleep(120*random.random())
        i=i+1
