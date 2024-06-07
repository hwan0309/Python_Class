import os
import pathlib

import numpy as np
import keras
import tf
from keras import layers
from tensorflow import data as tf_data
import matplotlib.pyplot as plt

dataset_url = 'https://poticket.interpark.com/CampingBook/BookMain.asp'
data_dir = tf.get_file(origin=dataset_url,
                                   fname='easymac',
                                   untar=True)
data_dir = pathlib.Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
