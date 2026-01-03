from abc import ABC, abstractmethod

class MediaHandler(ABC):
    @abstractmethod
    def handler(self):
        pass