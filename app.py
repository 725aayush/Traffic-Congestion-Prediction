from flask import Flask, request, render_template, send_file, redirect, url_for
from model_utils import predict_traffic
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
import uuid

app = Flask(__name__)
app.config['REPORT_FOLDER'] = 'reports'

history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', history=history)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'junction': int(request.form['junction']),
            'date_time': request.form['date_time']
        }

        prediction = predict_traffic(data)
        data['predicted_vehicles'] = prediction['predicted_vehicles']
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        history.append(data)

        # Save to JSON
        report_id = uuid.uuid4().hex
        report_path = os.path.join(app.config['REPORT_FOLDER'], f"report_{report_id}.json")
        with open(report_path, 'w') as f:
            json.dump(data, f, indent=4)

        return render_template('index.html', result=data['predicted_vehicles'], history=history)

    except Exception as e:
        return render_template('index.html', error=str(e), history=history)

@app.route('/graph')
def graph():
    try:
        if not history:
            return redirect(url_for('home'))

        junctions = [h['junction'] for h in history]
        predictions = [h['predicted_vehicles'] for h in history]

        plt.figure(figsize=(10, 5))
        plt.plot(junctions, predictions, marker='o')
        plt.xlabel('Junction')
        plt.ylabel('Predicted Vehicles')
        plt.title('Traffic Predictions by Junction')
        graph_path = os.path.join('static', 'prediction_graph.png')
        plt.savefig(graph_path)
        plt.close()

        return render_template('index.html', graph_url=graph_path, history=history)

    except Exception as e:
        return render_template('index.html', error=str(e), history=history)

@app.route('/map')
def map_view():
    return render_template('index.html', show_map=True, history=history)

@app.route('/download_latest')
def download_latest():
    try:
        files = sorted(os.listdir(app.config['REPORT_FOLDER']), reverse=True)
        latest = files[0]
        return send_file(os.path.join(app.config['REPORT_FOLDER'], latest), as_attachment=True)
    except Exception:
        return redirect(url_for('home'))

if __name__ == '__main__':
    os.makedirs(app.config['REPORT_FOLDER'], exist_ok=True)
    app.run(debug=True)
