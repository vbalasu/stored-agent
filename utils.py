def assume_role(role_arn):
    import boto3, os
    sts = boto3.client('sts')
    response = sts.assume_role(RoleArn=role_arn, RoleSessionName='mysession')
    credentials = response['Credentials']
    os.environ['AWS_ACCESS_KEY_ID'] = credentials['AccessKeyId']
    os.environ['AWS_SECRET_ACCESS_KEY'] = credentials['SecretAccessKey']
    os.environ['AWS_SESSION_TOKEN'] = credentials['SessionToken']
    return credentials

def assume_role_cloudmatica_s3_only():
    # Remember to set the AWS_PROFILE environment variable
    return assume_role('arn:aws:iam::251566558623:role/cloudmatica-s3-only')

def list_dir():
    from fs import open_fs
    s3fs = open_fs('s3://cloudmatica')
    print(s3fs.listdir('/'))
