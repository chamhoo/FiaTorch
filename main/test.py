path = 'ta\/connection.lk'


import pickle

with open(path, 'rb') as f:
    print(pickle.load(f))