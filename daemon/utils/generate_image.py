from daemon.utils.hash import generate_hash
from daemon.utils.s3 import get_file_from_s3, save_image_to_s3
from daemon.utils.sd import generate_image


def save_and_gen(worker_url, character_name, prompt, negative_prompt):
    face_bytes = get_file_from_s3(file_name=f"{character_name}.jpg", folder="hotify/faces", bucket="f96c0b95-s3-tg-bot")

    image = generate_image(face_image=face_bytes, prompt=prompt, negative_prompt=negative_prompt, url=worker_url)

    url = save_image_to_s3(file_name=f"{generate_hash(length=15)}.png", image_bytes=image, folder="hotify/generations",
                           bucket="f96c0b95-s3-tg-bot")

    return url
