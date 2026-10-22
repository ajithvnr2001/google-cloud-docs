---
url: https://docs.cloud.google.com/logging/docs/analyze/troubleshoot-upgrade-bucket/
title: Troubleshoot upgrading a bucket to use Observability Analytics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:37.839764+00:00
---

# Troubleshoot upgrading a bucket to use Observability Analytics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/troubleshoot-upgrade-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot upgrading a bucket to use Observability Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Upgrading a log bucket to use Observability Analytics lets you run SQL queries to analyze the log data stored in that bucket. If a log bucket upgrade fails or stalls, you can use this document to diagnose and resolve synchronous validation errors, asynchronous provisioning errors, and blocked operations. For information about how to upgrade a log bucket, see [Upgrade a bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket).

## About the upgrade process

Cloud Logging uses a two-step process when you issue a command to upgrade a log bucket to use Observability Analytics:

  1. **Synchronous validation** : Logging validates the command parameters. If validation fails, the command returns an error immediately.
  2. **Asynchronous provisioning** : If validation succeeds, then Logging starts a long-running operation that typically completes within 10 minutes.



Log bucket upgrades are audited operations. To check the status of the long-running operation or find error details, you can [poll the operation](https://docs.cloud.google.com/logging/docs/buckets#async-command) by using the `Operations.GetOperation` method, or you can query your audit logs.

## Log bucket state during an upgrade

When synchronous validation of an upgrade request succeeds, Logging changes the state of the log bucket from `ACTIVE` to `UPDATING` and starts the long-running operation. When the operation completes, the state of the log bucket returns to `ACTIVE`.

You can determine the current state of a log bucket by running the `gcloud logging buckets describe` command:
    
    
    gcloud logging buckets describe LOG_BUCKET_ID \
      --location=LOCATION_ID \
      --project=PROJECT_ID
    

Before you run the command, make the following replacements:

  * PROJECT_ID: Your project's ID.
  * LOCATION_ID: The location of your bucket.
  * LOG_BUCKET_ID: The ID of your bucket.



The `lifecycleState` field in the response shows the bucket's state:
    
    
    description: Default bucket
    lifecycleState: ACTIVE
    name: projects/PROJECT_ID/locations/LOCATION_ID/buckets/LOG_BUCKET_ID
    retentionDays: 30
    

In the Google Cloud console, while the log bucket is in the `UPDATING` state:

  * On the **Logs Storage** page, the **Observability Analytics available** column displays **Upgrading…** while the long-running operation is active (or **Not eligible for upgrade** if the console can't retrieve the operation status).
  * In the **Edit bucket** panel and the **Upgrade log bucket** panel, the option to upgrade the bucket is disabled and the tooltip lists **There are no pending updates** as an unmet requirement.



## VPC Service Controls perimeter considerations

Upgrades of log buckets inside a VPC Service Controls perimeter can fail due to APIs being blocked by the perimeter or due to cross-project configurations.

### APIs the perimeter must allow

To upgrade a log bucket that is inside a VPC Service Controls perimeter, the perimeter must not restrict the following services:

  * `logging.googleapis.com`
  * `cloudkms.googleapis.com`: Required to upgrade a log bucket that uses a customer-managed encryption key (CMEK).



Restricting these services causes the following behavior:

  * **`logging.googleapis.com` restricted**: The upgrade command fails immediately with a `PERMISSION_DENIED` error, and your log bucket remains in the `ACTIVE` state.

**Resolution** : Update the perimeter to allow the APIs listed at the beginning of this section and then retry the command.

  * **`cloudkms.googleapis.com` restricted**: For CMEK-protected log buckets, the long-running operation fails with an `INTERNAL` error and your log bucket returns to the `ACTIVE` state.

**Resolution** : Update the perimeter to allow the APIs listed at the beginning of this section and then retry the command.




### Cross-perimeter CMEK configurations

You can't use identity-based ingress or egress rules to grant cross-perimeter access to the Cloud Key Management Service key when your log bucket and your Cloud KMS key are in different VPC Service Controls perimeters.

For this configuration, if your ingress rule specifies only the Logging service account identity, then the following occurs:

  * Asynchronous provisioning fails with an `INTERNAL` error and your log bucket returns to the `ACTIVE` state.
  * A policy audit log for the Cloud KMS project records the failure. This audit log shows that the `google.cloud.kms.v1.KeyManagementService.Encrypt` method failed with a `NO_MATCHING_ACCESS_LEVEL` ingress violation and indicates it is for a BigQuery encryption service account.



**Resolution** : In the ingress rule that allows access to the Cloud KMS perimeter, set `identityType` to `ANY_IDENTITY` and specify the project that contains the log bucket as the source resource:
    
    
    - ingressFrom:
        identityType: ANY_IDENTITY
        sources:
        - resource: projects/PROJECT_NUMBER
      ingressTo:
        operations:
        - serviceName: cloudkms.googleapis.com
          methodSelectors:
          - method: '*'
        resources:
        - projects/KMS_PROJECT_NUMBER
    

In the preceding example, replace the following:

  * PROJECT_NUMBER: The project number of the project that contains the log bucket.
  * KMS_PROJECT_NUMBER: The project number of the project that contains the Cloud KMS key.



If you also specify an egress rule, it must also set `identityType: ANY_IDENTITY`.

## Query audit logs for failure information

The queries in this section can help you find log entries that report failures when updating or upgrading a log bucket. These queries are for use with the Logs Explorer.

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

### Query for all failed bucket updates or upgrades in a project
    
    
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.serviceName="logging.googleapis.com"
    (protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucket" OR
     protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucketAsync")
    severity=ERROR
    

If you use the Google Cloud console to both upgrade your log bucket to use Observability Analytics and create a linked BigQuery dataset, then use the following query:
    
    
    log_id("cloudaudit.googleapis.com/activity")
    (protoPayload.serviceName="logging.googleapis.com" OR
     protoPayload.serviceName="bigquery.googleapis.com")
    (protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucket" OR
     protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucketAsync" OR
     protoPayload.methodName="google.cloud.bigquery.v2.DatasetService.InsertDataset")
    severity=ERROR
    

The results of the previous query include log entries that indicate that creation of the linked BigQuery dataset failed. The error message can help you resolve the cause of the failure.

### Query for failed bucket updates or upgrades for a specific bucket

Before you use the following query, make the following replacements:

  * PROJECT_ID: Your project's ID.
  * LOCATION_ID: The location of your bucket.
  * LOG_BUCKET_ID: The ID of your bucket.


    
    
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.serviceName="logging.googleapis.com"
    (protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucket" OR
     protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucketAsync")
    protoPayload.resourceName="projects/PROJECT_ID/locations/LOCATION_ID/buckets/LOG_BUCKET_ID"
    severity=ERROR
    

### Query for long-running operation failures
    
    
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.serviceName="logging.googleapis.com"
    protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucketAsync"
    operation.last=true
    severity=ERROR
    

## `INVALID_ARGUMENT (3)`

The error message provided with an INVALID_ARGUMENT (3) error code contains sufficient information for you to resolve the failure. For this reason, this section doesn't enumerate all possible error messages.

### Resource name issues

To resolve issues with resource names, pass a valid bucket resource name in the format `projects/PROJECT_ID/locations/LOCATION_ID/buckets/LOG_BUCKET_ID`.

Make sure that the length of the resource name is within the length limits.

### Update mask issues

An error message that contains the text `update_mask` or `Update mask` indicates either a missing or malformed value.

To resolve this issue, in the API command, specify the `update_mask` and set the value to `"analytics_enabled"`.

### Log bucket eligibility issues

  * You can't upgrade a locked `_Default` log bucket or locked custom buckets. You can upgrade the `_Required` bucket while it is locked.

When a log bucket is locked, the error message is `"Bucket is not eligible for an upgrade to enable analytics"`.

To resolve this failure, create a new analytics-enabled bucket and route logs to it.

  * You can't upgrade a log bucket at the same time as you are making other changes to the bucket. For example, you can't upgrade a log bucket and update the bucket's description.

To resolve this failure, send a separate `UpdateBucket` or `UpdateBucketAsync` request with only `analytics_enabled` in `update_mask`, and update other log bucket fields in a separate request.

  * You can't upgrade log buckets in organizations, folders, or billing accounts. You can only upgrade log buckets whose parent is a Google Cloud project.

  * You can't upgrade a log bucket that has already been upgraded or is being upgraded.

Use `GetBucket` or `ListOperations` to determine whether an upgrade has already completed or is in progress.




### Cloud KMS key issues

**Error messages** :

  * `"Not a valid key reference (wrong type): 'KMS_KEY_NAME'"`
  * `"Name "KMS_KEY_NAME" is missing the COMPONENT component. Expected the form projects/[PROJECT_ID]/locations/[ID]/keyRings/[ID]/cryptoKeys/[ID]"`



**Resolution** : Update the log bucket's `cmek_settings.kms_key_name` to a valid Cloud KMS `CryptoKey` resource name before upgrading the bucket. You must update the resource name, not the key version, `CryptoKeyVersion`.

### Invalid argument message

If you see the message `"Request contains an invalid argument."`, then try the following for CMEK-enabled log buckets:

  * Ensure that the Logging service account associated with the bucket's CMEK configuration is initialized.
  * Make sure that the bucket has a positive retention period.



To find the name of the service account, run the following command after you update the log bucket, location, and project IDs:
    
    
    gcloud logging buckets describe LOG_BUCKET_ID --location=LOCATION_ID --project=PROJECT_ID
    

The service account might be in a project, folder, or organization.

## `DEADLINE_EXCEEDED (4)`

Use `UpdateBucketAsync` and poll the returned long-running operation by using the `Operations.GetOperation` method, or call `GetBucket` after the background upgrade finishes.

## `NOT_FOUND (5)`

To resolve these failures, try the following:

  * Verify that the project ID or project number is correct and that the project is active. If the project is pending deletion, restore the project first.
  * Make sure that the specified location is supported by Logging.
  * Verify that the log bucket ID and location exist in the project and that the target bucket isn't `_CloudTrace`.



## `PERMISSION_DENIED (7)`

A permission-denied error indicates that the requested action isn't allowed.

### Missing user permissions

To upgrade a log bucket, make sure that the caller has an Identity and Access Management (IAM) role that includes the `logging.buckets.update` permission (such as `roles/logging.configWriter` or `roles/logging.admin`), and verify that no custom organization policy blocks the update.

### Organization policy restrictions

To resolve the error message `"Request is prohibited by organization's policy. vpcServiceControlsUniqueIdentifier: [ID]"`, make sure that the VPC Service Controls perimeter doesn't restrict the `logging.googleapis.com` service. For more information, see VPC Service Controls perimeter considerations.

### Regional endpoint issues

To resolve permission-denied errors when regional endpoints are specified, send the request to the global endpoint (`logging.googleapis.com`) or to the regional endpoint that matches the log bucket's location.

## `RESOURCE_EXHAUSTED (8)`

To resolve this failure, wait for in-flight provisioning operations to finish and retry with exponential backoff.

## `FAILED_PRECONDITION (9)`

To resolve these failures, try the following:

  * Verify that the log bucket is in the `ACTIVE` state. You can't upgrade a log bucket that is being deleted or that is undergoing an update or provisioning operation.

For information about how to determine the state of a log bucket, see Log bucket state during an upgrade.

  * You can't upgrade a locked log bucket.

  * The generic message `"Precondition check failed."` indicates that the bucket state isn't `ACTIVE`. Wait until an in-progress operations complete and then retry the upgrade.




## `INTERNAL (13)`

**Error messages** :

  * Long-running operation (`Operations.GetOperation`): `"Failed to create analytics enabled bucket."`
  * Cloud Audit Logs and synchronous `UpdateBucket`: `"Internal error encountered."`



**Resolution** : Try the following:

  * For a CMEK-enabled log bucket, verify that the Cloud KMS key is enabled, that the Logging service account associated with the bucket's CMEK configuration has the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on the key, that the key is accessible to BigQuery, and that no organization policy or VPC Service Controls perimeter blocks Cloud KMS access.

To find the name of the service account, run the following command:
        
        gcloud logging buckets describe LOG_BUCKET_ID --location=LOCATION_ID --project=PROJECT_ID
        

The service account might be in a project, folder, or organization.

  * Inspect the existing log views on the bucket (`logging.views.list`) to ensure that their filters are valid, and retry the bucket upgrade.

  * Ensure that the log bucket hasn't been deleted (`DELETE_REQUESTED`) and that no conflicting administrative action is occurring on the bucket, and then retry the upgrade.

  * Retry the log bucket upgrade after transient BigQuery storage dataset or search index creation errors resolve, or once downstream BigQuery, Cloud KMS, or provisioning service availability is restored. If the failure persists, contact Cloud Customer Care.




## `UNAVAILABLE (14)`

If you see the message `"The service is currently unavailable."`, then retry the `UpdateBucketAsync` request with exponential backoff.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
