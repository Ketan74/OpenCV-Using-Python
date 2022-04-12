""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('../ImagesAndVideo/faces.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray, 1.1, 2)
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
