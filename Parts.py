# -*- coding: mbcs -*-
# Do not delete the following import lines
import math
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

###########################################
# Variables:
#############

# Rectangle coordinates:
p1 = (0.5,0.5)
p2 = (-0.5,-0.5)
area_ratio = 0.7

rectangle_area = abs(p1[0]-p1[0])*abs(p1[1]-p2[1])
radius = math.sqrt(area_ratio*rectangle_area/math.pi)

# Circle Coordinate
centre_point = (0,0)
circle_point = (radius,0)

# thickness
thickness = 0.1


matrix_sketch = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=10.0)
g, v, d, c = matrix_sketch.geometry, matrix_sketch.vertices, matrix_sketch.dimensions, matrix_sketch.constraints
matrix_sketch.setPrimaryObject(option=STANDALONE)
matrix_sketch.rectangle(point1=(p1[0], p1[1]), point2=(p2[0], p2[1]))
matrix_sketch.CircleByCenterPerimeter(center=(centre_point[0], centre_point[1]), point1=(circle_point[0], circle_point[1]))
matrix_part = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D,
                               type=DEFORMABLE_BODY)
matrix_part = mdb.models['Model-1'].parts['Matrix']
matrix_part.BaseSolidExtrude(sketch=matrix_sketch, depth=thickness)

matrix_sketch.unsetPrimaryObject()
matrix_part = mdb.models['Model-1'].parts['Matrix']
session.viewports['Viewport: 1'].setValues(displayedObject=matrix_part)
del mdb.models['Model-1'].sketches['__profile__']



fiber_sketch = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                             sheetSize=10.0)

g, v, d, c = fiber_sketch.geometry, fiber_sketch.vertices, fiber_sketch.dimensions, fiber_sketch.constraints
fiber_sketch.setPrimaryObject(option=STANDALONE)


fiber_sketch.CircleByCenterPerimeter(center=(centre_point[0], centre_point[1]), point1=(circle_point[0], circle_point[1]))
fiber_part = mdb.models['Model-1'].Part(name='Fiber', dimensionality=THREE_D,
                               type=DEFORMABLE_BODY)
fiber_part = mdb.models['Model-1'].parts['Fiber']
fiber_part.BaseSolidExtrude(sketch=fiber_sketch, depth=thickness)

fiber_sketch.unsetPrimaryObject()
fiber_part = mdb.models['Model-1'].parts['Fiber']
session.viewports['Viewport: 1'].setValues(displayedObject=fiber_part)
del mdb.models['Model-1'].sketches['__profile__']
