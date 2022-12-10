sudo pkill -f gunicorn
sudo gunicorn -w 2 main:app --daemon
