# main.py
import preprocess

#Step 1:Read all books provided like a good boy and then gives me one string with all the data
folder_path = 'D:/Github/generativeAI/scratch/booksDataset'
corpus = preprocess.read_and_concatenate_text_files(folder_path)

#Step 2: Data is stripped of wierd characters
normalized_corpus = preprocess.normalize_text(corpus)

# Step 3:Data is converted into processing tokens, reducing string size and return a workable list
tokens = preprocess.tokenize_text(normalized_corpus)

# Step 4:Spliting the tokens and creating sequences for the model to use
block_size = 128
sequences = preprocess.split_into_sequences(tokens, block_size)

# Step 5:Saving the data so that next time we dont have to pretrain again...
output_file = 'tokenized_data.pt'
preprocess.save_preprocessed_data(sequences, output_file)
