# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Start the FastAPI application when the container is run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]