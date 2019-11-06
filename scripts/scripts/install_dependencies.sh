#!/bin/bash
sudo yum update -y
sudo yum install python3 -y
sudo yum install python-pip3 -y
sudo pip3 install virtualenv
virtualenv /home/ec2-user/flask-app-mysql/flaskappenv
source /home/ec2-user/flask-app-mysql/flaskappenv/bin/activate
sudo pip3 install flask
sudo pip3 install pymysql
sudo pip3 install Flask-Table
sudo pip3 install flask-mysql
sudo pip3 install gunicorn
cp /home/ec2-user/flask-app-mysql/flask-app.service /etc/systemd/system/
sudo systemctl start flask-app