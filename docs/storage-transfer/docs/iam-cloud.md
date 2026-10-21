---
url: https://docs.cloud.google.com/storage-transfer/docs/iam-cloud/
title: Agentless transfer permissions \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:46.354672+00:00
---

# Agentless transfer permissions  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/iam-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Agentless transfer permissions Stay organized with collections  Save and categorize content based on your preferences. 

Agentless transfers include transfers within Cloud Storage, or from Amazon S3, Azure Blob Storage or Data Lake Storage Gen2, or URL lists of public objects. They do not require transfer agents or agent pools.

When transferring data between cloud providers in an agentless transfer, you must grant permissions to two principals:

  * The **user account** that's creating or managing the transfer.
  * A **[service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)** that's automatically created the first time you interact with Storage Transfer Service. You can delegate the service agent permissions to a user-managed service account; see [Delegate service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions).



To learn how to grant IAM roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Simplest method of granting permissions

The `gcloud` CLI can be used to grant the required permissions to the user account and to the service agent. These permissions allow the user to create, edit, and delete transfer jobs, and set or modify bandwidth limits.

If these permissions are too broad for your organization's policies, refer to the later sections in this document for the minimum permissions required by Storage Transfer Service.

To inspect existing permissions and print out any missing roles, run the following command:
    
    
    gcloud transfer authorize
    

To automatically apply those roles, use the `--add-missing` flag:
    
    
    gcloud transfer authorize --add-missing
    

To grant permissions to a user-managed service account in place of the user, pass the service account key file:
    
    
    gcloud transfer authorize --add-missing --creds-file=path/to/key.json
    

The command grants the following permissions.

  * To the user / user-managed service account:

    * `roles/owner`
    * `roles/storagetransfer.admin`
    * `roles/storagetransfer.transferAgent`
    * `roles/storage.objectAdmin`
    * `roles/pubsub.editor`
  * To the service agent:

    * `roles/storage.admin`
    * `roles/storagetransfer.serviceAgent`



For instructions on installing the `gcloud` CLI, see the [`gcloud` quickstart](https://docs.cloud.google.com/sdk/docs/install-sdk).

## User account permissions

The user account needs permission to execute Storage Transfer Service operations. These permissions are granted through one of two roles: **Storage Transfer User** or **Storage Transfer Admin**.

In addition, the account needs permission to retrieve the service agent in order to check its permissions.

To set up the user account or user-managed service account, grant the following IAM permissions and roles.

Role / Permission | What it does | Notes  
---|---|---  
**`resourcemanager.projects.getIamPolicy`** |  This permission is used to confirm that the service agent has the required permissions for a transfer.  | To grant this permission, grant the [Role Viewer (`roles/iam.roleViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) predefined role, or [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with this single permission and grant the custom role.  
One of the following roles:  
**Storage Transfer Admin (`roles/storagetransfer.admin`) ** |  Allows all Storage Transfer Service operations, including deleting transfer jobs.  |  For a detailed listing of permissions granted, see [ Storage Transfer Service Predefined roles](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles).   
**Storage Transfer User (`roles/storagetransfer.user`) ** |  Allows the user to create, get, update, and list transfers. Does not allow the user to delete transfer jobs.  | For a detailed listing of permissions granted, see [ Storage Transfer Service Predefined roles](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles).   
  
## Service agent permissions

Storage Transfer Service uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to move your data. This service account is automatically created the first time you create a transfer job, call `googleServiceAccounts.get`, or visit the job creation page in the Google Cloud console.

The service account's format is typically `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`. To retrieve your service account identifier, use the [`googleServiceAccounts.get`][googleServiceAccounts.get] API call.

### Automatically assigning roles

There are two ways to automatically assign the correct roles to the service agent:

  * Create your transfer using the Google Cloud console. The console automatically applies the required permissions.

  * Use `gcloud transfer authorize --add-missing`. See Simplest method of granting permissions.




### Manually assigning roles

To allow the service agent access to resources needed to complete transfers, assign the following roles, or equivalent permissions, to the service agent.

Role / Permission | What it does | Notes  
---|---|---  
**Storage Legacy Bucket Writer (`roles/storage.legacyBucketWriter`) ** |  Enables Storage Transfer Service to read bucket metadata, list objects in the bucket, and write objects to the destination bucket.  |  Grant on the Cloud Storage destination bucket. Cloud Storage `legacy` roles can only be granted at the bucket level.  
**Storage Object Viewer (`roles/storage.objectViewer`) ** |  Enables Storage Transfer Service to copy objects from a Cloud Storage source. Also enables Storage Transfer Service to determine if a file already exists in the Cloud Storage destination and whether it has changed. |  Grant on the Cloud Storage source bucket if you're transferring from Cloud Storage. Also grant on the Cloud Storage destination bucket if your transfer is configured to [overwrite objects](/storage-transfer/docs/reference/rest/v1/TransferOptions#OverwriteWhen) in the sink when different, or never. Not required if your transfer setting is to overwrite always. If appropriate for your situation, you can grant the role on a project level to the project that Storage Transfer Service is running from.  
**Storage Legacy Bucket Reader (`roles/storage.legacyBucketReader`) ** |  Enables Storage Transfer Service to read Cloud Storage bucket metadata.  |  Grant on the Cloud Storage source bucket if you're transferring from Cloud Storage. Cloud Storage `legacy` roles can only be granted at the bucket level.  
  
See [Grant the required permissions](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#grant_the_required_permissions) for instructions.

### Delegating to a user-managed service account

You can delegate the service agent permissions to a user-managed service account. This lets you separate bucket permissions for different transfer jobs across service accounts, instead of centralizing them in a single service agent.

For details, see [Delegate service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions).

## Cross-project Cloud Storage transfers

To transfer objects between Cloud Storage buckets in different projects, you must grant permission to a single service agent on both the source bucket and the destination bucket. The service agent belongs to the project from which you are creating the transfer.

The user or user-managed service account only needs permissions on the project that is creating the transfer.

To obtain the service agent's email, refer to [Find the service agent's email](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#find).

On the source bucket, grant the following roles at the bucket level to the service agent:

  * **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
  * **Storage Object Viewer** (`roles/storage.objectViewer`)



On the destination bucket, grant the following role at the bucket level to the **same** service agent:

  * **Storage Legacy Bucket Writer** (`roles/storage.legacyBucketWriter`)
  * In addition, for transfers configured to [overwrite objects in the sink](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--overwrite-when) when different, or never: **Storage Object Viewer** (`roles/storage.objectViewer`)



For instructions on granting roles at the bucket level, refer to the following pages:

  * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#add_the_service_agent_to_a_bucket-level_policy)
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#add_the_service_agent_to_a_bucket-level_policy)



Cloud Storage `Legacy` roles cannot be granted at the project level.

### Organizational restrictions

If your organization has applied [organization policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy) constraints such as [domain restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) (`constraints/iam.allowedPolicyMemberDomains`) or [disabling attachment of service accounts to resources in other projects](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts) (`constraints/iam.disableCrossProjectServiceAccountUsage`), these constraints must be updated before cross-project transfers can succeed.

You may also need to update any VPC Service Control settings to support cross-project transfers. See [Configure VPC Service Controls for cloud object storage transfers](https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc).

## AWS and Microsoft permissions

You must also configure access to your source files if they're in AWS S3 or Microsoft Azure Storage. The following documents detail the required steps:

  * [Configure access to AWS S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3)
  * [Configure access to Microsoft Azure Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
