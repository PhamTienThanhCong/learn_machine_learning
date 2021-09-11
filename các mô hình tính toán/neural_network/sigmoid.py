import numpy as np
import tensorflow as tf

x = np.array([0.0, 1.0, 50.0, 100.0])

# o = tf.math.sigmoid(3)

#dùng công thức
z1 = 1/(1 + np.exp(-x))

x = tf.constant([0.0, 1.0, 50.0, 100.0])
z2 = tf.math.sigmoid(x)

print(z1,z2)
