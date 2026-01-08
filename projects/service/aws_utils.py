import boto3

s3_client = boto3.client("s3")
total_bucket=[]
def get_bucket_info():
    buckets = s3_client.list_buckets()["Buckets"]

    for bucket in buckets:
        total_bucket.append(bucket)
    return {
        "total_bucket": len(total_bucket),
        "total_bucket_name": total_bucket["Name"]
    }
