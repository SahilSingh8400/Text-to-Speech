from gtts import gTTS

text = "hello my name is sahil singh, i am from mirzapur, can you tell me where are you from"

tts = gTTS(text=text, lang="en")

tts.save("gtts.mp3")

print("Punjabi audio generated successfully!")