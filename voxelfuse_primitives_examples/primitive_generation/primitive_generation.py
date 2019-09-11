"""
Copyright 2018
Dan Aukes, Cole Brauer
"""

import PyQt5.QtGui as qg
import sys
from voxelfuse_primitives.solid import Solid
from voxelfuse.mesh import Mesh
from voxelfuse.plot import Plot

if __name__=='__main__':
    app1 = qg.QApplication(sys.argv)

    model1 = Solid.cube(11, (0, 0, 0), 1)
    model2 = Solid.cuboid((11, 20, 6), (13, 0, 0), 2)
    model3 = Solid.sphere(5, (31, 5, 5), 3)
    model4 = Solid.cylinder(5, 15, (44, 5, 0), 4)
    model5 = Solid.cone(1, 5, 15, (57, 5, 0), 5)
    model6 = Solid.pyramid(0, 5, 15, (70, 5, 0), 6)

    model_result = model1 | model2 | model3 | model4 | model5 | model6

    # Create mesh data
    mesh1 = Mesh.fromVoxelModel(model_result)

    # Create plot
    plot1 = Plot(mesh1)
    plot1.show()
    app1.processEvents()

    app1.exec_()
