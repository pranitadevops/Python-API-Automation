import json
import jsonschema
import jsonschema.exceptions
from jsonschema.exceptions import SchemaError, ValidationError
from jsonschema import validate

# Define Json Schema
studentSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"},
    },
}


# Validate Data against the json schema:
def validateJson(json_data):
    try:
        validate(instance=json_data, schema=studentSchema)
    except jsonschema.exceptions.ValidationError as e:
        return False
    return True


# Define Data,Convert json to pytho object

json_data = json.loads('{"Name":"API Automation","rollnumber": 25,"marks":75}')

# Validate Data
isvalid = validateJson(json_data)

if isvalid:
    print(json_data)
    print("Given Json DATA is valid")
else:
    print(json_data)
    print("Given Json Data is NOT VALID")

# Define Data,Convert json to pytho object Validate with wrong format data
json_data = json.loads('{"Name":Pranita,"rollnumber":"22","marks":33}')
isvalid = validateJson(json_data)
if isvalid:
    print(json_data)
    print("Given Json DATA is valid")
else:
    print(json_data)
    print("Given Json Data is NOT VALID")
