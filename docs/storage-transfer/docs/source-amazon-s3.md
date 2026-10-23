---
url: https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3/
title: Configure access to a source: Amazon S3 \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:37.999945+00:00
---

# Configure access to a source: Amazon S3  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: Amazon S3 Stay organized with collections  Save and categorize content based on your preferences. 

You can set up access to an Amazon S3 bucket using either of two methods:

  * Access credentials
  * Federated identity



## Supported regions

Storage Transfer Service supports the following Amazon S3 regions:  `af-south-1`  
`ap-east-1`  
`ap-east-2`  
`ap-northeast-1`  
`ap-northeast-2`  
`ap-northeast-3`  
`ap-south-1`  
`ap-south-2`  
`ap-southeast-1`  
`ap-southeast-2` |  `ap-southeast-3`  
`ap-southeast-4`  
`ap-southeast-5`  
`ca-central-1`  
`ca-west-1`  
`eu-central-1`  
`eu-central-2`  
`eu-north-1`  
`eu-south-1`  
`eu-south-2` |  `eu-west-1`  
`eu-west-2`  
`eu-west-3`  
`il-central-1`  
`me-central-1`  
`me-south-1`  
`sa-east-1` |  `us-east-1`  
`us-east-2`  
`us-west-1`  
`us-west-2`  
`us-gov-east-1`  
`us-gov-west-1`  
---|---|---|---  
Transfers using the Google-managed private network support the following AWS regions:  `ap-east-1`  
`ap-northeast-1`  
`ap-northeast-2`  
`ap-northeast-3`  
`ap-south-1`  
`ap-south-2`  
`ap-southeast-1`  
`ca-central-1`  
`ca-west-1`  
`eu-central-1`  
`eu-central-2`  
|  `eu-north-1`  
`eu-south-1`  
`eu-south-2`  
`eu-west-1`  
`eu-west-2`  
`eu-west-3`  
`us-east-1`  
`us-east-2`  
`us-west-1`  
`us-west-2` |   
---|---|---  
  
## Required permissions

In order to use Storage Transfer Service to move data from an Amazon S3 bucket, your user account or federated identity role must have the appropriate permissions for the bucket:

Permission | Description | Use  
---|---|---  
`s3:ListBucket` | Allows Storage Transfer Service to list objects in the bucket. | Always required.  
`s3:GetObject` | Allows Storage Transfer Service to read objects in the bucket. | Required if you are transferring the current version of all objects. If your [manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) specifies an object version, use `s3:GetObjectVersion` instead.  
`s3:GetObjectVersion` | Allows Storage Transfer Service to read specific versions of objects in the bucket. | Required if your [manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) specifies an object version. Otherwise, use `s3:GetObject`.  
`s3:DeleteObject` | Allows Storage Transfer Service to delete objects in the bucket. | Required if you set `deleteObjectsFromSourceAfterTransfer` to `true`.  
  
## Authenticate using access credentials

To use an access key ID and secret key to authenticate to AWS:

  1. Create an AWS Identity and Access Management (AWS IAM) user with a name that you can recognize, such as `transfer-user`.

  2. For AWS access type, select **Access key - programmatic access**.

  3. Grant one of the following roles to the user:

     * **AmazonS3ReadOnlyAccess** to provide read-only access to the source. This allows transfers but does not support deleting objects at source once the transfer is complete.
     * **AmazonS3FullAccess** if your transfer is configured to delete objects at source.
     * A custom role with the appropriate permissions from the Required permissions table. The JSON for the minimum permissions looks like the following example:

###  Standard AWS regions 
           
           {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": [
                 "s3:GetObject",
                 "s3:ListBucket"
               ],
               "Resource": [
                 "arn:aws:s3:::S3_BUCKET_NAME/*",
                 "arn:aws:s3:::S3_BUCKET_NAME"
               ]
             }
           ]
           }

###  AWS GovCloud regions 
           
           {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": [
                 "s3:GetObject",
                 "s3:ListBucket"
               ],
               "Resource": [
                 "arn:aws-us-gov:s3:::S3_BUCKET_NAME/*",
                 "arn:aws-us-gov:s3:::S3_BUCKET_NAME"
               ]
             }
           ]
           }

  4. Note the **access key ID** and **secret access key** when the user is successfully created.




How you pass the access key ID and secret access key to Storage Transfer Service depends on the interface you use to initiate the transfer.

###  Google Cloud console 

Enter the values directly into the transfer job creation form.

See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) to get started.

###  gcloud CLI 

Create a JSON file with the following format:
    
    
    {
      "accessKeyId": "AWS_ACCESS_KEY_ID",
      "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
    }
    

Pass the location of the file to the `gcloud transfer jobs create` command using the `source-creds-file` flag:
    
    
    gcloud transfer jobs create s3://S3_BUCKET_NAME gs://GCS_BUCKET_NAME \
      --source-creds-file=PATH/TO/KEYFILE.JSON
    

###  REST API 

Your `transferSpec` object must contain the key info as part of the `awsS3DataSource` object:
    
    
    "transferSpec": {
      "awsS3DataSource": {
        "bucketName": "S3_BUCKET_NAME",
        "awsAccessKey": {
          "accessKeyId": "AWS_ACCESS_KEY_ID",
          "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
        }
      },
      "gcsDataSink": {
        "bucketName": "GCS_BUCKET_NAME"
      }
    }
    

###  Client libraries 

See the examples in the [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers#s3-to-cloud) page.

## Save your access credentials in Secret Manager

Secret Manager is a secure service that stores and manages sensitive data such as passwords. It uses strong encryption, role-based access control, and audit logging to protect your secrets.

Storage Transfer Service can leverage Secret Manager to protect your AWS access credentials. You load your credentials into Secret Manager, then pass the secret resource name to Storage Transfer Service.

### Enable the API

Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

### Configure additional permissions

#### User permissions

The user creating the secret requires the following role:

  * Secret Manager Admin (`roles/secretmanager.admin`)



Learn how to [grant a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

#### Service agent permissions

The Storage Transfer Service [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) requires the following IAM role:

  * Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)



To grant the role to your service agent:

###  Google Cloud console 

  1. Follow the instructions to [retrieve your service agent email](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#find).

  2. Go to the **IAM** page in the Google Cloud console.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Click **Grant access**.

  4. In the **New principals** field, enter the service agent email.

  5. In the **Select a role** drop-down, search for and select **Secret Manager Secret Accessor**.

  6. Click **Save**.




###  gcloud CLI 

Use the `gcloud projects add-iam-policy-binding` command to add the IAM role to your service agent.

  1. Follow the instructions to [retrieve your service agent email](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#find).

  2. From the command line, enter the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='serviceAccount:SERVICE_AGENT_EMAIL' \
           --role='roles/secretmanager.secretAccessor'
         




### Create a secret

Create a secret with Secret Manager:

###  Google Cloud console 

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Create secret**.

  3. Enter a name.

  4. In the **Secret value** field, enter your credentials in the following format:
         
         {
           "accessKeyId": "AWS_ACCESS_KEY_ID",
           "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
         }
         

  5. Click **Create secret**.

  6. Once the secret has been created, note the secret's full resource name:

     1. Select the **Overview** tab.

     2. Copy the value of **Resource ID**. It uses the following format:

`projects/1234567890/secrets/SECRET_NAME`




###  gcloud CLI 

To create a new secret using gcloud CLI, pass the JSON-formatted credentials to the `gcloud secrets create` command:
    
    
    printf '{
      "accessKeyId": "AWS_ACCESS_KEY_ID",
      "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
    }' | gcloud secrets create SECRET_NAME --data-file=-
    

Retrieve the secret's full resource name:
    
    
    gcloud secrets describe SECRET_NAME
    

Note the value of `name` in the response. It uses the following format:

`projects/1234567890/secrets/SECRET_NAME`

For more details about creating and managing secrets, refer to the [Secret Manager documentation](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

### Pass your secret to the job creation command

Using Secret Manager with Storage Transfer Service requires using the REST API to create a transfer job.

Pass the Secret Manager resource name as the value of the `transferSpec.awsS3DataSource.credentialsSecret` field:
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    
    {
      "description": "Transfer with Secret Manager",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "awsS3DataSource": {
          "bucketName": "S3_BUCKET_NAME",
          "credentialsSecret": "SECRET_RESOURCE_ID",
        },
        "gcsDataSink": {
          "bucketName": "GCS_BUCKET_NAME"
        }
      }
    }
    

## Authenticate using federated identity

To use federated identity to authenticate to AWS:

  1. Create a new IAM role in AWS.

  2. Select **Custom trust policy** as the trusted entity type.

  3. Copy and paste the following trust policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "Federated": "accounts.google.com"
               },
               "Action": "sts:AssumeRoleWithWebIdentity",
               "Condition": {
                 "StringEquals": {
                   "accounts.google.com:sub": "SUBJECT_ID"
                 }
               }
             }
           ]
         }
         

  4. Replace SUBJECT_ID with one of the following values:

###  Service agent 

If your transfer job doesn't specify a `serviceAccount` (i.e., you are not [delegating service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions)), replace SUBJECT_ID with the `subjectId` of the service agent that is automatically created when you start using Storage Transfer Service. To retrieve the `subjectId`:

     1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

An interactive panel opens, titled **Try this method**.

     2. In the panel, under **Request parameters** , enter your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). The project you specify here must be the project you're using to manage Storage Transfer Service.

     3. Click **Execute**. The `subjectId` is included in the response.

###  User-managed service account 

If you are [delegating service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions), the value of SUBJECT_ID is that service account's unique ID (`uniqueId`).

To retrieve the `uniqueId`, see [Retrieve a service account's unique ID](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions#retrieve-unique-id).

  5. Grant one of the following permissions policies to the role:

     * **AmazonS3ReadOnlyAccess** provides read-only access to the source. This allows transfers but does not support deleting objects at source once the transfer is complete.
     * **AmazonS3FullAccess** if your transfer is configured to delete objects at source.
     * A custom role with the appropriate permissions from the Required permissions table. The JSON for the minimum permissions looks like the following example:

###  Standard AWS regions 
           
           {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": [
                 "s3:GetObject",
                 "s3:ListBucket"
               ],
               "Resource": [
                 "arn:aws:s3:::S3_BUCKET_NAME/*",
                 "arn:aws:s3:::S3_BUCKET_NAME"
               ]
             }
           ]
           }

###  AWS GovCloud regions 
           
           {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": [
                 "s3:GetObject",
                 "s3:ListBucket"
               ],
               "Resource": [
                 "arn:aws-us-gov:s3:::S3_BUCKET_NAME/*",
                 "arn:aws-us-gov:s3:::S3_BUCKET_NAME"
               ]
             }
           ]
           }

  6. Assign a name to the role and create the role.




Once created, view the role details to retrieve the role's Amazon Resource Name (ARN). Note this value; it has one of the following formats:

  * For standard AWS regions: `arn:aws:iam::AWS_ACCOUNT:role/AWS_ROLE_NAME`
  * For AWS GovCloud regions: `arn:aws-us-gov:iam::AWS_ACCOUNT:role/AWS_ROLE_NAME`



How you pass the role ARN to Storage Transfer Service depends on the interface you use to initiate the transfer.

###  Google Cloud console 

Enter the role ARN directly into the transfer job creation form.

See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) to get started.

###  gcloud CLI 

Create a JSON file with the following format:
    
    
    {
      "roleArn": "AWS_ROLE_ARN"
    }
    

Pass the location of the file to the `gcloud transfer jobs create` command using the `source-creds-file` flag:
    
    
    gcloud transfer jobs create s3://S3_BUCKET_NAME gs://GCS_BUCKET_NAME \
      --source-creds-file=PATH/TO/ARNFILE.JSON
    

###  REST API 

Your `transferSpec` object must contain the role ARN info as part of the `awsS3DataSource` object:
    
    
    "transferSpec": {
      "awsS3DataSource": {
        "bucketName": "AWS_SOURCE_NAME",
        "roleArn": "AWS_ROLE_ARN"
      },
      "gcsDataSink": {
        "bucketName": "GCS_BUCKET_NAME"
      }
    }
    

###  Client libraries 

See the examples in the [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers#s3-to-cloud) page.

## IP restrictions

If your AWS project uses IP restrictions for access to storage, you must add the IP ranges used by Storage Transfer Service workers to your list of allowed IPs.

**Note:** If you're using agents instead of an agentless transfer, add your agent machine IP address(es) to the allowlist instead.

Because these IP ranges can change, we publish the current values as a JSON file at a permanent address:

[`https://www.gstatic.com/storage-transfer-service/ipranges.json`](https://www.gstatic.com/storage-transfer-service/ipranges.json)

When a new range is added to the file, we'll wait at least 7 days before using that range for requests from Storage Transfer Service.

We recommend that you pull data from this document at least weekly to keep your security configuration up to date. For a sample Python script that fetches IP ranges from a JSON file, [see this article from the Virtual Private Cloud documentation](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults).

To add these ranges as allowed IPs, use the `Condition` field in a bucket policy, as described in the AWS S3 documentation: [Managing access based on specific IP addresses](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-IP).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
