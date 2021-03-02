import cv2
import numpy as np
import os
from PIL import Image

# creates an image of the difference between the two inputted images
# useful for testing and visualizing differences in images
# INPUTS: numpy array (of difference image)
# OUTPUT: numpy array (of grayscale difference image)
def show_diff(diffa):
    # showing colored difference image and saving
    img = Image.fromarray(diffa, 'RGB')
    img.show()
    #cv2.waitKey(0)
    img.save('C:/Users/Andrew/Desktop/fixed.JPG')

    # converting difference image to grayscale
    new = cv2.imread('C:/Users/Andrew/Desktop/fixed.JPG')
    gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)

    return gray

# finds the absolute difference in an image
# necessary because np.subtract is circular and cv2.subtract is cut off
# there could be a subtract function from a library that does this, but haven't found one
# this also could be done in one line, but  this is more descriptive
# INPUTS: numpy array (of an image), numpy array (of an image)
# OUTPUT: numpy array (of an image)
def img_sub(img1, img2):
    truth_array = np.less(img1, img2)
    subbed12 = np.subtract(img1, img2)
    subbed21 = np.subtract(img2, img1)
    diffa = np.where(truth_array, subbed21, subbed12)

    return diffa

# weights difference image with higher weights on outside of image
# need more testing to decide if this is necessary or not
# INPUT: numpy array (of an image)
# OUTPUT: numpy array (of an image)
# not finished
def weigh_diff_img(img):
    pass
    # arr = [[int(max(abs(x - (img.shape[0] / 2)), abs(y - (img.shape[1] / 2)))) for x in range(img.shape[0])] for y in range(img.shape[1])]
    #return np.dot(arr, img)

def retrieve_images(path):
    files = os.listdir(path)
    print(files)
    images = []
    for file in files:
        images.append(cv2.imread(f'{path}{file}'))
    return images