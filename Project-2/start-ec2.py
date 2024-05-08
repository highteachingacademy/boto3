#import boto module
import boto3

#connect to the aws console
aws_management_console = boto3.session.Session(profile_name="terraform-user")
ec2_console = aws_management_console.client(service_name='ec2')

response = ec2_console.start_instances(
    InstanceIds= ['instance-id']
)
