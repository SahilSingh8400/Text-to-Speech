import torch
import soundfile as sf
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer

MODEL = "ai4bharat/indic-parler-tts"

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading model...")
model = ParlerTTSForConditionalGeneration.from_pretrained(MODEL).to(device)

tokenizer = AutoTokenizer.from_pretrained(MODEL)

description_tokenizer = AutoTokenizer.from_pretrained(
    model.config.text_encoder._name_or_path
)

# Hindi text
text = "शिक्षक पात्रता परीक्षा के लिए यह सामग्री हिंदी व्याकरण, भाषा कौशल और शिक्षण विधियों का व्यापक ज्ञान प्रदान करती है। यह अभ्यास सेट वर्णमाला से लेकर उपचारात्मक शिक्षण तक के मुख्य विषयों को कवर करता है।"

# Voice characteristics
description = (
    "A female speaker speaks clearly and naturally "
    "with a moderate speed and expressive tone. "
    "The recording is high quality with no background noise."
)

# Tokenize
description_inputs = description_tokenizer(
    description, return_tensors="pt"
).to(device)

text_inputs = tokenizer(
    text, return_tensors="pt"
).to(device)

# Generate speech
audio = model.generate(
    input_ids=description_inputs.input_ids,
    attention_mask=description_inputs.attention_mask,
    prompt_input_ids=text_inputs.input_ids,
    prompt_attention_mask=text_inputs.attention_mask
)

audio = audio.cpu().numpy().squeeze()

# Save
sf.write(
    "output.wav",
    audio,
    model.config.sampling_rate
)

print("Done! Audio saved as output.wav")