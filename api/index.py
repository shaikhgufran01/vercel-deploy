from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Hello from Flask on Vercel!"
    })

@app.route('/about')
def about():
    return jsonify({
        "status": "success",
        "message": "This is a sample Flask app running as a Serverless Function."
    })
