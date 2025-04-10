import json
import os

# Path to the input JSONL file
input_file = "./data/warnings.jsonl"

# Directory to save the output JSON files
output_dir = "./data/warnings_json"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the JSONL file and create individual JSON files
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        # Skip comment lines
        if line.strip().startswith('//'):
            continue

        # Parse the JSON object from the line
        json_obj = json.loads(line.strip())

        # Extract the ID (removing invalid characters for filenames)
        file_id = json_obj['id'].replace(':', '_').replace('/', '_')

        # Create a filename based on the ID
        filename = os.path.join(output_dir, f"{file_id}.json")

        # Write the JSON object to a file
        with open(filename, 'w', encoding='utf-8') as out_file:
            json.dump(json_obj, out_file, indent=4)

print(f"Conversion complete. JSON files saved to {output_dir}")
