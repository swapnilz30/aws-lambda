import json
import logging

print("Loading Function")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f'Incoming request is: {event}')
    print("EVENT:::", event)
    print(event["key1"])
    print("context:::", context)
    #transactionId = event['queryStringParameters'][transactionId]
    response = {}
    response["statusCode"] = 200
    response["headers"] = {}
    response["headers"]["Content-Type"] = "application/json"
    response["body"] = json.dumps(event)
    responseID = response["body"]
    res = json.loads(responseID)
    print(type(res))
    print(res["key3"])