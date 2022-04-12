""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

import cv2
import numpy as np
import matplotlib.pyplot as plt



org_image = cv2.imread('ImagesAndVideo/logo.png')
double_size_img = cv2.resize(org_image, (0, 0), fx=2, fy=2)
kernel = np.ones((5, 5), np.uint8)

while True:
    print("0. Original\n1. Resize\n2. Gaussian Blur\n3. Median Blur\n4. Bilateral Blur\n5. Erosion\n6. Border\n7. Dilation\n8. Grayscale Image")
    print("9. Rotation\n10. Shifting of image\n11. Edge Detection\n12. Graph\n13. Masking\n14. Draw Line\n15. Exit")
    choice = int(input("Enter Your Choice:- "))
    if choice == 0:
        cv2.imshow('Original Image', org_image)
        cv2.waitKey(0)
        print()

    elif choice == 1:
        large = cv2.resize(org_image, (0, 0), fx=3, fy=3)
        cv2.imshow("Resized Image", large)
        cv2.waitKey(0)
        print()

    elif choice == 2:
        Gaussian = cv2.GaussianBlur(double_size_img, (7, 7), 0)
        cv2.imshow('Gaussian Blurring', Gaussian)
        cv2.waitKey(0)
        print()

    elif choice == 3:
        median = cv2.medianBlur(double_size_img, 5)
        cv2.imshow('Median Blurring', median)
        cv2.waitKey(0)
        print()

    elif choice == 4:
        bilateral = cv2.bilateralFilter(double_size_img, 9, 75, 75)
        cv2.imshow('Bilateral Blurring', bilateral)
        cv2.waitKey(0)

    elif choice == 5:
        img_erosion = cv2.erode(double_size_img, kernel)
        cv2.imshow('Erosion', img_erosion)
        cv2.waitKey(0)
        print()

    elif choice == 6:
        img_border_const = cv2.copyMakeBorder(double_size_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
        img_border_reflect = cv2.copyMakeBorder(double_size_img, 100, 50, 100, 50, cv2.BORDER_REFLECT)
        cv2.imshow('Border_Const', img_border_const)
        cv2.imshow('Border_Reflect', img_border_reflect)
        cv2.waitKey(0)
        print()

    elif choice == 7:
        img_dilation = cv2.dilate(double_size_img, kernel)
        cv2.imshow('Dilation', img_dilation)
        cv2.waitKey(0)

    elif choice == 8:
        img_gray_scale = cv2.cvtColor(double_size_img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray Scale Image', img_gray_scale)
        cv2.waitKey(0)
        print()

    elif choice == 9:
        (rows, cols) = double_size_img.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -45, 1)
        img_rotation = cv2.warpAffine(double_size_img, M, (cols, rows))
        cv2.imshow('Rotation', img_rotation)
        cv2.waitKey(0)
        print()

    elif choice == 10:
        M = np.float32([[1, 0, 100], [0, 1, 50]])
        (rows, cols) = double_size_img.shape[:2]
        img_shift = cv2.warpAffine(double_size_img, M, (cols, rows))
        cv2.imshow('Shifting', img_shift)
        cv2.waitKey(0)
        print()

    elif choice == 11:
        img_edges = cv2.Canny(double_size_img, 40, 50)
        cv2.imshow('Edge Detection', img_edges)
        cv2.waitKey(0)
        print()

    elif choice == 12:
        img = cv2.imread('ImagesAndVideo\img.png', 0)
        plt.hist(img.ravel(), 256, [0, 256])
        cv2.imshow("Image", img)
        plt.show()
        cv2.waitKey(0)
        print()

    elif choice == 13:
        image = cv2.cvtColor(double_size_img, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([60, 35, 140])
        upper_blue = np.array([180, 255, 255])
        mask = cv2.inRange(image, lower_blue, upper_blue)
        result = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow('image', image)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)
        cv2.waitKey(0)
        print()

    elif choice == 14:
        thickness = 10
        image = cv2.line(double_size_img, (0, 0), (80, 450), (255, 0, 255), thickness)
        image = cv2.line(double_size_img, (450, 0), (380, 450), (255, 0, 255), thickness)
        cv2.imshow("Draw Line", image)
        cv2.waitKey(0)
        print()

    elif choice == 15:
        exit(0)

    else:
        print("Invalid Input...")
        print()
