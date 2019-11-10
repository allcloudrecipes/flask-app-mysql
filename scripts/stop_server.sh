#!/bin/bash
flaskapp=$(systemctl | grep flask-app)
if  [[ $flaskapp ]]
 then
 sudo systemctl stop flask-app       
fi
