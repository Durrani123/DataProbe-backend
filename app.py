from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os
import json
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Import other modules from your project. For example:
# from visualization.generate_chart import generate_chart

@app.route("/api/home", methods=['GET', 'POST'])
def return_home():
    if request.method == 'POST':
        file = request.files["file"]
        # Rest of your route code here...
        return jsonify({'chartData': chart_data})

    return jsonify({
        'message': "Hello World"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
