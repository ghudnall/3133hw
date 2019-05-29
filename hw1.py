from gurobipy import GRB, Model

m = Model('HW1')

#set parameters
m.setParam('OutputFlag', True)

#add variables

x11 = m.addVar(vtype = GRB.BINARY, name = 'x11')
x12 = m.addVar(vtype = GRB.BINARY, name = 'x12')
x13 = m.addVar(vtype = GRB.BINARY, name = 'x13')
x14 = m.addVar(vtype = GRB.BINARY, name = 'x14')
x15 = m.addVar(vtype = GRB.BINARY, name = 'x15')
x16 = m.addVar(vtype = GRB.BINARY, name = 'x16')
x17 = m.addVar(vtype = GRB.BINARY, name = 'x17')
x18 = m.addVar(vtype = GRB.BINARY, name = 'x18')
x19 = m.addVar(vtype = GRB.BINARY, name = 'x19')

x21 = m.addVar(vtype = GRB.BINARY, name = 'x21')
x22 = m.addVar(vtype = GRB.BINARY, name = 'x22')
x23 = m.addVar(vtype = GRB.BINARY, name = 'x23')
x24 = m.addVar(vtype = GRB.BINARY, name = 'x24')
x25 = m.addVar(vtype = GRB.BINARY, name = 'x25')
x26 = m.addVar(vtype = GRB.BINARY, name = 'x26')
x27 = m.addVar(vtype = GRB.BINARY, name = 'x27')
x28 = m.addVar(vtype = GRB.BINARY, name = 'x28')
x29 = m.addVar(vtype = GRB.BINARY, name = 'x29')

x31 = m.addVar(vtype = GRB.BINARY, name = 'x31')
x32 = m.addVar(vtype = GRB.BINARY, name = 'x32')
x33 = m.addVar(vtype = GRB.BINARY, name = 'x33')
x34 = m.addVar(vtype = GRB.BINARY, name = 'x34')
x35 = m.addVar(vtype = GRB.BINARY, name = 'x35')
x36 = m.addVar(vtype = GRB.BINARY, name = 'x36')
x37 = m.addVar(vtype = GRB.BINARY, name = 'x37')
x38 = m.addVar(vtype = GRB.BINARY, name = 'x38')
x39 = m.addVar(vtype = GRB.BINARY, name = 'x39')

y11 = m.addVar(vtype = GRB.BINARY, name = 'y11')
y12 = m.addVar(vtype = GRB.BINARY, name = 'y12')
y13 = m.addVar(vtype = GRB.BINARY, name = 'y13')
y14 = m.addVar(vtype = GRB.BINARY, name = 'y14')
y15 = m.addVar(vtype = GRB.BINARY, name = 'y15')
y16 = m.addVar(vtype = GRB.BINARY, name = 'y16')
y17 = m.addVar(vtype = GRB.BINARY, name = 'y17')
y18 = m.addVar(vtype = GRB.BINARY, name = 'y18')
y19 = m.addVar(vtype = GRB.BINARY, name = 'y19')

y21 = m.addVar(vtype = GRB.BINARY, name = 'y21')
y22 = m.addVar(vtype = GRB.BINARY, name = 'y22')
y23 = m.addVar(vtype = GRB.BINARY, name = 'y23')
y24 = m.addVar(vtype = GRB.BINARY, name = 'y24')
y25 = m.addVar(vtype = GRB.BINARY, name = 'y25')
y26 = m.addVar(vtype = GRB.BINARY, name = 'y26')
y27 = m.addVar(vtype = GRB.BINARY, name = 'y27')
y28 = m.addVar(vtype = GRB.BINARY, name = 'y28')
y29 = m.addVar(vtype = GRB.BINARY, name = 'y29')

y31 = m.addVar(vtype = GRB.BINARY, name = 'y31')
y32 = m.addVar(vtype = GRB.BINARY, name = 'y32')
y33 = m.addVar(vtype = GRB.BINARY, name = 'y33')
y34 = m.addVar(vtype = GRB.BINARY, name = 'y34')
y35 = m.addVar(vtype = GRB.BINARY, name = 'y35')
y36 = m.addVar(vtype = GRB.BINARY, name = 'y36')
y37 = m.addVar(vtype = GRB.BINARY, name = 'y37')
y38 = m.addVar(vtype = GRB.BINARY, name = 'y38')
y39 = m.addVar(vtype = GRB.BINARY, name = 'y39')

z11 = m.addVar(vtype = GRB.BINARY, name = 'z11')
z12 = m.addVar(vtype = GRB.BINARY, name = 'z12')
z13 = m.addVar(vtype = GRB.BINARY, name = 'z13')
z14 = m.addVar(vtype = GRB.BINARY, name = 'z14')
z15 = m.addVar(vtype = GRB.BINARY, name = 'z15')
z16 = m.addVar(vtype = GRB.BINARY, name = 'z16')
z17 = m.addVar(vtype = GRB.BINARY, name = 'z17')
z18 = m.addVar(vtype = GRB.BINARY, name = 'z18')
z19 = m.addVar(vtype = GRB.BINARY, name = 'z19')

z21 = m.addVar(vtype = GRB.BINARY, name = 'z21')
z22 = m.addVar(vtype = GRB.BINARY, name = 'z22')
z23 = m.addVar(vtype = GRB.BINARY, name = 'z23')
z24 = m.addVar(vtype = GRB.BINARY, name = 'z24')
z25 = m.addVar(vtype = GRB.BINARY, name = 'z25')
z26 = m.addVar(vtype = GRB.BINARY, name = 'z26')
z27 = m.addVar(vtype = GRB.BINARY, name = 'z27')
z28 = m.addVar(vtype = GRB.BINARY, name = 'z28')
z29 = m.addVar(vtype = GRB.BINARY, name = 'z29')

z31 = m.addVar(vtype = GRB.BINARY, name = 'z31')
z32 = m.addVar(vtype = GRB.BINARY, name = 'z32')
z33 = m.addVar(vtype = GRB.BINARY, name = 'z33')
z34 = m.addVar(vtype = GRB.BINARY, name = 'z34')
z35 = m.addVar(vtype = GRB.BINARY, name = 'z35')
z36 = m.addVar(vtype = GRB.BINARY, name = 'z36')
z37 = m.addVar(vtype = GRB.BINARY, name = 'z37')
z38 = m.addVar(vtype = GRB.BINARY, name = 'z38')
z39 = m.addVar(vtype = GRB.BINARY, name = 'z39')

#Every value j ∈ {1,2...,9} must appear in the matrix once and only once.
m.addConstr(x11+x21+x31+y11+y21+y31+z11+z21+z31 >= 1)
m.addConstr(x12+x22+x32+y12+y22+y32+z12+z22+z32 >= 1)
m.addConstr(x13+x23+x33+y13+y23+y33+z13+z23+z33 >= 1)
m.addConstr(x14+x24+x34+y14+y24+y34+z14+z24+z34 >= 1)
m.addConstr(x15+x25+x35+y15+y25+y35+z15+z25+z35 >= 1)
m.addConstr(x16+x26+x36+y16+y26+y36+z16+z26+z36 >= 1)
m.addConstr(x17+x27+x37+y17+y27+y37+z17+z27+z37 >= 1)
m.addConstr(x18+x28+x38+y18+y28+y38+z18+z28+z38 >= 1)
m.addConstr(x19+x29+x39+y19+y29+y39+z19+z29+z39 >= 1)

#Each square must assume one and only one value. 
m.addConstr(x11+x12+x13+x14+x15+x16+x17+x18+x19 >= 1)
m.addConstr(x21+x22+x23+x24+x25+x26+x27+x28+x29 >= 1)
m.addConstr(x31+x32+x33+x34+x35+x36+x37+x38+x39 >= 1)
m.addConstr(y11+y12+y13+y14+y15+y16+y17+y18+y19 >= 1)
m.addConstr(y21+y22+y23+y24+y25+y26+y27+y28+y29 >= 1)
m.addConstr(y31+y32+y33+y34+y35+y36+y37+y38+y39 >= 1)
m.addConstr(z11+z12+z13+z14+z15+z16+z17+z18+z19 >= 1)
m.addConstr(z21+z22+z23+z24+z25+z26+z27+z28+z29 >= 1)
m.addConstr(z31+z32+z33+z34+z35+z36+z37+z38+z39 >= 1)

#Sum constraints given in problem description. Each binary variable is multiplied by the j value it represents in order to weight them to add to the appropriate value.
m.addConstr((1*x11+2*x12+3*x13+4*x14+5*x15+6*x16+7*x17+8*x18+9*x19)+(1*y11+2*y12+3*y13+4*y14+5*y15+6*y16+7*y17+8*y18+9*y19) >= 12)
m.addConstr((1*x11+2*x12+3*x13+4*x14+5*x15+6*x16+7*x17+8*x18+9*x19)+(1*y11+2*y12+3*y13+4*y14+5*y15+6*y16+7*y17+8*y18+9*y19) <= 12)

m.addConstr((1*y11+2*y12+3*y13+4*y14+5*y15+6*y16+7*y17+8*y18+9*y19)+(1*z11+2*z12+3*z13+4*z14+5*z15+6*z16+7*z17+8*z18+9*z19) >= 7)
m.addConstr((1*y11+2*y12+3*y13+4*y14+5*y15+6*y16+7*y17+8*y18+9*y19)+(1*z11+2*z12+3*z13+4*z14+5*z15+6*z16+7*z17+8*z18+9*z19) <= 7)

m.addConstr((1*x21+2*x22+3*x23+4*x24+5*x25+6*x26+7*x27+8*x28+9*x29)+(1*y21+2*y22+3*y23+4*y24+5*y25+6*y26+7*y27+8*y28+9*y29) >= 8)
m.addConstr((1*x21+2*x22+3*x23+4*x24+5*x25+6*x26+7*x27+8*x28+9*x29)+(1*y21+2*y22+3*y23+4*y24+5*y25+6*y26+7*y27+8*y28+9*y29) <= 8)

m.addConstr((1*x21+2*x22+3*x23+4*x24+5*x25+6*x26+7*x27+8*x28+9*x29)+(1*x31+2*x32+3*x33+4*x34+5*x35+6*x36+7*x37+8*x38+9*x39) >= 7)
m.addConstr((1*x21+2*x22+3*x23+4*x24+5*x25+6*x26+7*x27+8*x28+9*x29)+(1*x31+2*x32+3*x33+4*x34+5*x35+6*x36+7*x37+8*x38+9*x39) <= 7)

m.addConstr((1*y21+2*y22+3*y23+4*y24+5*y25+6*y26+7*y27+8*y28+9*y29)+(1*y31+2*y32+3*y33+4*y34+5*y35+6*y36+7*y37+8*y38+9*y39) >= 14)
m.addConstr((1*y21+2*y22+3*y23+4*y24+5*y25+6*y26+7*y27+8*y28+9*y29)+(1*y31+2*y32+3*y33+4*y34+5*y35+6*y36+7*y37+8*y38+9*y39) <= 14)

m.addConstr((1*x31+2*x32+3*x33+4*x34+5*x35+6*x36+7*x37+8*x38+9*x39)+(1*y31+2*y32+3*y33+4*y34+5*y35+6*y36+7*y37+8*y38+9*y39) >= 13)
m.addConstr((1*x31+2*x32+3*x33+4*x34+5*x35+6*x36+7*x37+8*x38+9*x39)+(1*y31+2*y32+3*y33+4*y34+5*y35+6*y36+7*y37+8*y38+9*y39) <= 13)

m.addConstr((1*y31+2*y32+3*y33+4*y34+5*y35+6*y36+7*y37+8*y38+9*y39)+(1*z31+2*z32+3*z33+4*z34+5*z35+6*z36+7*z37+8*z38+9*z39) >= 15)
m.addConstr((1*y31+2*y32+3*y33+4*y34+5*y35+6*y36+7*y37+8*y38+9*y39)+(1*z31+2*z32+3*z33+4*z34+5*z35+6*z36+7*z37+8*z38+9*z39) <= 15)

#The sum of all variables Wij must equal to 9. 
m.addConstr(x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x21 + x22 + x23 + x24 + x25 + x26 + x27 + x28 + x29 + x31 + x32 + x33 + x34 + x35 + x36 + x37 + x38 + x39 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 +z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z21 + z22 + z23 + z24 + z25 + z26 + z27 + z28 + z29 + z31 + z32 + z33 + z34 + z35 + z36 + z37 + z38 + z39 >= 9)
m.addConstr(x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x21 + x22 + x23 + x24 + x25 + x26 + x27 + x28 + x29 + x31 + x32 + x33 + x34 + x35 + x36 + x37 + x38 + x39 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 +z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z21 + z22 + z23 + z24 + z25 + z26 + z27 + z28 + z29 + z31 + z32 + z33 + z34 + z35 + z36 + z37 + z38 + z39 <= 9)

m.setObjective(0, GRB.MINIMIZE)
m.optimize() 

x1dict = {x11.x: 1, x12.x: 2, x13.x: 3, x14.x: 4, x15.x: 5, x16.x: 6, x17.x: 7, x18.x: 8, x19.x: 9}
x2dict = {x21.x: 1, x22.x: 2, x23.x: 3, x24.x: 4, x25.x: 5, x26.x: 6, x27.x: 7, x28.x: 8, x29.x: 9}
x3dict = {x31.x: 1, x32.x: 2, x33.x: 3, x34.x: 4, x35.x: 5, x36.x: 6, x37.x: 7, x38.x: 8, x39.x: 9}

y1dict = {y11.x: 1, y12.x: 2, y13.x: 3, y14.x: 4, y15.x: 5, y16.x: 6, y17.x: 7, y18.x: 8, y19.x: 9}
y2dict = {y21.x: 1, y22.x: 2, y23.x: 3, y24.x: 4, y25.x: 5, y26.x: 6, y27.x: 7, y28.x: 8, y29.x: 9}
y3dict = {y31.x: 1, y32.x: 2, y33.x: 3, y34.x: 4, y35.x: 5, y36.x: 6, y37.x: 7, y38.x: 8, y39.x: 9}

z1dict = {z11.x: 1, z12.x: 2, z13.x: 3, z14.x: 4, z15.x: 5, z16.x: 6, z17.x: 7, z18.x: 8, z19.x: 9}
z2dict = {z21.x: 1, z22.x: 2, z23.x: 3, z24.x: 4, z25.x: 5, z26.x: 6, z27.x: 7, z28.x: 8, z29.x: 9}
z3dict = {z31.x: 1, z32.x: 2, z33.x: 3, z34.x: 4, z35.x: 5, z36.x: 6, z37.x: 7, z38.x: 8, z39.x: 9}


# print([x1dict[1], x2dict[1], x3dict[1]])
# print([y1dict[1], y2dict[1], y3dict[1]])
# print([z1dict[1], z2dict[1], z3dict[1]])

matrix = [[x1dict[1], x2dict[1], x3dict[1]], [y1dict[1], y2dict[1], y3dict[1]], [z1dict[1], z2dict[1], z3dict[1]]]

print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in matrix]))
