import cv2
import numpy as np
from PIL import Image

def main():
    no1 = cv2.imread('C:/Users/Andrew/Desktop/images/same2.JPG')
    yes1 = cv2.imread('C:/Users/Andrew/Desktop/images/same1.JPG')
    print(no1.shape)

    no1np = np.asarray(no1)
    yes1np = np.asarray(yes1)

    diff = np.subtract(no1np, yes1np)
    diffa = np.absolute(diff)
    print(1 - (np.sum(diffa) / (640 * 3 * 480 * 256)))

    diffa[np.logical_and(diffa <= 100, diffa >= 300)] = 0
    print(diffa)

    img = Image.fromarray(diffa, 'RGB')
    img.show()
    img.save('C:/Users/Andrew/Desktop/fixed.JPG')

    new = cv2.imread('C:/Users/Andrew/Desktop/fixed.JPG')
    gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
    cv2.imshow('diff image from grayscale', gray)
    cv2.waitKey(0)

    #cv2.imshow("first image", no1)
    #cv2.imshow("second image", yes1)
    #cv2.waitKey(0)

if __name__ == '__main__':
    main()