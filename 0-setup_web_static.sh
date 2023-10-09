#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo sh -c 'echo "Hello in this world --__--" > /data/web_static/releases/test/index.html'
sudo -sf ln /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sh -c 'echo "
server {
    listen 80;
    add_header X_Served_by \$HOSTNAME;
    listen [::]:80 default_server;
    server_name elshafae.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'
sudo service nginx restart
