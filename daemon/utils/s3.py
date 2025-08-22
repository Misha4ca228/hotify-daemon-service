from loguru import logger

from daemon.core.loader import s3_client


def save_image_to_s3(file_name: str, image_bytes: bytes, folder: str = "", bucket: str = "your-bucket") -> str:
    try:
        key = f"{folder}/{file_name}" if folder else file_name
        s3_client.put_object(Body=image_bytes, Bucket=bucket, Key=key)
        url = f"{s3_client.meta.endpoint_url}/{bucket}/{key}"
        return url
    except Exception as e:
        logger.error(f"Failed to upload {file_name} to S3: {e}")
        raise


def get_file_from_s3(file_name: str, folder: str = "", bucket: str = "your-bucket") -> bytes:
    try:
        key = f"{folder}/{file_name}" if folder else file_name
        response = s3_client.get_object(Bucket=bucket, Key=key)
        file_bytes = response["Body"].read()
        return file_bytes
    except Exception as e:
        logger.error(f"Failed to download {file_name} from S3: {e}")
        raise
