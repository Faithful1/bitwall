#!/bin/bash
cd ./nginx && openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 -subj "/C=US/ST=NC/L=Local/O=Dev/CN=mysite.local" -keyout ./ssl.key -out ./ssl.crt