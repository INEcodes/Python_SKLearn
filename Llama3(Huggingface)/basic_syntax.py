from transformers import pipeline
import torch

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = pipeline(model=model_id)
pipeline("Hey how are you doing today?")
