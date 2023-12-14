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
    
    print("Print info: ", body["key1"])
    
    for key, value in body.items():
      print(f"{key}: {value}")
    
    print(body)
