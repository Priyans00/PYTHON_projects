from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello():
    render_template("index.html")

@app.route('/heh')
def jk():
    return "hope"

if __name__=="__main__":
    app.run(debug=True)

