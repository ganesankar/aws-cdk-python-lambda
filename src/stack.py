import os
from aws_cdk import (
    Stack,
    aws_lambda as _lambda, 
    aws_iam as iam,
    Duration
)
from constructs import Construct

class S3CSVReaderStack(Stack):
    """
    Construct an S3 CSV Reader stack.

    This stack creates a CDK app that deploys a Lambda function to read a CSV
    file from an S3 bucket and return its contents. The Lambda function is
    configured to be triggered by an S3 bucket event.

    :param scope: The parent construct (usually the CDK app).
    :param construct_id: The name of this construct (used by CDK).
    :param kwargs: Additional keyword arguments to pass to the base class.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        
        
        # Create Lambda function
        lambda_function = _lambda.Function(
            self, "CSVReaderLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("src/lambda_function"),
            timeout=Duration.seconds(30)
        )
        
        # Grant Lambda function access to S3 bucket
        bucket = "ganesan-dev-backend2-dev-attachmentsbucket-1svbzlbxky934" 
        bucket_arn = f"arn:aws:s3:::{bucket}"
        bucket_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "s3:GetObject"
            ],
            resources=[
                bucket_arn,
                f"{bucket_arn}/*"
            ]
        )
        lambda_function.add_to_role_policy(bucket_policy)


# To use this stack, you'll need to create a CDK app in app.py
