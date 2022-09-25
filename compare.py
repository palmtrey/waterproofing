import json
from MendNet.mendnet.python.core import metrics
import numpy as np
import os
import trimesh
from tqdm import tqdm

    
if __name__ == '__main__':

    depth_offset_factors = list(np.arange(0.1, 5.1, 0.1))
    depth_offset_factors = [round(x, 2) for x in depth_offset_factors]
    print('Depth Offset Factors:')
    print(depth_offset_factors)

    truncation_factors = list(np.arange(1, 21, 1))
    print('\nTruncation Factors:')
    print(truncation_factors)

    padding_factors = list(np.arange(0.01, 0.5, 0.02))
    padding_factors = [round(x, 3) for x in padding_factors]
    print('\nPadding Factors:')
    print(padding_factors)


    output_dict = {}

    in_obj = trimesh.load('fractured_mug.obj')

    for depth_offset_factor in tqdm(depth_offset_factors):
        os.system('python -m processor.process_waterproof2 fractured_mug.obj out3.obj --depth_offset_factor ' + str(depth_offset_factor))
        
        out_obj = trimesh.load('out3.obj')
        distance = metrics.chamfer(in_obj, out_obj)

        print('Depth Offset Factor: ' + str(depth_offset_factor))
        print('Distance: ' + str(distance))
        
        output_dict[depth_offset_factor] = distance

    print(output_dict)

    with open('depth_offset_factor_results.txt', 'w') as f:
        json.dump(output_dict, f)