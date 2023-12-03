from datetime import datetime
import boto3
import os
import uuid
import json
import logging
import dynamo # helper function


logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamo = boto3.client('dynamodb')
table_name = str(os.environ['DYNAMODB_TABLE'])

def create(event, context):
    logger.info(f'Incoming request is: {event}')

    response = {
        "statusCode": 500,
        "body": "An error occured while creating post."
    }

    post_str = event['body']
    post = json.loads(post_str)
    current_timestamp = datetime.now().isoformat()
    post['createAt'] = current_timestamp
    post['id'] = str(uuid.uuid4)

    res = dynamodb.put_item(
        TableName=table_name,
        Item=dynamo.to_item(post)
    )