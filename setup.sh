#!/bin/bash
sudo apt-get update -y
sudo apt-get install python3-pip -y
sudo pip3 install -r requirements.txt
cd webapp
nohup python3 app.py &