# create symbolic link to a new nginx config
sudo -s ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/django.conf

sudo unlink /etc/nginx/sites-enabled/default
sudo -s rm /etc/nginx/sites-enabled/default

# restart nginx
sudo -s /etc/init.d/nginx restart
sudo -s /etc/init.d/gunicorn restart

# creare symbolic links to gunicorn configs
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
