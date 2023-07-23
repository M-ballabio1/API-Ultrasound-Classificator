# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port that the FastAPI application will listen on
EXPOSE 8080

# Set the entrypoint command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
