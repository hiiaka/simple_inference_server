import sagemaker
from sagemaker import get_execution_role
from sagemaker.model import Model

# get session and execution role
sagemaker_session = sagemaker.Session()

# Your account ID
# aws sts get-caller-identity --query Account --output text

# URI for ECR repository
# image_uri = 'your_account_id.dkr.ecr.your_region.amazonaws.com/your_repository_name:your_tag'
image_uri = 'your_account_id.dkr.ecr.your_region.amazonaws.com/my-inference-image:latest'

# get role for SageMaker
# role = "your_sagemaker_execution_role_arn"
role = "arn:aws:iam::your_account_id:role/service-role/AmazonSageMakerServiceCatalogProductsUseRole"

# generate SageMaker model for inference
model = Model(image_uri, model_data=None, role=role, sagemaker_session=sagemaker_session)

# deploy endpoint
_ = model.deploy(initial_instance_count=1, instance_type='ml.m5.large')

# get endpoint name
endpoint_name = model.endpoint_name
print(f"Endpoint name: {endpoint_name}")

# they will return
# Endpoint name: <repository-name>-<timestamp>