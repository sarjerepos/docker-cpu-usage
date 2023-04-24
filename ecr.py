import boto3

ecr_client = boto3.client("ecr",
                        aws_access_key_id = 'AKIAQZRJPNWZJ6NOG74K',
                        aws_secret_access_key = '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',
                        region_name = 'us-east-1'
                          )

repository_name = "ms-usage-repo"

response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response["repository"]["repositoryUri"]

print(repository_uri)