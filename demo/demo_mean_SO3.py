import os

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

import numpy as np

import pySymStat

if __name__ == '__main__':

    n = 100

    # generated N spatial rotations represented by unit quaternions
    quats = np.random.randn(n, 4)
    quats /= np.linalg.norm(quats, axis = 1)[:, np.newaxis]
    print(quats)

    # print(np.linalg.norm(quats, axis = 1))
    print("mean of 100 spatial rotations:\n", pySymStat.averaging_SO3.mean_SO3(quats))
