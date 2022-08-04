import cv2
import numpy as np
from fps import advance_fps
from showDimensions import dims
import time
def main():
    path = 'lane1_1.mp4'
    cap = cv2.VideoCapture(path)
    prev = 0
    new = 0
    while cap.isOpened():
        try:
            _, frame = cap.read()
            prev = advance_fps(frame, time.time(), prev)
            resize = cv2.resize(frame, (720, 480))
            cv2.imshow('Lane', resize)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(e)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()