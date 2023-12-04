import json
import logging

print("Loading Function")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f'Incoming request is: {event}')
    body = {
        "key1": "MH",
        "key2": "UP",
        "key3": "Goa"
    }
    print(body)
    print(response)