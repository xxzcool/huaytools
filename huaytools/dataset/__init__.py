""""""
from .mnist import load_data as load_mnist, load_data_npz as load_mnist_npz
from .mnist_fashion import load_data as load_mnist_fashion, load_data_npz as load_mnist_fashion_npz

import numpy as np


def save_to_npz(file, compressed=True, *args, **kwargs):
    """
    保存到 .npz 文件

    Examples:
        save_to_npz(file, x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test)
    """
    if compressed:
        np.savez_compressed(file, *args, **kwargs)
    else:
        np.savez(file, *args, **kwargs)

