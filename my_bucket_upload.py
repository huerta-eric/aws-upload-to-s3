import boto3
import os
from secrets import access_key_id, secret_access_key

s3_client = boto3.client("s3",
                         aws_access_key_id=access_key_id,
                         aws_secret_access_key=secret_access_key)

bucket_name = "my-bucket-uploads-39"
bucket_dir = "csv-dir/"
path = os.getcwd() + "/upload"

for file in os.listdir(path):
    if ".csv" in file:
        print("Pushing " + file + " to S3.")
        full_path = path + "/" + file
        upload_file_key = bucket_dir + str(file)

        s3_client.upload_file(full_path, bucket_name, upload_file_key)


