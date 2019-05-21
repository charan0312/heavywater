#!/bin/bash
sudo apt-get update -y
sudo apt-get install python3-pip -y
sudo pip3 install -r requirements
git clone https://github.com/charan0312/heavywater.git
cd webapp
nohup python3 app.py &