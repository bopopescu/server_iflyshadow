#!/bin/bash
sudo service nginx restart
uwsgi --ini pystray_uwsgi.ini --daemonize /var/log/uwsgi/uwsgi.log