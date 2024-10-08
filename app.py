from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)


# Load the JSON data from a file
def load_json():
    with open(r'data\input\split_files\split_1.json', encoding='utf-8') as f:
        return json.load(f)

# Save data to a new JSON file
def save_json(data):
    with open(r'data\output\new_data.json', 'w',encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False, indent=4)
        

@app.route("/")
def index():
     # Get the data from the JSON file and send it to the front-end
    data = load_json()
    return render_template('index.html', title="Enter QA pair", data=data)
    
    
@app.route('/submit', methods=['POST'])
def submit():
    new_data = request.json

    print("Data received:", new_data)

    save_json( request.json)

    # Return a success response
    return jsonify({'message': 'Data saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)