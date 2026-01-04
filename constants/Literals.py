from numpy import array, uint8

QUIT = "q"
WAIT_KEYS = 10
PRIMARY_CAMERA = 0
WINDOW_SIZE = (1280, 640)


WHITE_THRESHOLD = 200
LOWER_WHITE = array([WHITE_THRESHOLD, WHITE_THRESHOLD, WHITE_THRESHOLD], dtype=uint8)
UPPER_WHITE = array([255, 255, 255], dtype=uint8)

LOWER_YELLOW = array([15, 38, 115], dtype=uint8)
UPPER_YELLOW = array([35, 204, 255], dtype=uint8)

PATH = "static/test_images/*.jpg"
VIDEO_PATH = "static/lane1_1.mp4"
CAMERA_WINDOW = 'Camera Window'
VIDEO_WINDOW = 'Video Window'