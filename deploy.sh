#!/bin/bash

# Definir variables
AWS_REGION="us-east-1"
STACK_NAME="ci-cd"
ECR_IMAGE_URI="714715362869.dkr.ecr.us-east-1.amazonaws.com/reponaodigital:latest:$BUILD_ID"

# Desplegar usando AWS CloudFormation o AWS SAM
# Ejemplo con AWS SAM para una aplicación serverless
sam deploy --template-file template.yaml \
           --stack-name $STACK_NAME \
           --region $AWS_REGION \
           --image-repository $ECR_IMAGE_URI \
           --no-fail-on-empty-changeset \
           --capabilities CAPABILITY_IAM
