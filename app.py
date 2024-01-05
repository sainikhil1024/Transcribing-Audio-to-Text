# -*- coding: utf-8 -*-
#pip install SpeechRecognition
import speech_recognition as sr
import IPython
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

app = Flask(__name__)

male_path = "LJ001-0009.wav"
IPython.display.Audio(male_path)

#female_path = 'testSpeech.wav'
#IPython.display.Audio(female_path)

r = sr.Recognizer()

@app.route('/')
def home():
   return render_template('index.html')


#Convert Speech to Text 
@app.route('/send', methods = ['POST', 'GET'])
def send():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
      
        with sr.AudioFile(f.filename) as source:
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text)
                print('Converting audio transcripts into text ...')
                # print(text)
            except:
                 print('Sorry.. run again...')
        
            return render_template('index.html',result=text)


if __name__ == '__main__':
   app.run()