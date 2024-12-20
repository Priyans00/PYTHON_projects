from flask import Flask, jsonify, render_template, request
from model import db, Truth, Dare
import random
from sqlalchemy.sql.expression import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///truth_dare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)


# Function to initialize default data
def init_default_data():
    with app.app_context():
        db.create_all()
        
    
        if Truth.query.count() == 0:
            default_truths = [
                "What is the most embarrassing thing you've ever done?",
                "Have you ever kept a secret from your best friend?",
                "What is a lie you've told that you're ashamed of?",
                "Who was your first crush?",
                "What is the most awkward moment you've experienced?"
            ]
            for truth in default_truths:
                db.session.add(Truth(question=truth))

        
        if Dare.query.count() == 0:
            default_dares = [
                "Do 10 push-ups right now.",
                "Dance like a chicken for 1 minute.",
                "Sing the chorus of your favorite song loudly.",
                "Try to lick your elbow.",
                "Speak in an accent for the next 3 minutes."
            ]
            for dare in default_dares:
                db.session.add(Dare(challenge=dare))

        db.session.commit()

init_default_data()

@app.route('/')
def main():
    truths = [truth.question for truth in Truth.query.all()]
    dares = [dare.challenge for dare in Dare.query.all()]
    return render_template('index.html', truths=truths, dares=dares)

@app.route('/get_truth')
def get_truth():
    random_truth = Truth.query.order_by(func.random()).first()
    return jsonify({"message": [random_truth.id,random_truth.question]})

@app.route('/get_dare')
def get_dare():
    random_dare = Dare.query.order_by(func.random()).first()
    return jsonify({
        "message": [random_dare.id,random_dare.challenge]
    })

@app.route('/add_truth', methods=['POST'])
def add_truth():
    data = request.get_json()
    new_truth = data.get('truth')
    if new_truth and new_truth.strip():
        truth = Truth(question=new_truth.strip())
        db.session.add(truth)
        db.session.commit()
        return jsonify({"message": "truth added successfully"}), 200
    return jsonify({"message": "error occurred"}), 400

@app.route('/add_dare', methods=['POST'])
def add_dare():
    data = request.get_json()
    new_dare = data.get('dare')
    if new_dare and new_dare.strip():
        dare = Dare(challenge=new_dare.strip())
        db.session.add(dare)
        db.session.commit()
        return jsonify({"message": "dare added successfully"}), 200
    return jsonify({"message": "error occurred"}), 400

@app.route('/del_truth', methods=['POST'])
def del_truth():
    data = request.get_json()
    id = data.get('truth')
    if id:
    
        truth = Truth.query.get(id)
        if truth:
            db.session.delete(truth) 
            db.session.commit()
            return jsonify({"message": "Truth removed successfully"}), 200
    return jsonify({"message": "Error: Truth not found"}), 404

@app.route('/del_dare', methods=['POST'])
def del_dare():
    data = request.get_json()
    id = data.get('dare')
    if id:
        
        dare = Dare.query.get(id)
        if dare:
            db.session.delete(dare)  
            db.session.commit()
            return jsonify({"message": "Dare removed successfully"}), 200
    return jsonify({"message": "Error: Dare not found"}), 404


if __name__ == '__main__':
    init_default_data()
    app.run(debug=True)

