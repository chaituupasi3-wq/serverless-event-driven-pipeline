import json

def lambda_handler(event, context):
    """
    Consumes events asynchronously from the SQS queue and processes them.
    """
    for record in event.get('Records', []):
        payload = json.loads(record['body'])
        print(f"Processing Order ID: {payload.get('order_id')}")
        print(f"Item Details: {payload.get('item')}")
        print(f"Current Status: {payload.get('status')}")
        
        # Business logic processing goes here
        print("Order processed successfully and marked as COMPLETED.")

    return {
        "statusCode": 200,
        "body": json.dumps("Batch processed successfully.")
    }
