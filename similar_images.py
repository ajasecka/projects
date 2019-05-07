import cv2
import numpy as np
from similar_images_functions import *

'''
checks if images are similiar
does not use Machine Learning
'''

def main():
    #getting images and checking for similar dimensions
    img1 = cv2.imread('C:/Users/Andrew/Desktop/images/same2.JPG')
    img2 = cv2.imread('C:/Users/Andrew/Desktop/images/same1.JPG')
    if img1.shape != img2.shape:
        raise Exception('Image dimensions are not the same')

    #displaying images and dimensions
    cv2.imshow("first image", img1)
    cv2.imshow("second image", img2)
    print(img1.shape)
    cv2.waitKey(0)

    #converting images to numpy array
    img1np = np.asarray(img1)
    img2np = np.asarray(img2)

    #function for testing
    show_diff(img1np, img2np)



if __name__ == '__main__':
    main()