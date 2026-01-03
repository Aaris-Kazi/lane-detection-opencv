from typing import Optional
from utils import Logs
from mediaController import MediaHandler, VideoHandler, ImageHandler, CameraHandler
class LaneDetectionApplication():
    """
    This class is to handle the Mode of Media to be choose
    """
    mediaHandler: MediaHandler = Optional[MediaHandler]

    def __init__(self, options: int) -> None:
        logs = Logs()
        log = logs.get_Logger("LaneDetectionApplication")
        log.info("Application Initialized\n")
        if options == 1:
            mediaHandler = VideoHandler
        elif options == 2:
            mediaHandler = ImageHandler
        elif options == 3:
            mediaHandler = CameraHandler
        else:
            print("You choose wrong option")

        mediaHandler.handler(self)