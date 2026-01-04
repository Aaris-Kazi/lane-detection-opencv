from . import MediaHandler
from utils import CommonHandler, Logs
from cv2 import VideoCapture
from constants.Literals import VIDEO_WINDOW
from constants.Literals import VIDEO_PATH
from numpy import ndarray


class VideoHandler(MediaHandler):

    
    def handler(self):
        logs = Logs()
        log = logs.get_Logger("VideoHandler")
        log.info("Video Handler Initialized")
        cap: ndarray = VideoCapture(VIDEO_PATH)
        CommonHandler.captureHandler(cap, VIDEO_WINDOW)