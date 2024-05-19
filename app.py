from flask import render_template, request, Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('templates/index.html')

@app.route('/data', methods=['POST'])
def do():
    user = request.form['username']
    pw = request.form['password']
    return render_template('templates/index.html')

if __name__ == "__main__":
    app.run(debug=True)
