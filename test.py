# coding=utf-8
from PIL import Image
import numpy as np
import tensorflow as tf
from time import sleep
from random import random
import binascii
from os import listdir
from os.path import isfile, join

mypath = "./data/"

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for each in onlyfiles:
    im = Image.open(join(mypath,each))
    imgry = im.convert('1')
    box = (87, 0, 100, 20)
    box1 = (65, 0, 78, 20)
    box2 = (87, 0, 100, 20)
    region = imgry.crop(box)
    file_result = join(mypath+'test/',each)
    region.save(file_result)

print('finished')