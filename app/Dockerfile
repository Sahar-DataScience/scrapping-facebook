FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim


WORKDIR /code
# Copy requirements
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy application files
RUN pip install --no-cache-dir webdriver-manager==4.0.1
COPY . /code/app

# Expose FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]