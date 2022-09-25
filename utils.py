import json
from MendNet.mendnet.python.core import metrics
import numpy as np
import os
import trimesh
from tqdm import tqdm


def compare(in_obj: trimesh.Geometry, depth_offset_factor: float, truncation_factor: float, padding_factor: float) -> float:
    os.system('python -m processor.process_waterproof2 fractured_mug.obj temp.obj --depth_offset_factor ' + \
        str(depth_offset_factor) + ' --truncation_factor ' + str(truncation_factor) + ' --padding ' + str(padding_factor))
    
    out_obj = trimesh.load('temp.obj')
    return metrics.chamfer(in_obj, out_obj)