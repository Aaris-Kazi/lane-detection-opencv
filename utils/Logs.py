import logging


class Logs():
    _instance = None
    _initialized = False
    log: logging.Logger
    def __new__(cls, *args, **kwargs):
        """
        This is a singleton class to manage logging across the application.
        """
        if not cls._instance:
            cls._instance = super(Logs, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self):
        if self._initialized:
            return
        self.log = logging.getLogger("Logs")
        logging.basicConfig(level=logging.INFO, format="%(levelname)s :: %(name)s :: %(message)s")
        self.log.info("Initializing logs")
        self._initialized = True

    def getLogger(self) -> logging.Logger:
        return self.log
    
    
    def get_Logger(self, TAG: str) -> logging.Logger:
        return logging.getLogger(TAG)