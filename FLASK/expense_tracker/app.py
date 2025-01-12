from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    result = request.get_json()
    amt = result.get('amount')
    name = result.get('name')

    if name and amt is not None:
        new_expense = Expense(name=name, amount=amt)
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": 'added successfully'})
    return jsonify({"message": 'Error: Missing name or amount'})

@app.route('/show', methods=['GET'])
def show():
    print("Show route accessed")  # Debugging statement
    expenses = Expense.query.all()
    print(f"Expenses retrieved: {expenses}")  # Debugging statement
    expense_list = [{'name': expense.name, 'amount': expense.amount} for expense in expenses]
    return jsonify({'message': expense_list})  # Ensure the response is structured correctly
    



