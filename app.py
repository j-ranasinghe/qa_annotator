import json
import os
from flask import Flask, render_template, request, jsonify
from utils.file_utils import load_json, save_json

app = Flask(__name__)
        
# Get the data from the JSON file and send it to the front-end
@app.route("/")
def index():
    data = load_json()
    return render_template('index.html', title="Enter QA pair", data=data)
    
 # Save the data to a new JSON file  from  client side
@app.route('/submit', methods=['POST'])
def submit():
    new_data = request.json

    #print("Data received:", new_data)

    for paragraph in new_data.get('paragraphs', []):
        # Iterate over Q&A pairs in each paragraph
        for qa in paragraph.get('qas', []):
            qa_id = qa.get('id')

    save_json( new_data,qa_id)

    # Return a success response
    return jsonify({'message': 'Data saved successfully!'})


if __name__ == '__main__':
    app.run(debug=True)