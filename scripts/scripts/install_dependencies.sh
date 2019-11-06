#!/bin/bash
sudo yum update -y
sudo yum install python3 -y
sudo yum install mysql -y
sudo yum install python-pip3 -y
sudo pip3 install flask
sudo pip3 install pymysql
sudo pip3 install Flask-Table
sudo pip3 install flask-mysql
sudo pip3 install gunicorn
sudo yum install systemd -y