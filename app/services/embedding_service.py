from transformers import AutoTokenizer, AutoModel
from functools import lru_cache
import torch

@lru_cache()
def get_embedding_components(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModel.from_pretrained(model_name)
  return tokenizer, model

class EmbeddingService:
  def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    self.tokenizer, self.model = get_embedding_components(model_name)

  def get_embedding(self, text: str):
    inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
      outputs = self.model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

@lru_cache()
def get_embedding_service():
  return EmbeddingService()
