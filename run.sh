#!/bin/sh

# switch conda environment
#conda activate rl

nohup python server/manage.py runserver 30.210.212.42:8000 > logs/ser.log 2>&1 &

nohup python pve_server/run_dmc.py > logs/pve.log 2>&1 &

nohup npm start > logs/npm.log 2>&1 &

