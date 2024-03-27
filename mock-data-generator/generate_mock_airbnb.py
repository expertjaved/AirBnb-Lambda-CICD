import boto3
import json
import random
import string

def data_generator():
    message = {
        "bookingId": str(random.randint(10000, 99999)),
        "userId": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        "propertyId": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        "location": random.choice(["Tampa, Florida", "Hyd, Ind", "BLR, Ind"]),
        "startDate": random.choice(["2024-03-12", "2024-03-13", "2024-03-14"]),
        "endDate": random.choice(["2024-03-13", "2024-03-14", "2024-03-15"]),
        "price": '$' + str(random.randint(100, 999))
    }
    return message

def lambda_handler(event, context):
    sqs_client = boto3.client('sqs', region_name='us-east-1')  # Specify the correct region
    queue_url = 'https://sqs.us-east-1.amazonaws.com/533267408419/AirbnbBookingQueue'  # Provide the correct Queue URL
    
    for i in range(5):
        message_body = json.dumps(data_generator())
        sqs_client.send_message(QueueUrl=queue_url, MessageBody=message_body)

# To test the lambda function locally, you can call the lambda_handler function
# lambda_handler(None, None)
