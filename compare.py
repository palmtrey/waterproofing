import json
from MendNet.mendnet.python.core import metrics
import numpy as np
import os
import trimesh
from tqdm import tqdm
import utils

    
if __name__ == '__main__':

    # depth_offset_factors = list(np.arange(0.1, 5.1, 0.1))
    # depth_offset_factors = [round(x, 2) for x in depth_offset_factors]
    # print('Depth Offset Factors:')
    # print(depth_offset_factors)

    # truncation_factors = list(np.arange(1, 21, 1))
    # print('\nTruncation Factors:')
    # print(truncation_factors)

    # padding_factors = list(np.arange(0.01, 0.5, 0.02))
    # padding_factors = [round(x, 3) for x in padding_factors]
    # print('\nPadding Factors:')
    # print(padding_factors)


    output_dict = {}

    depth_offset_factor = 1.5
    truncation_factor = 10
    padding = 0.1

    alpha = 10000

    utils.modified_gradient_descent(depth_offset_factor, truncation_factor, padding, alpha, iterations=10)
        