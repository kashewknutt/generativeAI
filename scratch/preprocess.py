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

    #convert to lowercase so that each character had equal meaning
    corpus = corpus.lower() 

    #a very clever way to remove weird characters 
    corpus = re.sub(r'[^a-zA-Z0-9\s]', '', corpus)
    print("Normalization complete!")
    return corpus

def tokenize_text(corpus):
    """
    Tokens are basically collections of 3-4 letters at a time. 
    They like create modifiable and relatable data. 
    i.e. data that can be used for inferences
    
    Parameters:
    corpus (str): The corpus we just processed and removed the wierd characters
    
    Returns:
    List[int]: A list of tokens. Waaaay smaller than the original corpus (Second layer of preprocessing: Tokernizing)
    """

    #pre-existing transformer (encoder-decoder) model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    #Tokenize the corpus
    tokens = tokenizer.encode(corpus)
    print("Tokenization complete!")
    print("Number of tokens:", len(tokens))
    return tokens

def split_into_sequences(tokens, block_size=128):
    """
    This is where it gets interesting. the block size is how big a particular training sequence is required.
    i.e. how many tokens will allocate in a sequence..
    
    Parameters:
    tokens (List[int]): the tokens list we just created
    block_size (int): how long each sequence should be
    
    Returns:
    List[List[int]]: The sequences of tokens. We will use these sequence (after pairing) to train. (Third layer of preprocessing)
    """

    #Selects tokens every block size step till it reaches a point where no more blocks can be used the rest tokens are ignored for now
    sequences = [tokens[i:i+block_size] for i in range(0, len(tokens) - block_size + 1, block_size)]


    print("Splitting into sequences complete!")
    print("Number of sequences:", len(sequences))
    return sequences

def save_preprocessed_data(sequences, output_file='tokenized_data.pt'):
    """
    Saving the data to a specific file.

    Parameters:
    sequences (List[List[int]]): Our token sequences list
    output_file (str): Path to the output file.

    Returns:
    Nothing
    """
    torch.save(sequences, output_file)
    print(f"Data saved to {output_file}!")
