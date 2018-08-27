#!/usr/bin/env python3
from sympy import *
from print_js import printJS

# time, gravity, length, mass, tension
(t, g, L, m, T) = symbols('t, g, L, m, T')
(a1, a2) = symbols('a1:3') # base basis

# angle
theta = Function('theta')(t)

# basis at joint
b1 = Function('b1')(t)
b2 = Function('b2')(t)

b1aexp = a1 * cos(theta) + a2 * sin(theta)
b2aexp = -a1 * sin(theta) + a2 * cos(theta)

aexps_from_bexps = solve([Eq(b1, b1aexp), Eq(b2, b2aexp)], a1, a2)
a1bexp, a2bexp = [aexps_from_bexps[a] for a in (a1, a2)]

### Single pendulum ###

# kinematics for point Q (tip of the single pendulum)
posQ = L * b1
velQ = diff(posQ, t)
accelQ = diff(velQ, t)
printJS('kinematics', accelQ, False)

# f=ma for point Q
forceQ = Eq(m * accelQ, (m * g * a1) - (T * b1))
printJS('force', forceQ, False)

# convert from basis b to basis a, and execute derivatives
forceQ = forceQ.subs([
    (b1, b1aexp),
    (b2, b2aexp),
]).doit()

# expand to 2 equations for each basis (dot each with a1 and a2)
eq1 = forceQ.subs([(a1, 0), (a2, 1)]).simplify();
eq2 = forceQ.subs([(a1, 1), (a2, 0)]).simplify();

# solve for thetadotdot
thetaDotDotSymbol = Derivative(theta, (t, 2));
thetaDotDot = solve([eq1, eq2], T, thetaDotDotSymbol)[thetaDotDotSymbol]
printJS('thetaDotDot', thetaDotDot, False)
