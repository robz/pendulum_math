`pendulum_math.py` derives the differential equations for a double pendulum using Newton's equations. They are printed out in Javascript syntax (see `output.js`), and simulated here: https://jsfiddle.net/hu7w5s6L/361/

See `double_pendulum.jpg` for an diagram indicating what the variables are.

Prereqs:
  - python: https://www.python.org/
  - sympy: https://www.sympy.org/en/index.html
  - yarn: https://yarnpkg.com/en/

Clone this repo, then run `yarn install` to get prettier (a JS code formatter), and then run `./run.sh` to execute the derivation.

It takes about 30 secs to to execute on a macbook pro.

`single_pendulum_math.py` follows the same approach for the single pendulum.
