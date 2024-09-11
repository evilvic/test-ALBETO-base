# Load model directly
from transformers import AutoTokenizer, AutoModelForPreTraining

tokenizer = AutoTokenizer.from_pretrained("dccuchile/albert-base-spanish")
model = AutoModelForPreTraining.from_pretrained("dccuchile/albert-base-spanish")

# Save model
model.save_pretrained("albert-base-spanish")
tokenizer.save_pretrained("albert-base-spanish")