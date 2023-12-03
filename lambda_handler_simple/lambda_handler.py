import json

print("Loading Function")

def lambda_handler(event, context):
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
