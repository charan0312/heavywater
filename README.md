# heavywater
Document classification Flask Web Application


The web application is currently hosted on an [ec2 instance](http://ec2-52-90-246-255.compute-1.amazonaws.com:5000)
and api is hosted [here](http://ec2-52-90-246-255.compute-1.amazonaws.com:6000)

The deployment can be done using a boto and jenkins with one click.

TO do manually:
Steps for deployment:
$sudo apt-get update -y
$sudo apt-get install python3-pip -y
$sudo pip3 install -r requirements
$git clone https://github.com/charan0312/heavywater.git
For Webapp:
$cd heavywater/webapp
$nohup python3 app.py &
For api:
$cd ~/heavywater/api
$nohup python3 app.py &
