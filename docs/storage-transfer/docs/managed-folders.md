---
url: https://docs.cloud.google.com/storage-transfer/docs/managed-folders/
title: Transfer Cloud Storage managed folders \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:52.700637+00:00
---

# Transfer Cloud Storage managed folders  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/managed-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer Cloud Storage managed folders Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Storage managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) provide fine-grained access control to objects in Cloud Storage buckets. Permissions can be set at a folder level within buckets that use universal bucket-level access. When transferring objects between Cloud Storage buckets with Storage Transfer Service, these managed folder permissions can be retained.

## Limitations

The following limitations apply to transfers of managed folders:

  * The destination bucket must use [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).
  * Managed folder transfers do not support the `deleteObjectsUniqueInSink` or `deleteObjectsFromSourceAfterTransfer` options.
  * There must be no [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) on the destination bucket or its project that use the _bucket_ resource type (`storage.googleapis.com/Bucket`) or the _object_ resource type (`storage.googleapis.com/Object`). If any bucket within a project has an IAM Condition that uses either of these resource types, managed folders cannot be transferred to any of the buckets within that project, even if the condition is later removed.
  * Event-driven transfers are not supported.
  * Manifest transfers are not supported.



## IAM permissions

The following Google Cloud Identity and Access Management (IAM) permissions are required by the Storage Transfer Service [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

For both the source and the destination, permissions can be set at the bucket level, or can be [set on the managed folder](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders). To set permissions on a destination managed folder, that folder must already exist.

We do not recommend setting managed folder permissions at a project level; see Security considerations for additional info.

On the source bucket or managed folder:

  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.get`



On the destination bucket or managed folder:

  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.create`



These are in addition to the standard permissions required by Storage Transfer Service:

  * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage)
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)



To grant the required managed folder permissions, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with only the permissions required.

## Create a managed folder transfer

To create a transfer containing a managed folder, specify `managedFolderTransferEnabled: true` in your `transferSpec`. You can optionally specify a `path` value to transfer only a specific managed folder.
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
      "name": "transferjobs/NAME",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "gcsDataSource": {
          "bucketName": "SOURCE_BUCKET",
          "path": "SOURCE_PATH",
          "managedFolderTransferEnabled": true
        },
        "gcsDataSink": {
          "bucketName": "DESTINATION_BUCKET",
          "path": "DESTINATION_PATH",
        }
      },
      "status": "ENABLED"
    }
    

If the correct managed transfer permissions are not set at the source and the destination, the transfer fails.

See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers?tab=rest#create-a-transfer) for details on creating a transfer using the REST API, or refer to the [`transferJobs.create` reference](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create).

## Security considerations

Granting managed folder permissions to a service agent enables the account to modify IAM policies on destination folders, or on all folders if the role is granted at the project level. This poses a security risk: a user with job edit permissions could exploit this to grant privileges to a malicious actor. To mitigate this risk, consider isolating managed folder transfers within a dedicated Google Cloud project.

## Cloud Logging

Managed folder actions are logged by Cloud Logging. See [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for details.

## Troubleshooting

For help creating and managing managed folders, refer to the [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#folders) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
