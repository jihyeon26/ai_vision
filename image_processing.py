import random
from PIL import Image, ImageDraw

def random_color():
    """
    Generates a random RGB color.

    Returns:
        tuple: Random RGB color.
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_image(feature_list, image_path, response_json):
    """
    Draws bounding boxes on the image based on the response JSON.

    Args:
        feature_list (list): List of features to process.
        image_path (str): Path to the image file.
        response_json (dict): API response JSON.

    Returns:
        PIL.Image.Image: Annotated image.
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    for feature in feature_list:
        result_key = f"{feature}Result"
        if result_key in response_json:
            result_object = response_json[result_key]
            color = random_color()

            if "values" in result_object:
                values = result_object["values"]

                for value in values:
                    if "boundingBox" in value:
                        bounding_box = value["boundingBox"]
                        x, y, w, h = bounding_box['x'], bounding_box['y'], bounding_box['w'], bounding_box['h']
                        draw.rectangle([(x, y), (x + w, y + h)], outline=color, width=2)
    return image
