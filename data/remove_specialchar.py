import json
import os

# Directory containing the split files
split_dir = r'data\input\split_files'

# Get a list of all split files
split_files = [f for f in os.listdir(split_dir) if f.endswith('.json')]

# Process each split file
for split_file in split_files:
    file_path = os.path.join(split_dir, split_file)

    # Load the split file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Remove specified fields and any quotes and backslashes in the title and context fields
    for item in data:
        item.pop('category', None)
        item.pop('site', None)
        item.pop('url', None)

        # Remove quotes and backslashes in the title field if present
        if 'title' in item:
            item['title'] = item['title'].replace('"', '').replace("'", "").replace("\\", "")
        
        # Remove quotes and backslashes in the context field if present
        if 'context' in item:
            item['context'] = item['context'].replace('"', '').replace("'", "").replace("\\", "")

    # Save the updated data back to the split file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Processed {split_file}.")



