from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model():
    model_name = "t5-small" 
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer
