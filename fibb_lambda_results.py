import json


def lambda_handler(event, context):

    body = json.dumps(
        [
            {
                "order_id": 1,
                "fib_index": 1,
                "fib_value": 1,
                "cost_credits": 1,
                "status": 1,  #   1 - done, 0 - in prograess,  2 - failed
                "order_date": "2021-02-12 10:15:00",
            },
            {
                "order_id": 2,
                "fib_index": 10,
                "fib_value": 55,
                "cost_credits": -1,  # -1 it's not available yet
                "status": 0,  #   1 - done, 0 - in prograess,  2 - failed
                "order_date": "2021-02-12 11:15:00",
            },
        ]
    )

    response = {"statusCode": 200, "headers": {"x-fibb-version": 1}, "body": body}

    return response
