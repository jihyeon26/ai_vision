# Vision Analysis and Background Removal with Gradio

This project is a Python-based web application that leverages **Azure Cognitive Services** to perform image analysis and background removal. Built with **Gradio**, the application provides an intuitive interface for exploring features like object detection, text extraction, and smart cropping.

![UI Screenshot](results/result_img.png)<br>

## Features

- **Image Analysis**
  - Detect objects, tags, and people in images.
  - Generate captions and dense captions for images.
  - Perform smart cropping with custom aspect ratios.<br>
  ![UI Screenshot](results/result_img2.png)<br>
  ![UI Screenshot](results/result_read.png)<br>

- **Background Removal**
  - Remove the background or apply foreground matting to images.<br>
 ![UI Screenshot](results/result_bg.png)<br>

- **Dynamic User Interface**
  - Change language settings dynamically.
  - Display Smart Crops parameters only when applicable.

## Tech Stack

- **Python**: Core programming language.
- **Gradio**: Web interface framework.
- **Azure Cognitive Services**: Vision API for image analysis.
- **Pillow (PIL)**: Image processing library.
- **Requests**: HTTP library for API calls.

## Project Structure

```project_directory/
    ├── main.py                 # Gradio UI and event handling
    ├── vision.py               # Vision API-related functions
    ├── background_removal.py   # Background removal API functions
    ├── drawing.py              # Image processing and drawing functions
    ├── constants.py            # Shared constants like features and language codes
    ├── requirements.txt        # Python dependencies
    ├── .gitignore              # Files and folders to exclude from version control
    ├── README.md               # Project documentation
```


