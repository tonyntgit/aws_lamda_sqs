import json
import requests

def handler(event, context):
    print('Start SQS-Lamda Event:')
    print(event)

    records = event['Records']

    for record in records:
        username = record['body']        
        user_data = get_user_detail(username)

        print(user_data)

    return {
        'statusCode': 200,
        'body': 'Lamda executed success one item from SQS'
    }

def get_user_detail(username: str):
    user_data = requests.get('https://api.github.com/users/%s' % username).json()

    return user_data
