---
url: https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs/
title: Troubleshoot CMEK and default resource settings for Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:37.265301+00:00
---

# Troubleshoot CMEK and default resource settings for Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot CMEK and default resource settings for Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to find and mitigate common CMEK configuration errors. It also describes how to identify errors that occur when configuring default resource settings for Cloud Logging. Those settings can be configured for organizations and folders.

## Troubleshoot setting the location for new system-created log buckets

For an organization or folder, you attempt to update the default resource settings for Cloud Logging. Your update is either to set or modify the location setting. However, the command fails with an error similar to the following:
    
    
    ERROR: (gcloud.logging.settings.update) INVALID_ARGUMENT: The KMS key location must match the storage location. Received KMS key location: us-central1, storage location: us-west1
    - '@type': type.googleapis.com/google.rpc.DebugInfo
      detail: '[ORIGINAL ERROR] generic::invalid_argument: The KMS key location must match
        the storage location. Received KMS key location: us-central1, storage location:
        us-west1 [google.rpc.error_details_ext] { message: "The KMS key location must
        match the storage location. Received KMS key location: us-central1, storage location:
        us-west1" }'
    

To resolve this error, set location in the default resource settings to be the location of the Cloud Key Management Service key.

## Troubleshoot VPC Service Controls and domain restricted sharing

You configured your default resource settings for Cloud Logging to have a CMEK setting or you created a log bucket with CMEK enabled. You then configure VPC Service Controls. After you configure VPC Service Controls, you restrict access to Cloud Key Management Service in VPC Service Controls or [enable domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).

At least one of the following occurs:

  * You received a notification from Cloud Logging about CMEK access issues.

  * You notice that CMEK isn't enabled for the `_Default` and `_Required` log buckets when you create new Google Cloud projects in your organization or in a folder.

  * You receive errors when you read from log buckets with CMEK enabled. The errors you see are similar to the following error:
        
        ERROR: (gcloud.logging.read) FAILED_PRECONDITION: service account `cmek-PROJECT_ID@gcp-sa-logging.iam.gserviceaccount.com` must have both encrypt and decrypt access to the CMEK KMS key `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`
        

  * You receive errors when you create or update log buckets with CMEK enabled. The errors you see are similar to the following error:
        
        ERROR: (gcloud.logging.buckets.create) service account `cmek-PROJECT_ID@gcp-sa-logging.iam.gserviceaccount.com` must have both encrypt and decrypt access to the CMEK KMS key `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`
        - '@type': type.googleapis.com/google.rpc.DebugInfo
          detail: '[ORIGINAL ERROR] generic::permission_denied: Request is prohibited by
          organization's policy. vpcServiceControlsUniqueIdentifier: <var>ERRORID</var>;'
        




To determine if these problems are due to the VPC Service Controls configuration, do the following:

  1. Identify the Cloud Logging settings for the resource that contains the CMEK configuration. A resource can be a project, a folder, or an organization. If you created log buckets with CMEK enabled, then select the PROJECT resource.

###  PROJECT 
         
         gcloud logging settings describe --project=PROJECT_ID
         

Before you run the command, replace PROJECT_ID with the project ID that contains the log bucket.

###  FOLDER 
         
         gcloud logging settings describe --folder=FOLDER_ID
         

Before you run the command, replace FOLDER_ID with the ID of the folder.

###  ORGANIZATION 
         
         gcloud logging settings describe --organization=ORGANIZATION_ID
         

Before you run the command, replace ORGANIZATION_ID with the ID of the organization.

The previous command returns information similar to the following:
         
         kmsServiceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
         loggingServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
         

For organizations and folders, the following field is also returned:
         
         kmsKeyName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY
         

The value of the `kmsKeyName` field include thes Google Cloud project that stores the key.

  2. Determine whether you need to migrate service accounts:

     * If the value of the `kmsServiceAccountId` field has the prefix `service-`, then you don't need to migrate your service account. For information about CMEK configuration errors, see the Troubleshoot CMEK section of this document.

     * If the value of `kmsServiceAccountId` has the prefix `cmek-`, then proceed to the next step.

  3. Confirm that you must migrate service accounts by disabling [domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) or by removing Cloud Key Management Service from the list of VPC Service Controls restricted services.

If the errors are resolved, then to resolve the failures you must migrate the affected resources to a new service account. For information about these steps, see the next section.




### Migrate CMEK service accounts

The following process describes how to change the service account that Cloud Logging uses to access configured Cloud Key Management Service keys. The change in service account resolves a known issue with VPC Service Controls and domain restricted sharing.

  1. Identify the `loggingServiceAccountId` for your resource. A resource can be a project, a folder, or an organization. If you created log buckets with CMEK enabled, then select the PROJECT resource.

###  PROJECT 
         
         gcloud logging settings describe --project=PROJECT_ID
         

Before you run the command, replace PROJECT_ID with the project ID that contains the log bucket.

###  FOLDER 
         
         gcloud logging settings describe --folder=FOLDER_ID
         

Before you run the command, replace FOLDER_ID with the ID of the folder.

###  ORGANIZATION 
         
         gcloud logging settings describe --organization=ORGANIZATION_ID
         

Before you run the command, replace ORGANIZATION_ID with the ID of the organization.

The previous command returns information similar to the following:
         
         kmsServiceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
         loggingServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
         

For organizations and folders, the following field is also returned:
         
         kmsKeyName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY
         

The value of the `kmsKeyName` field include thes Google Cloud project that stores the key.

  2. If, for your organization or for folders, you configured the default resource settings for Cloud Logging with CMEK settings, then do the following:

     1. In the KMS_PROJECT_ID, grant the [Cloud Key Management Service CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role to the service account identified by the `loggingServiceAccountId` field.

     2. Run the following curl command, which changes the Cloud Key Management Service service account used by the resource.

###  PROJECT 

Not applicable.

###  FOLDER 
            
            curl -X PATCH -H "Authorization: Bearer \"$(gcloud auth print-access-token)\"" -H "Content-Type: application/json; charset=utf-8" -d '{"kmsServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com"}' https://logging.googleapis.com/v2/folders/FOLDER_ID/settings?updateMask=kmsServiceAccountId
            

Before you run the command, do the following:

        * Replace FOLDER_ID with the ID of the folder.
        * Replace SERVICE_ACCT_NAME with the `loggingServiceAccountId` identified earlier.

###  ORGANIZATION 
    
    curl -X PATCH -H "Authorization: Bearer \"$(gcloud auth print-access-token)\"" -H "Content-Type: application/json; charset=utf-8" -d '{"kmsServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com"}' https://logging.googleapis.com/v2/organizations/ORGANIZATION_ID/settings?updateMask=kmsServiceAccountId
    

Before you run the command, do the following:

        * Replace ORGANIZATION_ID with the ID of the organization.
        * Replace SERVICE_ACCT_NAME with the `loggingServiceAccountId` identified earlier.

The result of the previous command is similar to the following;
    
    {
      "name": ".../settings",
      "kmsKeyName": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY",
      "kmsServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com",
      "storageLocation": "...",
      "loggingServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com"
    }
    

**Note:** The new service account is used for new resources created in the organization or folder. The service account for existing resources isn't modified.
  3. For each Google Cloud project or folder that contain existing log buckets enabled with CMEK, do the following:

     1. In the project or folder, for each log bucket enabled with CMEK, do the following:

        1. Identify the Google Cloud project that stores the Cloud Key Management Service key:

###  PROJECT 
               
               gcloud logging buckets describe BUCKET_ID --location=LOCATION --project=PROJECT_ID
               

Before you run the command, do the following:

           * Replace PROJECT_ID with the project ID that contains the log bucket.
           * Replace LOCATION with the location of the log bucket.

###  FOLDER 
    
    gcloud logging buckets describe BUCKET_ID --location=LOCATION --folder=FOLDER_ID
    

Before you run the command, do the following:

           * Replace FOLDER_ID with the ID of the folder.
           * Replace LOCATION with the location of the log bucket.

The result of the previous command is similar to the following:
    
    cmekSettings:
      kmsKeyName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY
      kmsKeyVersionName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY/cryptoKeyVersions/1
      serviceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    createTime: '2022-10-31T12:00:00.0000000Z'
    lifecycleState: ACTIVE
    name: projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    retentionDays: 30
    createTime: '2022-10-31T13:00:00.0000000Z'
    

        2. Go to the Google Cloud project that owns the Cloud Key Management Service key, KMS_PROJECT_ID, and grant the [Cloud Key Management Service CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role to the service account identified by the `loggingServiceAccountId` field.

     2. For the project, run the following curl command, which changes the Cloud Key Management Service service account:

###  PROJECT 
            
            curl -X PATCH -H "Authorization: Bearer \"$(gcloud auth print-access-token)\"" -H "Content-Type: application/json; charset=utf-8" -d '{"kmsServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com"}' https://logging.googleapis.com/v2/projects/PROJECT_ID/settings?updateMask=kmsServiceAccountId
            

Before you run the command, do the following:

        * Replace PROJECT_ID with the project ID that contains the log bucket.
        * Replace SERVICE_ACCT_NAME with the `loggingServiceAccountId` identified earlier.

###  FOLDER 

No action necessary, as you changed the Cloud Key Management Service service account used by the folder in a previous step.

The result of the previous command is similar to the following;
    
    {
      "name": ".../settings",
      "kmsServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com",
      "loggingServiceAccountId": "SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com"
    }
    

  4. For the each log bucket with CMEK enabled, do the following:

     1. [Rotate the Cloud KMS key](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#rotate-key).

     2. Confirm the migration. The parent resource for the log bucket determines which Google Cloud CLI command to run. The parent might be a project, folder, or organization.

###  PROJECT 
            
            gcloud logging buckets describe BUCKET_ID --location=LOCATION --project=PROJECT_ID
            

Before you run the command, do the following:

        * Replace PROJECT_ID with the project ID that contains the log bucket.
        * Replace LOCATION with the location of the log bucket.

###  FOLDER 
    
    gcloud logging buckets describe BUCKET_ID --location=LOCATION --folder=FOLDER_ID
    

Before you run the command, do the following:

        * Replace FOLDER_ID with the ID of the folder.
        * Replace LOCATION with the location of the log bucket.

For a project, the result of the previous command is similar to the following:
    
    cmekSettings:
      kmsKeyName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY
      kmsKeyVersionName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY/cryptoKeyVersions/1
      serviceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    createTime: '2022-10-31T12:00:00.0000000Z'
    lifecycleState: ACTIVE
    name: projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    retentionDays: 30
    createTime: '2022-10-31T13:00:00.0000000Z'
    

Ensure that `serviceAccountId` matches the `loggingServiceAccountId` identified earlier.

  5. Wait at least 30 minutes before revoking permissions on the previous service account. If you experience any issues after revoking permissions on the previous service account, then restore the permissions and contact Cloud Support.




## Troubleshoot CMEK

As you configure CMEK, the Google Cloud project containing the Cloud KMS key is notified of related issues. For example, updates fail when the KMS_KEY_NAME is invalid, when the associated service account doesn't have the required [Cloud Key Management Service CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role, or when access to the key is disabled.

After you configure CMEK, at least on of the following occurs:

  * You received a notification from Cloud Logging about CMEK access issues.

  * You notice that CMEK isn't enabled for the `_Default` and `_Required` log buckets when you create new Google Cloud projects in your organization or in a folder.

  * You receive errors when you read from log buckets with CMEK enabled, or if you try to create or update log buckets.




The notification provides information about the failure and it contains that you can take to mitigate the issue:

Error | Recommendation  
---|---  
Cryptographic key permission denied | The Logging service account associated with your Google Cloud project doesn't have sufficient IAM permissions to operate on the specified Cloud KMS key. Follow the instructions in the error or see the following documents:

  * If you have enabled VPC Service Controls, then see the Troubleshoot VPC Service Controls and domain restricted sharing. section of this document.
  * [Assign the Encrypter/Decrypter role for log buckets](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#assign-role)
  * [Assign the Encrypter/Decrypter role for organizations and folders](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#assign-role)

  
Cryptographic key is disabled | The specified Cloud KMS key was disabled. Follow the instructions in the error to re-enable the key.  
Cryptographic key was destroyed | The specified Cloud KMS key was destroyed. Follow the instructions or see the following documents:

  * [Manage your Cloud KMS key for a log bucket](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#manage-key)
  * [Manage your Cloud KMS key for a folder or organization](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#manage-key)

  
  
### Identify project that contains the Cloud KMS key

To identify the ID of the Google Cloud project that contains the encryption key used by a log bucket, folder, or organization, do the following:

###  PROJECT 
    
    
    gcloud logging settings describe --project=PROJECT_ID
    

Before you run the command, replace PROJECT_ID with the project ID that contains the log bucket.

###  FOLDER 
    
    
    gcloud logging settings describe --folder=FOLDER_ID
    

Before you run the command, replace FOLDER_ID with the ID of the folder.

###  ORGANIZATION 
    
    
    gcloud logging settings describe --organization=ORGANIZATION_ID
    

Before you run the command, replace ORGANIZATION_ID with the ID of the organization.

The previous command returns information similar to the following:
    
    
    kmsServiceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    loggingServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    

For organizations and folders, the following field is also returned:
    
    
    kmsKeyName: projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY
    

The value of the `kmsKeyName` field include thes Google Cloud project that stores the key.

### Verify key usability

To verify the key's usability, run the following command to list all keys:
    
    
    gcloud kms keys list \
    --location=KMS_KEY_LOCATION \
    --keyring=KMS_KEY_RING
    

This command returns information about each key in a tabular format. The first line of the output is a list of column names:
    
    
    NAME PURPOSE ...
    

Verify that the Cloud KMS key is listed in the command's output as `ENABLED`, and that the purpose of the key is symmetric encryption: the `PURPOSE` column must contain `ENCRYPT_DECRYPT` and the `PRIMARY_STATE` column must contain `ENABLED`.

If necessary, [create a new key](https://docs.cloud.google.com/kms/docs/creating-keys).

### Verify permissions configuration

Service accounts that are associated with the organization's CMEK settings must have the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role for the configured key.

To list the key's IAM policy, run the following command:
    
    
    gcloud kms keys get-iam-policy KMS_KEY_NAME
    

If necessary, add the service account that contains the Cloud KMS CryptoKey Encrypter/Decrypter role to the key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
