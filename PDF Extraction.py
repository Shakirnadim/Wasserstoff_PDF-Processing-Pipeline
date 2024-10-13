#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json

# Load the JSON file that contains the PDF URLs
with open('E:/wasserstoff AiInternTask/Dataset.json', 'r') as file:
    data = json.load(file)

pdf_urls = list(data.values())  # Extract URLs into a list


# In[6]:


import requests

def download_pdf(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download: {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Example to download all PDFs from URLs
def download_all_pdfs(pdf_urls, download_folder):
    for i, url in enumerate(pdf_urls):
        file_name = f"pdf_{i+1}.pdf"  # Name the file with an index
        save_path = f"{download_folder}/{file_name}"  # Path to save the file
        download_pdf(url, save_path)

# folder where  downloaded PDFs are saved
download_folder = "E:/wasserstoff AiInternTask"

# Call the function to download all PDFs
download_all_pdfs(pdf_urls, download_folder)


# In[ ]:





# In[ ]:




