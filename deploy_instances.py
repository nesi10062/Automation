import boto3
from time import sleep

def deploy_instances():
    print("""
available images: 

name: Ubuntu Server 18.04 (simple)
ID:   ami-0dd9f0e7df0f0a138

name: Ubuntu Server 18.04 (with Docker)
ID:   ami-019f6f20ec51566bc

name: Red Hat Enterprise Linux 8 (HVM)
ID:   ami-03d64741867e7bb94
    """)
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
    ImageId=input("insert ImageID: "),
    MinCount=1,
    MaxCount=int(input("insert amount: ")) ,
    InstanceType='t2.micro',
    KeyName='nesi_kp'
     )
     
