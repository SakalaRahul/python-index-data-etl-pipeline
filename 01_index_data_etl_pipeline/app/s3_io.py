import boto3
from app.config import settings

def download_s3_object(key: str, destination: str):
    if not settings.s3_bucket:
        raise RuntimeError("S3_BUCKET is not configured")
    boto3.client("s3", region_name=settings.aws_region).download_file(
        settings.s3_bucket, key, destination)

def upload_file(path: str, key: str):
    if not settings.s3_bucket:
        raise RuntimeError("S3_BUCKET is not configured")
    boto3.client("s3", region_name=settings.aws_region).upload_file(
        path, settings.s3_bucket, key)
