from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def theory():
    return render_template('theory.html')

@app.route('/notebook')
def index():
    return render_template('Untitled.html')

if __name__ == "__main__":
    app.run(debug=True)
