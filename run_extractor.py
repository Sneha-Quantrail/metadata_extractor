from metadata_extractor.extractor import extract_schema

# Use SQLite as example, or change this to your actual DB
db_url = "sqlite:///sample.db"  # This assumes 'sample.db' exists in the same folder

# Extract and print schema
schema = extract_schema(db_url)

# Pretty print
import json
print(json.dumps(schema, indent=2))
