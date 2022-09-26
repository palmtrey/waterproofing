import json
from MendNet.mendnet.python.core import metrics
import numpy as np
import os
import trimesh
from tqdm import tqdm


def compare(in_obj, depth_offset_factor: float, truncation_factor: float, padding_factor: float) -> float:
    os.system('python -m processor.process_waterproof2 fractured_mug.obj temp.obj --depth_offset_factor ' + str(depth_offset_factor) + ' --truncation_factor ' + str(truncation_factor) + ' --padding ' + str(padding_factor))
    
    out_obj = trimesh.load('temp.obj')
    return metrics.chamfer(in_obj, out_obj)


# TODO: Separate alpha into three separate learning rates, one for each factor.
#       These should appropriately scale the gradients so they are updated correctly 
#       and do not explode/vanish. 

def modified_gradient_descent(depth_offset_factor: float, truncation_factor: float, padding_factor: float, alpha: float, iterations: int = 100) -> tuple:

    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations, 3))

    # theta_history[0, 0] = depth_offset_factor
    # theta_history[0, 1] = truncation_factor
    # theta_history[0, 2] = padding_factor

    
    in_obj = trimesh.load('fractured_mug.obj')
    for it in range(iterations):
        
        print('Iteration: ' + str(it))
        print('Calculating... ')

        current_cost = compare(in_obj, depth_offset_factor, truncation_factor, padding_factor)
        gradient_dof = (current_cost - cost_history[it]) / (theta_history[it, 1] - depth_offset_factor)
        gradient_tf = (current_cost - cost_history[it]) / (theta_history[it, 2] - truncation_factor)
        gradient_pf = (current_cost - cost_history[it]) / (theta_history[it, 1] - padding_factor)

        cost_history[it + 1] = current_cost
        theta_history[it + 1, 0] = depth_offset_factor
        theta_history[it + 1, 1] = truncation_factor
        theta_history[it + 1, 2] = padding_factor


        depth_offset_factor = depth_offset_factor - alpha * gradient_dof
        truncation_factor = truncation_factor - alpha * gradient_tf
        padding_factor = padding_factor - alpha * gradient_pf

        print('Current Cost: ' + str(current_cost))
        print('Gradient (dof): ' + str(gradient_dof))
        print('Gradient (tf): ' + str(gradient_tf))
        print('Gradient (pf): ' + str(gradient_pf))

        print('Depth Offset Factor (Old): ' + str(theta_history[it + 1, 0]))
        print('Depth Offset Factor (New): ' + str(depth_offset_factor))

        print('Truncation Factor (Old): ' + str(theta_history[it + 1, 1]))
        print('Truncation Factor (New): ' + str(truncation_factor))

        print('Padding Factor (Old): ' + str(theta_history[it + 1, 2]))
        print('Padding Factor (New): ' + str(padding_factor))


def plot_results(json_file: str) -> None:

    with json.load(json_file) as f:
        