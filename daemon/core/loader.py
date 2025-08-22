import asyncio

import boto3
from botocore.config import Config


import daemon.core.config as cfg
import aio_pika



async def init_rabbitmq():
    connection = await aio_pika.connect_robust(
        cfg.RABBIT_URL, heartbeat=30
    )
    channel = await connection.channel()
    await channel.declare_queue("sd_gen_queue", durable=True)
    await channel.declare_queue("message", durable=True)

    exchange = channel.default_exchange
    return connection, channel, exchange


connection, channel, exchange = asyncio.run(init_rabbitmq())

s3_client = boto3.client(
    's3',
    endpoint_url=cfg.S3_ENDPOINT,
    aws_access_key_id=cfg.S3_ACCESS_KEY,
    aws_secret_access_key=cfg.S3_SECRET_ACCESS_KEY,
    region_name=cfg.S3_REGION,
    config=Config(s3={'addressing_style': 'path'})
)