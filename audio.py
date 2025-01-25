import fitz  # PyMuPDF
from gtts import gTTS

def pdf_to_audio(pdf_path, output_audio_path, language='en'):
    try:
        pdf_document = fitz.open(pdf_path)  # Open the PDF file
        text = ""
        for page in pdf_document:
            text += page.get_text()  # Extract text from each page

        if not text.strip():
            print("No text found in the PDF.")
            return

        # Convert text to audio
        tts = gTTS(text=text, lang=language)
        tts.save(output_audio_path)
        print(f"Audio saved at: {output_audio_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Update the path to your file
pdf_path = r"C:\Suresh\PYTHON\projects\hi\text_to_audio\sample.pdf"
output_audio_path = "output_audio.mp3"
pdf_to_audio(pdf_path, output_audio_path)
