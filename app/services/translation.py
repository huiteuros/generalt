from app.models import translation_model, translation_tokenizer, device

def translate_en_to_fr(text):
    encoded = translation_tokenizer(text, return_tensors="pt", padding=True).to(device)
    translated = translation_model.generate(**encoded)
    return translation_tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
