import json

import aio_pika

from daemon.core.loader import init_rabbitmq


async def publish(exchange: aio_pika.Exchange, routing_key: str, payload: dict):
    if exchange.channel.is_closed:
        connection, channel, exchange = await init_rabbitmq()
    body = json.dumps(payload).encode("utf-8")
    message = aio_pika.Message(body=body, delivery_mode=aio_pika.DeliveryMode.PERSISTENT)
    await exchange.publish(message, routing_key=routing_key)