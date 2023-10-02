#!/bin/bash

if ! command -v docker &> /dev/null; then
    echo "Docker is not installed on your system."
    echo "Please install Docker"
    echo "\n"

else
    :
fi

#docker run --rm -p 8000:8000 --name mkdocs-serve -v $(pwd):/app ghcr.io/uhobeike/mkdocs-serve:latest
#docker run --rm -p 8000:8000 --name mkdocs-serve -v $(pwd):/app ghcr.io/ikuoshige/mkdocs-serve:latest
#docker run --rm -p 8000:8000 --name mkdocs-serve -v $(pwd):/docs ikuoshige/mkdocs_docker:latest
#docker run --rm -it -v ${PWD}:/docs ikuoshige/mkdocs_docker:latest build
docker run --rm -it -v ${PWD}:/docs ikuoshige/mkdocs_docker:insider build -f mkdocs_blog-pass.yml
sudo chown ikuo -R ./site/
docker run --rm --name first-nginx -v ${PWD}/site:/usr/share/nginx/html:ro -p 8080:80 nginx
