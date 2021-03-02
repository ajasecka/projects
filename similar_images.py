import cv2
import numpy as np
import pprint as pp
from similar_images_functions import *
from pathlib import Path


def main():
    # image_groups: [{'avg':<array in shape of averaged images>, 'photos':<list of similar photos>}]
    image_groups = []
    path = input('Path of folder with images: ')
    if path == '':
        path = 'C:/Users/Andrew/Desktop/images/'

    same_image_path = input('Path for folder to store similar images:')
    if same_image_path == '':
        same_image_path = 'C:/Users/Andrew/Desktop/'
    images = retrieve_images(path)

    # cv2.imshow('image', images[0])
    # cv2.waitKey(0)

    if len(images) > 1:
        image_groups.append({'avg': np.asarray(images[0]), 'photos': [images[0]]})
        for image in images[1:]:
            similar_flag = False
            for group in image_groups:
                if image.shape != group['avg'].shape:
                    raise Exception('Image dimensions are not the same')

                # converting images to numpy array
                img1arr = np.asarray(image)
                img2arr = np.asarray(group['avg'])

                # calculates difference between pixels of images
                diff = img_sub(img1arr, img2arr)

                # TODO add weights to pixels

                # removing all values lower than 50 in difference image
                diff = np.where(diff < 50, 0, diff)
                pix_difference = 1 - (np.sum(diff) / (640 * 3 * 480 * 256))

                # final decision (simple, manual decision checking comparison of pixel differences in images)
                if pix_difference > .85:
                    print('Images are same')
                    group['photos'].append(image)
                    group['avg'] = group['avg'] * ((len(group['photos']) - 1) / len(group['photos'])) + img1arr / len(group['photos'])
                    similar_flag = True
                    break

            if not similar_flag:
                print('Images are different')
                image_groups.append({'avg': np.asarray(image), 'photos': [image]})

    print(f'group length: {len(image_groups)}')
    Path(f'{same_image_path}sortedImages/').mkdir(parents=True, exist_ok=True)
    for i, group in enumerate(image_groups):
        print(f'(group photos length: {len(group["photos"])}')
        for j, img in enumerate(group['photos']):
            Path(f'{same_image_path}sortedImages/group{i}/').mkdir(parents=True, exist_ok=True)
            cv2.imwrite(f'{same_image_path}sortedImages/group{i}/image{j}.jpg', img)



if __name__ == '__main__':
    main()
