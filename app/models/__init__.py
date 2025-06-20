from transformers import BlipProcessor, BlipForConditionalGeneration, MarianMTModel, MarianTokenizer
import torch

# Captioning
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Translation
translation_model_name = "Helsinki-NLP/opus-mt-en-fr"
translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
caption_model.to(device)
translation_model.to(device)
