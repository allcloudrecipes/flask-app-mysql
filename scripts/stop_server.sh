#!/bin/bash
isExistApp=`pgrep flask-app`
if [[ -n  $isExistApp ]]; then
    systemctl stop flask-app       
fi