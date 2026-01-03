from . import MediaHandler
from utils import Logs

class CameraHandler(MediaHandler):

    
    def handler(self):
        logs = Logs()
        log = logs.get_Logger("CameraHandler")
        log.info("Camera Handler Initialized")
        