from botocore.exceptions import ClientError
from dotenv import load_dotenv
import boto3
import time
import os 

load_dotenv()

DISTRIBUTION_ID = os.getenv('DISTRIBUTION_ID')
cloudfront_client = boto3.client('cloudfront') 

def create_invalidation(paths):
    """Create an invalidation for a CloudFront distribution.

    :param paths: List of paths to invalidate (e.g., ['/*'])
    :return: Invalidation ID if successful, None otherwise
    """
    
    try:
        # Create the invalidation batch with unique caller reference
        caller_reference = str(time.time()).replace('.', '')
        invalidation_batch = {
            'Paths': {
                'Quantity': len(paths),
                'Items': paths
            },
            'CallerReference': caller_reference
        }

        # Create the invalidation
        response = cloudfront_client.create_invalidation(
            DistributionId=DISTRIBUTION_ID,
            InvalidationBatch=invalidation_batch
        )

        invalidation_id = response['Invalidation']['Id']
        print(f'Invalidation created with ID: {invalidation_id}')
        return invalidation_id

    except ClientError as e:
        print(f'Error creating invalidation: {e}')
        return None
