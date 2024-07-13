#!/bin/bash
export WINDOWID=$(xdotool getwindowfocus)

for py_file in assets/*.py;
do
    base_name=$(basename "$py_file" .py)
    ttyrec -e "poetry run python $py_file"
    ttygif ttyrecord
    rm ttyrecord
    mv tty.gif "assets/${base_name}.gif"
done
