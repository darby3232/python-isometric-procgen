import json
import sys
import toml

if len(sys.argv) < 3: raise Exception('Usage is `json_to_toml.py input.json output.toml`')
json_file = sys.argv[1]
output_file = sys.argv[2]

with open(json_file) as source:
    config = json.loads(source.read())

toml_config = toml.dumps(config)

with open(output_file, 'w') as target:
    target.write(toml_config)