import os
import shutil
import pickle
import numpy as np
from numpy.random import randint


class Block(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.__name__ = name


class Link(object):
    def __init__(self) -> None:
        super().__init__()
        self.list = list()

    def add(self, from_b, to_b, func):
        self.list.append([from_b, to_b, func])

    def __drop_by__(self, isto, name, silence=True):
        assert isinstance(isto, bool), TypeError('isto in bool')
        drop_idx = []
        for i, lst in enumerate(self.list):
            if lst[isto] == name:
                drop_idx.append(i)
        for i in drop_idx[::-1]:
            self.list.pop(i)
        if not silence:
            print(f'{len(drop_idx)} rules have been dropped')

    def drop_by_to(self, name, silence=True):
        self.__drop_by__(True, name, silence)

    def __connect__(self, isnext, name):
        colist = list()
        for l in self.list:
            if l[int(1-isnext)] == name:
                colist.append(l[isnext])
        return colist

    def next(self, name):
        return self.__connect__(True, name)

    def before(self, name):
        return self.__connect__(False, name)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.list, f)
            
    def load(self, path):
        with open(path, 'rb') as f:
            self.list = pickle.load(f)


class Task(dict):

    def __init__(self, path=None) -> None:
        super().__init__()
        self.head_block = set()
        # init path
        if path is None:
            default_path = '.\/task' + str(randint(0, 10*6))
            self.__path__ = default_path
        else:
            self.__path__ = path
        # mkdir if not exist
        if not os.path.isdir(self.__path__):
            os.mkdir(self.__path__)
            self.link = Link()
        else:
            self.link = Link.load(self.__path__ + '\/connection.lk')

    def add_block(self, name):
        # if block is exist, DO NOTHING
        block_path = f'{self.__path__}\/{name}'
        if not os.path.isdir(block_path):
            os.mkdir(block_path)
            self.head_block.add(name)
            self[name] = Block(name)
            print(f'block {name} is builded up successfully.')
        else:
            print(f'block {name} is exist')

    def __getattr__(self, name):
        return self[name]
    
    def __dir__(self):
        return super().__dir__() + [k for k in self.keys()]

    def __setattr__(self, name, value):
        # prohibit adding new attribution if atttr in self.keys()
        if name in self.keys():
            raise AttributeError
        return super().__setattr__(name, value)

    def BFS(self):
        # search blocks by BFS, but it will be recorded provided ALL the prerequisite added in the returned list
        block_list = list(self.head_block)
        block_set = set(self.head_block)

        while block_set:
            bs = set()
            for block_name in block_set:
                for bn in self.link.next(block_name):
                    # if all the prerequisite are contained in block_list, join in it
                    if set(block_list).issuperset(self.link.before(block_name)):
                        bs.add(bn)
                        block_list.append(bn)
            block_set = bs
        return block_list

    def drop_block(self, block_name):
        next_blk = self.link.next(block_name)
        if next_blk:
            print(f'{block_name} has offsprings: {next_blk}')
        else:
            self.link.drop_by_to(block_name)
            self.__delitem__(block_name)
    
    def structure(self):
        # order sequences and connections in the network of blocks.
        # return [(block_from: block 1, block_to: block 2),
        #         (block_from: block 1, block_to: block 3),
        #         ...
        #        ] 
        return [(f, t) for f, t, r in self.link.list]

    def show(self):
        pass

        



if __name__ == "__main__":
    t = Task('ta')
    #t.add_block('1')
    #t.add_block('2')
    #t.add_block('3')
    #t.add_block('4')
    #t.add_block('5')
    #t.add_block('6')
    #t.add_block('7')

    # 暂时还没有制作data loader
    #t.link.add('1', '2', np.abs)
    #t.link.add('1', '3', np.abs)
    #t.link.add('2', '6', np.abs)
    #t.link.add('3', '4', np.abs)
    #t.link.add('3', '5', np.abs)
    #t.link.add('4', '6', np.abs)
    #t.link.add('6', '7', np.abs)
    #t.link.add('5', '7', np.abs)

    print(t.BFS())
