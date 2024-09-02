# app.py

import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Use S3 to upload a file
    s3.put_object(Body='Hello, World!', Bucket='my-bucket', Key='hello.txt')

    # Use DynamoDB to store data
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my-table')
    table.put_item(Item={'name': 'John', 'age': 30})

    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }