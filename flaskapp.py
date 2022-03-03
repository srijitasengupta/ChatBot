from flask import Flask,render_template,request,jsonify
import main

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')
    #return "<p>Hello, World!</p>"

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    response=main.send_message(text)
    message={"answer":response}
    return jsonify(message)


if __name__=="__main__":
    app.run(debug=True)