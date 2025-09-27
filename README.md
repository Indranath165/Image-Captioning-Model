<h1>📸 Image Caption Generator</h1>

<p>
    This project represents a sophisticated fusion of Computer Vision (CV) and Natural Language Processing (NLP) techniques, culminating in an effective Image Caption Generator.
    The core of the system is a classic <b>Encoder-Decoder architecture</b> built using <b>TensorFlow/Keras</b>. The <b>VGG16 CNN</b> acts as the Encoder, extracting high-dimensional visual features, which are then fed to an <b>LSTM network</b> (the Decoder) to generate descriptive sentences.
    Crucially, the model incorporates an <b>Attention Mechanism</b> to ensure the captioning process dynamically focuses on the most relevant parts of the image as each word is generated, leading to more accurate and contextually rich descriptions.
</p>
<p>
    The deployment script leverages <b>Streamlit</b> for a clean, user-friendly interface. While the core training uses your custom CNN-LSTM model, the final web application is enhanced by integrating the modern <b>Salesforce BLIP model</b> (via Hugging Face Transformers) for state-of-the-art inference speed and quality, showcasing a robust, full-stack machine learning solution.
</p>
<p>
    Check out the live demo of this Image Caption Generator web application at
    <a href="https://image-captioning-model.streamlit.app/" target="_blank">Streamlit App Link</a>.
</p>

<hr>

<h2>✨ Features</h2>

<h3>🧠 Model Architecture</h3>
<ul>
    <li><b>Encoder-Decoder Design</b>: Uses a two-part neural network system for image-to-text translation.</li>
    <li><b>VGG16 Encoder</b>: Utilizes a pre-trained VGG16 CNN model for robust image feature extraction.</li>
    <li><b>LSTM Decoder with Attention</b>: A custom Bidirectional LSTM network generates the caption, incorporating an <b>Attention Mechanism</b> for focused word generation.</li>
</ul>

<h3>🌐 Deployment Ready</h3>
<ul>
    <li><b>Streamlit App</b>: Includes a basic web application (<code>app.py</code>) for easy demonstration.</li>
    <li><b>Evaluation</b>: Model performance is measured using the standard <b>BLEU Scores</b> metric.</li>
</ul>

<hr>

<h2>💻 Model Architecture Summary</h2>

<table>
    <thead>
        <tr>
            <th>Component</th>
            <th>Role</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Encoder (CNN)</b></td>
            <td>Feature Extraction</td>
            <td>Pre-trained <b>VGG16</b> (ImageNet weights)</td>
        </tr>
        <tr>
            <td><b>Decoder (RNN)</b></td>
            <td>Caption Generation</td>
            <td>Custom <b>Bidirectional LSTM</b></td>
        </tr>
        <tr>
            <td><b>Core Mechanism</b></td>
            <td>Alignment</td>
            <td><b>Dot-Product Attention</b></td>
        </tr>
        <tr>
            <td><b>Framework</b></td>
            <td>Deep Learning</td>
            <td><b>TensorFlow 2.x / Keras</b></td>
        </tr>
        <tr>
            <td><b>Dataset</b></td>
            <td>Training Data</td>
            <td><b>Flickr8k Dataset</b> (<a href="https://www.kaggle.com/datasets/adityajn105/flickr8k" target="_blank">Kaggle Link</a>)</td>
        </tr>
    </tbody>
</table>

<hr>

<h2>🚀 Quick Start (Training & Installation)</h2>

<h3>1. Acquire Dependencies and Repository</h3>
<p>First, clone the project repository and install the necessary Python libraries:</p>
<pre><code>git clone https://github.com/Indranath165/Image-Captioning-Model.git
cd Image-Captioning-Model
pip install tensorflow keras numpy matplotlib pillow tqdm nltk streamlit transformers</code></pre>

<h3>2. Prepare the Dataset</h3>
<p>Download the <b>Flickr8k Dataset</b> from <a href="https://www.kaggle.com/datasets/adityajn105/flickr8k" target="_blank">Kaggle</a> (Images folder and <code>captions.txt</code>) and upload the <b>Flickr8k_Dataset</b> folder to your Google Drive.</p>

<h3>3. Run Training in Google Colab</h3>
<ol>
    <li>Upload the <code>image-captioner.ipynb</code> notebook to Google Colab.</li>
    <li>Enable the <b>GPU runtime</b> (Runtime &gt; Change runtime type).</li>
    <li>Mount Google Drive and update the <code>INPUT_DIR</code> variable in the notebook's second cell to point to your dataset location (e.g., <code>/content/drive/MyDrive/Flickr8k_Dataset</code>).</li>
    <li>Execute all cells sequentially to run Feature Extraction, Training (50 epochs), and Evaluation.</li>
    <li>The trained model will be saved as <code>mymodel.h5</code>.</li>
</ol>

<h3>4. Run the Streamlit Application (Inference)</h3>
<p>After training, you can run the demonstration web application:</p>
<pre><code>streamlit run app.py</code></pre>
<p>Open the web app in your browser: <a href="http://localhost:8501" target="_blank">http://localhost:8501</a></p>

<hr>

<h2>📂 Project Structure</h2>

<pre><code>.
├── image-captioner.ipynb    # Main training and evaluation notebook (CNN-LSTM-Attention)
├── mymodel.h5               # Trained model weights (Output)
├── tokenizer.pkl            # Saved vocabulary tokenizer (Output)
├── app.py                   # Streamlit web application for demonstration
└── README.md                # This file
</code></pre>

<hr>
<h2>&#128640; Technologies Used</h2>
<ul>
    <li><b>Deep Learning Framework:</b> TensorFlow / Keras</li>
    <li><b>Computer Vision Model:</b> VGG16 (for feature extraction)</li>
    <li><b>Natural Language Model:</b> LSTM (with Bidirectional wrappers)</li>
    <li><b>Interface:</b> Streamlit</li>
    <li><b>Data Processing:</b> NumPy, Pandas</li>
    <li><b>Evaluation:</b> NLTK (Natural Language Toolkit)</li>
    <li><b>Language:</b> Python 3.x</li>
</ul>

<hr>

<h2>💾 Data Preprocessing Steps</h2>
<p>This section details the critical steps taken to transform the raw text and image data into a format suitable for the neural network:</p>
<ul>
    <li><b>Caption Normalization</b>: Details how raw text is treated (lowercased, punctuation removed, single characters filtered) to create a clean, standardized vocabulary.</li>
    <li><b>Start/End Tokenization</b>: Explains the addition of <code>startseq</code> and <code>endseq</code> tokens, which are essential markers for the LSTM decoder to know when to begin and terminate sentence generation.</li>
    <li><b>Vocabulary and Padding</b>: Specifies that a consistent vocabulary is built and all input sequences are padded to a single maximum length, a requirement for batch processing in the Keras model.</li>
    <li><b>Feature Persistence</b>: Highlights that VGG16 features are pre-extracted and saved (using <code>pickle</code>) to disk, eliminating the need to re-run the time-consuming extraction process for every training session.</li>
</ul>

<hr>

<h2>📈 Model Performance & Metrics</h2>
<p>This section follows the Inference and Evaluation part and provides a deeper breakdown of your model's performance on the test set:</p>
<ul>
    <li><b>Greedy Search Decoding</b>: Explicitly states that the current inference mechanism uses Greedy Search, where the model selects the single word with the highest probability at each step to build the caption.</li>
    <li><b>BLEU Score Breakdown</b>: Provides the final, trained BLEU scores (BLEU-1, BLEU-2, etc.) and explains what each score represents (e.g., BLEU-1 measures unigram matching, BLEU-2 measures bigram matching).</li>
    <li><b>Validation Loss Tracking</b>: Mentions that the model tracks validation loss during the 50 epochs to ensure training generalizes well and does not overfit to the training data.</li>
</ul>
<hr>

<h2>🤝 Contributions</h2>
<p>
        Contributions are welcome! We value your input and encourage you to actively participate in the project. 
        If you have any ideas, suggestions, bug reports, or feature requests, please don't hesitate to open an issue on GitHub. 
        Additionally, we appreciate any code contributions you may have. If you'd like to contribute code, please submit a pull request, 
        and we will review it as soon as possible. Thank you for your support!
</p>
