from . import MediaHandler
from utils import Logs
from glob import glob
from constants.Literals import PATH
from cv2 import imread, imshow
import matplotlib.pyplot as plt
class ImageHandler(MediaHandler):
    
    def handler(self):
        logs = Logs()
        log = logs.get_Logger("ImageHandler")
        log.info("Image Handler Initialized")

        for img_path in glob(PATH):
            log.info(f"Processing Image: {img_path}")
            try:
                img = imread(img_path)
                plt.imshow(img)
                plt.show()

            except Exception as e:
                log.error(f"Error processing image {img_path}: {e}")