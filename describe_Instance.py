import boto3


"""ec2 = boto3.client('ec2')

def create_tags(event, context):
    reservations = ec2.describe_instances()
    for response in reservations['Reservations']:
        for instance in response['Instances']:
            tags = {}
            for tag in instance['Tags']:
                tags[tag['Key']] = tag['Value']
                print(tags)

                '''if not 'Name' in tags:
                    instance_ids.append(instance['InstanceId'])
                    ec2.create_tags(Resources=instance_ids, Tags=[{'Key': 'Name', 'Value':'Toto'}])'''

"""



import boto3
ec2 = boto3.client("ec2")
reservations =   ec2.describe_instances()
mytags = [{
    "Key" : "Name",
       "Value" : "Mehdi"
    },
    {
       "Key" : "APP",
       "Value" : "webapp"
    },
    {
       "Key" : "Team",
       "Value" : "tototeam"
    }]
for reservation in reservations['Reservations']:
    for each_instance in reservation['Instances']:
        ec2.create_tags(Resources = [each_instance["InstanceId"] ], Tags= mytags)
