# Use a lightweight Python image
FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the static website files into the container
COPY ./index.html .
COPY ./resources ./resources

# Command to start Python's built-in HTTP server on port 8000.
# Ensure Coolify is configured to use port 8000 for this service.
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]