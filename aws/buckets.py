from pathlib import Path
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize S3 client
s3 = boto3.client('s3', region_name="ap-south-1", aws_access_key_id="test_key", aws_secret_access_key="access_key")

BUCKET_NAME = "bucket_name"

def upload_file(file_name, bucket, object_name=None):
    try:
        object_name = object_name or file_name.name
        s3.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
    except NoCredentialsError:
        print("Credentials not available.")

def download_file(object_name, bucket, file_name=None):
    try:
        file_name = file_name or object_name
        s3.download_file(bucket, object_name, file_name)
        print(f"File {object_name} downloaded from {bucket} to {file_name}")
    except NoCredentialsError:
        print("Credentials not available.")

# Example usage
parent = Path(__file__).parent
path = parent.joinpath("example.txt")
for object in s3.list_objects(Bucket=BUCKET_NAME)["Contents"]:
    print(object["Key"])
upload_file(path, BUCKET_NAME)
# download_file(str(parent.joinpath("remote_file.txt")), BUCKET_NAME, "local_copy.txt")