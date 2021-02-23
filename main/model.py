import os
from glob import glob


class Model(object):

    def __init__(self, path, name, model, params):
        self.name = name
        self.path = os.path.join(path, name)
        self.best_params = None
        self.max_lr = None
        self.search_result = dict()
        self.model = model
        self.parmas = params

    def load_data(self, name, path, catagory='arr'):
        # catagory: 'arr' or 'torch'
        # return a torch.dataloader/numpy.array
        if os.path.isdir(path):
            file_list = os.listdir(path)
            suffix = os.path.splitext(path[0])[-1]
            def joint(folder_path, file_path, suffix):
                assert suffix == os.path.splitext(file_path)[-1], "find different suffix"
                return os.path.join(folder_path, file_path)
            file_list = [joint(path, fi, suffix) for fi in file_list]
            

                


    def transform(self):
        pass

    def find_max_lr(self):
        pass

    def train(self):
        pass

    def show_params(self):
        pass

    def plot_params(self):
        pass

    def search(self):
        pass

    def train_best(self):
        pass

    def predict(self):
        pass
    