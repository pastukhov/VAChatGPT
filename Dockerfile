FROM python:3.8


RUN apt update && apt install portaudio19-dev python3-pyaudio -y
# Install required libraries

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install pip install -r requirements.txt

# Add your code to the image
COPY . .

# Run the main script when the container starts
CMD ["python", "main.py"]
