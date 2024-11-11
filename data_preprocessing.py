# -*- coding: utf-8 -*-
"""data_preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ubl8oH3KV0bc7ucqsD7ZJveS7vvZztZa
"""

### loading the data
import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train.shape      ###size,dimension of channel

x_train = x_train.reshape(-1, 28, 28, 1)    ## reshaping to get number of channels also
x_test = x_test.reshape(-1, 28, 28, 1)

x_train.shape    ### 1 is the numbe rof cchannel,ie. greyscale image

x_train, y_train = np.array(x_train), np.array(y_train)
x_test, y_test = np.array(x_test), np.array(y_test)

"""Normalization"""

x_train, x_test = x_train / 255.0, x_test / 255.0

num_classes = 10
y_train_onehot = np.zeros((y_train.size, num_classes))
y_train_onehot[np.arange(y_train.size), y_train] = 1

y_test_onehot = np.zeros((y_test.size, num_classes))
y_test_onehot[np.arange(y_test.size), y_test] = 1

"""data augmentation"""

import random
from scipy.ndimage import rotate
from scipy.ndimage import shift

def random_rotation(images):
    return np.array([rotate(img.squeeze(), angle=random.uniform(-10, 10), reshape=False)[:, :, np.newaxis] for img in images])

def random_shift(images):
    return np.array([np.roll(np.roll(img.squeeze(), random.randint(-2, 2), axis=0), random.randint(-2, 2), axis=1)[:, :, np.newaxis] for img in images])

print(x_train_augmented.shape)  # Should be (60000, 28, 28, 1)
print(y_train_onehot.shape)