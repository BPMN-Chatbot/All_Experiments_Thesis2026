import os
import json
from jsonschema import validate, ValidationError

# Root directory to search
ROOT_DIR = "./"  # change to your folder
SCHEMA_FILE = "schema.json"  # path to your JSON schema

# Load JSON schema
with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
    schema = json.load(f)

# Statistics
total_files = 0
valid_files = 0
invalid_files = 0
invalid_paths = []

# Walk through all subfolders recursively
for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    for filename in filenames:
        if filename.lower().endswith(".json") and "diagram" in filename.lower():
            total_files += 1
            file_path = os.path.join(dirpath, filename)
            try:
                # Step 1: load stringified JSON
                with open(file_path, 'r', encoding='utf-8') as f:
                    string_content = json.load(f)

                # Step 2: parse the string into actual JSON
                data = json.loads(string_content)

                # Validate JSON
                validate(instance=data, schema=schema)
                valid_files += 1

            except (json.JSONDecodeError, ValidationError):
                invalid_files += 1
                invalid_paths.append(file_path)

# Print statistics
print(f"Total JSON files with 'diagram' in name: {total_files}")
print(f"Valid files: {valid_files}")
print(f"Invalid files: {invalid_files}")

if invalid_paths:
    print("\nInvalid files:")
    for path in invalid_paths:
        print(path)
