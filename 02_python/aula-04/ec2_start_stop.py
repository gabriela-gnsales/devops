import boto3

instance_id = 'i-058638a1d8332b20b'

ec2_client = boto3.client('ec2', region_name='us-east-1')

def action_instance(action, instanceids):
    if action == 'start':
        response = ec2_client.start_instances(
            InstanceIds = instance_id
        )
        for info in response['StartingInstances']:
            current_state = info['CurrentState']['Name']
            previus_state = info['PreviusState']['Name']
            print(f'Status anterior: {previus_state} - Status atual: {current_state}')

    elif action == 'stop':
        response = ec2_client.stop_instances(
            InstanceIds = instance_id
        )
        for info in response['StoppingInstances']:
            current_state = info['CurrentState']['Name']
            previus_state = info['PreviusState']['Name']
            print(f'Status anterior: {previus_state} - Status atual: {current_state}')
    else:
        print('Ação inválida!')


    # describe_instances

action_instance(action='start', instanceids=[instance_id])


# OUTRO MODO

def action_instance(action, instance_id):
    if action == 'start':
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        response_key = 'StartingInstances'

    elif action == 'stop':
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        response_key = 'StoppingInstances'

    else:
        print('Ação inválida')

    for info in response[response_key]:
        current_state = info['CurrentState']['Name']
    previous_state = info['PreviousState']['Name']
    instance = info['InstanceId']
    pprint(
        f'instance: {instance} – current state: {current_state} - previous state: {previous_state}\n'
    )
