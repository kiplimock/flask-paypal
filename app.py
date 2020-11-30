from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def  index():
    return render_template('index.html')

@app.route('/payment')
def payment():
    return jsonify({'paymentID':'PAYMENTID'})

if __name__ == '__main__':
    app.run(debug=True)