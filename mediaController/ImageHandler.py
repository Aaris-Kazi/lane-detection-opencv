from . import MediaHandler
from utils import Logs, ColorFilters
from glob import glob
from constants.Literals import PATH
from cv2 import imread
from matplotlib.pyplot import show, imshow
from numpy import ndarray


class ImageHandler(MediaHandler):
    
    def handler(self):
        logs = Logs()
        colorFilters = ColorFilters()
        log = logs.get_Logger("ImageHandler")
        log.info("Image Handler Initialized")

        for img_path in glob(PATH):
            log.info(f"Processing Image: {img_path}")
            try:
                img: ndarray = imread(img_path)
                img: ndarray = colorFilters.filter_colors(img)
                imshow(img)
                show()

            except Exception as e:
                log.error(f"Error processing image {img_path}: {e}")