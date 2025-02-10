import boto3
import requests
from confluent_kafka import Producer

# Obtener credenciales de AWS desde el entorno o IAM Role
session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

# URL de autenticación para MSK IAM
AWS_REGION = "us-east-1"  # Cambia a la región de tu MSK
AUTH_URL = f"https://sts.{AWS_REGION}.amazonaws.com"
 
# Generar token de autenticación OAUTH para MSK
def get_aws_msk_iam_token():
    headers = {
        "X-Amz-Security-Token": credentials.token,
    } if credentials.token else {}
 
    response = requests.post(AUTH_URL, headers=headers)
    response.raise_for_status()
    return response.text
 
# Configuración del productor Kafka
conf = {
    "bootstrap.servers": "boot-zlqiji0t.c3.kafka-serverless.us-east-1.amazonaws.com:9098",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "OAUTHBEARER",
    "sasl.oauthbearer.token_refresh_cb": get_aws_msk_iam_token,  # Usa la función para obtener el token
    "client.id": "python-producer",
    "acks": "1"
}

# Crear el productor
producer = Producer(conf)

# Enviar mensaje a MSK Serverless
producer.produce("new_topic", key="message", value="Hola MSK IAM!", callback=lambda err, msg: print("Enviado" if not err else f"Error: {err}"))
producer.flush()