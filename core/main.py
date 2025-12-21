import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)

# Gemini Setup
genai.configure(api_key="AIzaSyClYMSP3p44TcU2yrI5_FWdrrwj7DkrL0M")
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    # Ek simple hacker theme wala HTML return karega
    return """
    <html>
        <body style="background-color:black; color:#00FF00; font-family:monospace;">
            <h1>SHADOW-X SECURITY ONLINE</h1>
            <p>Shadow AI is active...</p>
        </body>
    </html>
    """

@app.route('/ask', methods=['POST'])
def ask_shadow(self):
    user_msg = request.json.get("message")
    try:
        response = model.generate_content(user_msg)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # Port 5000 Render ke liye standard hai
    app.run(host='0.0.0.0', port=5000)