import base64
import json
from flask import Flask, render_template, request
from worker import speech_to_text, text_to_speech, openai_process_message
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = requests.data # Get the user's speech from their request
    text = speech_to_text(audio_binary) # Call STT fxn to transcribe the speech

    # Return the response back to the user in JSON
    response = app.response_class(
        response=json.dumps({'text' : text}),
        status=200,
        mimetype='application/json'
    )

    print(response)
    print(response.data)
    return response

@app.route('/process-message', methods=['POST'])
def process_prompt_route():
    user_message = request.json['userMessage'] # Get user message from request
    print('user_message', user_message)

    voice = request.json['voice'] # Get user's preferred voice from request
    print('voice', voice)

    # Call openai_process_message to process and respond
    openai_response_text = openai_process_message(user_message)

    # Clean response to remove empty line
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

    # Call TTS fxn to convert response to speech
    openai_response_speech = text_to_speech(openai_response_text. voice)

    # Convert speech to base64 string so it can be sent back in JSON response
    openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Send a JSON response back to user with response in text and speech
    response = app.response_class(
        response=json.dumps({"openaiResponseText": None, "openaiResponseSpeech": None}),
        status=200,
        mimetype='application/json'
    )

    print(response)
    return response


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
