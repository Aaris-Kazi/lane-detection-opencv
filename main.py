from LaneDetectionApplication import LaneDetectionApplication
from utils import Logs


if __name__ == "__main__":
    logs = Logs()
    log = logs.get_Logger("Main")
    banner = """
        For the Input of Video input: 1
        For the Input of Images input: 2
        For the Input of Camera input: 3
    """
    print(banner)
    options = int(input("Please give input: "))
    log.info("Main Initialization")
    LaneDetectionApplication(options)