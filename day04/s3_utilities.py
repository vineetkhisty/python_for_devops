import boto3 # this package interacts with the AWS services and does the specified operations
import pdb # Debugger

def get_connection(services):
    return boto3.client(services)

def show_buckets(s3_client):
    buckets = s3_client.list_buckets()
    return buckets

def create_buckets(s3_client,bucket_name,location):
    # pdb.set_trace()
    try:
        buckets = s3_client.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration={
            'LocationConstraint': location,
        }, 
        )
        return buckets
    except Exception as e:
        print("Error:",e)

def upload(s3_client,file_path,bucket_name,key_name):
     s3_client.upload_file(file_path,bucket_name,key_name)
     print("File uploaded successfully")




s3 = get_connection("s3")

bucket_list = show_buckets(s3)

for bucket in bucket_list["Buckets"]:
     print(bucket["Name"])

response = create_buckets(s3,"vineet-devops-practice7","us-west-2")

try:
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("Bucket created successfully")
except Exception as e:
        print("Error in creating bucket", e)


upload(s3,"output.json","vineet-devops-practice1","output.json")