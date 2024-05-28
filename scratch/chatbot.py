import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer # type: ignore

# Load the model and tokenizer
model = GPT2LMHeadModel.from_pretrained('./results/final_model')
tokenizer = GPT2Tokenizer.from_pretrained('./results/final_model')

# Set pad_token_id to eos_token_id to avoid warnings
model.config.pad_token_id = model.config.eos_token_id

# Move model to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def generate_response(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors='pt').to(device)
    attention_mask = torch.ones(inputs.shape, device=device)  # Create attention mask
    outputs = model.generate(
        inputs, 
        attention_mask=attention_mask, 
        max_length=max_length, 
        do_sample=True,  # Set do_sample=True
        num_return_sequences=1
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
prompt = "Hello, how are you?"
response = generate_response(prompt)
print("Bot:", response)
