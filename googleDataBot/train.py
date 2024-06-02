import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from torch.utils.data import Dataset, DataLoader

class TextDataset(Dataset):
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.data = []
        self.load_data()

    def load_data(self):
        for file_path in self.file_paths:
            self.data.extend(torch.load(file_path))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return torch.tensor(self.data[i], dtype=torch.long).squeeze(0)

# Define the folder containing the tokenized data batches
data_folder = 'path_to_your_tokenized_data_batches'

# Get a list of all tokenized data batch files
data_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.startswith('tokenized_data_batch_')]

# Initialize the dataset
train_dataset = TextDataset(data_files)

# Initialize the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

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
    fp16=True,                       # use mixed precision (16-bit) training
    dataloader_num_workers=4,        # number of dataloader workers
    logging_dir='./logs',            # directory for storing logs
    report_to="none"                 # do not report to any logging framework
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
