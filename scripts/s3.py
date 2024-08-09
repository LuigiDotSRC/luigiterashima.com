import logging
import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.client('s3')

MIME_TYPES = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.txt': 'text/plain',
    '.pdf': 'application/pdf',
}

def get_content_type(file_name):
    _, ext = os.path.splitext(file_name)
    return MIME_TYPES.get(ext, 'application/octet-stream')  

def list_buckets():
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'    {bucket["Name"]}')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Get the content type based on file extension
    content_type = get_content_type(file_name)

    # Upload the file
    try:
        # Specify ContentType in ExtraArgs
        response = s3.upload_file(file_name, bucket, object_name, ExtraArgs={'ContentType': content_type})
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_bucket_timestamps(bucket):
    """List the timestamps of each object in an S3 bucket 

    :param bucket: Bucket to check
    :return: dict[str] filename: time_last_updated
    """
    timestamps = {} 
    try:
        response = s3.list_objects(Bucket=bucket)
        for object in response['Contents']:
            timestamps[object['Key']] = object['LastModified'] 
        
    except ClientError as e:
        logging.error(e)

    return timestamps

