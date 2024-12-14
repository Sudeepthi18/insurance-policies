# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment path
ENV PATH="/usr/local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy application and dependencies
COPY main.py /app/
COPY requirements.txt /app/

# Install dependencies explicitly
RUN pip install --no-cache-dir -r requirements.txt

# Debug: Check installation
RUN which uvicorn

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
