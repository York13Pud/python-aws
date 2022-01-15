# --- Prior to starting, ensure that you have AWS CLI configured with your
# --- region, Secret and access keys (run aws configure in the CLI).
# --- Alternatively, you can pass all oll ot them as part of the s3_client configuration.
#
# --- Also, install the boto3 SDK in python3. Run pip3 install boto3 in the CLI.

# --- Import the AWS Python SDK:
import boto3

# --- Create a variable to create a client to access S3:
s3_client = boto3.client("s3")

# --- Create another variable to call the s3_client and return a dictionary of all the s3 buckets:
response = s3_client.list_buckets()

# --- Show the complete dictionary stored in response:
print(response)

# --- Use a for loop to display only the names of the buckets that you have access to:
for bucket in response['Buckets']:
    print(f"Bucket Name: {bucket['Name']}\n")