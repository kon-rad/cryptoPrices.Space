#!/bin/bash

sudo git reset --hard
sudo git pull
cd frontend
sudo npm install
sudo npm run build

# start virtual env, update requirements, rebuild app
cd ../
virtualenv .
source bin/activate
pip install -r requirements.txt
python manage.py collectstatic
# restarts gunicorn, resets .sock
pkill gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn
deactivate