''' Base class for all game AIs '''

from abc import ABC, abstractmethod


class BaseAI(ABC):
    ''' AI base classes '''

    def __init__(self, config):
        self.config = config

    def get_model_filename(self):
        """ gets the file name of the saved model file """
        return 'data/' + self.config['SaveFile']

    @abstractmethod
    def move(self):
        ''' base method for move. used to determine ai selected move for a game '''
        pass

    @abstractmethod
    def learn(self):
        ''' base method for ai to learn a defined game '''
        pass
