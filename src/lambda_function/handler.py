import json
import boto3
import csv
import io

def lambda_handler(event, context):
    """
    Lambda function to read a CSV file from S3 and return its contents
    
    :param event: AWS Lambda uses this to pass in event data
    :param context: Runtime information provided by AWS Lambda
    :return: JSON response with CSV data
    """
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Get bucket and key from event (or set defaults for testing)
    bucket = event.get('bucket', 'ganesan-dev-backend2-dev-attachmentsbucket-1svbzlbxky934')
    key = event.get('key', 'customers-100.csv')
    
    try:
        # Download the CSV file from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        
        # Read the CSV file
        csv_content = response['Body'].read().decode('utf-8')
        csv_reader = csv.DictReader(io.StringIO(csv_content))
        
        # Convert CSV to list of dictionaries
        data = list(csv_reader)
        
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    
    except Exception as e:
        print(f"Error reading CSV from S3: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
