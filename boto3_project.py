import boto3
from time import sleep

# deploying ec2 instnaces,
# user can choose from the menu below which Amazon Machine Image 
# he want for the instance creation.
# he also can decide how many instances he want to deploy.

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
    
 # start instances
 
    def start_instances():
    list = input("enter the IDs of the instance you want to start: ")
    ids = list.split(" ")
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).start()

# stop instances

def stop_instances():
    list = input("enter the IDs of the instances you want to stop (minimum 1): ")
    ids = list.split(" ")
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).stop()

# terminate instances

def terminate_instances():
    list = input("enter the IDs of the instances you want to terminate (minimum 1): ")
    ids = list.split(" ")
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).terminate()

# information about instances:
#   Instance ID + Public IP Address + Current Status 

def info_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for resp in response['Reservations']:
        for instance in resp['Instances']:
            print("\nID: " + instance['InstanceId'])
            # if ip found: print it. if not: print 'no connection'.
            if instance.get('PublicIpAddress') == None: print('Public IP Address: no connection')
            else: print("Public IP Address: " + instance.get('PublicIpAddress'))
            print("Status: " + instance.get('State')['Name'])
            print("\n--------------------------------------")

# grouping all functions into nice menu
# user can choose which operation he wants to do
# options limited 1-5, if user choosing wrong, loop starts over
# after operation ends, he can decide if he want to do onther operation or to quit.

def menu():
    while (True):
        print("""
- - - - - - - - - - - - - - - - - - - - 
menu:
~~~~~
1. deploy instances
2. terminate instance
3. start instance
4. stop instance
5. get information about all instances
- - - - - - - - - - - - - - - - - - - -""")
        sleep(1)
        choose = input("\nchoose(1-5):")
        if choose == "1":
            sleep(1)
            deploy_instances()
        elif choose == "2":
            sleep(1)
            terminate_instances()
        elif choose == "3":
            sleep(1)
            start_instances()
        elif choose == "4":
            sleep(1)
            stop_instances()
        elif choose == "5":
            sleep(1)
            info_instances()
        else:
            sleep(1)
            print("\n1-5 only\n")
            sleep(1)
            continue
        exit=input("\ndo you want to exit? (yes/no)\nanswer: ")
        if(exit=="yes"):
            print("Bye..\n")
            break

### main script ###

menu()
