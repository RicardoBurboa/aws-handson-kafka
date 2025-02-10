# aws-handson-kafka
Creates a Producer and Consumer leveraging AWS MSK for Apache Kafka.

## Description
This project demonstrates how to set up and run a simple Kafka producer and consumer using **AWS Managed Streaming for Kafka (MSK)**. The four Python files (`topic.py`, `holamundo.py`, `consumer.py` and `delete.py`) are intended to be executed inside an EC2 instance, which is configured with Docker to run a **JupyterLab** web environment for easy testing and interaction.

## Files
- `topic.py`: Creates a topic.
- `holamundo.py`: Creates a producer and sends a message.
- `consumer.py`: Creates a consumer and receives the message.
- `delete.py`: Deletes the topic that was created previously.

## Prerequisites

Before you can run this project, ensure that you have the following set up:

1. **AWS MSK Cluster:**
   - Set up an AWS MSK cluster with appropriate configurations (security groups, IAM roles, etc.).
   - Ensure you have the Kafka brokers' endpoint to configure the producer and consumer.
   
2. **EC2 Instance:**
   - Create an EC2 instance with sufficient permissions to connect to your AWS MSK cluster.
   
3. **Docker & Docker Compose:**
   - Install Docker on your EC2 instance.
   - Optionally, Docker Compose can be used to manage the containers more efficiently.

4. **Python Dependencies:**
   - Install Python 3.11 or higher.
   - Install the necessary Python libraries:
     - `kafka-python`
     - `boto3` (optional, if you need to interact with other AWS services)

5. **JupyterLab:**
   - This project runs within a JupyterLab Docker container to facilitate running the producer and consumer interactively.

## Results

### Create a Topic
![01 Create Topic](https://github.com/user-attachments/assets/4d2419bb-9e2a-4676-805c-35b436a93710)

### Produce a Message
![02 Hola Mundo](https://github.com/user-attachments/assets/f8b88d26-20f0-458b-a0d5-25eeb7d0a734)

### Consume a Message
![03 Consumer](https://github.com/user-attachments/assets/4a551671-1fa7-466d-81b5-a715834b52c3)

### Delete the Topic
![04 Delete Topic](https://github.com/user-attachments/assets/43f61439-b2d5-43ec-b006-c78232d4a4e9)
