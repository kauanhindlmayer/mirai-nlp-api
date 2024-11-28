import numpy as np
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(text: str) -> list[float]:
  inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
  outputs = model(**inputs)
  embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
  return embeddings.tolist()
