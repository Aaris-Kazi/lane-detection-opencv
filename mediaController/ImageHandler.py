from . import MediaHandler
from utils import Logs

class ImageHandler(MediaHandler):
    
    def handler(self):
        logs = Logs()
        log = logs.get_Logger("ImageHandler")
        log.info("Image Handler Initialized")