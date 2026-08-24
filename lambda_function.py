def lambda_handler(event, context):
    print(1+1)
    return {
        'statusCode': 200,
        'body': 'Hello from Atlantis automated Lambda!222'
    }