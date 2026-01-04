import cv2
import numpy as np
from numpy import ndarray
from fps import advance_fps
import time
from showLines import show_lines
from show_combo_lines import combo_lines
from utils import ColorFilters, CommonHandler


def main():
    path = 'lane1_1.mp4'
    cap = cv2.VideoCapture(path)
    colorFilters = ColorFilters()
    prev = 0
    while cap.isOpened():
        
        _, frame = cap.read()
        prev = advance_fps(frame, time.time(), prev, cv2)
        hsv: ndarray = colorFilters.filter_colors(frame)
        edges: ndarray = colorFilters.blur_frame_edge(hsv)
        aoi: ndarray = CommonHandler.area_of_interest(edges)
        lines = cv2.HoughLinesP(aoi, 2, np.pi / 180, 100, np.array([]), 20, 5)
                # lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 30, np.array([]), 100, 180)
        avg_lines = combo_lines(aoi, lines)
        clines = show_lines(frame, avg_lines, cv2, np)
        color_image_line = cv2.addWeighted(frame, 0.9, clines, 1, 1)
        resize = cv2.resize(color_image_line, (720, 480))
        cv2.imshow('Lane', resize)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()