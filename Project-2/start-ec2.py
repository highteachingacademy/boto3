#import boto module
import boto3

#connect to the aws console
aws_management_console = boto3.session.Session(profile_name="terraform-user")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.stop_instances(
    InstanceId= 'instance-id',
    Hibernate=True|False,
    DryRun=True|False
    Force=True|False
)
