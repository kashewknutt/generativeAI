import gzip
import json
import os
import torch
from transformers import GPT2Tokenizer

def load_data_from_gz(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            yield json.loads(line.strip())

def preprocess_data(file_paths, tokenizer, max_length=16384, batch_size=1000000):
    tokenized_sequences = []
    batch_counter = 0

    for file_path in file_paths:
        for entry in load_data_from_gz(file_path):
            context = entry.get("context", [])
            response = entry.get("response", [])
            conversation = context + response
            if conversation:
                text = " ".join(conversation)
                tokens = tokenizer(text, truncation=True, max_length=max_length, return_tensors="pt").input_ids
                tokenized_sequences.append(tokens)
                
                if len(tokenized_sequences) >= batch_size:
                    torch.save(tokenized_sequences, f'tokenizedData/tokenized_data_batch_{batch_counter}.pt')
                    tokenized_sequences = []
                    batch_counter += 1
                    
    if tokenized_sequences:
        torch.save(tokenized_sequences, f'tokenized_data_batch_{batch_counter}.pt')

    print(f"Data preprocessing complete and tokenized data saved in {batch_counter + 1} batches!")

# Define the folder containing the .jsonl.gz files
folder_path = 'D:/v1.0/train'

# Get a list of all .jsonl.gz files
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jsonl.gz')]

# Initialize the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Preprocess the data
preprocess_data(file_paths, tokenizer)
