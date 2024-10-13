#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import numpy as np
import PyPDF2
import nltk
from pymongo import MongoClient
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sumy.parsers.plaintext import PlaintextParser  
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer 

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# In[ ]:


# Text Cleaning Function
def clean_text(text):
    print("Cleaning text...")
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove unwanted characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Tokenization Function
def tokenize_text(text):
    print("Tokenizing text...")
    return word_tokenize(text.lower())

# Function to remove stopwords
def remove_stopwords(tokens):
    print("Removing stopwords...")
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Lemmatization Function
def lemmatize_tokens(tokens):
    print("Lemmatizing tokens...")
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

# Full Preprocessing Pipeline
def preprocess_text(text):
    print("Preprocessing text...")
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    tokens = remove_stopwords(tokens)
    lemmatized_tokens = lemmatize_tokens(tokens)
    return lemmatized_tokens

# Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    print(f"Extracting text from PDF: {pdf_path}")
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + ' '
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

# Summarization Function using Sumy
def generate_summary(text, sentence_count):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()  # Using LSA for summarization
        summary = summarizer(parser.document, sentence_count)  # Summarize to a specific number of sentences
        return ' '.join(str(sentence) for sentence in summary)  # Join sentences into a single string
    except Exception as e:
        print(f"Error generating summary: {e}")
        return text  # Return original text on error

# Extract Keywords using TF-IDF
def extract_keywords(text):
    print("Extracting keywords...")
    try:
        processed_tokens = preprocess_text(text)
        processed_text = ' '.join(processed_tokens)
        vectorizer = TfidfVectorizer(stop_words='english')  # Exclude common English stopwords
        X = vectorizer.fit_transform([processed_text])
        indices = np.argsort(X.toarray()).flatten()[-15:]  # Get the top 15 keywords
        keywords = [vectorizer.get_feature_names_out()[i] for i in indices]
        
        # Filter out generic keywords 
        generic_keywords = set(['the', 'is', 'and', 'to', 'in', 'for', 'of', 'a', 'on'])
        domain_specific_keywords = [kw for kw in keywords if kw not in generic_keywords]
        
        return domain_specific_keywords
    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return []

# Process a single PDF file
def process_single_pdf(pdf_path):
    try:
        print(f"Processing PDF: {pdf_path}")
        text = extract_text_from_pdf(pdf_path)
        if text:
            words = text.split()  # Split text into words
            word_count = len(words)
            
            # Determine summary length based on text length
            # Minimum of 1 sentence and maximum of 10% of the total word count
            
            sentence_count = min(max(word_count // 100, 1), 10)  # Example: 1-10 sentences based on word count
            summary = generate_summary(text, sentence_count)
            keywords = extract_keywords(text)
            return {
                "pdf_path": pdf_path,
                "text": text,
                "summary": summary,
                "keywords": keywords
            }
        else:
            print(f"No text extracted for {pdf_path}.")
            return None
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

# Store results in MongoDB
def store_in_mongodb(pdf_data):
    print("Connecting to MongoDB...")
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['pdf_data_db']
        collection = db['pdf_metadata']

        for data in pdf_data:
            keywords = data["keywords"].tolist() if isinstance(data["keywords"], np.ndarray) else data["keywords"]
            document = {
                "pdf_path": data["pdf_path"],
                "text": data["text"],
                "summary": data["summary"],  # Store summary
                "keywords": keywords
            }
            collection.insert_one(document)
            print(f"Stored metadata for {os.path.basename(data['pdf_path'])} in MongoDB.")
    except Exception as e:
        print(f"Error storing data in MongoDB: {e}")

# Process PDFs from folder one by one
def process_pdfs_from_folder(folder_path):
    print(f"Looking for PDF files in folder: {folder_path}")
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    print(f"Found {len(pdf_files)} PDF files.")

    if not pdf_files:
        print("No PDF files found.")
        return

    pdf_results = []
    for pdf in pdf_files:
        result = process_single_pdf(pdf)
        if result:
            pdf_results.append(result)

    # Store results in MongoDB
    if pdf_results:
        store_in_mongodb(pdf_results)

#  specify folder path
folder_path = r"E:/wasserstoff AiInternTask"  
process_pdfs_from_folder(folder_path)


# In[ ]:




