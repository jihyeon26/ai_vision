import requests

FEATURES = ["read", "caption", "denseCaptions", "smartCrops", "objects", "tags", "people"]

def request_vision(feature_list, image_path, subscription_key, endpoint):
    """
    Sends an image to the Azure Computer Vision API for analysis.

    Args:
        feature_list (list): List of features to analyze.
        image_path (str): Path to the image file.
        subscription_key (str): Azure subscription key.
        endpoint (str): API endpoint.

    Returns:
        dict: Response from the API.
    """
    params = {
        "api-version": "2024-02-01",
        "language": "en",
        "features": ",".join(feature_list),
        "gender-neutral-caption": "false"
    }
    headers = {
        "ocp-apim-subscription-key": subscription_key,
        "Content-Type": "application/octet-stream"
    }

    with open(image_path, "rb") as image:
        image_data = image.read()

    response = requests.post(endpoint, params=params, headers=headers, data=image_data)

    if response.status_code == 200:
        return response.json()
    else:
        return dict(status=response.status_code, message=response.text)
