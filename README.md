Image Captioning Model

Overview
- Generates natural language captions for images using a feature extractor and a trained sequence model.
- Provides a simple Streamlit web app to upload an image and view its generated caption.

Features
- Upload `jpg`, `jpeg`, or `png` images from the browser.
- Displays the uploaded image and the generated caption.
- Clean, minimal UI that runs locally via Streamlit.

Tech Stack
- Python 3.10
- Streamlit for the web interface
- TensorFlow/Keras for model loading (`mymodel.h5`)
- MobileNetV2 for image feature extraction
- NLTK/Python utilities for text processing

Project Structure
- `app.py` — Streamlit application entry point
- `requirements.txt` — Python dependencies
- `mymodel.h5` — Trained captioning model (binary)
- `tokenizer.pkl` — Fitted tokenizer object
- `image-captioner.ipynb` — Notebook used during development
- `Flickr8k_Dataset/` — Dataset directory (ignored by Git)

Prerequisites
- Python 3.10 installed and available via the Windows `py` launcher.
- A virtual environment is recommended.

Setup
1. Navigate to the project folder:
   - `cd "c:\Users\KIIT\Documents\Machine Learning Projects\Project 12 Image Captioning Model"`
2. Install dependencies (Windows):
   - `py -m pip install -r requirements.txt`
   - If `pip` is outdated, update it:
     - `py -m pip install --upgrade pip`
3. Verify that `mymodel.h5` and `tokenizer.pkl` are present in the project root.

Run Locally
- Start the web app:
  - `streamlit run app.py`
- Or specify a port if needed:
  - `streamlit run app.py --server.port 8502`
- Open the displayed local URL in your browser (e.g., `http://localhost:8502`).

Usage
- Click "Choose an image" and upload a file.
- The app shows the image and then renders a generated caption.

Notes
- The dataset folder `Flickr8k_Dataset/` is excluded from version control via `.gitignore`.
- Large files: `mymodel.h5` is included for convenience and may exceed GitHub’s recommended size. Consider using Git LFS for long-term storage.

Troubleshooting
- Pip dependency resolution errors:
  - Ensure you’re using Python 3.10 and run `py -m pip install -r requirements.txt`.
  - If you see typing-extensions conflicts, update it via `py -m pip install typing_extensions==4.8.0`.
- Performance:
  - CPU-only inference works out of the box. If you have a compatible NVIDIA GPU, you can install a CUDA-enabled PyTorch build to speed up inference.
- Streamlit won’t start:
  - Confirm installation: `py -m pip show streamlit`.
  - Try a different port: `streamlit run app.py --server.port 8502`.

Acknowledgments
- Flickr8k dataset creators and maintainers.
- Open-source libraries and frameworks that enabled this project.