from s3 import get_bucket_timestamps, upload_file
from file_check import get_files_in_dir
from dotenv import load_dotenv
import os 

load_dotenv() 
IMAGES_BUCKET = os.getenv('IMAGES_BUCKET_NAME')
IMAGES_DIR = os.getenv('IMAGES_DIR')

if __name__ == '__main__':
    bucket_files = get_bucket_timestamps(IMAGES_BUCKET)

    for file in get_files_in_dir(IMAGES_DIR):
        file_name = os.path.basename(file)

        if file_name not in bucket_files:
            response = upload_file(file, IMAGES_BUCKET, file_name)
            print(f'UPLOADING: {file_name} | https://s3.amazonaws.com/{IMAGES_BUCKET}/{file_name}')