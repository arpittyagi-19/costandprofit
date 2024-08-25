from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def theory():
    return render_template('theory.html')

@app.route('/notebook')
def index():
    return render_template('Untitled.html')

if __name__ == "__main__":
    # Ensure your Flask app listens on the correct host and port
    port = int(os.environ.get("PORT", 10000))  # Use the PORT environment variable provided by Render
    app.run(host="0.0.0.0", port=port)
