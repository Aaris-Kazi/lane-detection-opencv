from cv2 import VideoCapture, destroyAllWindows, imshow, resize, waitKey
from . import Logs
from constants.Literals import QUIT, WAIT_KEYS, WINDOW_SIZE

class CommonHandler:
    def __init__(self):
        pass

    @staticmethod
    def captureHandler(capture: VideoCapture, windowName: str) -> None:
        """
        A common method to handle different media sources.
        :param source: The media source (file path, camera index, etc.)
        :return: Captured media object
        """

        logs = Logs()
        log = logs.get_Logger("CommonHandler")

        # Implementation for capturing media from the source
        while capture.isOpened():
            try:
                _, frame = capture.read()
                res = resize(frame, WINDOW_SIZE)
                imshow(windowName, res)
                if waitKey(WAIT_KEYS) & 0xFF == ord(QUIT):
                    log.info("Quitting media capture")
                    break  # to quit press q
            except Exception as e:
                log.error(f"Error capturing media: {e}")
                break
        capture.release()
        destroyAllWindows()