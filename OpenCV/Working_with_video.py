""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

import cv2


capture = cv2.VideoCapture('ImagesAndVideo/Sample.mp4')

if (capture.isOpened() == False):
    print("Error opening video  file")

# Read until video is completed
while (capture.isOpened()):

    # Capture frame-by-frame
    ret, frame = capture.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
capture.release()

# Closes all the frames
cv2.destroyAllWindows()