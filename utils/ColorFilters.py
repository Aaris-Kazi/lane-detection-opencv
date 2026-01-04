from cv2 import inRange, cvtColor, bitwise_and, addWeighted, COLOR_BGR2HLS

from constants.Literals import LOWER_YELLOW, UPPER_YELLOW, LOWER_WHITE, UPPER_WHITE
from numpy import ndarray


class ColorFilters:

    def filter_colors(self, image: ndarray) -> ndarray:

        white_mask = inRange(image, LOWER_WHITE, UPPER_WHITE)
        white_image = bitwise_and(image, image, mask=white_mask)

        hsv = cvtColor(image, COLOR_BGR2HLS)
        yellow_mask = inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)
        yellow_image = bitwise_and(image, image, mask=yellow_mask)
        image = addWeighted(white_image, 1., yellow_image, 1., 0.)
        return image