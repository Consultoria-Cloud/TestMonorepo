import json
from src.libs.lib1.lib1 import lib1

def lambda_handler(event, context):
    # TODO implement
    result = lib1 ()
    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda 1! Version v1.0.0')
    }