FROM tensorflow/tensorflow:latest-gpu

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8500

# Run the command to start the TensorFlow Serving
CMD ["tensorflow_model_server", "--rest_api_port=8500", "--model_name=mnist", "--model_base_path=/app/models"]