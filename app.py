from flask import Flask, jsonify, request,send_file
from flask_cors import CORS
import io
import os
import json
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)


CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Allow requests from http://localhost:3000


from visualization.generate_chart import generate_chart


# generates image
@app.route("/api/home", methods=['GET', 'POST'])  
def return_home():
    if request.method == 'POST':
        file = request.files["file"]

        columns_json = request.form.get("columns")
        chosenReq_json = request.form.get("chosenReq")
        chart_json = request.form.get("chart")
        selectedCustom_json = request.form.get("selectedCustom")

        columns = json.loads(columns_json)
        chosenReq = json.loads(chosenReq_json)
        chart = json.loads(chart_json)
        selectedCustom = json.loads(selectedCustom_json)
        
        fig = generate_chart(file,columns,chosenReq,chart,selectedCustom)
        chart_data = fig.to_json()
        return jsonify({'chartData': chart_data})

    return jsonify({
        'message': "Hellos World"
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000)
