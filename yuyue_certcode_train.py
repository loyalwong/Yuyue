# coding=utf-8
from PIL import Image
import numpy as np
import tensorflow as tf
from time import sleep
from random import random
import binascii

def trainning_single_image_data_get(filename):
    im = Image.open(filename)
    imgry = im.convert('1')
    box = (50, 0, 100, 20)
    region = imgry.crop(box)
    region.show()
    region.save('result.jpg')
    x_train = []
    y_train = []
    return x_train,y_train

def trainning_data_get():
    x_train, y_train = trainning_single_image_data_get('verifycode.jpg')


def tensorflow_train(x_train,y_train):
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    for _ in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    
    print("trainning_data_get()")

if __name__ == "__main__":
    trainning_single_image_data_get('verifycode.jpg')
    x_train, y_train = trainning_data_get()
    tensorflow_train(x_train, y_train)
    print("finished")