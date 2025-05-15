import torch

def generate_response(query, context, model, tokenizer):
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
