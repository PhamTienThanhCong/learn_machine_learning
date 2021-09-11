import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.python.eager.context import graph_mode

print("load....")

mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

plt.subplot(2,2,1)
plt.title("Trước train")
plt.imshow(x_test[5],cmap='gray')

# chia model về dạng 0 tới 1 hay x_test/255
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# xây dụng model 
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)

model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict(x_test)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)

print(np.argmax(predictions[5]))
plt.subplot(2,2,2)
plt.title("sau train")
plt.imshow(x_test[5],cmap='gray')
plt.show()
