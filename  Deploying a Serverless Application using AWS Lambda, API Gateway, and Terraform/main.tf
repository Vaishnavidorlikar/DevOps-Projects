# main.tf

provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "hello_lambda" {
  filename      = "app.py.zip"
  function_name = "hello-lambda"
  handler       = "app.lambda_handler"
  runtime       = "python3.8"
  role          = "arn:aws:iam::123456789012:role/lambda-execution-role"
}

resource "aws_api_gateway_rest_api" "hello_api" {
  name        = "hello-api"
  description = "Hello API"
}

resource "aws_api_gateway_resource" "hello_resource" {
  rest_api_id = aws_api_gateway_rest_api.hello_api.id
  parent_id   = aws_api_gateway_rest_api.hello_api.root_resource_id
  path_part   = "hello"
}

resource "aws_api_gateway_method" "hello_post" {
  rest_api_id = aws_api_gateway_rest_api.hello_api.id
  resource_id = aws_api_gateway_resource.hello_resource.id
  http_method = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "hello_integration" {
  rest_api_id = aws_api_gateway_rest_api.hello_api.id
  resource_id = aws_api_gateway_resource.hello_resource.id
  http_method = aws_api_gateway_method.hello_post.http_method
  integration_http_method = "POST"
  type        = "LAMBDA"
  uri         = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/${aws_lambda_function.hello_lambda.arn}/invocations"
}