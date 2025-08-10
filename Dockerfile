# 1. Start with an official Python base image
FROM python:3.13-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code into the container
# This copies both the 'src' and 'resources' folders
COPY ./src ./src
COPY ./resources ./resources

# 6. Expose the port that Streamlit runs on
EXPOSE 8501

# 7. Define the command to run your app when the container starts
CMD ["streamlit", "run", "src/main.py"]