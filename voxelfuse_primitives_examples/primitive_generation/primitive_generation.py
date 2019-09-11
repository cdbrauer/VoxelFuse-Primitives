"""
Copyright 2018
Dan Aukes, Cole Brauer

Generate coupon for tensile testing
"""

import PyQt5.QtGui as qg
import sys
from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.plot import Plot
from voxelfuse_primitives.solid import Solid

if __name__=='__main__':
    # Settings
    model1 = Solid.cube(5)

    # Create mesh data
    mesh1 = Mesh.fromVoxelModel(model1)

    # Create plot
    plot1 = Plot(mesh1, grids=True)
    plot1.show()
    app1.processEvents()

    app1.exec_()
