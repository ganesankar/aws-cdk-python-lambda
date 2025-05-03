# AWS CDK S3 CSV Reader Lambda

## Project Overview
This project creates an AWS Lambda function that reads a CSV file from an S3 bucket and returns its contents.

## Prerequisites
- Python 3.9+
- AWS CDK
- AWS CLI configured with appropriate credentials

## Setup
1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Deployment
Deploy the CDK stack:
```bash
cdk deploy
```

## Usage
1. Upload a CSV file to the created S3 bucket
2. Invoke the Lambda function with the bucket and key as event parameters

## Notes
- The Lambda function expects a CSV file and returns its contents as a JSON array
- Modify `handler.py` to customize CSV parsing as needed

## Troubleshooting
### CDK Deployment Errors
- If you encounter `--app is required` error:
  1. Ensure `cdk.json` exists in project root
  2. Verify `app.py` is correctly configured
  3. Make sure you're in the correct virtual environment
  4. Run `cdk bootstrap` if this is your first CDK deployment

### Common Issues
- Ensure AWS CLI is configured with correct credentials
- Check that you have the latest version of AWS CDK
- Verify Python dependencies are installed correctly