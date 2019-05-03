import cv2
import numpy as np

def main():
    no1 = cv2.imread('C:/Users/Andrew/Desktop/images/same4.JPG')
    yes1 = cv2.imread('C:/Users/Andrew/Desktop/images/no2.JPG')
    print(no1.shape)

    no1np = np.asarray(no1)
    yes1np = np.asarray(yes1)
    print(no1np)
    print('next\n')
    print(yes1np)

    diff = np.subtract(no1np, yes1np)
    diffa = np.absolute(diff)
    print(1 - (np.sum(diffa) / (640 * 3 * 480 * 256)))

    cv2.imshow("first image", no1)
    cv2.waitKey(0)
    cv2.imshow("second image", yes1)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()