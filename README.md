# RabbitMQ_MQTT
configuration and use of RabbitMQ for MQTT messages.
# MQTT Message Processing with RabbitMQ and MongoDB

## Overview
This project demonstrates how to process incoming MQTT messages using RabbitMQ as the message broker and store them in MongoDB. It includes Python scripts to handle message processing, RabbitMQ integration, and MongoDB integration.
## Project Structure
- `main_code/`: Contains the main Python scripts.
  - `main.py`: Establishes connections to RabbitMQ and MongoDB, defines MongoDB schema, and provides a collection object. 
- `test/`: Contains test scripts.
  - `treceive.py`: Unit tests for the receive module.
  - `send.py`: Unit tests for the send module.

## Requirements
- Python 3.x
- RabbitMQ server
- MongoDB server

## Installation
1. Install Python dependencies:
pip install -r requirements.txt

2. Ensure RabbitMQ server is running. If not installed, refer to the RabbitMQ installation guide.

3. Ensure MongoDB server is running. If not installed, refer to the MongoDB installation guide.

## Usage
1. Run the RabbitMQ consumer script to listen for incoming MQTT messages and store them in MongoDB:
2. Send MQTT messages to the RabbitMQ server using your preferred MQTT client.
## Contributing
Contributions are welcome! Please submit pull requests or open issues if you encounter any problems or have suggestions for improvement.




