# main.py
import preprocess

# Step 1: Read and concatenate text files
folder_path = 'D:/Github/generativeAI/scratch/booksDataset'
corpus = preprocess.read_and_concatenate_text_files(folder_path)

# Step 2: Normalize the text
normalized_corpus = preprocess.normalize_text(corpus)

# Step 3: Tokenize the text
tokens = preprocess.tokenize_text(normalized_corpus)

# Step 4: Split the tokenized text into sequences
block_size = 128
sequences = preprocess.split_into_sequences(tokens, block_size)

# Step 5: Save the preprocessed data
output_file = 'tokenized_data.pt'
preprocess.save_preprocessed_data(sequences, output_file)
