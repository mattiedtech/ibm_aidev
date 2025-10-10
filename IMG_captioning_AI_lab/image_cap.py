import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# LOAD & PREPROCESS AN IMAGE
# Load you image
img_path = "https://static.wikia.nocookie.net/pixar/images/f/f3/Witch.jpg/revision/latest?cb=20120606163554"
# Convert to RGB
image = Image.open(img_path).convert('RGB')

# No question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50) #caption up to 50 tokens long

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)
