import sys
import math
import random
import itertools
from gurobipy import *
poop = 'poop'
model = Model('HW1')
n = 9
m = 150
c = 20

#set parameters
model.setParam('OutputFlag', True)

x01 = m.addVar(vtype = GRB.BINARY, name = 'x01')
x02 = m.addVar(vtype = GRB.BINARY, name = 'x02')
x03 = m.addVar(vtype = GRB.BINARY, name = 'x03')
x04 = m.addVar(vtype = GRB.BINARY, name = 'x04')
x05 = m.addVar(vtype = GRB.BINARY, name = 'x05')
x06 = m.addVar(vtype = GRB.BINARY, name = 'x06')
x07 = m.addVar(vtype = GRB.BINARY, name = 'x07')
x08 = m.addVar(vtype = GRB.BINARY, name = 'x08')
x09 = m.addVar(vtype = GRB.BINARY, name = 'x09')

x10 = m.addVar(vtype = GRB.BINARY, name = 'x10')
x12 = m.addVar(vtype = GRB.BINARY, name = 'x12')
x13 = m.addVar(vtype = GRB.BINARY, name = 'x13')
x14 = m.addVar(vtype = GRB.BINARY, name = 'x14')
x15 = m.addVar(vtype = GRB.BINARY, name = 'x15')
x16 = m.addVar(vtype = GRB.BINARY, name = 'x16')
x17 = m.addVar(vtype = GRB.BINARY, name = 'x17')
x18 = m.addVar(vtype = GRB.BINARY, name = 'x18')
x19 = m.addVar(vtype = GRB.BINARY, name = 'x19')

x20 = m.addVar(vtype = GRB.BINARY, name = 'x20')
x21 = m.addVar(vtype = GRB.BINARY, name = 'x21')
x23 = m.addVar(vtype = GRB.BINARY, name = 'x23')
x24 = m.addVar(vtype = GRB.BINARY, name = 'x24')
x25 = m.addVar(vtype = GRB.BINARY, name = 'x25')
x26 = m.addVar(vtype = GRB.BINARY, name = 'x26')
x27 = m.addVar(vtype = GRB.BINARY, name = 'x27')
x28 = m.addVar(vtype = GRB.BINARY, name = 'x28')
x29 = m.addVar(vtype = GRB.BINARY, name = 'x29')


x30 = m.addVar(vtype = GRB.BINARY, name = 'x30')
x31 = m.addVar(vtype = GRB.BINARY, name = 'x31')
x32 = m.addVar(vtype = GRB.BINARY, name = 'x32')
x34 = m.addVar(vtype = GRB.BINARY, name = 'x33')
x35 = m.addVar(vtype = GRB.BINARY, name = 'x34')
x36 = m.addVar(vtype = GRB.BINARY, name = 'x35')
x37 = m.addVar(vtype = GRB.BINARY, name = 'x37')
x38 = m.addVar(vtype = GRB.BINARY, name = 'x38')
x39 = m.addVar(vtype = GRB.BINARY, name = 'x39')

x40 = m.addVar(vtype = GRB.BINARY, name = 'x40')
x41 = m.addVar(vtype = GRB.BINARY, name = 'x41')
x42 = m.addVar(vtype = GRB.BINARY, name = 'x42')
x43 = m.addVar(vtype = GRB.BINARY, name = 'x43')
x45 = m.addVar(vtype = GRB.BINARY, name = 'x45')
x46 = m.addVar(vtype = GRB.BINARY, name = 'x46')
x47 = m.addVar(vtype = GRB.BINARY, name = 'x47')
x48 = m.addVar(vtype = GRB.BINARY, name = 'x48')
x49 = m.addVar(vtype = GRB.BINARY, name = 'x49')

x50 = m.addVar(vtype = GRB.BINARY, name = 'x50')
x51 = m.addVar(vtype = GRB.BINARY, name = 'x51')
x52 = m.addVar(vtype = GRB.BINARY, name = 'x52')
x53 = m.addVar(vtype = GRB.BINARY, name = 'x53')
x54 = m.addVar(vtype = GRB.BINARY, name = 'x54')
x56 = m.addVar(vtype = GRB.BINARY, name = 'x56')
x57 = m.addVar(vtype = GRB.BINARY, name = 'x57')
x58 = m.addVar(vtype = GRB.BINARY, name = 'x58')
x59 = m.addVar(vtype = GRB.BINARY, name = 'x59')

x60 = m.addVar(vtype = GRB.BINARY, name = 'x60')
x61 = m.addVar(vtype = GRB.BINARY, name = 'x61')
x62 = m.addVar(vtype = GRB.BINARY, name = 'x62')
x63 = m.addVar(vtype = GRB.BINARY, name = 'x63')
x64 = m.addVar(vtype = GRB.BINARY, name = 'x64')
x56 = m.addVar(vtype = GRB.BINARY, name = 'x65')
x57 = m.addVar(vtype = GRB.BINARY, name = 'x67')
x58 = m.addVar(vtype = GRB.BINARY, name = 'x68')
x59 = m.addVar(vtype = GRB.BINARY, name = 'x69')

y1 = m.addVar(vtype = GRB.BINARY, name = 'y1')
y2 = m.addVar(vtype = GRB.BINARY, name = 'y2')
y3 = m.addVar(vtype = GRB.BINARY, name = 'y3')
y4 = m.addVar(vtype = GRB.BINARY, name = 'y4')
y5 = m.addVar(vtype = GRB.BINARY, name = 'y5')
y6 = m.addVar(vtype = GRB.BINARY, name = 'y6')
y7 = m.addVar(vtype = GRB.BINARY, name = 'y7')
y8 = m.addVar(vtype = GRB.BINARY, name = 'y8')
y9 = m.addVar(vtype = GRB.BINARY, name = 'y9')
y_list = [y1, y2, y3, y4, y5, y6, y7, y8, y9]

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

p1 = 3
p2 = 5
p3 = 6
p4 = 7
p5 = 8
p6 = 9
p7 = 2
p8 = 4
p9 = 5
p_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

k1 = 2
k2 = 6
k3 = 8
k4 = 9
k5 = 5
k6 = 4
k7 = 6
k8 = 9
k9 = 10
k_list = [k1, k2, k3, k4, k5, k6, k7, k8, k9]

# dist = {'01': 21.18962, '02': 19.79899, '03': 57.55867, '12': 21.84033, '13': 51.41984}

vars = model.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='e')

# for i,j in vars.keys():
#     vars[j,i] = vars[i,j]

for i,j in vars.keys():
    print(vars[i,j])

model.addConstr(sum([k1*y1 + k2*y2 + k3*y3 + k4*y4 + k5*y5 + k6*y6 + k7*y7 + k8*y8 + k9*y9]) <= c)

for i in range(len(y_list)):

    for j in range(len(y_list)):
        if i == j:
            continue
        else:
            model.addConstr(


model.setObjective(sum([p1*y1, p2*y2, p3*y3, p3*y4, p5*y5, p6*y6, p7*y7, p8*y8, p9*y9]), GRB.MAXIMIZE)
model.optimize
