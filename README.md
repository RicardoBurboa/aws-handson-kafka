# aws-handson-kafka
Creates a Producer and Consumer leveraging AWS MSK for Apache Kafka.

## Description
This project demonstrates how to set up and run a simple Kafka producer and consumer using **AWS Managed Streaming for Kafka (MSK)**. The two Python files (`producer.py` and `consumer.py`) are intended to be executed inside an EC2 instance, which is configured with Docker to run a **JupyterLab** web environment for easy testing and interaction.

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
