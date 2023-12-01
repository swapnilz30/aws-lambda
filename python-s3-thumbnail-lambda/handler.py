from datetime import datetime
import boto3
from io import BytesIO
from PIL import Image, ImageOps
import os
import uuid
import json
import urllib.parse

s3 = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])

def s3_thumbnail_generator(event, context):
    print("EVENT:::", event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    img_size = event['Records'][0]['s3']['object']['size']
    
    #decoded_string = urllib.parse.unquote_plus(key)
    #cleaned_string = decoded_string.replace(' ', '')
    #cleaned_key = cleaned_string.replace('\u202F', '')
    print("cleaned_key:::", key)

    if (not key.endswith("_thumbnail.png")):
        
        image = get_s3_image(bucket, key)

        thumbnail = image_to_thumbnail(image)
        
        thumbnail_key = new_filename(key)

        url = upload_to_s3(bucket, thumbnail_key, thumbnail, img_size)

        return url

def image_to_thumbnail(image):
    return ImageOps.fit(image, (size, size), Image.ANTIALIAS)

def new_filename(key):
    decoded_string = urllib.parse.unquote(key)
    final_string = decoded_string.replace('+', ' ')
    key_split = final_string.rsplit('.', 1)
    return key_split[0] + "_thumbnail.png"

def get_s3_image(bucket, key):
    decoded_key = urllib.parse.unquote_plus(key)

    response = s3.get_object(Bucket=bucket, Key=decoded_key)
    imagecontent = response['Body'].read()

    file = BytesIO(imagecontent)
    img = Image.open(file)
    return img

def upload_to_s3(bucket, key, image, img_size):
    out_thumbnail = BytesIO()

    image.save(out_thumbnail, 'PNG')
    out_thumbnail.seek(0)
    
    response = s3.put_object(
        Body=out_thumbnail,
        Bucket=bucket,
        ContentType='image/png',
        Key=key
    )
    print(response)

    url = '{}/{}/{}'.format(s3.meta.endpoint_url, bucket, key)

    return url