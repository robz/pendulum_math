f=$(mktemp).js
python pendulum_math.py > $f
yarn prettier $f --print-width=75 || cat $f
