---
url: https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions/
title: Agent-based transfer permissions \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:41.925418+00:00
---

# Agent-based transfer permissions  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Agent-based transfer permissions Stay organized with collections  Save and categorize content based on your preferences. 

Before creating an agent-based transfer, you must configure permissions for the following entities:

  * The **user or user-managed service account** being used to create the transfer. This is the account that is signed in to the Google Cloud console, or the account that is specified when authenticating to the `gcloud` CLI. The user account can be a regular user account, or a user-managed service account.

  * The **[service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)** used by Storage Transfer Service. This account is generally identified by its email address, which uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.

  * The **transfer agent account** that provides Google Cloud permissions for transfer agents. Transfer agent accounts use the credentials of the user installing them, or the credentials of a user-managed service account, to authenticate.




For more information on granting IAM roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Simplest method of granting permissions

The `gcloud` CLI can be used to grant the required permissions to the user / user-managed service account and to the service agent. These permissions allow the user to create, edit, and delete transfer jobs, and set or modify bandwidth limits.

If these permissions are too broad for your organization's policies, refer to the later sections in this document for the minimum permissions required by Storage Transfer Service.

To inspect existing permissions and print out any missing roles, run the following command:
    
    
    gcloud transfer authorize
    

To automatically apply those roles, use the `--add-missing` flag:
    
    
    gcloud transfer authorize --add-missing
    

To grant permissions to a user-managed service account, pass the service account key file:
    
    
    gcloud transfer authorize --add-missing --creds-file=path/to/key.json
    

For instructions on creating a service account, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

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

## User or user-managed service account permissions

This section covers the roles required for the accounts managing and executing transfers. Your organization's requirements will dictate the exact roles for each persona; this section assumes that you will create an administrator and a user.

### Administrator accounts

Storage Transfer Service administrator accounts manage transfer agents, set bandwidth usage limits, and delete transfer jobs.

To set up an administrator account, assign the following IAM permissions and roles:

Role / Permission | What it does | Notes  
---|---|---  
**`resourcemanager.projects.getIamPolicy`** |  This permission is used to confirm that the [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) has the required permissions for a transfer.  | To grant this permission, grant the [Role Viewer (`roles/iam.roleViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) predefined role, or [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with this single permission and grant the custom role.  
**Storage Transfer Admin (`roles/storagetransfer.admin`) ** |  Enables administrative actions in the transfer project, such as project set up and agent monitoring.  |  For a detailed listing of permissions granted, see [ Storage Transfer Service Predefined roles](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles).   
  
### User accounts

Storage Transfer Service user accounts are used to create and execute transfers. These accounts typically don't have access to delete transfer jobs.

A user account can be a Google Cloud console user, or a service account. If you're using a service account, the method you use to pass the credentials to Storage Transfer Service varies depending on the interface you use.

To set up a user account, assign the following permissions and roles to the account:

Role / Permission | What it does | Notes  
---|---|---  
**`resourcemanager.projects.getIamPolicy`** |  Used to confirm that the [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) has the required Pub/Sub permissions for a transfer.  | To grant this permission, grant the [Role Viewer (`roles/iam.roleViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) predefined role, or [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with this single permission and grant the custom role.  
**Storage Transfer User (`roles/storagetransfer.user`) ** |  Enables the user to create, get, update, and list transfers.  | For a detailed listing of permissions granted, see [ Storage Transfer Service Predefined roles](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles).   
  
## Service agent permissions

Storage Transfer Service uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to move your data. This service account is automatically created the first time you create a transfer job, call `googleServiceAccounts.get`, or visit the job creation page in the Google Cloud console.

The service account's format is typically `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`. To retrieve your service account identifier, use the `[ googleServiceAccounts.get](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get)` API call.

### Automatically assigning roles

There are two ways to automatically assign the correct roles to the service agent:

  * Create your transfer using the Google Cloud console. The console automatically applies the required permissions.

  * Use `gcloud transfer authorize --add-missing`. See Simplest method of granting permissions.




### Manually assigning roles

To allow the service agent access to resources needed to complete transfers, assign the following roles, or equivalent permissions, to the service account.

Role / Permission | What it does | Notes  
---|---|---  
**Storage Object Creator (`roles/storage.objectCreator`) ** |  Enables Storage Transfer Service to create [transfer logs](https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format) in the Cloud Storage bucket connected to this transfer.  |  Grant to all Cloud Storage buckets used in a transfer. If appropriate for your situation, you can grant the role on a project level to the project that Storage Transfer Service is running from.   
  
For a detailed listing of the permissions these roles grant, see [ Cloud Storage Predefined roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles).   
**Storage Object Viewer (`roles/storage.objectViewer`) ** |  Enables Storage Transfer Service to determine if a file has already been transferred to or from Cloud Storage.   
**Storage Transfer Service Agent (`roles/storagetransfer.serviceAgent`) ** |  Enables Storage Transfer Service to automatically create and modify Pub/Sub topics to communicate from Google Cloud to transfer agents.  |  Apply the role on a project level to the project that Storage Transfer Service is running from.   
  
For a detailed listing of the permissions this role grants, see [Permissions and roles](https://docs.cloud.google.com/storage-transfer/docs/access-control#serviceagent).   
**Storage Legacy Bucket Reader (`roles/storage.legacyBucketReader`) ** |  Enables Storage Transfer Service to read Cloud Storage bucket metadata.  |  Grant to each Cloud Storage bucket used in a transfer. Cloud Storage `legacy` roles can only be granted at the bucket level.  
  
See [Grant the required permissions](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#grant_the_required_permissions) for instructions.

## Transfer agent account permissions

Storage Transfer Service transfer agents can be run with either the user's account, or with a [service account](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#service-credentials).

To set up a transfer agent service account or user account running the transfer agents, assign the following role:

Role / Permission | What it does | Notes  
---|---|---  
**Storage Transfer Agent (`roles/storagetransfer.transferAgent`) ** |  Gives transfer agents the Storage Transfer Service permissions required to complete a transfer. This role also includes permissions required to log skipped files.  |  Grant this role to the user or service account being used by agents.   
  
For a detailed listing of the permissions this role grants, see [ Access Control with IAM](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles).   
  
### Source and destination permissions

You must also ensure that the agent account has the correct permissions to access the source data and to write to the destination.

#### File system, S3-compatible storage, or HDFS to Cloud Storage

If your transfer destination is a Cloud Storage bucket, the transfer agent needs the following permissions on the destination bucket. See [Add a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add) for instructions.

Permission | Description  
---|---  
`storage.objects.create` | Allows the agent account to write Cloud Storage objects during transfer.  
`storage.objects.get` | Allows the agent account to read object data and metadata.  
`storage.objects.list` | Allows the agent account to list objects in the Cloud Storage bucket.  
`storage.objects.delete` | Required if your transfer is configured to overwrite or delete objects in the sink; for example, if `overwriteObjectsAlreadyExistingInSink` or `deleteObjectsUniqueInSink` are set in your transfer's [ transferOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions) configuration.  
  
To grant these permissions, grant the following role:

  * [Storage Object Admin](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectAdmin`)



Or, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the specific permissions and grant the custom role.

Additional permissions are required to enable multipart uploads.

#### Cloud Storage to file system

If your transfer's source is a Cloud Storage bucket, the transfer agent needs the following permission on the source bucket.

Permission | Description  
---|---  
`storage.objects.create` | Allows the agent account to write transfer logs and transfer-related metadata to the Cloud Storage source bucket.  
`storage.objects.get` | Allows the agent account to read object data and metadata.  
`storage.objects.list` | Allows the agent account to list objects in the Cloud Storage bucket.  
`storage.objects.delete` | Required if your transfer is configured to delete objects from the source. See [ `deleteObjectsFromSourceAfterTransfer`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions).  
  
To grant this permission, grant the following role:

  * [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectViewer`)



Or, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the single permission and grant the custom role.

#### File system to file system

If your transfer is between two file systems, the transfer agent needs the following permissions on the intermediate bucket.

Permission | Description  
---|---  
`storage.objects.create` | Allows the agent account to write Cloud Storage objects during transfer.  
`storage.objects.get` | Allows the agent account to read object data and metadata.  
`storage.objects.list` | Allows the agent account to list objects in the Cloud Storage bucket.  
`storage.objects.delete` | Required if your transfer is configured to delete objects in the intermediate bucket after the transfer is complete.  
  
To grant these permissions, grant the following role:

  * [Storage Object Admin](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectAdmin`)



Or, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the specific permissions and grant the custom role.

Additional permissions are required to enable multipart uploads.

## Multipart uploads

To enable [multipart uploads](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#enable_multipart_uploads) for file system to Cloud Storage transfers or transfers between file systems, additionally grant the following permissions to the agent.

  * For transfers to Cloud Storage, assign the permissions to the destination bucket.
  * For transfers between file systems, assign the permissions to the intermediate bucket.

Multipart upload permission name | Description  
---|---  
`storage.multipartUploads.create` | Upload objects in multiple parts.  
`storage.multipartUploads.abort` | Abort multipart upload sessions.  
`storage.multipartUploads.listParts` | List the uploaded object parts in a multipart upload session.  
`storage.multipartUploads.list` | List the multipart upload sessions in a bucket.  
  
To grant these permissions, grant the following role:

  * [Storage Object Admin](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectAdmin`)



Or, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the specific permissions and grant the custom role.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
