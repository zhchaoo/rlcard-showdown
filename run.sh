#!/bin/sh

# switch conda environment
#conda activate rl

nohup python server/manage.py runserver > logs/ser.log 2>&1 &

nohup python pve_server/run_dmc.py > logs/pve.log 2>&1 &

nohup npm start > logs/npm.log 2>&1 &

