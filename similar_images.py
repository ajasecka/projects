import cv2
import numpy as np
import pprint as pp
from similar_images_functions import *

'''
checks if images are similiar
no machine learning, but would prefer to if there was enough data
'''

def main():
    #getting images and checking for similar dimensions
    img1 = cv2.imread('C:/Users/Andrew/Desktop/images/same3.JPG')
    img2 = cv2.imread('C:/Users/Andrew/Desktop/images/no2.JPG')
    if img1.shape != img2.shape:
        raise Exception('Image dimensions are not the same')

    #displaying images and dimensions
    cv2.imshow("first image", img1)
    cv2.imshow("second image", img2)
    print('image dimensions: {}'.format(img1.shape))
    cv2.waitKey(0)

    #converting images to numpy array
    img1 = np.asarray(img1)
    img2 = np.asarray(img2)

    # calculates difference between pixels of images
    diffa = img_sub(img1, img2)

    # adding weights to pixels

    # removing all values lower than 50 in difference image
    diffa = np.where(diffa < 50, 0, diffa)
    pix_difference = 1 - (np.sum(diffa) / (640 * 3 * 480 * 256))
    print('percentage of similarities between colored image pixel values (after threshold): {}'.format(pix_difference))

    #final decision
    if pix_difference > .85:
        print('Images are same')
    else:
        print('Images are different')

if __name__ == '__main__':
    #main()
    xx = 8
    yy = 8
    arr = [[int(max(abs(x - (xx / 2)), abs(y - (yy / 2)))) for x in range(xx)] for y in range(yy)]
    pp.pprint(arr)
