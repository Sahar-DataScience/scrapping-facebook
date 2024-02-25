FROM mysql/mysql-server:8.0

# ROOT PASSWORD
ENV MYSQL_ROOT_PASSWORD=$unshine1!

# Database will be automatically created
COPY ./init.sql /docker-entrypoint-initdb.d

# PORT
EXPOSE 3306