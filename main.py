from utils import Logs
if __name__ == "__main__":
    logs = Logs()
    log = logs.get_Logger("Main")
    log.info("Lane Detection Initialization")