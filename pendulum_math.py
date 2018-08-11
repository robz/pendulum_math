#!/usr/bin/env python3
from sympy import *

(t, g) = symbols('t, g') # time, gravity
(L1, L2) = symbols('L1:3') # lengths of bars
(m1, m2) = symbols('m1:3') # point masses
(a1, a2) = symbols('a1:3') # base basis
(T1, T2) = symbols('T1:3') # tensions

# angles
theta1 = Function('theta1')(t)
theta2 = Function('theta2')(t)

# basis at each joint
b1 = Function('b1')(t)
b2 = Function('b2')(t)
c1 = Function('c1')(t)
c2 = Function('c2')(t)

# conversion between basis
b1aexp = a1 * cos(theta1) + a2 * sin(theta1)
b2aexp = -a1 * sin(theta1) + a2 * cos(theta1)

aexps_from_bexps = solve([Eq(b1, b1aexp), Eq(b2, b2aexp)], a1, a2)
a1bexp, a2bexp = [aexps_from_bexps[a] for a in (a1, a2)]

c1bexp = b1 * cos(theta2) + b2 * sin(theta2)
c2bexp = -b1 * sin(theta2) + b2 * cos(theta2)
bexps_from_cexps = solve([Eq(c1, c1bexp), Eq(c2, c2bexp)], b1, b2)
b1cexp, b2cexp = [bexps_from_cexps[b] for b in (b1, b2)]

c1aexp = c1bexp.subs([(b1, b1aexp), (b2, b2aexp)])
c2aexp = c2bexp.subs([(b1, b1aexp), (b2, b2aexp)])
aexps_from_cexps = solve([Eq(c1, c1aexp), Eq(c2, c2aexp)], a1, a2)
a1cexp, a2cexp = [aexps_from_cexps[a] for a in (a1, a2)]

# kinematics for point Q (tip of the single pendulum)
posQ = L1 * b1
velQ = diff(posQ, t)
accelQ = diff(velQ, t)

# kinematics for point R (tip of the double pendulum)
posR = posQ + L2 * c1
velR = diff(posR, t)
accelR = diff(velR, t)

# F=ma for point R and Q
forceRInitial = Eq(m2 * accelR, m2 * g * a1 - T2 * c1)
forceQInitial = Eq(m1 * accelQ, m1 * g * a1 - T1 * b1 + T2 * c1)

# convert forces on R to a basis and take derivatives
forceR = forceRInitial.subs([
    (b1, b1aexp),
    (b2, b2aexp),
    (c1, c1aexp),
    (c2, c2aexp),
]).doit()

# convert to c basis and dot with c2 (remove T2)
forceR = forceR.subs([
    (a1, a1cexp),
    (a2, a2cexp),
]).subs([
    (c1, 0),
    (c2, 1),
]).simplify()

# get theta2DotDot in terms of theta1DotDot
theta2DotDot = solve(
    forceR,
    Derivative(theta2, (t, 2)),
)[0].simplify()

# add Q forces to R forces (remove T1)
combinedForces = Eq(
    forceQInitial.lhs + forceRInitial.lhs,
    forceQInitial.rhs + forceRInitial.rhs,
)

# convert a,b,c basis to just a basis to take derivatives
combinedForces = combinedForces.subs([
    (b1, b1aexp),
    (b2, b2aexp),
    (c1, c1aexp),
    (c2, c2aexp),
]).doit().simplify()

# convert to b basis to dot with b2 (remove T1)
combinedForces = combinedForces.subs([
    (a1, a1bexp),
    (a2, a2bexp),
]).subs([
    (b1, 0),
    (b2, 1),
]).simplify()

# solve for theta1DotDot and theta2DotDot
theta1DotDot = solve(
    [forceR, combinedForces],
    Derivative(theta1, (t, 2)),
    Derivative(theta2, (t, 2)),
)[Derivative(theta1, (t, 2))]

def printJS(name, exp):
    import re
    s = str(exp)
    s = re.sub(r"\(t\)", "", s)
    s = re.sub(r"Derivative\(theta([0-9]), t\)", r"theta\1Dot", s)
    s = re.sub(r"Derivative\(theta([0-9]), \(t, 2\)\)", r"theta\1DotDot", s)
    s = re.sub(r"theta", "\u03B8", s)
    name = re.sub(r"theta", "\u03B8", name)
    print('const ' + name + ' = ')
    print(s)

printJS('theta1DotDot', theta1DotDot)
printJS('theta2DotDot', theta2DotDot)
