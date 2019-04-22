f=$(mktemp).js

echo 'deriving...'

python3 src/equations/pendulum_math.py > $f

echo 'result:'

yarn prettier $f --print-width=75 --write
cat $f

echo 'const {sin, cos} = Math;' > src/ui/calcThetaDotDots.js
echo 'const g = 9.8;' >> src/ui/calcThetaDotDots.js
echo 'function calcThetaDotDots({theta1, theta2, theta1Dot, theta2Dot}, {L1, L2, m1, m2}, {F}) {' >> src/ui/calcThetaDotDots.js
cat $f >> src/ui/calcThetaDotDots.js
echo 'return { theta1DotDot, theta2DotDot }; }' >> src/ui/calcThetaDotDots.js

yarn prettier src/ui/calcThetaDotDots.js --print-width=75 --write

echo 'wrote result to src/ui/calcThetaDotDots.js'

rm $f
