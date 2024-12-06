import gradio as gr
from dotenv import load_dotenv
import os
import io
from vision import request_vision
from background_removal import request_background_removal
from drawing import draw_image
from constants import FEATURES

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and endpoints from environment variables
API_KEY = os.getenv("API_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
SEGMENT_ENDPOINT = os.getenv("SEGMENT_ENDPOINT")

LANGUAGE_CODE = "en"  # Default language

def change_image(feature_list, image_path, smartcrops_value):
    if len(feature_list) == 0 or not image_path:
        return None, None
    
    if not "smartCrops" in feature_list:
        smartcrops_value = None
        
    response_json = request_vision(
        feature_list, image_path, API_KEY, VISION_ENDPOINT, LANGUAGE_CODE, smartcrops_value
    )
    image=draw_image(feature_list, image_path, response_json)
    return response_json, image

def change_background_image(removal_type_radio, image_path):
    return request_background_removal(removal_type_radio, image_path, API_KEY, SEGMENT_ENDPOINT)


def change_smartcrops_value(value):
    print(value)
    
with gr.Blocks() as demo:
    smartcrops_value = gr.State("")
    with gr.Tab("Image Analysis"):
        language_radio = gr.Radio(label="select language", choices=["en", "ko"], value="en")              
        features_checkbox = gr.Checkboxgroup(label="Features", choices=FEATURES)
        
        @language_radio.change(inputs=[language_radio], outputs=[features_checkbox])
        def change_features(language):
            global LANGUAGE_CODE
            LANGUAGE_CODE = language
            if language == "ko":
                return gr.Checkboxgroup(label="Features", choices=FEATURES[:4])
            else:
                return gr.Checkboxgroup(label="Features", choices=FEATURES)

        @gr.render(inputs=[features_checkbox])
        def render_smartcrops_params(features):
            def change(value):
                print(smartcrops_value)
                return value
                
            if "smartCrops" in features:
                smartcrops_params_textbox = gr.Textbox(key="123", label="Ratios", visible=True)
                smartcrops_params_textbox.change(fn=change, inputs=[smartcrops_params_textbox], outputs=[smartcrops_value])
        
        input_image = gr.Image(label="Input Image", type="filepath")
        
        with gr.Row():
            result_image = gr.Image(label="Output Image", type="pil", interactive=False)
            result_json = gr.Json(label="Output Json")
        
    
    with gr.Tab("Remove Background"):
        removal_type_radio = gr.Radio(label="type", choices=["backgroundRemoval", "foregroundMatting"], value="backgroundRemoval")
        input_background_image = gr.Image(label="Input Image", type="filepath")
        output_background_image = gr.Image(label="Output Image", type="pil", interactive=False)
    
    input_background_image.change(fn=change_background_image, 
                                  inputs=[removal_type_radio, input_background_image], 
                                  outputs=[output_background_image])
    input_image.change(fn=change_image, 
                       inputs=[features_checkbox, input_image, smartcrops_value], 
                       outputs=[result_json, result_image])
    

    
demo.launch()
