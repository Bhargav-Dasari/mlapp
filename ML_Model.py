import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import get_file, load_img, img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow import expand_dims
from tensorflow.keras.models import load_model
from tensorflow.nn import softmax

def reshape_and_normalize(images):

    (x,y,z) = images.shape
    images = images.reshape((x,y,z,1))
    images = images/np.max(images)

    return images

(training_images, training_labels), (test_images,test_labels) = tf.keras.datasets.mnist.load_data()

training_images = reshape_and_normalize(training_images)

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self,epoch, logs = {}):
        if logs['accuracy'] > 0.995 :
            self.model.stop_training = True
            print("\n Reached 99.5% accuracy so cancelling training!")

def convolutional_model():

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32,(3,3),activation = 'relu', input_shape = (28,28,1)),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128,activation='relu'),
        tf.keras.layers.Dense(10,activation= 'softmax')

    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

model = convolutional_model()

callbacks = myCallback()

history = model.fit(training_images, training_labels, epochs=6, validation_data = (test_images,test_labels), verbose=1)

model.save('mnist_model.keras')
