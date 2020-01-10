### Basic Flask app running behind Nginx & uWSGI in a Docker container

Clone the repo:

```sh
git clone https://github.com/Faithful1/bitwall.git
```

To develop locally, create a new virtual env in the `flask` directory & run the app:

```sh
cd app
python -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Go to - http://127.0.0.1:5000

## To run using docker-compose

## dependencies

### 0. setup

Ensure these are installed before going further:

- docker@\^18.05.0-ce
- docker-compose@^1.21.2

### 1. run

- navigate to /etc/hosts and edit the host file mapping a virtual host domain to your localhost in my case `127.0.0.1 bitwalla.lh`
- navigate into the root folder of our cloned application
- run `chmod +x init-ssl.sh`
- run `sudo ./init-ssl.sh` to generate our self-signed certificates
- run `docker-compose up -d`
  You can begin editing code on your host machine, changes will be detected and all relevant processes restarted or live-reloaded inside their containers.

### 2. inspect

- `docker-compose ps` (print status) to see all running containers
- `docker-compose logs service-name(e.g api or mongo)` (attaches to logs of one or more services)

### 3. run

Go to - localhost or http://127.0.0.1/ or (virtual_host domain) on your browser and see the app redirect to https

### Notes

- `nginx` logs and `uwsgi` logs will be logged to `/var/log/nginx` and `/var/log/uwsgi` respectively. This can be changed by changing the `volume` mounts in the `docker-compose.yml`.

Alternatively, delete the `volumes` to have Docker log to `Stdout`.

- consider using proper certificates authorities like letsencrypt or cloudflare for a production environment
