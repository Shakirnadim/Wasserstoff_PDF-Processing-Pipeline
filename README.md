# Domain-Specific-PDF-Summarization-Keyword-Extraction-Pipeline



## Overview
This PDF Processing Pipeline extracts text, generates summaries, identifies keywords from multiple PDF files, and stores the results in MongoDB. The solution handles PDFs of various lengths and structures while optimizing performance and resource management.

## Features
- Batch processing of PDFs from a specified folder
- Text extraction using PyPDF2
- Comprehensive text preprocessing (cleaning, tokenization, stopword removal, lemmatization)
- Keyword extraction using TF-IDF
- PDF summarization  using custom text summarization techniques
- MongoDB integration for storing extracted text, summaries, and metadata

## System Requirements
- Python 
- MongoDB (installed and running)

## Dependencies
The project requires the following Python libraries:
- `PyPDF2`
- `nltk`
- `pymongo`
- `scikit-learn`
- `numpy`

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shakirnadim/rishi-pawar-wasserstoff-AiInternTask
   cd rishi-pawar-wasserstoff-AiInternTask

   ```

2. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB**
   Ensure MongoDB is installed and running on your local machine. You can use the default settings, or modify the connection string in the code if necessary.

5. **Run the Pipeline**
   Modify the `folder_path` variable in the code to point to the directory containing your PDF files:
   ```python
   folder_path = r"E:/wasserstoff AiInternTask"  # Update with your folder path
   ```

   Execute the script to process the PDFs:
   ```bash
   python <your_script_name>.py
   ```

## Explanation of the Solution

### PDF Ingestion
The pipeline begins by scanning a specified folder for PDF files. It processes each PDF one by one, ensuring that text extraction is efficient and robust.

### Text Extraction
Text is extracted from PDFs using the `PyPDF2` library, which works with a wide range of PDF formats.

### Text Preprocessing
1. **Cleaning**: The text is stripped of non-alphabetic characters and excess whitespace.
2. **Tokenization**: The cleaned text is split into individual words (tokens).
3. **Stopword Removal**: Common stopwords are removed using the NLTK library.
4. **Lemmatization**: The tokens are lemmatized (converted to their root forms) using the WordNetLemmatizer.

### PDF Summarization
After text extraction and preprocessing, the pipeline generates a **summary** of the content. A simple summarization technique (e.g., sentence ranking, text reduction) is applied to condense the text into a few key sentences that represent the document’s main points.

### Keyword Extraction
The TF-IDF (Term Frequency-Inverse Document Frequency) method is used to extract keywords from the preprocessed text, providing the most relevant terms in each document.

### MongoDB Storage
The extracted text, summary, keywords, and metadata (such as file paths) are stored in a MongoDB database for easy retrieval and further analysis.


```






