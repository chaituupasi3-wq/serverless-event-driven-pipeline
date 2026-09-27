import json
import boto3
import os

sqs = boto3.client('sqs', region_name=os.getenv('AWS_REGION', 'us-east-1'))
QUEUE_URL = os.getenv('SQS_QUEUE_URL', 'https://sqs.us-east-1.amazonaws.com/123456789012/order-processing-queue')

def lambda_handler(event, context):
    """
    Produces serverless events and dispatches them to an SQS queue.
    """
    payload = {
        "order_id": "ORD-2026-9981",
        "item": "Cloud Infrastructure Blueprint",
        "status": "PENDING"
    }

    try:
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(payload)
        )
        print(f"Successfully sent message: {response['MessageId']}")
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Event published successfully", "id": response['MessageId']})
        }
    except Exception as e:
        print(f"Error publishing message: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
