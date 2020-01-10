FROM nginx

RUN mkdir /etc/nginx/ssl/

COPY ./ssl.crt /etc/nginx/ssl/ssl.crt

COPY ./ssl.key /etc/nginx/ssl/ssl.key

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/