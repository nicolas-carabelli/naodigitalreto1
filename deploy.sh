#!/bin/bash

# Definir variables
AWS_REGION="us-east-1"
STACK_NAME="ci-cd"
S3_BUCKET="bucketnaodigital" # Add your S3 bucket name here
ECR_IMAGE_URI="714715362869.dkr.ecr.us-east-1.amazonaws.com/reponaodigital:$BUILD_ID"

# Desplegar usando AWS CloudFormation o AWS SAM
sam deploy --template-file template.yaml \
           --stack-name $STACK_NAME \
           --region $AWS_REGION \
           --s3-bucket $S3_BUCKET \  # Add this line
           --image-repository $ECR_IMAGE_URI \
           --no-fail-on-empty-changeset \
           --capabilities CAPABILITY_IAM


