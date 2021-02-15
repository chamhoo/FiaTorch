import os


class Model(object):

    def __init__(self, path, name):
        self.name = name
        self.path = os.path.join(path, name)

    def search(self):
        pass

    def predict(self):
        pass

    def feature_engineering(self):
        pass

    