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
x01 = model.addVar(vtype = GRB.BINARY, name = 'x01')
x02 = model.addVar(vtype = GRB.BINARY, name = 'x02')
x03 = model.addVar(vtype = GRB.BINARY, name = 'x03')
x04 = model.addVar(vtype = GRB.BINARY, name = 'x04')
x05 = model.addVar(vtype = GRB.BINARY, name = 'x05')
x06 = model.addVar(vtype = GRB.BINARY, name = 'x06')
x07 = model.addVar(vtype = GRB.BINARY, name = 'x07')
x08 = model.addVar(vtype = GRB.BINARY, name = 'x08')
x09 = model.addVar(vtype = GRB.BINARY, name = 'x09')

x10 = model.addVar(vtype = GRB.BINARY, name = 'x10')
x12 = model.addVar(vtype = GRB.BINARY, name = 'x12')
x13 = model.addVar(vtype = GRB.BINARY, name = 'x13')
x14 = model.addVar(vtype = GRB.BINARY, name = 'x14')
x15 = model.addVar(vtype = GRB.BINARY, name = 'x15')
x16 = model.addVar(vtype = GRB.BINARY, name = 'x16')
x17 = model.addVar(vtype = GRB.BINARY, name = 'x17')
x18 = model.addVar(vtype = GRB.BINARY, name = 'x18')
x19 = model.addVar(vtype = GRB.BINARY, name = 'x19')

x20 = model.addVar(vtype = GRB.BINARY, name = 'x20')
x21 = model.addVar(vtype = GRB.BINARY, name = 'x21')
x23 = model.addVar(vtype = GRB.BINARY, name = 'x23')
x24 = model.addVar(vtype = GRB.BINARY, name = 'x24')
x25 = model.addVar(vtype = GRB.BINARY, name = 'x25')
x26 = model.addVar(vtype = GRB.BINARY, name = 'x26')
x27 = model.addVar(vtype = GRB.BINARY, name = 'x27')
x28 = model.addVar(vtype = GRB.BINARY, name = 'x28')
x29 = model.addVar(vtype = GRB.BINARY, name = 'x29')

x30 = model.addVar(vtype = GRB.BINARY, name = 'x30')
x31 = model.addVar(vtype = GRB.BINARY, name = 'x31')
x32 = model.addVar(vtype = GRB.BINARY, name = 'x32')
x34 = model.addVar(vtype = GRB.BINARY, name = 'x33')
x35 = model.addVar(vtype = GRB.BINARY, name = 'x34')
x36 = model.addVar(vtype = GRB.BINARY, name = 'x35')
x37 = model.addVar(vtype = GRB.BINARY, name = 'x37')
x38 = model.addVar(vtype = GRB.BINARY, name = 'x38')
x39 = model.addVar(vtype = GRB.BINARY, name = 'x39')

x40 = model.addVar(vtype = GRB.BINARY, name = 'x40')
x41 = model.addVar(vtype = GRB.BINARY, name = 'x41')
x42 = model.addVar(vtype = GRB.BINARY, name = 'x42')
x43 = model.addVar(vtype = GRB.BINARY, name = 'x43')
x45 = model.addVar(vtype = GRB.BINARY, name = 'x45')
x46 = model.addVar(vtype = GRB.BINARY, name = 'x46')
x47 = model.addVar(vtype = GRB.BINARY, name = 'x47')
x48 = model.addVar(vtype = GRB.BINARY, name = 'x48')
x49 = model.addVar(vtype = GRB.BINARY, name = 'x49')

x50 = model.addVar(vtype = GRB.BINARY, name = 'x50')
x51 = model.addVar(vtype = GRB.BINARY, name = 'x51')
x52 = model.addVar(vtype = GRB.BINARY, name = 'x52')
x53 = model.addVar(vtype = GRB.BINARY, name = 'x53')
x54 = model.addVar(vtype = GRB.BINARY, name = 'x54')
x56 = model.addVar(vtype = GRB.BINARY, name = 'x56')
x57 = model.addVar(vtype = GRB.BINARY, name = 'x57')
x58 = model.addVar(vtype = GRB.BINARY, name = 'x58')
x59 = model.addVar(vtype = GRB.BINARY, name = 'x59')

x60 = model.addVar(vtype = GRB.BINARY, name = 'x60')
x61 = model.addVar(vtype = GRB.BINARY, name = 'x61')
x62 = model.addVar(vtype = GRB.BINARY, name = 'x62')
x63 = model.addVar(vtype = GRB.BINARY, name = 'x63')
x64 = model.addVar(vtype = GRB.BINARY, name = 'x64')
x65 = model.addVar(vtype = GRB.BINARY, name = 'x65')
x67 = model.addVar(vtype = GRB.BINARY, name = 'x67')
x68 = model.addVar(vtype = GRB.BINARY, name = 'x68')
x69 = model.addVar(vtype = GRB.BINARY, name = 'x69')

x70 = model.addVar(vtype = GRB.BINARY, name = 'x70')
x71 = model.addVar(vtype = GRB.BINARY, name = 'x71')
x72 = model.addVar(vtype = GRB.BINARY, name = 'x72')
x73 = model.addVar(vtype = GRB.BINARY, name = 'x73')
x74 = model.addVar(vtype = GRB.BINARY, name = 'x74')
x75 = model.addVar(vtype = GRB.BINARY, name = 'x75')
x76 = model.addVar(vtype = GRB.BINARY, name = 'x76')
x78 = model.addVar(vtype = GRB.BINARY, name = 'x78')
x79 = model.addVar(vtype = GRB.BINARY, name = 'x79')

x80 = model.addVar(vtype = GRB.BINARY, name = 'x80')
x81 = model.addVar(vtype = GRB.BINARY, name = 'x81')
x82 = model.addVar(vtype = GRB.BINARY, name = 'x82')
x83 = model.addVar(vtype = GRB.BINARY, name = 'x83')
x84 = model.addVar(vtype = GRB.BINARY, name = 'x84')
x85 = model.addVar(vtype = GRB.BINARY, name = 'x85')
x86 = model.addVar(vtype = GRB.BINARY, name = 'x86')
x87 = model.addVar(vtype = GRB.BINARY, name = 'x87')
x89 = model.addVar(vtype = GRB.BINARY, name = 'x89')

x90 = model.addVar(vtype = GRB.BINARY, name = 'x90')
x91 = model.addVar(vtype = GRB.BINARY, name = 'x91')
x92 = model.addVar(vtype = GRB.BINARY, name = 'x92')
x93 = model.addVar(vtype = GRB.BINARY, name = 'x93')
x94 = model.addVar(vtype = GRB.BINARY, name = 'x94')
x95 = model.addVar(vtype = GRB.BINARY, name = 'x95')
x96 = model.addVar(vtype = GRB.BINARY, name = 'x96')
x97 = model.addVar(vtype = GRB.BINARY, name = 'x97')
x98 = model.addVar(vtype = GRB.BINARY, name = 'x98')


#Yi - whether or not we visit location i
y0 = 1
y1 = model.addVar(vtype = GRB.BINARY, name = 'y1')
y2 = model.addVar(vtype = GRB.BINARY, name = 'y2')
y3 = model.addVar(vtype = GRB.BINARY, name = 'y3')
y4 = model.addVar(vtype = GRB.BINARY, name = 'y4')
y5 = model.addVar(vtype = GRB.BINARY, name = 'y5')
y6 = model.addVar(vtype = GRB.BINARY, name = 'y6')
y7 = model.addVar(vtype = GRB.BINARY, name = 'y7')
y8 = model.addVar(vtype = GRB.BINARY, name = 'y8')
y9 = model.addVar(vtype = GRB.BINARY, name = 'y9')
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
t61 = t16
t17 = 38.0788655293195
t71 = t17
t18 = 51.1077293567225
t81 = t18
t19 = 69.5269731830747
t91 = t19

t23 = 71.2530701092942
t32 = t23
t24 = 48.1040538832227
t42 = t24
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

model.addConstr(sum([k1*y1 + k2*y2 + k3*y3 + k4*y4 + k5*y5 + k6*y6 + k7*y7 + k8*y8 + k9*y9]) <= c)

#must enter each location no more than once, no less than 0
model.addConstr(sum([x10*y1 + x12*y1 + x13*y1 + x14*y1 + x15*y1 + x16*y1 + x17*y1 + x18*y1 + x19*y1]) <= 1)
model.addConstr(sum([x20*y2 + x21*y2 + x23*y1 + x24*y1 + x25*y1 + x26*y1 + x27*y1 + x28*y1 + x29*y1]) <= 1)
model.addConstr(sum([x30*y3 + x31*y3 + x32*y3 + x34*y3 + x35*y3 + x36*y3 + x37*y3 + x38*y3 + x39*y3]) <= 1)
model.addConstr(sum([x40*y4 + x41*y4 + x42*y4 + x43*y4 + x45*y4 + x46*y4 + x47*y4 + x48*y4 + x49*y4]) <= 1)
model.addConstr(sum([x50*y5 + x51*y5 + x52*y5 + x53*y5 + x54*y5 + x56*y5 + x57*y5 + x58*y5 + x59*y5]) <= 1)
model.addConstr(sum([x60*y6 + x61*y6 + x62*y6 + x63*y6 + x64*y6 + x65*y6 + x67*y6 + x68*y6 + x69*y6]) <= 1)
model.addConstr(sum([x70*y7 + x71*y7 + x72*y7 + x73*y7 + x74*y7 + x75*y7 + x76*y7 + x78*y7 + x79*y7]) <= 1)
model.addConstr(sum([x80*y8 + x81*y8 + x82*y8 + x83*y8 + x84*y8 + x85*y8 + x86*y8 + x87*y8 + x89*y8]) <= 1)
model.addConstr(sum([x90*y9 + x91*y9 + x92*y9 + x93*y9 + x94*y9 + x95*y9 + x96*y9 + x97*y9 + x98*y9]) <= 1)

model.addConstr(sum([x10*y1 + x12*y1 + x13*y1 + x14*y1 + x15*y1 + x16*y1 + x17*y1 + x18*y1 + x19*y1]) >= 0)
model.addConstr(sum([x20*y2 + x21*y2 + x23*y1 + x24*y1 + x25*y1 + x26*y1 + x27*y1 + x28*y1 + x29*y1]) >= 0)
model.addConstr(sum([x30*y3 + x31*y3 + x32*y3 + x34*y3 + x35*y3 + x36*y3 + x37*y3 + x38*y3 + x39*y3]) >= 0)
model.addConstr(sum([x40*y4 + x41*y4 + x42*y4 + x43*y4 + x45*y4 + x46*y4 + x47*y4 + x48*y4 + x49*y4]) >= 0)
model.addConstr(sum([x50*y5 + x51*y5 + x52*y5 + x53*y5 + x54*y5 + x56*y5 + x57*y5 + x58*y5 + x59*y5]) >= 0)
model.addConstr(sum([x60*y6 + x61*y6 + x62*y6 + x63*y6 + x64*y6 + x65*y6 + x67*y6 + x68*y6 + x69*y6]) >= 0)
model.addConstr(sum([x70*y7 + x71*y7 + x72*y7 + x73*y7 + x74*y7 + x75*y7 + x76*y7 + x78*y7 + x79*y7]) >= 0)
model.addConstr(sum([x80*y8 + x81*y8 + x82*y8 + x83*y8 + x84*y8 + x85*y8 + x86*y8 + x87*y8 + x89*y8]) >= 0)
model.addConstr(sum([x90*y9 + x91*y9 + x92*y9 + x93*y9 + x94*y9 + x95*y9 + x96*y9 + x97*y9 + x98*y9]) >= 0)

#must leave each location no more than once, no less than 0
model.addConstr(sum([x01*y1 + x21*y1 + x31*y1 + x41*y1 + x51*y1 + x61*y1 + x71*y1 + x81*y1 + x91*y1]) <= 1)
model.addConstr(sum([x02*y2 + x12*y2 + x32*y2 + x42*y2 + x52*y2 + x62*y2 + x72*y2 + x82*y2 + x92*y2]) <= 1)
model.addConstr(sum([x03*y3 + x13*y3 + x23*y3 + x43*y3 + x53*y3 + x63*y3 + x73*y3 + x83*y3 + x93*y3]) <= 1)
model.addConstr(sum([x04*y4 + x14*y4 + x24*y4 + x34*y4 + x54*y4 + x64*y4 + x74*y4 + x84*y4 + x94*y4]) <= 1)
model.addConstr(sum([x05*y5 + x15*y5 + x25*y5 + x35*y5 + x45*y5 + x65*y5 + x75*y5 + x85*y5 + x95*y5]) <= 1)
model.addConstr(sum([x06*y6 + x16*y6 + x26*y6 + x36*y6 + x46*y6 + x56*y6 + x76*y6 + x86*y6 + x96*y6]) <= 1)
model.addConstr(sum([x07*y7 + x17*y7 + x27*y7 + x37*y7 + x47*y7 + x57*y7 + x67*y7 + x87*y7 + x97*y7]) <= 1)
model.addConstr(sum([x08*y8 + x18*y8 + x28*y8 + x38*y8 + x48*y8 + x58*y8 + x68*y8 + x78*y8 + x98*y8]) <= 1)
model.addConstr(sum([x09*y9 + x19*y9 + x29*y9 + x39*y9 + x49*y9 + x59*y9 + x69*y9 + x79*y9 + x89*y9]) <= 1)

model.addConstr(sum([x01*y1 + x21*y1 + x31*y1 + x41*y1 + x51*y1 + x61*y1 + x71*y1 + x81*y1 + x91*y1]) >= 0)
model.addConstr(sum([x02*y2 + x12*y2 + x32*y2 + x42*y2 + x52*y2 + x62*y2 + x72*y2 + x82*y2 + x92*y2]) >= 0)
model.addConstr(sum([x03*y3 + x13*y3 + x23*y3 + x43*y3 + x53*y3 + x63*y3 + x73*y3 + x83*y3 + x93*y3]) >= 0)
model.addConstr(sum([x04*y4 + x14*y4 + x24*y4 + x34*y4 + x54*y4 + x64*y4 + x74*y4 + x84*y4 + x94*y4]) >= 0)
model.addConstr(sum([x05*y5 + x15*y5 + x25*y5 + x35*y5 + x45*y5 + x65*y5 + x75*y5 + x85*y5 + x95*y5]) >= 0)
model.addConstr(sum([x06*y6 + x16*y6 + x26*y6 + x36*y6 + x46*y6 + x56*y6 + x76*y6 + x86*y6 + x96*y6]) >= 0)
model.addConstr(sum([x07*y7 + x17*y7 + x27*y7 + x37*y7 + x47*y7 + x57*y7 + x67*y7 + x87*y7 + x97*y7]) >= 0)
model.addConstr(sum([x08*y8 + x18*y8 + x28*y8 + x38*y8 + x48*y8 + x58*y8 + x68*y8 + x78*y8 + x98*y8]) >= 0)
model.addConstr(sum([x09*y9 + x19*y9 + x29*y9 + x39*y9 + x49*y9 + x59*y9 + x69*y9 + x79*y9 + x89*y9]) >= 0)

#for leaving starting point
model.addConstr(sum([x01*y0 + x02*y0 + x03*y0 + x04*y0 + x05*y0 + x06*y0 + x07*y0 + x08*y0 + x09*y0]) <= 1) 
model.addConstr(sum([x01*y0 + x02*y0 + x03*y0 + x04*y0 + x05*y0 + x06*y0 + x07*y0 + x08*y0 + x09*y0]) >= 1)

#for entering end point
model.addConstr(sum([x10*y0 + x20*y0 + x30*y0 + x40*y0 + x50*y0 + x60*y0 + x70*y0 + x80*y0 + x90*y0]) <= 1)
model.addConstr(sum([x10*y0 + x20*y0 + x30*y0 + x40*y0 + x50*y0 + x60*y0 + x70*y0 + x80*y0 + x90*y0]) >= 1)


model.addConstr(sum([x01 * t01 + x02 * t02 + x03 * t03 + x04 * t04 + x05 * t05 + x06 * t06 + x07 * t07 + x08 * t08 + x09 * t09 + x10 * t10 + x12 * t12 + x13 * t13 + x14 * t14 + x15 * t15 + x16 * t16 + x17 * t17 + x18 * t18 + x19 * t19 + x20 * t20 + x21 * t21 + x23 * t23 + x24 * t24 + x25 * t25 + x26 * t26 + x27 * t27 + x28 * t28 + x29 * t29 + x30 * t30 + x31 * t31 + x32 * t32 + x34 * t34 + x35 * t35 + x36 * t36 + x37 * t37 + x38 * t38 + x39 * t39 + x40 * t40 + x41 * t41 + x42 * t42 + x43 * t43 + x45 * t45 + x46 * t46 + x47 * t47 + x48 * t48 + x49 * t49 + x50 * t50 + x51 * t51 + x52 * t52 + x53 * t53 + x54 * t54 + x56 * t56 + x57 * t57 + x58 * t58 + x59 * t59 + x60 * t60 + x61 * t61 + x62 * t62 + x63 * t63 + x64 * t64 + x65 * t65 + x67 * t67 + x68 * t68 + x69 * t69 + x70 * t70 + x71 * t71 + x72 * t72 + x73 * t73 + x74 * t74 + x75 * t75 + x76 * t76 + x78 * t78 + x79 * t79 + x80 * t80 + x81 * t81 + x82 * t82 + x83 * t83 + x84 * t84 + x85 * t85 + x86 * t86 + x87 * t87 + x89 * t89 + x90 * t90 + x91 * t91 + x92 * t92 + x93 * t93 + x94 * t94 + x95 * t95 + x96 * t96 + x97 * t97 + x98 * t98]) <= m)

model.setObjective(sum([p1*y1, p2*y2, p3*y3, p3*y4, p5*y5, p6*y6, p7*y7, p8*y8, p9*y9]), GRB.MAXIMIZE)
model.optimize()

for i,y in enumerate(y_list):
	print((i+1, y.x))

print('')
print('')

xij = [x01, x02, x03, x04, x05, x06, x07, x08, x09, x10, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x45, x46, x47, x48, x49, x50, x51, x52, x53, x54, x56, x57, x58, x59, x60, x61, x62, x63, x64, x65, x67, x68, x69, x70, x71, x72, x73, x74, x75, x76, x78, x79, x80, x81, x82, x83, x84, x85, x86, x87, x89, x90, x91, x92, x93, x94, x95, x96, x97, x98]

for i,j in enumerate(xij):
	if j.x == 1:
		print((i,j.x))