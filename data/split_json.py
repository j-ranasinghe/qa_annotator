import json
import os

# Load the JSON file
input_file = r'data\input\updated_dataset.json'
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Split data into 10 parts
num_splits = 26
split_size = len(data) // num_splits

# Ensure the output directory exists
output_dir = 'data\input\split_files'
os.makedirs(output_dir, exist_ok=True)

# Write each part into a new JSON file
for i in range(num_splits):
    start_idx = i * split_size
    if i == num_splits - 1:  # Include remaining data in the last file
        end_idx = len(data)
    else:
        end_idx = (i + 1) * split_size

    split_data = data[start_idx:end_idx]
    
    output_file = os.path.join(output_dir, f'split_{i + 1}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(split_data, f, ensure_ascii=False, indent=4)

    print(f"File {output_file} created with {len(split_data)} items.")
