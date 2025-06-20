from app.models import caption_model, caption_processor, device
import torch

def generate_caption(image):
    inputs = caption_processor(images=image, return_tensors="pt").to(device)
    outputs = caption_model.generate(**inputs, max_length=64, num_return_sequences=1)
    return caption_processor.decode(outputs[0], skip_special_tokens=True)
