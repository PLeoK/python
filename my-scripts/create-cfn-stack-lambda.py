import json #importing JSON library
import boto3
from datetime import datetime

#TODO:
# Stack name input validation.

#REF:
# https://aws.amazon.com/blogs/infrastructure-and-automation/scheduling-automatic-deletion-of-aws-cloudformation-stacks/
# https://medium.com/@shotin93/how-to-schedule-to-create-aws-cloudformation-stack-861bd1feba7f

# Set the region variable for CFN API call.
CFN_STACK_REGION = '<putAWSRegionNameHere>'

# Set CFN API call parameter values.
STACK_NAME_PREFIX = 's' # s for stack 
TEMPLATE_URL = '<putURLHere>'
MAIN_STACK_SELECTION = '<putStackSelectionHere>'
ENABLE_AUTO_DELETE = 'yes'
TTL = '6'
AZ1_SELECTION = '<putAWSAZnNameHere>'
AZ2_SELECTION = '<putAWSAZnNameHere>'
INSTANCE_TYPE = '<putInstanceTypeHere>'
KEY_PAIR = '<putKeyPairHere>'

# Set CFN client (to a variable called cfn_client). 
# This cfn_client is what allows us to call CF API.
cfn_client = boto3.client('cloudformation', region_name=CFN_STACK_REGION)

def generate_cfn_stack_name(stack_name_prefix):
    """The function to generate stack name."""
    print("The stack name prefix is:", stack_name_prefix)
    date_utc_suffix = datetime.utcnow().strftime('%d-%m-%y')
    print("The date (UTC) (stack name suffix) is:", date_utc_suffix)
    stack_name = stack_name_prefix + "-" + date_utc_suffix
    print("The stack name is:", stack_name)
    return stack_name

def lambda_handler(event, context):
    """The main function to create stack."""
    # This is where our function really starts.
    # Lambda handler is the function that will be executed by Lambda to do all the work.
    # We are actually passing 2 parameters to Lambda handler: "event" and "context" object. 
    # "event" object is what we are referencing in flow such as Event Triggers > S3 Event > Event object
    # "Context" object - we are not really using it in this lab 
    # But it allows to interact with Lambda and the request itself. You can pull info on request time etc.
    
    # Genrate CFN stack name
    stack_name = generate_cfn_stack_name(STACK_NAME_PREFIX)
    
    # Create CFN stack
    response = cfn_client.create_stack(
            # Stack name can include letters (A–Z and a–z), numbers (0–9) and dashes (-).
            # It must start with a letter.
            StackName=stack_name,
            TemplateURL=TEMPLATE_URL,
            Capabilities=[
                'CAPABILITY_IAM',
                'CAPABILITY_AUTO_EXPAND',
            ],
            Parameters=[
                {
                    'ParameterKey': 'MainStackSelection',
                    'ParameterValue': MAIN_STACK_SELECTION
                },
                {
                    'ParameterKey': 'EnableAutoDelete',
                    'ParameterValue': ENABLE_AUTO_DELETE
                },
                {
                    'ParameterKey': 'TTL',
                    'ParameterValue': TTL 
                },
                {
                    'ParameterKey': 'AvailabilityZone1Selection',
                    'ParameterValue': AZ1_SELECTION
                },
                {
                    'ParameterKey': 'AvailabilityZone2Selection',
                    'ParameterValue': AZ2_SELECTION
                },
                {
                    'ParameterKey': 'InstanceType',
                    'ParameterValue': INSTANCE_TYPE
                },
                {
                    'ParameterKey': 'KeyPair',
                    'ParameterValue': KEY_PAIR
                }
            ]
        )
    
    print("CFN CreateStack API initiated creation of stack ARN:")
    print(response["StackId"])
    
