import json

def jsonDeserialize(filePath: str) -> dict:
    with open(filePath, 'r', encoding = "utf-8") as file:
        data: dict = json.load(file)

    return data


def jsonSerialize(filePath: str, data: dict) -> None:
    with open(filePath, 'w', encoding = "utf-8") as file:
        json.dump(data, file, indent = 4)


def print_dictionary(data: dict) -> None:
    for key, value in data.items():
        print(f"key: {key} ---- value: {value}")
        if isinstance(value, dict):
            print_dictionary(value)

        elif isinstance(value, list):
            for element in value:
                if isinstance(element, dict):
                    print_dictionary(element)
