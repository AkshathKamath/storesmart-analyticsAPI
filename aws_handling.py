import os
import boto3
from dotenv import load_dotenv

def aws_img_saver(image_buffer, s3_file):
    load_dotenv()
    
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY_ID')
    AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME_ID')
    AWS_REGION = os.getenv('AWS_REGION_ID')

    s3_client = boto3.client(
        service_name = 's3',
        region_name = AWS_REGION,
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_KEY
    )

    s3_client.upload_fileobj(image_buffer, AWS_S3_BUCKET_NAME, s3_file)

    print("AWS image upload successful!")