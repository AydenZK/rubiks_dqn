from abc import ABC, abstractmethod

class BaseEnvironment(ABC):
    def __init__(self):
        self.state = self.reset()

    def reset(self):
        return self.state
    
    @abstractmethod
    def step(self, action):
        raise NotImplementedError()

    @abstractmethod
    def render(self):
        pass