from pathlib import Path
import json


def path(schema_name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{schema_name}'))


def load_schema(filepath):
    with open(path(filepath)) as file:
        schema = json.load(file)
        return schema
