# Domain-Specific-PDF-Summarization-Keyword-Extraction-Pipeline

# Overview
This repository implements a robust PDF processing pipeline capable of handling a large volume of PDF files. The pipeline extracts text from each PDF, preprocesses the text, extracts relevant keywords using TF-IDF, and stores the results in a MongoDB database for further analysis.


# Key Features:

Text Extraction:  Extracts textual content from PDF files.

Text Preprocessing: Cleans and processes extracted text by removing non-alphabetic characters, stopwords, and performs tokenization and lemmatization.

Keyword Extraction: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to identify and extract key terms from the processed text.

MongoDB Integration: Stores PDF metadata (id, pdf_path, text , summary, and keywords ) in MongoDB for easy retrieval and analysis.



# Pipeline Steps

Text Extraction: Extracts text from PDF files using PyPDF2.

Text Cleaning: Removes unwanted characters and normalizes whitespace.

Tokenization: Converts cleaned text into individual tokens (words).

Stopword Removal: Filters out common stopwords from tokenized text.

Lemmatization: Reduces words to their base forms using WordNet.

Keyword Extraction: Uses TF-IDF to identify and rank keywords from the processed text.

Storage in MongoDB: Each PDF's metadata, including the extracted text and keywords, is stored in MongoDB.


# Folder Structure

/src: Contains all the source code for the pipeline.

/data: Directory where the PDFs are stored (provided path).

/docs: Documentation files for better understanding of the pipeline.


# How to Use

Place all your PDF files in the designated folder.

Run the pipeline to process each PDF and store the results in MongoDB.

Retrieve and analyze the stored metadata in MongoDB as needed.


# Prerequisites:

Ensure that MongoDB is set up locally or remotely to store the extracted data.


