#!/bin/bash

# backup mkdocs.yml
cp mkdocs.yml mkdocs.yml.backup

rm -rf site-i18n/ site-blog/ site-blog-pass/

# blog double
docker run --rm -it -v ${PWD}:/docs ikuoshige/mkdocs_docker:insider build -f mkdocs_blog.yml
sudo chown ikuo -R ./site/
mv site/ site-blog/

# i18n
docker run --rm -it -v ${PWD}:/docs ikuoshige/mkdocs_docker:insider build
sudo chown ikuo -R ./site/
mv ./site/ site-i18n/

# change version
#python3 src/remove_i18n.py
#python3 src/add_encrycontent.py

# blog-password
docker run --rm -it -v ${PWD}:/docs ikuoshige/mkdocs_docker:insider build -f mkdocs_blog_pass.yml
sudo chown ikuo -R ./site/
mv site/ site-blog-pass/

# password
cp -r site-blog-pass/assets/ site-i18n/
cp site-blog-pass/encryptcontent-plugin.json site-i18n/
#cp -r site-blog-pass/assets/ site-blog/
#cp site-blog-pass/encryptcontent-plugin.json site-blog/

# add blog html for site-i18n
cp -r site-blog-pass/blog_private/* site-i18n/blog_private/
#cp -r site-blog-pass/blog/* site-i18n/blog_private/
sed -i 's/<a class="md-tabs__link" href="..\/blog_private\/">/<a class="md-tabs__link" href="..\/blog\/">/' ${PWD}/site-i18n/blog_private/index.html
#sed -i 's/<a class="md-tabs__link" href="..\/blog\/">/<a class="md-tabs__link" href="..\/blog_private\/">">/' ${PWD}/site-i18n/blog_private/index.html

#cp -r site-blog-pass/blog/* site-blog/blog_private/
#cp -r site-blog/blog/* site-blog/blog_private/
cp -r site-blog/blog/* site-i18n/blog/
#cp -r site-blog/blog/* site-18n/blog_private/

mv site-i18n/ site/
#mv site-blog/ site/

docker run --rm --name first-nginx -v ${PWD}/site:/usr/share/nginx/html:ro -p 8080:80 nginx

# restore backup file
cp mkdocs.yml.backup mkdocs.yml