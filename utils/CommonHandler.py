import time
from cv2 import VideoCapture, destroyAllWindows, imshow, resize, waitKey, putText, FONT_HERSHEY_SIMPLEX

from . import Logs
from .ColorFilters import ColorFilters
from constants.Literals import QUIT, WAIT_KEYS, WINDOW_SIZE
from numpy import ndarray

class CommonHandler:
    fps = 0.0

    def __init__(self):
        pass
    
    @staticmethod
    def showFpsMethod(frame: ndarray, curr_time: float, prev_time: float) -> tuple[ndarray, float]:
        instant_fps = 1 / (curr_time - prev_time)
        CommonHandler.fps = 0.9 * CommonHandler.fps + 0.1 * instant_fps
        prev_time = curr_time
        fps_text = f"FPS: {int(CommonHandler.fps)}"
        putText(frame, fps_text, (10, 30), FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return frame, prev_time

    @staticmethod
    def captureHandler(capture: VideoCapture, windowName: str) -> None:
        """
        A common method to handle different media sources.
        :param source: The media source (file path, camera index, etc.)
        :return: Captured media object
        """

        logs = Logs()
        log = logs.get_Logger("CommonHandler")
        prev: float = time.perf_counter()
        colorFilters = ColorFilters()
        

        # Implementation for capturing media from the source
        while capture.isOpened():
            try:
                ret: bool = False
                frame: ndarray = None
                _, frame = capture.read()
                frame, prev = CommonHandler.showFpsMethod(frame, time.perf_counter(), prev)
                frame: ndarray = colorFilters.filter_colors(frame)
                edges: ndarray = colorFilters.blur_frame_edge(frame)
                res = resize(edges, WINDOW_SIZE)
                imshow(windowName, res)
                if waitKey(WAIT_KEYS) & 0xFF == ord(QUIT):
                    log.info("Quitting media capture")
                    break  # to quit press q
            except Exception as e:
                log.error(f"Error capturing media: {e}")
                break
        capture.release()
        destroyAllWindows()