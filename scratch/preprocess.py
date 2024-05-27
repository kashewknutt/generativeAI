# preprocess.py
import os
import re
import torch
from transformers import GPT2Tokenizer # type: ignore

def read_and_concatenate_text_files(folder_path):
    """
    Reads all the books available in the Dataset and then converts them into one very very very long string
    
    Parameters:
    folder_path (str): The directory of the files. Recommended to enter from Drive letter eg: C:/path/..
    
    Returns:
    str: One string (corpus) basic concatenation no rocket science
    """
    corpus = "" #The final corpus

    #For loop goes through the entire directory and selects only the .txt files
    for filename in os.listdir(folder_path): 
        if filename.endswith(".txt"):
            #opens, reads then appends to the next line in the corpus with \n for newLine
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                corpus += text + "\n"
    
    #print logs to help me track the cureent status
    print("Concatenation complete!")
    print("Corpus length:", len(corpus), "characters")
    return corpus

def normalize_text(corpus):
    """
    TEchnically removes all weird symbols
    
    Parameters:
    corpus (str): Our holy corpus
    
    Returns:
    str: Processed text. (First layer of preprocessing)
    """
    corpus = corpus.lower()  # Convert to lowercase
    corpus = re.sub(r'[^a-zA-Z0-9\s]', '', corpus)  # Remove special characters
    print("Normalization complete!")
    return corpus

def tokenize_text(corpus):
    """
    Tokenize the text using GPT-2 tokenizer.
    
    Parameters:
    corpus (str): The input text.
    
    Returns:
    List[int]: Tokenized text.
    """
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokens = tokenizer.encode(corpus)
    print("Tokenization complete!")
    print("Number of tokens:", len(tokens))
    return tokens

def split_into_sequences(tokens, block_size=128):
    """
    Split the tokenized text into sequences of fixed length.
    
    Parameters:
    tokens (List[int]): Tokenized text.
    block_size (int): Length of each sequence.
    
    Returns:
    List[List[int]]: List of sequences.
    """
    sequences = [tokens[i:i+block_size] for i in range(0, len(tokens) - block_size + 1, block_size)]
    print("Splitting into sequences complete!")
    print("Number of sequences:", len(sequences))
    return sequences

def save_preprocessed_data(sequences, output_file='tokenized_data.pt'):
    """
    Save the preprocessed data to a file.
    
    Parameters:
    sequences (List[List[int]]): Preprocessed sequences.
    output_file (str): Path to the output file.
    """
    torch.save(sequences, output_file)
    print(f"Data saved to {output_file}!")
