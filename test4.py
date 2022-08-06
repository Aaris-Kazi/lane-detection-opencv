import cv2
import numpy as np
from fps import advance_fps
import time
from showFilters import filter_colors
from showLines import show_lines
from show_combo_lines import combo_lines

def area_of_interest_video(img):
    ht = img.shape[0]
    wt = img.shape[1]
    triangle = np.array([
        [(0, ht - 60), (wt, ht - 60), (740, 420), (540, 420)]
    ])
    mask = np.zeros_like(img)  # creating a copy of image with arrays of 0
    cv2.fillPoly(mask, triangle, 255)  # function that create polygons of visible region
    masked_image = cv2.bitwise_and(img, mask)  # it will hide other data and show only the visible part
    return masked_image


def main():
    path = 'lane1_1.mp4'
    cap = cv2.VideoCapture(path)
    prev = 0
    while cap.isOpened():
        
        _, frame = cap.read()
        prev = advance_fps(frame, time.time(), prev, cv2)
        hsv = filter_colors(frame, cv2, np)
        edges = cv2.Canny(hsv, 50, 150)  # to find the edges
        aoi = area_of_interest_video(edges)
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