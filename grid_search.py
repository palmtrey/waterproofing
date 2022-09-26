import datetime
import json
from MendNet.mendnet.python.core import metrics
import numpy as np
import trimesh
import time
from tqdm import tqdm
import utils

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 




if __name__ == '__main__':

    output_file = 'results_fine.json'

    depth_offset_factors = list(np.arange(0.1, 1.1, 0.1))
    depth_offset_factors = [round(x, 2) for x in depth_offset_factors]
    
    truncation_factors = [2]
    
    padding_factors = list(np.arange(0.001, 0.101, 0.01))
    padding_factors = [round(x, 3) for x in padding_factors]
    

    print('Depth Offset Factors:')
    print(depth_offset_factors)

    print('\nTruncation Factors:')
    print(truncation_factors)

    print('\nPadding Factors:')
    print(padding_factors)

    total_comparisons = len(depth_offset_factors) * len(truncation_factors) * len(padding_factors)
    complete_comparisons = 0

    results = {}

    in_obj = trimesh.load('fractured_mug.obj')
    
    for dof_idx, depth_offset_factor in enumerate(depth_offset_factors):
        
        for tf_idx, truncation_factor in enumerate(truncation_factors):
            

            for pf_idx, padding_factor in enumerate(padding_factors):
                print('\n----------Comparing ' + str(complete_comparisons+1) + '/' + str(total_comparisons) + '----------')
                print('Depth Offset Factor: ' + str(depth_offset_factor) + ' (' + str(dof_idx) + '/' + str(len(depth_offset_factors)) + ')')
                print('Truncation Factor: ' + str(truncation_factor) + ' (' + str(tf_idx) + '/' + str(len(truncation_factors)) + ')')
                print('Padding Factor: ' + str(padding_factor) + ' (' + str(pf_idx) + '/' + str(len(padding_factors)) + ')')
                

                before = time.time()
                result = utils.compare(in_obj, depth_offset_factor, truncation_factor, padding_factor)
                results['depth offset factor: ' + str(depth_offset_factor) + ', truncation factor: ' + str(truncation_factor) + ', padding factor: ' + str(padding_factor)] = result
                after = time.time()

                complete_comparisons += 1

                print('Chamfer Distance: ' + str(round(result, 8)))
                print('Time elapsed: ' + str(round(after-before, 2)) + ' seconds')
                print('Done comparing ' + str(complete_comparisons) + '/' + str(total_comparisons))
                print('Approximate time remaining: ' + str(datetime.timedelta(seconds=round((after-before) * (total_comparisons-complete_comparisons)))))
                print('--------------------------------------------------\n')

                with open(output_file, 'w') as f:
                    json.dump(results, f)

                # break
            # break
        # break

 