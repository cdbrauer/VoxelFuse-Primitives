"""
Copyright 2018-2019
Dan Aukes, Cole Brauer

Extends the VoxelModel class with functions for generating linkages
"""

import os
import subprocess
import meshio
import numpy as np
from pyvox.parser import VoxParser
from voxelfuse.materials import materials
from scipy import ndimage
from numba import njit, prange

class Solid(VoxelModel):
    @classmethod
    def cube(cls, size = 1, mat = 1, x_coord = 0, y_coord = 0, z_coord = 0):
        model = np.ones((size, size, size, len(materials)))
        model = model.setMaterial(mat)
        return cls(model, x_coord, y_coord, z_coord)

