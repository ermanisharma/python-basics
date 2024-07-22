from PIL import Image
from numpy import asarray

# load the image and convert into

# numpy array

img = Image.open('Biden.png')

# asarray() class is used to convert

# PIL images into NumPy arrays

numpydata = asarray(img)

print('Biden image - In array - Using numpy :')

print(numpydata)

# <class 'numpy.ndarray'>

#print(type(numpydata))

#  shape

#print(numpydata.shape)