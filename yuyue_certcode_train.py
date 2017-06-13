# coding=utf-8
from PIL import Image
import tensorflow as tf
from os import listdir
from os.path import isfile, join
import numpy as np
import math
import string
from time import sleep
from random import random
import binascii

def trainning_single_image_data_get(filename):
    im = Image.open(filename)
    imgry = im.convert('1')
    box1 = (65, 0, 78, 20)
    box2 = (87, 0, 100, 20)
    region1 = imgry.crop(box1)
    list_char1 = list(region1.getdata())
    x_train_char1 = []
    for each in list_char1:
        x_train_char1.append(each/255)
    return x_train_char1

def trainning_data_get():
    mypath = "./data/"
    filenames_image = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and '.jpg' in f)]
    file_label = list(open(join(mypath,'label'),'r'))
    x_train = []
    y_train = []
    for each_lable in file_label:
        for each_image in filenames_image:
            if each_lable[0:18] == each_image:
                if each_lable[22:23] != '':
                    x_train_char1 = trainning_single_image_data_get(join(mypath,each_image))
                    list_tmp1 = sorted(list(bin(int(math.pow(2,int(each_lable[22:23])-1))))[2:],reverse=False)
                    y_train_char1 =[int(list_tmp1[i]) for i in range(len(list_tmp1))]+[0 for _ in range(10-len(list_tmp1))]
                    y_train_char1 = list_tmp1.append()
                    x_train.append(x_train_char1)
                    y_train.append(y_train_char1)
    x_train_np = np.array(x_train)
    y_train_np = np.array(y_train)
    return x_train_np, y_train_np

def tensorflow_train(x_train,y_train):
    # Create the model
    x = tf.placeholder(tf.float32, [None, 260])
    W = tf.Variable(tf.zeros([260, 6]))
    b = tf.Variable(tf.zeros([6]))
    y = tf.matmul(x, W) + b

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 6])

    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
    cross_entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    # Train
    for _ in range(1000):
        batch_xs, batch_ys = x_train,y_train
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: x_train,
                                        y_: y_train}))
    
    print("trainning_data_get()")

if __name__ == "__main__":
    x_train, y_train = trainning_data_get()
    tensorflow_train(x_train, y_train)
    print("finished")