from transformers import pipeline
from functools import lru_cache

@lru_cache()
def get_summarization_pipeline():
  return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

class SummarizationService:
  def __init__(self):
    self.summarizer = get_summarization_pipeline()

  def summarize(self, text: str) -> str:
    result = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]["summary_text"]

@lru_cache()
def get_summarization_service():
  return SummarizationService()
