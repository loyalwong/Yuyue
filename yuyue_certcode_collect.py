# coding=utf-8
import urllib.request
import datetime
import time
import random

if __name__ == "__main__":
    i = 0
    time_sleep = 0
    while i<=10000:
        i=i+1
        time.sleep(time_sleep+120*random.random())
        try:
            url_image = urllib.request.urlopen("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()")
            content_image = url_image.read()
            time_sleep = 0
        except Exception:
            time_sleep = time_sleep + 60*10 + 120*random.random()

        filename = "./data/" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        file_image = open(filename,'wb')
        file_image.write(content_image)
        file_image.close()

