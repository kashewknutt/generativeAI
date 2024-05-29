import gzip
import json
import os
import torch
from transformers import GPT2Tokenizer

def load_data_from_gz(file_path):
    data = []

    #Preexisting function to handle the specially archived data in the google data folder
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def preprocess_data(file_paths, tokenizer, max_length=512):
    tokenized_sequences = []
    for file_path in file_paths:
        data = load_data_from_gz(file_path)
        for entry in data:
            context = entry.get("context", [])
            response = entry.get("response", [])
            conversation = context + response
            if conversation:
                # Concatenate the conversation into a single string
                text = " ".join(conversation)
                # Tokenize the text
                tokens = tokenizer(text, truncation=True, max_length=max_length, return_tensors="pt").input_ids
                tokenized_sequences.append(tokens)
    return tokenized_sequences

# Define the folder containing the .jsonl.gz files
folder_path = 'D:/v1.0/train'

# Get a list of all .jsonl.gz files
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jsonl.gz')]

# Initialize the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Preprocess the data
tokenized_data = preprocess_data(file_paths, tokenizer)

# Save the tokenized data
torch.save(tokenized_data, 'tokenized_data.pt')

print("Data preprocessing complete and tokenized data saved!")
