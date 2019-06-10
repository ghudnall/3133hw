import sys
import math
import random
import itertools
from gurobipy import *

t01 = 21.18962
t10 = 21.18962

t02 = 19.79899
t20 = 19.79899

t03 = 57.55867
t30 = 57.55867

t12 = 21.84033
t21 = 21.84033

t13 = 51.41984
t31 = 51.41984

# dist = {'01': 21.18962, '02': 19.79899, '03': 57.55867, '12': 21.84033, '13': 51.41984}
# m = Model()

vars = m.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='e')

# for i,j in vars.keys():
#     vars[j,i] = vars[i,j]

for i,j in vars.keys():
    print(vars[i,j])
