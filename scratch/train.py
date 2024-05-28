import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling # type: ignore
from torch.utils.data import Dataset

def load_preprocessed_data(file_path):
    """
    This gets the datafile we created during preprocessing and extracts the sequences from it
    
    Parameters:
    file_path (str): Path to the file containing preprocessed data.
    
    Returns:
    List[List[int]]: The sequences we'll use to train
    """
    sequences = torch.load(file_path)
    print(f"Loaded {len(sequences)} sequences from {file_path}")
    return sequences

# Load the preprocessed data
data_file = 'tokenized_data.pt'
sequences = load_preprocessed_data(data_file)

class TextDataset(Dataset):
    def __init__(self, sequences):
        self.examples = sequences

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        return torch.tensor(self.examples[i], dtype=torch.long)

# Initialize the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Move model to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Prepare the dataset
train_dataset = TextDataset(sequences)

# Initialize the data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Set up the training arguments
training_args = TrainingArguments(
    output_dir='./results',          # output directory
    overwrite_output_dir=True,       # overwrite the content of the output directory
    num_train_epochs=3,              # number of training epochs
    per_device_train_batch_size=4,   # batch size for training
    save_steps=10_000,               # save checkpoint every 10,000 steps
    save_total_limit=2,              # limit the total amount of checkpoints
    prediction_loss_only=True,
    # Enable GPU training
    fp16=True if torch.cuda.is_available() else False,  # Enable mixed precision training if using GPU
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Save the final model
trainer.save_model('./results/final_model')
tokenizer.save_pretrained('./results/final_model')

print("Training complete and model saved!")
