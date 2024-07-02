from abc import ABC, abstractmethod


class GitCommandState(ABC):
    @abstractmethod
    def execute(self, context):
        pass
