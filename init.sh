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


# restart gunicorn, nginx
sudo -s /etc/init.d/gunicorn restart
sudo -s /etc/init.d/nginx restart

# run MySQL & create DB
# echo 'innodb_use_native_aio = 0' | sudo tee --append /etc/mysql/my.cnf
sudo -s /etc/init.d/mysql start && \
    mysql -uroot -e "CREATE DATABASE qa CHARACTER SET utf8 COLLATE utf8_general_ci;"
    mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'root'@'localhost';"

#
mkdir ~/web
#
cd /home/box/web && \
    git clone https://github.com/smaystr/stepic_web_project.git
    pip install -r requirements/production.txt
#
cd /home/box/web/ask && \
    python manage.py syncdb && \
    python manage.py makemigrations qa && \
    python manage.py migrate qa

sudo service mysql restart