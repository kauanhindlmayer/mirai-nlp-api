from transformers import AutoTokenizer, AutoModel

class EmbeddingService:
  def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    self.model = AutoModel.from_pretrained(model_name)

  def get_embedding(self, text: str):
    inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = self.model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

def get_embedding_service():
  return EmbeddingService()
