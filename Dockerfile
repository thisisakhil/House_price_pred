# Use a base image with Python pre-installed
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY Code/requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from your local directory to the container
COPY . .

# Command to run your Python application
CMD ["streamlit","run", "Code/app.py"]
