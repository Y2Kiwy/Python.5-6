from json_handler import *
from jsonschema import *

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
        }
    },
    "required": ["name"],
    "additionalProperties": False
}

path: str = "/home/user/Documenti/ICTAcademy/Python.5-6/Lessons/05/example2.json"

data: dict = jsonDeserialize(path)

try:
    validate(data, schema)
    print("L'istanza è coerente con lo schema")
except ValidationError:
    print("L'istanza non è valida")