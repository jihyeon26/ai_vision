from PIL import Image, ImageDraw, ImageFont
import platform
import random

def random_color():
    """
    Generates a random RGB color.
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_image(feature_list, image_path, response_json):
    """
    Draws bounding boxes and annotations on the image based on API response.
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font_size = 10
    if platform.system() == "Darwin":
        font = ImageFont.truetype("AppleGothic.ttf", size=font_size)
    elif platform.system() == "Windows":
        font = ImageFont.truetype("malgun.ttf", size=font_size)
    else:
        font = ImageFont.load_default()

    for feature in feature_list:
        result_key = f"{feature}Result"
        result_object = response_json.get(result_key, {})
        color = random_color()

        if "values" in result_object:
            for value in result_object["values"]:
                if "boundingBox" in value:
                    box = value["boundingBox"]
                    x, y, w, h = box["x"], box["y"], box["w"], box["h"]
                    draw.rectangle([(x, y), (x + w, y + h)], outline=color, width=2)
        elif "blocks" in result_object:
            for block in result_object["blocks"]:
                for line in block.get("lines", []):
                    text = line["text"]
                    polygon = [(p["x"], p["y"]) for p in line["boundingPolygon"]]
                    draw.polygon(polygon, outline=color, width=2)
                    draw.text((polygon[3][0], polygon[3][1]+3), text=text, fill=color, font=font)
    return image
