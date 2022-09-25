# Overview of Waterproofing Hyperparameter Optimization

## Setup of workspace
- cd /home/lambne/dev/projects/MendNet3-Internal
- source setup.sh
- cd ~/waterproofing
- python -m processor.process_waterproof2 -h (Show help)

## Hyperparameters that affect expansion and resolution of the object. 
Optimize with respect to these three hyperparameters to begin with:
- Depth offset factor (probably changes size expansion most drastically)
  - Default: 1.5
- Truncation factor (may also have impact on expansion)
  - Default: 10
- Padding (probably affects size of voxels)
  - Default: 0.1

## Notes
- It should only be necessary to use one object to optimize with.
- Use the trimesh library to import and export models.
- Use metrics.py chamfer function to compare before and after models. Distance should be smallest possible using the hyperparameters.
- Using the --smooth option will perform voxel smoothing, making the model output model more similiar to the original.
    This is, however, time consuming. Therefore, optimize the hyperparameters without the --smooth option to begin with. Once the
    params have been optimized without the --smooth option, they may be optimized further using the --smooth option.
