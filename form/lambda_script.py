import boto3

client = boto3.client('ec2')

response = client.describe_tags(
    DryRun=False,
    Filters=[
        {
            'Name': 'environment',
            'Values': [
                'development',
            ]
        },
    ],
    MaxResults=1000,
    NextToken='environment'
)

