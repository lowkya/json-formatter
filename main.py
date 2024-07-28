import json

def parseJSON(key, value, tabCount):
    tab_string = "\t" * tabCount
    if value is None or isinstance(value, (str, int, float, bool)):
        print(f"{tab_string}{key} : {value}")
    elif isinstance(value, dict):
        if key and key != "":
            print(f"{tab_string}{key} : {{")
        for k, v in value.items():
            parseJSON(k, v, tabCount + 1)
        if key and key != "":
            print(f"{tab_string}}}")
    elif isinstance(value, list):
        print(f"{tab_string}{key} : [")
        for item in value:
            parseJSON("", item, tabCount + 1)  # Lists don't have keys, so use an empty key
        print(f"{tab_string}]")
    else:
        print(f"{tab_string}{key} : (unknown type)")

def parse(json_string):
    try:
        # Load the main JSON object
        parsed_json = json.loads(json_string)
        print("{")
        for key, value in parsed_json.items():
            if isinstance(value, str):
                try:
                    # Try to load nested JSON string
                    nested_value = json.loads(value)
                    print(f"\t{key} : {{")
                    parseJSON("", nested_value, 2)
                    print(f"\t\t}}")
                except json.JSONDecodeError:
                    # If it's not a valid JSON string, print it as is
                    print(f"\t{key} : {value}")
            else:
                parseJSON(key, value, 1)
        print("}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

if __name__ == '__main__':
    json_string = input("Enter the JSON string to parse: ")
    parse(json_string)

