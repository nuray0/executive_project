# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3:$PATH

# Expose port 8000 to the outside world
EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]