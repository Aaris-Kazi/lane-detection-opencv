from cv2 import inRange, cvtColor, bitwise_and, addWeighted, COLOR_BGR2HLS, GaussianBlur, Canny

from constants.Literals import LOWER_YELLOW, UPPER_YELLOW, LOWER_WHITE, UPPER_WHITE, KERNEL_THRESHOLD, ZERO, BLUR_TH1, BLUR_TH2
from numpy import ndarray


class ColorFilters:

    def __init__(self):
        self.kernel_threshold = KERNEL_THRESHOLD
        self.zero = ZERO
        self.blur_th1 = BLUR_TH1
        self.blur_th2 = BLUR_TH2

    def filter_colors(self, image: ndarray) -> ndarray:

        white_mask = inRange(image, LOWER_WHITE, UPPER_WHITE)
        white_image = bitwise_and(image, image, mask=white_mask)

        hsv = cvtColor(image, COLOR_BGR2HLS)
        yellow_mask = inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)
        yellow_image = bitwise_and(image, image, mask=yellow_mask)
        image = addWeighted(white_image, 1., yellow_image, 1., 0.)
        return image


    def blur_frame_edge(self, frame: ndarray) -> ndarray:
        blur = GaussianBlur(frame, self.kernel_threshold, self.zero)
        edges = Canny(blur, self.blur_th1, self.blur_th2)
        return edges