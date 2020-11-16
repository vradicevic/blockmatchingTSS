import numpy as np
import cv2
import tss
import new_tss
import os
import copy
import framecollect

videopath = "casa_480.mp4"
#framecollect.getFrames(videopath)
#cv2.arrowedLine(image, start_point, end_point, color, thickness)
prevFrame= "testImages/frame10.png"
frame = "testImages/frame12.png"
cv2.imread(prevFrame)
editedFrame = new_tss.main(cv2.imread(prevFrame),cv2.imread(frame))
cv2.imshow(videopath,editedFrame)
cv2.waitKey()
        
"""
def play_video(videopath):
    # load video capture from file
    video = cv2.VideoCapture(videopath)
    # window name and size
    #cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)
    prevFrame = None
    N= 8
    count=False
    while video.isOpened():
        # Read video capture
        ret, frame = video.read()
        
        if count<1:
            prevFrame= frame
        
        editedFrame = tss.main(prevFrame,frame)
        
        #cv2.imshow("video", editedFrame)
        
        
            
        # Quit when 'q' is pressed
        cv2.imshow(videopath,editedFrame)
        if cv2.waitKey(1) == ord('q'):
            break
        count+=1
    # Release capture object
    video.release()
    # Exit and distroy all windows
    cv2.destroyAllWindows()


play_video(videopath)
"""