import os
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import save
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    text = request.form.get("text")
    language = request.form.get("language")
    voice = request.form.get("voice")
    speed = request.form.get("speed")
    pitch = request.form.get("pitch")

    print("========== TTS REQUEST ==========")
    print("Text:", text)
    print("Language:", language)
    print("Voice:", voice)
    print("Speed:", speed)
    print("Pitch:", pitch)
    print("=================================")

    return "Data received successfully!"


# load_dotenv()

# api_key = os.getenv("SARVAM_API_KEY")

# if not api_key:
#     raise RuntimeError("SARVAM_API_KEY was not found in .env")


# client = SarvamAI(
#     api_subscription_key=api_key
# )

# audio = client.text_to_speech.convert(
#     text="""नमस्ते! आज का दिन बहुत सुंदर है।
# मुझे नई चीज़ें सीखना और नए विचारों को आज़माना पसंद है।
# तकनीक हमारे जीवन को आसान और बेहतर बनाने में महत्वपूर्ण भूमिका निभाती है।
# मेहनत, धैर्य और सही दिशा से कोई भी लक्ष्य हासिल किया जा सकता है।
# हर सुबह अपने साथ एक नई उम्मीद और नया अवसर लेकर आती है।""",
#     language_code="hi-IN",
#     speaker="aditya",
#     model="bulbul:v3",
#     output_audio_codec="mp3"
# )

# save(audio, "kavita.mp3")

# print("Audio generated successfully!")

if __name__ == "__main__":
    app.run(debug=True)