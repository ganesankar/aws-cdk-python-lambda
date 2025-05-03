#!/usr/bin/env python3
import aws_cdk as cdk
from constructs import Construct
from src.stack import S3CSVReaderStack

class MyStack(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        S3CSVReaderStack(self, "S3CSVReaderStack")

app = cdk.App()
MyStack(app, "S3CSVReaderLambdaApp")
app.synth()
