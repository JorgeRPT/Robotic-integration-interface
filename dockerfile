FROM python
# Set the working directory in the container


# Copy the current directory contents into the container at /app
COPY . .

RUN pip install fastapi uvicorn motor

# Command to run the Python script
CMD ["python", "app/main.py"]