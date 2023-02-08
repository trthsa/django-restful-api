import boto3
import os

dynamodb = boto3.resource('dynamodb', region_name=os.environ.get('region_name'),
                       aws_access_key_id=os.environ.get('aws_access_key_id'),
                       aws_secret_access_key=os.environ.get('aws_secret_access_key'))
table = dynamodb.Table('devices')