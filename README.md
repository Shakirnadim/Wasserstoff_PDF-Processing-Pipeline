# Domain-Specific-PDF-Summarization-Keyword-Extraction-Pipeline

## Overview
The PDF Processing Pipeline is designed to efficiently extract text and keywords from multiple PDF files and store the results in MongoDB. This solution handles PDFs of varying lengths and structures, optimizing performance and resource management.

## Features
- Batch processing of PDFs from a specified folder
- Text extraction using PyPDF2
- Comprehensive text preprocessing (cleaning, tokenization, stopword removal, lemmatization)
- Keyword extraction using TF-IDF
- MongoDB integration for storing extracted text and metadata

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




 **Set Up MongoDB**
   Ensure MongoDB is installed and running on your local machine. You can use the default settings, or modify the connection string in the code if necessary.

 **Run the Pipeline**
   Modify the `folder_path` variable in the code to point to the directory containing your PDF files:
   ```python
   folder_path = r"E:/wasserstoff AiInternTask"  # Update with your folder path
   ```

  

## Explanation of the Solution

### PDF Ingestion
The pipeline begins by scanning a specified folder for PDF files. It processes each PDF file one at a time, ensuring that text extraction is efficient and robust.

### Text Extraction
The text is extracted from PDFs using the `PyPDF2` library, which effectively handles the extraction process across various PDF formats.

### Text Preprocessing
1. **Cleaning**: Non-alphabetic characters and excessive whitespace are removed.
2. **Tokenization**: The cleaned text is split into individual words (tokens).
3. **Stopword Removal**: Common words that do not contribute meaningful information are filtered out using the NLTK stopwords library.
4. **Lemmatization**: Tokens are converted to their base forms to standardize the text.

### Keyword Extraction
The pipeline employs the TF-IDF method to extract relevant keywords from the processed text, helping to identify the most significant terms in each document.

### MongoDB Storage
Finally, the extracted text and metadata (including file paths and keywords) are stored in a MongoDB database, allowing for efficient retrieval and analysis of the processed documents.






