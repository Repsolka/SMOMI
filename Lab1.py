from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import datetime
from tensorflow.keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()

model.add(layers.Flatten())
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))

model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
               metrics=["accuracy"])

Log_Dir="logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=Log_Dir, histogram_freq=1)

history = model.fit(train_images, train_labels, epochs=30,
                    validation_data=(test_images, test_labels), callbacks=[tensorboard_callback])

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)
