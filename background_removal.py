import requests
from PIL import Image
import io

def request_background_removal(mode, image_path, api_key, endpoint):
    """
    Calls the Vision API to remove the background of an image.
    """
    params = {
        "api-version": "2023-04-01-preview",
        "mode": mode
    }
    headers = {
        "ocp-apim-subscription-key": api_key,
        "Content-Type": "application/octet-stream"
    }

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = requests.post(endpoint, params=params, headers=headers, data=image_data)

    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content))
    else:
        return None
