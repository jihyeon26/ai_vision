import requests

def request_vision(feature_list, image_path, api_key, endpoint, language_code, smartcrops_value=None):
    """
    Calls the Vision API to analyze an image.
    """
    params = {
        "api-version": "2024-02-01",
        "language": language_code,
        "gender-neutral-caption": "false",
        "features": ",".join(feature_list)
    }
    headers = {
        "ocp-apim-subscription-key": api_key,
        "Content-Type": "application/octet-stream"
    }

    if smartcrops_value:
        params.update({"smartcrops-aspect-ratios": smartcrops_value})

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = requests.post(endpoint, params=params, headers=headers, data=image_data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status": response.status_code, "message": response.text}
