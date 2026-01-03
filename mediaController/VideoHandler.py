from . import MediaHandler
from utils import Logs

class VideoHandler(MediaHandler):

    
    def handler(self):
        logs = Logs()
        log = logs.get_Logger("VideoHandler")
        log.info("Video Handler Initialized")