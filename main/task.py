import os
import shutil
import numpy as np
from numpy.random import randint


def make_new(_type, path):
    if os.path.isdir(path):
        print(f'This {_type} is exist, [delete[D]/load[L]/quit[Q]] ?:')
        status = 0
        for _ in range(3):
            if status == 0:
                f = input()
                if f in ['delete', 'D', 'd']:
                    status += 1
                    print('This "delete" operation is permanent, do you want to continue? [Y/N]:')
                    if input() in ['Y', 'y', 'yes']:
                        shutil.rmtree(path)
                        os.mkdir(path)
                    else: status += 1
                elif f in ['load', 'l', 'L']: status += 1
                elif f in ['quit', 'Q', 'q']: status += 2
                else:
                    print('no such option')
            if status == 2: 
                print('exit')
                exit()
    else:
        os.mkdir(path)


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
        make_new('block', os.path.join(self.__path__, name))
        self.head_block.append(name)
        self.__setitem__(k=name, v=Block(name=name))

    

        



if __name__ == "__main__":
    t = Task("soso")
    t.add_block('b1')