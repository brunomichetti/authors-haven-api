FROM postgres:14.1

# - Copy the maintance content
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance


# - Give permissions
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
   && rmdir /usr/local/bin/maintenance
