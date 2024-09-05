# Use the official Python 3.10 image based on Alpine Linux for a lightweight environment
FROM python:3.10-alpine

# Add the server.py file from the local directory to the root of the container's filesystem
ADD server.py .

# Add the requirements.txt file from the local directory to the root of the container's filesystem
ADD requirements.txt .

# Create a directory named 'templates' in the container's filesystem
RUN mkdir ./templates

# Add the contents of the 'templates' directory from the local directory to the container's 'templates' directory
ADD templates ./templates

# Install the Python packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the default command to run 'server.py' using Python when the container starts
CMD ["python", "./server.py"]
