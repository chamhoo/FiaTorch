import os
import numpy as np


class CsvSet(object):
    def __init__(self, path, col, target):


class DataItem(object):
    def __init__(self, is_x, source):
        self.len = None
        self.is_x = is_x
        self.source = source
        self.source_catagory = None
        
        if isinstance(self.source, np.ndarray):
            self.len = self.source.shape[0]
            if self.source.ndim == 2:
                self.source_catagory = "2dim_array"  # Tabular data [n_samples, n_features], like read from a csv file.
            elif self.source.ndim == 4:
                self.source_catagory = "4dim_array"   # image data, [n_samples, w, h, dims]
            else:
                raise ValueError(f"{self.source.ndim}-dim numpy array is not supported.")

        elif isinstance(self.source, str):
            _, suffix = os.path.splitext(self.source)
            if suffix == "":
                self.len = self.verify_folder(self.source)
                self.source_catagory = "image_folder"
            elif suffix == ".csv":
                self.source_catagory = "csvfile"
                self.len = self.csv_len(self.source)
            else:
                raise ValueError(f"{suffix} file is not supported.")

        elif self.is_upper_output():
            idx, pathstr = self.source
            self.len = len(idx)
            _, suffix = os.path.splitext(pathstr)
            if suffix == "":
                self.source_catagory = "image_folder_with_idx"
                n = self.verify_folder(self.source[-1])
            elif suffix == ".csv":
                self.source_catagory = "csvfile_with_idx"
                n = self.csv_len(self.source[-1])
            else:
                raise (f"{suffix} file is not supported")
            assert idx <= n, "idx > n_samples"

        else:
            raise ValueError(f"{type(self.source)} is not supported.")

    def is_upper_output(self):
        idx, pathstr = self.source
        if isinstance(idx, list) and isinstance(pathstr, str):
            return True
        else:
            return False
    
    def verify_folder(self, folder, min_file=2**3):
        stand_suffix = None
        with os.scandir(folder) as entries:
            for i, entry in enumerate(entries):
                path = entry.path
                suffix = os.path.splitext(path)
                if i == 0:
                    stand_suffix = suffix
                else:
                    assert suffix == stand_suffix, f"standard suffix is {stand_suffix}, not {suffix} in {path}"
        n = i+1
        assert n >= min_file, f"The number of files[{n}] which is inside of the specified folder[{self.source}] does not meet the minimum number of it, which is {min_file}"
        return n

    def csv_len(self, csvfile):
        count = 0
        with open(csvfile) as f:
            f.__next__







class Data(object):

    def __init__(self):
        self.len = None
        super().__init__()

    def __len__(self):
        return self.len

    def localize(self):
        pass

    def generator(self):
        pass

    def output(self):
        pass