from flask import Flask, jsonify,render_template
import random

app = Flask(__name__)

truths = [
    "What is the most embarrassing thing you've ever done?",
    "Have you ever kept a secret from your best friend?",
    "What is a lie you've told that you're ashamed of?",
    "Who was your first crush?",
    "What is the most awkward moment you've experienced?"
]

dares = [
    "Do 10 push-ups right now.",
    "Dance like a chicken for 1 minute.",
    "Sing the chorus of your favorite song loudly.",
    "Try to lick your elbow.",
    "Speak in an accent for the next 3 minutes."
]
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get_truth')
def get_truth():
    result = random.choice(truths)
    return jsonify({"message": result})

@app.route('/get_dare')
def get_dare():
    result = random.choice(dares)
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)

