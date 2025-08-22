import base64

import requests


def generate_image(face_image: bytes,
                   prompt: str,
                   negative_prompt: str = "",
                   steps: int = 85,
                   sd_model_name: str = "uberRealisticPornMerge_v23Final",
                   sampler: str = "Euler a",
                   width: int = 512,
                   height: int = 512,
                   cfg_scale: int = 9,
                   url: str = "http://127.0.0.1:7860",
                   preprocessor: str = "ip-adapter_clip_h",
                   control_net_model: str = "ip-adapter-plus-face_sd15",
                   weight=0.35):
    face_b64 = base64.b64encode(face_image).decode("utf-8")

    url = f"{url}/sdapi/v1/txt2img"
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": steps,
        "sampler_name": sampler,
        "width": width,
        "height": height,
        "cfg_scale": cfg_scale,
        "override_settings": {
            "sd_model_checkpoint": sd_model_name
        },
        "alwayson_scripts": {
            "controlnet": {
                "args": [
                    {
                        "input_image": face_b64,
                        "module": preprocessor,
                        "model": control_net_model,
                        "weight": weight,
                        "resize_mode": "Crop and Resize",
                        "lowvram": False,
                        "processor_res": 512,
                        "threshold_a": 100,
                        "threshold_b": 200,
                        "guidance": 1.0,
                        "control_mode": "Balanced"
                    }
                ]
            }
        }
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    result = response.json()
    image_base64 = result["images"][0]


    return base64.b64decode(image_base64)


