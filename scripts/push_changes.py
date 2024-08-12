from s3 import upload_file, get_bucket_timestamps
from file_check import get_file_modification_time, get_files_in_dir
from cloudfront import create_invalidation
from dotenv import load_dotenv
from datetime import timedelta
import os 

load_dotenv() 
TIME_LENIENCY = timedelta(minutes=5)
FILE_DIR = os.getenv('FILE_DIR')
BUCKET_NAME = os.getenv('BUCKET_NAME')

if __name__ == '__main__':
    updated_files = []
    files = get_files_in_dir(FILE_DIR)  
    bucket_timestamps = get_bucket_timestamps(BUCKET_NAME)

    print(f'synchronizing deltas with ${FILE_DIR}')
    for file in files:
        file_name = os.path.basename(file)
        mod_time = get_file_modification_time(file)
        
        if file_name not in bucket_timestamps or mod_time > bucket_timestamps[file_name] + TIME_LENIENCY:
            try:
                print(f'{file_name} not updated since {mod_time - bucket_timestamps[file_name]}')
            except KeyError:
                print(f'{file_name} not in s3')
            upload_file(file, BUCKET_NAME, file_name)
            updated_files.append(f'/{file_name}')
    
    if updated_files:
        invalidation = create_invalidation(updated_files)     
        print(f'started invalidation | {invalidation}')
