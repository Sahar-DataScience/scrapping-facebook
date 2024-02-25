# 
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir -r /code/requirements.txt

# 
RUN pip install --no-cache-dir webdriver-manager==4.0.1
COPY . /code/app

EXPOSE 8000

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]