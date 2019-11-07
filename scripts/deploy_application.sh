#!/bin/bash
pip3 install virtualenv
virtualenv /home/ec2-user/flask-app-mysql/flaskappenv
source /home/ec2-user/flask-app-mysql/flaskappenv/bin/activate
pip3 install flask
pip3 install pymysql
pip3 install Flask-Table
pip3 install flask-mysql
pip3 install gunicorn
cp /home/ec2-user/flask-app-mysql/flask-app.service /etc/systemd/system/
systemctl start flask-app
systemctl enable flask-app