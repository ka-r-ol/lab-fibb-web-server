import json


def lambda_handler(event, context):

    body = json.dumps({"status": "Accepted", "id": 1234567890})
    response = {
        "statusCode": 200,
        "headers": {"x-fibb-version": 1},
        "body": body,
    }

    return response
