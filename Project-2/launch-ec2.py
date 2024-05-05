#import boto module
import boto3

#connect to the aws console
aws_management_console = boto3.session.Session(profile_name="terraform-user")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.run_instances(
    ImageId= 'ami',
    InstanceType= 't2.micro',
    MaxCount= 1,
    MinCount= 1
)
