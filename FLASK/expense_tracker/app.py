from flask import Flask,render_template,request,jsonify


app=Flask(__name__)

expense={'shoes':500,'shirt':2000}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():
    result = request.get_json()
    amt = result.get('amount')
    name = result.get('name')

    if name and amt is not  None:
        expense[name]=amt
        return jsonify({"message":'added successfully'})
    return jsonify({"message":'Error : Missing name or amount'})

@app.route('/show',methods=['GET'])
def show():
    
    for i in expense:
        return jsonify({'message':f" expense = {i} , amount = {expense[i]}"})
    



