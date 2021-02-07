import os
import shutil
import numpy as np
from numpy.random import randint


def make_new(_type, path):
    # status 0, 2: Fail and exit
    # status 1: old
    # status 3: init new
    if os.path.isdir(path):
        print(f'This {_type} is exist, [delete[D]/load[L]/quit[Q]] ?:')
        status = 0
        for _ in range(3):
            if status == 0:
                f = input()
                if f in ['delete', 'D', 'd']:
                    print('This "delete" operation is permanent, do you want to continue? [Y/N]:')
                    if input() in ['Y', 'y', 'yes']:
                        shutil.rmtree(path)
                        os.mkdir(path)
                        status = 3
                    else: status = 2
                elif f in ['load', 'l', 'L']: status = 1
                elif f in ['quit', 'Q', 'q']: status = 2
                else:
                    print('no such option')
            if status == 2: 
                print('exit')
                exit()
    else:
        os.mkdir(path)
        status = 3
    return status


class Block(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.before = list()
        self.next = list()
        self.__name__ = name


class Task(dict):
    def __init__(self, path=None) -> None:
        super().__init__()
        # head block
        self.head_block = []
        # init path
        if path is None:
            default_path = '.\/task' + str(randint(0, 10*6))
            self.__path__ = default_path
        else:
            self.__path__ = path
        make_new("task", self.__path__)

    def add_block(self, name):
        status = make_new('block', os.path.join(self.__path__, name))
        self.head_block.append(name)
        self[name] = Block(name)

    

        



if __name__ == "__main__":
    t = Task("soso")
    t.add_block('b1')