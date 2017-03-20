#!/usr/bin/env bash
# create symbolic link to a new nginx config
sudo -s ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/django.conf
sudo unlink /etc/nginx/sites-enabled/default
sudo -s rm /etc/nginx/sites-enabled/default

# restart nginx
sudo -s /etc/init.d/nginx restart
# restart gunicorn
sudo -s /etc/init.d/gunicorn restart

# creare symbolic links to gunicorn configs
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo -s ln -sf /home/box/web/etc/django-gunicorn.conf  /etc/gunicorn.d/django-gunicorn.conf

#
cd /home/box/web && \
    virtualenv venv && \
    source venv/bin/activate && \
    pip install -r requirements/production.txt && \
    export PYTHONPATH=$(pwd):$PYTHONPATH && \
    cd /home/box/web/ask && \
    python manage.py migrate && \
    exec gunicorn --bind=0.0.0.0:8000 --workers=4 ask.wsgi:application