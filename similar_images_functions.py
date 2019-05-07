import cv2
import numpy as np
from PIL import Image

#creates an image of the difference between the two inputted images
#useful for testing and visualizing differences in images
#INPUTS: numpy array (of an image), numpy array (of an image)
#OUTPUT: N/A
def show_diff(img1, img2):
    #calculates difference between pixels of images
    diff = np.subtract(img1, img2)
    diffa = np.absolute(diff)

    #removing all values lower than 128 in difference image
    diffa = np.where(diffa < 128, 0, diffa)
    print('percentage of difference between colored image pixel values (after thresholding): {}'.format(1 - (np.sum(diffa) / (640 * 3 * 480 * 256))))


    #showing colored difference image and saving
    img = Image.fromarray(diffa, 'RGB')
    #img.show()
    img.save('C:/Users/Andrew/Desktop/fixed.JPG')

    #converting difference image to grayscale
    new = cv2.imread('C:/Users/Andrew/Desktop/fixed.JPG')
    gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('diff image from grayscale', gray)
    #cv2.waitKey(0)
    print('percentage of difference between grayscale image pixel values (after thresholding): {}'.format(1 - (np.sum(diffa) / (640 * 3 * 480 * 256))))