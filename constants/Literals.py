from numpy import array, uint8

QUIT = "q"
WAIT_KEYS = 10
PRIMARY_CAMERA = 0
WINDOW_SIZE = (1280, 640)

WHITE = 255
WHITE_THRESHOLD = 200
LOWER_WHITE = array([WHITE_THRESHOLD, WHITE_THRESHOLD, WHITE_THRESHOLD], dtype=uint8)
UPPER_WHITE = array([255, 255, 255], dtype=uint8)

LOWER_YELLOW = array([15, 38, 115], dtype=uint8)
UPPER_YELLOW = array([35, 204, 255], dtype=uint8)

VERT_X2 = (740, 420)
VERT_Y2 = (540, 420)

KERNEL_THRESHOLD = (5, 5)
ZERO = 0
BLUR_TH1 = 50
BLUR_TH2 = 150

PATH = "static/test_images/*.jpg"
VIDEO_PATH = "static/lane1_1.mp4"
CAMERA_WINDOW = 'Camera Window'
VIDEO_WINDOW = 'Video Window'