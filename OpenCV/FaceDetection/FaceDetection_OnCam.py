""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    _, img = capture.read()

    image = cv2.resize(img, (750, 640))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 10)

    for (x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)
    image = cv2.flip(image, 180)
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()