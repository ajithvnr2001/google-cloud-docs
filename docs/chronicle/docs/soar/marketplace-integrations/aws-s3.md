---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-s3/
title: Integrate AWS S3 with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:52.143205+00:00
---

# Integrate AWS S3 with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-s3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AWS S3 with Google SecOps

This document describes how to integrate AWS S3 with Google Security Operations.

## Use cases

  1. Manage buckets
  2. Download files from buckets
  3. Upload files to buckets



## Before you begin

Before you configure the AWS S3 integration in Google SecOps, verify that your network environment and AWS credentials satisfy all operational prerequisites.

To prepare your environment for integration, make sure you complete the following:

  1. Verify network line-of-sight between Google SecOps and AWS S3 regional service endpoints.

  2. Obtain AWS programmatic API credentials (an Access Key ID and Secret Access Key) with appropriate IAM permissions.

  3. Configure and test the integration instance within Google SecOps.




### Network requirements

Google SecOps communicates directly with the AWS S3 service using HTTPS REST APIs and the AWS Python SDK (`boto3`).

Make sure your network environment meets the following connectivity rules:

  * **Outbound HTTPS access** : Enable outbound HTTPS communication from your Google SecOps instance or Remote Agent to the AWS S3 regional endpoint (`s3.<region>.amazonaws.com` or `s3.amazonaws.com`) over port `443/TCP`.

For more information, see [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in AWS documentation.

  * **Proxy configuration** : If your organization routes outbound traffic through an HTTP/HTTPS proxy, configure standard environment proxy variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) on the Google SecOps server or Remote Agent host.




### Authentication and credentials

The AWS S3 integration requires programmatic API credentials to authenticate requests using AWS Signature Version 4.

Make sure your AWS environment satisfies the following authentication requirements:

  * **Programmatic credentials** : Obtain a valid AWS Access Key ID and AWS Secret Key associated with an AWS IAM user or role.

For information on creating IAM identities and generating credentials, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) and [IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in AWS documentation.

  * **Least privilege** : Restrict permissions to only the actions and bucket resources required for your automated workflows, and rotate credentials periodically.

For details on security recommendations, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in AWS documentation.




### Configure action permissions

Grant the authenticating AWS IAM identity the specific permissions required for the actions your Google SecOps playbooks execute.

**Important:** Every AWS S3 action script in Google SecOps executes an internal connectivity verification during initialization that calls `s3_client.list_buckets()`. Therefore, `s3:ListAllMyBuckets` is required for all AWS S3 actions to prevent runtime initialization errors.

Refer to the minimal permissions for **AWS S3** actions in the following table:

Action Name | Required AWS IAM Permission (`ActionName:Permission`) | Prerequisite Permission | Description / Resource Scope  
---|---|---|---  
**Download File From Bucket** | `s3:GetObject` | `s3:ListAllMyBuckets` | Downloads an object from an S3 bucket. Resource: `arn:aws:s3:::<bucket-name>/*`.  
**Get Bucket Policy** | `s3:GetBucketPolicy` | `s3:ListAllMyBuckets` | Retrieves the bucket access policy. Resource: `arn:aws:s3:::<bucket-name>`.  
**List Bucket Objects** | `s3:ListBucket` | `s3:ListAllMyBuckets` | Lists objects within an S3 bucket. Resource: `arn:aws:s3:::<bucket-name>`.  
**List Buckets** | `s3:ListAllMyBuckets` | — | Lists all S3 buckets owned by the account. Resource: `*`.  
**Ping** | `s3:ListAllMyBuckets` | — | Validates integration connectivity. Resource: `*`.  
**Set Bucket Policy** | `s3:PutBucketPolicy` | `s3:ListAllMyBuckets` | Sets or modifies an S3 bucket policy. Resource: `arn:aws:s3:::<bucket-name>`.  
**Upload File To Bucket** | `s3:PutObject` | `s3:ListAllMyBuckets` | Uploads an object into an S3 bucket. Resource: `arn:aws:s3:::<bucket-name>/*`.  
  
#### Quick reference (`ActionName:Permission`)

Use the following quick reference to review the required permissions for each action:
    
    
    Ping: s3:ListAllMyBuckets
    Download File From Bucket: s3:GetObject, s3:ListAllMyBuckets
    Get Bucket Policy: s3:GetBucketPolicy, s3:ListAllMyBuckets
    List Bucket Objects: s3:ListBucket, s3:ListAllMyBuckets
    List Buckets: s3:ListAllMyBuckets
    Set Bucket Policy: s3:PutBucketPolicy, s3:ListAllMyBuckets
    Upload File To Bucket: s3:PutObject, s3:ListAllMyBuckets
    

### Sample IAM policy (least privilege)

The following example policy demonstrates the permissions required to run all AWS S3 actions in Google SecOps.

For instructions on creating and attaching IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in AWS documentation.
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "SecOpsS3Discovery",
          "Effect": "Allow",
          "Action": [
            "s3:ListAllMyBuckets"
          ],
          "Resource": "*"
        },
        {
          "Sid": "SecOpsS3BucketOperations",
          "Effect": "Allow",
          "Action": [
            "s3:ListBucket",
            "s3:GetBucketPolicy",
            "s3:PutBucketPolicy"
          ],
          "Resource": "arn:aws:s3:::*"
        },
        {
          "Sid": "SecOpsS3ObjectOperations",
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:PutObject"
          ],
          "Resource": "arn:aws:s3:::*/*"
        }
      ]
    }
    

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | Yes | AWS default region to use in integration, for example us-west-2.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Download File From Bucket

Download file from bucket in AWS S3.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Bucket File Path | String | s3://{bucket_name}/{file_name} | Yes | Specify the path to the file in the bucket. Example: s3://siemplify/syslog/log.txt  
Download Path | String | N/A | Yes | Specify the path, where to download the file.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "bucket_file_path": "s3://testsiemplify/test/123.txt"
    "download_path": "/usr/bin/share/download.txt"
    }
    

#### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If status code == 200 (is_success = true)_ "Successfully downloaded '{0}' from AWS S3".format(bucket_file_path) _If other status code (is_success=false):_ "Action wasn't able to download '{0}' from AWS S3. Reason: file with that download path already exists." **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to the server, SDK errors, other:_ "Error executing action "Download File From Bucket". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Bucket Policy

Retrieve information about the bucket policy from AWS S3.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Bucket Name | String | N/A | Yes | Specify name of the bucket from which to retrieve policy information.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Policy": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AddPerm",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::testsiemplify/*"
                }
            ]
        }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If status code == 200 (is_success = true)_ "Successfully retrieved information about the policy of the "{0}" bucket in AWS S3".format(bucket_name) _If other status code (is_success=false):_ "Action wasn't able to return information about the policy of the '{0}' bucket in AWS S3".format(bucket_name) **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to the server, other:_ "Error executing action "Get Bucket Policy". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Bucket Objects

Enables the user to deactivate a user account. The request body contains the user to disable. The account enabled property of the account should be set to false.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Bucket Name | String | N/A | Yes | Specify the name of the bucket from which to retrieve objects.  
Max Objects to Return | Integer | N/A | No | Specify how many objects to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "Contents": [
            {
                "Key": "text.txt",
                "LastModified": %Y-%m-%dT%H:%M:%S,
                "ETag": "d41d8cd98f00b204e9800998ecf8427e",
                "Size": 0,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "lab_aws",
                    "ID": "935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"
                }
            },
            {
                "Key": "text_1.txt",
                "LastModified": %Y-%m-%dT%H:%M:%S,
                "ETag": "d41d8cd98f00b204e9800998ecf8427e",
                "Size": 0,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "lab_aws",
                    "ID": "935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"
                }
            }
        ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If status code == 200 (is_success = true)_ "Successfully returned objects of the "{0}" bucket in AWS S3".format(bucket_name) _If other status code (is_success=false):_ "Action wasn't able to return objects of the '{0}' bucket in AWS S3".format(bucket_name) **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to the server, other:_ "Error executing action "List Bucket Objects". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** '{0}' Bucket Objects **Columns:**

  * Key (mapped as Key)
  * Last Modified (mapped as LastModified)
  * Size (Bytes) (mapped as Size)
  * Owner (mapped as Owner/DisplayName)
  * Storage Class (mapped as Storage Class)

| General  
  
### List Buckets

Retrieve a list of buckets from AWS S3.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Buckets": [
            {
                "CreationDate": %Y-%m-%dT%H:%M:%S,
                "Name": "testsiemplify"
            }
        ],
        "Owner": {
            "DisplayName": "lab_aws",
            "ID": "935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"
        },
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If status code == 200 (is_success = true)_ "Successfully listed available buckets in AWS S3". _If other status code (is_success=false):_ "Action wasn't able to list available buckets in AWS S3. **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to the server, other:_ "Error executing action "List Buckets". Reason: {0}''.format(error.Stacktrace) | General  
  
### Ping

Test connectivity to AWS S3 with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Use cases

Test Connectivity.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the AWS S3 server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the AWS S3 server! Error is {0}".format(exception.stacktrace) | General  
  
### Set Bucket Policy

Set a policy in the bucket from AWS S3.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Bucket Name | String | N/A | Yes | Specify the name of the bucket on which you want to update the policy.  
Policy JSON Object | String | N/A | Yes | Specify the JSON object of the policy that you want to set for the bucket. Examples can be found here: https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If status code == 204 (is_success = true)_ "Successfully updated policy of the "{0}" bucket in AWS S3".format(bucket_name) _If other status code (is_success=false):_ "Action wasn't able to update the policy of the '{0}' bucket in AWS S3".format(bucket_name) **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to the server, other:_ "Error executing action "Set Bucket Policy". Reason: {0}''.format(error.Stacktrace) |   
  
### Upload File To Bucket

Upload file to bucket in AWS S3.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Path | String | N/A | Yes | Specify the path to the file that needs to be uploaded.  
Bucket Upload Path | String | s3://{bucket_name}/{file_name} | Yes | Specify the path in the bucket to where the path should be uploaded. Example: s3://siemplify/syslog/log.txt  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "bucket_upload_path": "s3://testsiemplify/test/123.txt"
    "file_path": "/usr/bin/share/download.txt"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If status code == 200 (is_success = true)_ "Successfully uploaded '{0}' to AWS S3 {1} bucket".format(file_path, bucket name aka first string after s3://) _If the file does not exist (is_success = false)_ "Action wasn't able to upload '{0}' to AWS S3. Reason: file with that upload path does not exist." **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to the server, SDK errors, other:_ "Error executing action "Upload File To Bucket". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
