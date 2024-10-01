# Use a Python 3 base image (adjust the version if needed)
FROM python:3.9.6-slim

# Create a working directory inside the container
WORKDIR /DICOMn

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies based on requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project directory structure
COPY . .

# Specify the command to run your application (adjust the script name)
CMD ["tail", "-f", "/dev/null"]