FROM squidfunk/mkdocs-material:9
RUN pip install mkdocs-macros-plugin
RUN pip install mkdocs-glightbox
RUN pip install mkdocs-static-i18n
RUN pip install mkdocs-encryptcontent-plugin
