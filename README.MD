# Django Restful API

## Introduction

This is a simple Restful API built with Django, AWS DynamoDB, AWS API Gateway and AWS Lambda.

## Requirements

- Python
- Django
- AWS DynamoDB
- AWS API Gateway
- AWS Lambda
- Serverless Framework

# Running the API

1. Clone the repository:

```bash
git clone https://github.com/trthsa/django-restful-api.git
```

2. Change directory to the cloned repository:

```bash
cd django-restful-api
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the Django development server:

```bash
python manage.py runserver
```

## API Endpoints

The API has two endpoints:

- `/api/devices` for creating a new device
- `/api/devices/{id}` for retrieving a device by its id

## API Requests

## POST `/api/devices`

This endpoint creates a new device in the AWS DynamoDB. The request body should be in JSON format and contain the following fields:

- id
- deviceModel
- name
- note
- serial

Example Request

```bash
HTTP POST
URL: https://<api-gateway-url>/api/devices
Body (application/json):
{
  "id": "/devices/id1",
  "deviceModel": "/models/id1",
  "name": "Sensor",
  "note": "Testing a sensor.",
  "serial": "A0400102"
}
```

Example Response - Success

```
HTTP 201 Created
```

Example Response - Failure 1
If any of the payload fields are missing, the response will be:

```
HTTP 400 Bad Request
```

Example Response - Failure 2
If any exceptional situation occurs on the server side, the response will be:

```
HTTP 500 Internal Server Error
```

## GET `/api/devices/{id}`
This endpoint retrieves a device by its id from the AWS DynamoDB.

Example Request

```
HTTP GET
URL: https://<api-gateway-url>/api/devices/{id}
Example: GET https://api123.amazonaws.com/api/devices/id1
```

Example Response - Success

```
HTTP 200 OK
Body (application/json):
{
  "id": "/devices/id1",
  "deviceModel": "/models/id1",
  "name": "Sensor",
  "note": "Testing a sensor.",
  "serial": "A0400102"
}
```

Example Response - Failure 1
If the request id does not exist, the response will be:

```
HTTP 404 Not Found
```

Example Response - Failure 2
If any exceptional situation occurs on the server side, the response will be:

```
HTTP 500 Internal Server Error
```

## Testing

The API has unit tests. To run the tests, run the following command:

```bash
python manage.py test
```

## Conclusion

This is a basic implementation of a Restful API using Django, AWS DynamoDB, AWS API Gateway
