#!/bin/bash

sudo chown ikuo -R ./site/    
docker run --rm --name first-nginx_1 -v ${PWD}/site:/usr/share/nginx/html:ro -p 8080:80 nginx
#docker run --rm --name first-nginx -v ${PWD}/site-i18n:/usr/share/nginx/html:ro -p 8080:80 nginx
#docker run --rm --name first-nginx -v ${PWD}/tmp/site-i18n:/usr/share/nginx/html:ro -p 8080:80 nginx
