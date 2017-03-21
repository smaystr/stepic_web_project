#!/usr/bin/env bash

# check & create symbolic link to a new nginx config
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo unlink /etc/nginx/sites-enabled/default
    sudo -s rm /etc/nginx/sites-enabled/default
fi
sudo -s ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/django.conf

# creare symbolic links to gunicorn configs
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo -s ln -sf /home/box/web/etc/gunicorn_ask.conf  /etc/gunicorn.d/gunicorn_ask.conf

# restart nginx, gunicorn
sudo -s /etc/init.d/nginx restart
sudo -s /etc/init.d/gunicorn restart
