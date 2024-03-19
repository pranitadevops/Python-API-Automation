import json
import jsonschema
import requests
from Test_Case.Environment import baseUrl,Auth

# Define json schema
schema = {
    "definitions": {
        "Welcome8": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                },
                "image": {
                    "type": "string"
                },
                "video": {
                    "type": "string"
                },
                "imagesContent": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/ImagesContent"
                    }
                }
            },
            "required": [
                "id",
                "image",
                "imagesContent",
                "text",
                "title",
                "video"
            ],
            "title": "Welcome8"
        },
        "ImagesContent": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "image": {
                    "type": "string"
                },
                "imageContentType": {
                    "type": "string"
                },
                "entityId": {
                    "type": "integer"
                },
                "createdDate": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "createdDate",
                "entityId",
                "image",
                "imageContentType"
            ],
            "title": "ImagesContent"
        }
    }
}
