# api_gateway.py

import boto3

apigateway = boto3.client('apigateway')

# Create a new API
api_id = apigateway.create_rest_api(
    name='hello-api',
    description='Hello API'
)['id']

# Create a new resource
resource_id = apigateway.create_resource(
    restApiId=api_id,
    parentId='/',
    pathPart='hello'
)['id']

# Create a new POST method
apigateway.put_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='POST',
    authorization='NONE'
)

# Integrate the Lambda function with the API
apigateway.put_integration(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='POST',
    integrationHttpMethod='POST',
    type='LAMBDA',
    uri=f'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:hello-lambda/invocations'
)