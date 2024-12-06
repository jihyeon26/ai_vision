import gradio as gr
from vision import request_vision, FEATURES
from image_processing import draw_image
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

# 2. Retrieve API key and endpoint from environment variables
SUBSCRIPTION_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

# 3. Function to integrate with Gradio
def change_image(feature_list, image_path):
    """
    Handles the image processing workflow.

    Args:
        feature_list (list): List of selected features.
        image_path (str): Path to the input image.

    Returns:
        tuple: Response JSON and annotated image.
    """
    if not feature_list:
        return None, None

    # Call the Vision API
    response_json = request_vision(feature_list, image_path, SUBSCRIPTION_KEY, ENDPOINT)
    # Process the image based on the API response
    image = draw_image(feature_list, image_path, response_json)
    return response_json, image

# 4. Define the Gradio UI
with gr.Blocks() as demo:
    features_checkbox = gr.Checkboxgroup(label="Features", choices=FEATURES)
    input_image = gr.Image(label="Input Image", type="filepath")
    with gr.Row():
        result_image = gr.Image(label="Result Image", type="pil", interactive=False)
        result_json = gr.Json(label="Response JSON")

    # Call the processing function when the input image is changed
    input_image.change(fn=change_image, inputs=[features_checkbox, input_image], outputs=[result_json, result_image])

# 5. Launch the Gradio interface
demo.launch()
