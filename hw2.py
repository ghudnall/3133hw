import sys
import math
import random
import itertools
from gurobipy import *

model = Model('HW2')
n = 9
m = 150
c = 20

#set parameters
model.setParam('OutputFlag', True)


#Xij
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
x66 = m.addVar(vtype = GRB.BINARY, name = 'x65')
x67 = m.addVar(vtype = GRB.BINARY, name = 'x67')
x68 = m.addVar(vtype = GRB.BINARY, name = 'x68')
x69 = m.addVar(vtype = GRB.BINARY, name = 'x69')

x70 = m.addVar(vtype = GRB.BINARY, name = 'x70')
x71 = m.addVar(vtype = GRB.BINARY, name = 'x71')
x72 = m.addVar(vtype = GRB.BINARY, name = 'x72')
x73 = m.addVar(vtype = GRB.BINARY, name = 'x73')
x74 = m.addVar(vtype = GRB.BINARY, name = 'x74')
x75 = m.addVar(vtype = GRB.BINARY, name = 'x75')
x76 = m.addVar(vtype = GRB.BINARY, name = 'x76')
x78 = m.addVar(vtype = GRB.BINARY, name = 'x78')
x79 = m.addVar(vtype = GRB.BINARY, name = 'x79')

x80 = m.addVar(vtype = GRB.BINARY, name = 'x80')
x81 = m.addVar(vtype = GRB.BINARY, name = 'x81')
x82 = m.addVar(vtype = GRB.BINARY, name = 'x82')
x83 = m.addVar(vtype = GRB.BINARY, name = 'x83')
x84 = m.addVar(vtype = GRB.BINARY, name = 'x84')
x85 = m.addVar(vtype = GRB.BINARY, name = 'x85')
x86 = m.addVar(vtype = GRB.BINARY, name = 'x86')
x87 = m.addVar(vtype = GRB.BINARY, name = 'x87')
x89 = m.addVar(vtype = GRB.BINARY, name = 'x89')

x90 = m.addVar(vtype = GRB.BINARY, name = 'x90')
x91 = m.addVar(vtype = GRB.BINARY, name = 'x91')
x92 = m.addVar(vtype = GRB.BINARY, name = 'x92')
x93 = m.addVar(vtype = GRB.BINARY, name = 'x93')
x94 = m.addVar(vtype = GRB.BINARY, name = 'x94')
x95 = m.addVar(vtype = GRB.BINARY, name = 'x95')
x96 = m.addVar(vtype = GRB.BINARY, name = 'x96')
x97 = m.addVar(vtype = GRB.BINARY, name = 'x97')
x98 = m.addVar(vtype = GRB.BINARY, name = 'x98')


#Yi - whether or not we visit location i
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

t01 = 21.189620100417
t10 = 21.189620100417
t02 = 19.7989898732233
t20 = 19.7989898732233
t03 = 57.5586657246326
t30 = 57.5586657246326
t04  = 43.8406204335659
t40 = t04
t05 = 55.1543289325507
t50 = t05
t06 = 58.309518948453
t60 = t06
t07 = 57.0350769263968
t70 = t07
t08 = 72.0069441095787
t80 = t08
t09 = 89.6270048590267
t90 = t09

t12 = 21.8403296678415
t21 = 21.8403296678415
t13 = 51.4198405287297
t31 = 51.4198405287297
t14 = 26.4007575648881
t41 = t14
t15 = 37.2155881318567
t51 = t15
t16 = 47.6340214552582
t16 = t61
t17 = 38.0788655293195
t71 = t17
t18 = 51.1077293567225
t81 = t18
t19 = 69.5269731830747
t91 = t19

t23 = 71.2530701092942
t32 = t23
t24 = 48.1040538832227
t42 t24
t25 = 58.6003412959344
t52 = t25
t26 = 39.3954312071844
t62 = t26
t27 = 44.6430285710994
t72 = t27
t28 = 68.622153857191
t82 = t28
t29 = 88.5268320906153
t92 = t29

t34 = 34.7131099154195
t43 = t34
t35 = 35.8468966578698
t53 = t35
t36 = 96.6074531286277
t63 = t36
t37 = 76.694197955256
t73 = t37
t38 = 60.9261848469112
t83 = t38
t39 = 65.1920240520264
t93 = t39

t45 = 11.3137084989847
t54 = t45
t46 = 63.8905313798531
t64 = t46
t47 = 42.0119030752
t74 = t47
t48 = 33.060550509633
t84 = t48
t49 = 46.9574275274955
t94 = t49

t56 = 69.8713102782536
t65 = t56
t57 = 44.7772263544762
t75 = t57
t58 = 25.7099202643648
t85 = t58
t59 = 36.4005494464025
t95 = t59

t67 = 28.8617393793236
t76 = t67
t68 = 64.5368112010502
t86 = t68
t69 = 85.1645466141868
t96 = t69

t78 = 35.6931365951495
t87 = t78
t79 = 56.3205113613148
t97 = t79

t89 = 21.0237960416286
t98 = t89


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
>>>>>>> 2b8e9f483945232eb29bb433658a368984809c8e
