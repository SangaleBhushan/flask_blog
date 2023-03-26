from flask import Flask, render_template
import requests

app = Flask(__name__)

# API endpoint URLs
API_URL = 'http://localhost:5000/api/v1/records'

@app.route('/')
def index():
    return render_template('bstrap.html')

if __name__ == '__main__':
    app.run(debug=True)
