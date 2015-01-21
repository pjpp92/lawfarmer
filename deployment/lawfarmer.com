server {
        listen 80;
        server_name przemus.wojtass.pl;
        access_log /var/log/nginx/lawfarmer.access.log;
        client_max_body_size 20M;

        location / {
                include uwsgi_params;
                uwsgi_pass unix:///run/uwsgi/app/lawfarmer/socket;
        }
        location /static {
                gzip_static on;
                alias /home/wojtas/lawfarmer/static/;
        }
        location /media {
		gzip_static on;
                alias /home/wojtas/lawfarmer/media/;
		expires 30d;
		add_header Pragma public;
		add_header Cache-Control "public";
        }
}
