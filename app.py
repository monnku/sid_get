from testapp import app
from flask import render_template, request, Flask
app = Flask(__name__)

def load_config(app, config_file='config.json'):
    with open(config_file) as f:
        config = json.load(f)
        app.config.update(config)

load_config(app)

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
