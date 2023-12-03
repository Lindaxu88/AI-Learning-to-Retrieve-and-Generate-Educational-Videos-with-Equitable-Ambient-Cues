
import os
import cv2
import numpy as np


directory_name = r'D:\yolov5-5.0\image\ori'  # directory read the position of the pic
save_directory_name = r'D:\yolov5-5.0\image\post'  # save_directory save the pic location

for filename in os.listdir(directory_name):
    img = cv2.imread(directory_name + '/' + filename)

    sobel_x = cv2.Sobel(img, -1, 1, 0)

    sobel_y = cv2.Sobel(img, -1, 0, 1)

    sobel_xy = sobel_x + sobel_y
    img4 = cv2.add(img,sobel_xy)
    blur_img = cv2.GaussianBlur(img4, (0, 0), 5)

    a = 1.3

    b = -0.52

    c = 9

    usm = cv2.addWeighted(img, a, blur_img, b, c)

    hsv = cv2.cvtColor(usm, cv2.COLOR_RGB2HSV)



    random_br = 1.3

    mask = hsv[:, :, 2] * random_br > 255  # hsv[:, :, 2]

    v_channel = np.where(mask, 255, hsv[:, :, 2] * random_br)

    hsv[:, :, 2] = v_channel
    usm = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)



    # img1 = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # # img5 = cv2.medianBlur(img4,3)
    # # img5 = cv2.blur(img4, (5,5))
    # img5 = cv2.GaussianBlur(img4, (3,3),1)

    cv2.imwrite(save_directory_name + '/' + filename, usm)