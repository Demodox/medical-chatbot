from transformers import pipeline

# Load Hugging Face model for text generation 
generator = pipeline("text-generation", model="google/flan-t5-base", max_new_tokens=150)

def generate_response(query, context):
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    result = generator(prompt, do_sample=True, temperature=0.7)
    return result[0]['generated_text']
