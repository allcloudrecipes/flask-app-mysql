sudo yum update -y
sudo yum install git -y
sudo yum -y install python-pip
sudo pip install flask

sudo git clone https://github.com/allcloudrecipes/flask-app-mysql.git
sudo python flask-app-mysql/main.py