# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command to run your application (e.g., `extract.py`)
CMD ["python", "src/data_extraction/extract.py"]