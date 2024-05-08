# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file initially
COPY . .

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose port 8080 to the outside world
EXPOSE 8080

# Run the application using uvicorn server
CMD ["uvicorn", "app:app", "--reload","--host", "0.0.0.0", "--port", "8080"]
