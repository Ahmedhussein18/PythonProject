# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY python.py .

# Install any necessary packages (if needed)
# RUN pip install -r requirements.txt

# Run the Python script
CMD ["python", "python.py"]
