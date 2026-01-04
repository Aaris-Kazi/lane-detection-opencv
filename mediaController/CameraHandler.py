from . import MediaHandler
from utils import Logs, CommonHandler
from constants.Literals import PRIMARY_CAMERA, CAMERA_WINDOW
from cv2 import VideoCapture
from numpy import ndarray

class CameraHandler(MediaHandler):

    
    def handler(self):
        logs = Logs()
        log = logs.get_Logger("CameraHandler")
        log.info("Camera Handler Initialized")
        cap:ndarray = VideoCapture(PRIMARY_CAMERA)
        CommonHandler.captureHandler(cap, CAMERA_WINDOW)



        