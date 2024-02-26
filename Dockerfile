# Stage 1: Build Selenium environment
FROM selenium/standalone-chrome-debug:latest

# Download and install ChromeDriver
COPY ./chromedriver /usr/local/bin/chromedriver

# Stage 2: Build FastAPI environment
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy application files
RUN pip install --no-cache-dir webdriver-manager==4.0.1
COPY ./app /code/app

# Expose FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Stage 3: Copy MySQL configuration (optional)

FROM mysql:8.0  

# Set environment variable for MySQL connection details root password
ENV MYSQL_ROOT_PASSWORD=$unshine1!

#SQL Query to Grant to create and grant privilege to a new user
COPY ./init.sql /docker-entrypoint-initdb.d

# Expose MySQL port
EXPOSE 3306

# Command to run MySQL in the background
CMD ["mysqld"]