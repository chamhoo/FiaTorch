import os
import shutil
import pickle
from networkx.algorithms.bipartite.basic import color
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy.random import randint
from .block import Block


class ObjControl(object):
    # manage objects automatically
    # when you init this instance, if this path is exist, it will be loaded,
    # if not, a sv-file will be constituted 
    # Once this object has any modification, the controler can update local file simultaneously. 
    def __init__(self, path, init_val_if_empty) -> None:
        self.path = path
        if os.path.isfile(self.path):
            self.val = self._load()
        else:
            self.val = init_val_if_empty
            self._save()

    def _load(self):
        with open(self.path, 'rb')as f:
            return pickle.load(f)

    def __getattr__(self, name):
        return getattr(self.val, name)

    def _save(self):
        if os.path.isfile(self.path):
            os.remove(self.path)

        with open(self.path, 'wb') as f:
            pickle.dump(self.val, f)

    def change(self, opt):
        self._save()
        

class Link(object):
    def __init__(self) -> None:
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


class Task(dict):

    def __init__(self, path=None) -> None:
        super().__init__()
        # path
        if path is None:
            self.__path__ = os.path.join(f'task{randint(10**8)}')
        else:
            self.__path__ = path

        if not os.path.isdir(self.__path__):
            os.mkdir(self.__path__)
        # link & head
        self.head = ObjControl(os.path.join(self.__path__, 'head.sv'), set())
        self.link = ObjControl(os.path.join(self.__path__, 'link.sv'), Link())

    def add_block(self, name):
        # if block is exist, DO NOTHING
        block_path = os.path.join(self.__path__, name)
        if not os.path.isdir(block_path):
            os.mkdir(block_path)
            self.head.change(self.head.add(name))
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
        block_list = list(self.head.val)
        block_set = set(self.head.val)

        while block_set:
            bs = set()
            for block_name in block_set:
                for bn in self.link.next(block_name):
                    # if all the prerequisite are contained in block_list, join in it
                    if set(block_list).issuperset(self.link.before(bn)) and (bn not in block_list):
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
        s_list = self.structure()
        G = nx.Graph()
        G.add_edges_from(s_list)
        # color 
        color_list = []
        for n in G.nodes():
            if n in self.head.val:
                color_list.append('salmon')
            else:
                color_list.append('gray')
        nx.draw_networkx(G, with_labels=True, font_weight='bold', node_color=color_list)
        plt.show()


if __name__ == "__main__":
    t = Task('ta')
    print(t.show())


    '''
    t.add_block('1')
    t.add_block('2')
    t.add_block('3')
    t.add_block('4')
    t.add_block('5')
    t.add_block('6')
    t.add_block('7')

    # 暂时还没有制作data loader

    t.link.change(t.link.add('1', '2', np.abs))
    t.link.change(t.link.add('1', '3', np.abs))
    t.link.change(t.link.add('2', '6', np.abs))
    t.link.change(t.link.add('3', '4', np.abs))
    t.link.change(t.link.add('3', '5', np.abs))
    t.link.change(t.link.add('4', '6', np.abs))
    t.link.change(t.link.add('6', '7', np.abs))
    t.link.change(t.link.add('5', '7', np.abs))

    t.head.change(t.head.remove('4'))
    t.head.change(t.head.remove('2'))
    t.head.change(t.head.remove('3'))
    t.head.change(t.head.remove('5'))
    t.head.change(t.head.remove('6'))
    t.head.change(t.head.remove('7'))

    print(t.link.list)
    print(t.BFS())
    '''