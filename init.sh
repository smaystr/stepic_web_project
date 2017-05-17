#!/usr/bin/env bash

# check & create symbolic link to a new nginx config
touch /home/box/web/nginx.log
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo unlink /etc/nginx/sites-enabled/default
    sudo -s rm /etc/nginx/sites-enabled/default
fi
sudo -s ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/ask.conf


# creare symbolic links to gunicorn configs
touch /home/box/web/gunicorn.log
# sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo -s ln -sf /home/box/web/etc/gunicorn_ask.conf  /etc/gunicorn.d/ask


# start gunicorn, nginx
sudo  service gunicorn start
sudo service nginx start

#
cd /home/box/web && \
    pip install -r requirements/production.txt
#
cd /home/box/web/ask && \
#    python manage.py syncdb && \
    python manage.py makemigrations qa && \
    python manage.py migrate qa

# restart gunicorn, nginx
sudo  service gunicorn restart
sudo service nginx restart