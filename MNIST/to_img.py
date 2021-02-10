import os
import shutil
from tqdm import tqdm
import numpy as np
import pandas as pd
from PIL import Image as im


train_csv = "MNIST\/train.csv"
test_csv = "MNIST\/test.csv"

label = []

for _type, csv in [['train', train_csv], ['test', test_csv]]:
    # new folder
    path = "MNIST\/" + _type
    if os.path.isdir(path):
        print("Path is exist, DROP it? [Y/N]")
        isy = input()
        if isy in ['Y','y', 'yes']:
            shutil.rmtree(path)
        else:
            exit()
    os.mkdir(path)

    with open(csv) as f:
        title = f.readline()
        for n, line in tqdm(enumerate(f)):
            im_list = list(eval(line))
            if _type == 'train':
                im_label = im_list.pop(0)
                label.append(im_label)
            im_array = np.array(im_list).reshape([28, 28]).astype(np.uint8)
            im_img = im.fromarray(im_array, mode="L")
            img_path = os.path.join(path, "{n}.png".format(n = n))
            im_img.save(img_path, format="PNG")

    if _type == 'train': 
        df = pd.DataFrame(label, columns=['label'])
        df.to_csv('MNIST\/label.csv')

    print("{_type} done".format(_type = _type))
