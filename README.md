# heavywater
Document classification Flask Web Application

Various models were tested against the dataset and the details are in the .ipynb file
The best model for the document classification came out to be a sequential model with loss: 0.3412 and acc: 0.8979

The web application is currently hosted on an [ec2 instance](http://ec2-107-23-158-79.compute-1.amazonaws.com:5000)

The deployment can be done using a boto and jenkins with one click.

TO do manually:
Clone the repo and run setup.sh script
