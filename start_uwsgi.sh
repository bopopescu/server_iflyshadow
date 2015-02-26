#!/bin/bash
killall -9 uwsgi
sudo service nginx stop
sudo service nginx restart
uwsgi --ini pystray_uwsgi.ini --daemonize /var/log/uwsgi/uwsgi.log