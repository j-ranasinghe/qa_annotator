import json
import os

# Load the JSON data from a file
def load_json():
    with open(r'data\input\split_files\split_1.json', encoding='utf-8') as f:
        return json.load(f)

# Save data to a new JSON file
def save_json(data, name):
    path= f'data/output/{name}.json'
    with open(path,'w',encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False, indent=4)