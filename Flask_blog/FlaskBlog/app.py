from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'greetings':'Hi this is flask'})

if __name__ == "__main__":
    app.run(debug=True)