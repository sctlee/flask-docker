FROM sctlee/flask-base:nginx-uwsgi

MAINTAINER sctlee <haichuang221@163.com>


ENV DEBIAN_FRONTEND noninteractive


RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /var/log/uwsgi/app/


RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
COPY uwsgi.ini /var/www/app/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf


RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY singledog /var/www/app

RUN pip install -r /var/www/app/requirements.txt

EXPOSE 80

CMD ["/usr/bin/supervisord"]
