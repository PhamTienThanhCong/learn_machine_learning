import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure
from tensorflow.keras.datasets import mnist
import numpy as np
from sklearn import decomposition

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def f_hog(x):
    f_hog_lis = []
    for i in range(len(x)):
        f = hog(x_train[i], orientations=9, pixels_per_cell=(4,4),cells_per_block=(2,2), visualize=False)
        f_hog_lis.append(f)
    return f_hog_lis

f_hog_train = f_hog(x_train)
f_hog_test = f_hog(x_test)

e = 1e-9
imag_mean = np.mean(f_hog_train,axis = 0, keepdims=True)
imag_std = np.std(f_hog_train,axis = 0, keepdims=True)
f_hog_train -= imag_mean;   f_hog_train /= (imag_std + e)   
f_hog_test -= imag_mean;    f_hog_test /= (imag_std + e)

n_components = 10
pca = decomposition.PCA(n_components=n_components)
pca.fit(f_hog_train)

Z_train = pca.transform(f_hog_train)
Z_test = pca.transform(f_hog_test)

np.save('y_test', Z_test)
