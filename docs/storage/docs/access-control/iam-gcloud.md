---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-gcloud/
title: IAM permissions for gcloud storage commands \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:04.214200+00:00
---

# IAM permissions for gcloud storage commands  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM permissions for gcloud storage commands Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) permissions required to run [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage). IAM permissions are bundled together to make [roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). You [grant roles to principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).

See the sections below the table for notes on using wildcards, the `--recursive` flag, and the `--billing-project` flag.

Command | Flag | Required IAM Permissions  
---|---|---  
`batch-operations jobs create` |  | `storagebatchoperations.jobs.create`  
`batch-operations jobs cancel` |  | `storagebatchoperations.jobs.cancel`  
`batch-operations jobs delete` |  | `storagebatchoperations.jobs.delete`  
`batch-operations jobs get` |  | `storagebatchoperations.jobs.get`  
`batch-operations jobs list` |  | `storagebatchoperations.jobs.list`  
`buckets add-iam-policy-binding` |  | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`buckets anywhere-caches create` |  | `storage.anywhereCaches.create`  
`buckets anywhere-caches describe` |  | `storage.anywhereCaches.get`  
`buckets anywhere-caches list` |  | `storage.anywhereCaches.list`  
`buckets anywhere-caches update` |  | `storage.anywhereCaches.update`  
`buckets anywhere-caches pause` |  | `storage.anywhereCaches.pause`  
`buckets anywhere-caches resume` |  | `storage.anywhereCaches.resume`  
`buckets anywhere-caches disable` |  | `storage.anywhereCaches.disable`  
`buckets create` |  | `storage.buckets.create`   
`storage.buckets.setIpFilter`14  
`buckets delete` |  | `storage.buckets.delete`  
`buckets describe` |  | `storage.buckets.get`  
`storage.buckets.getIamPolicy`1  
`storage.buckets.getIpFilter`15  
`buckets get-iam-policy` |  | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`buckets list` |  | `storage.buckets.list`  
`storage.buckets.getIamPolicy`1  
`buckets notifications create` |  | `storage.buckets.get`  
`storage.buckets.update`  
`pubsub.topics.get` (for the project containing the Pub/Sub topic)  
`pubsub.topics.create`3 (for the project containing the Pub/Sub topic)  
`pubsub.topics.getIamPolicy` (for Pub/Sub topic receiving notifications)  
`pubsub.topics.setIamPolicy`3 (for Pub/Sub topic receiving notifications)  
`buckets notifications create` | `--skip-topic-setup` | `storage.buckets.get`  
`storage.buckets.update`  
`buckets notifications delete` |  | `storage.buckets.get`  
`storage.buckets.update`  
`buckets notifications describe` |  | `storage.buckets.get`  
`buckets notifications list` |  | `storage.buckets.get`  
`buckets relocate` |  | `storage.buckets.relocate`  
`buckets remove-iam-policy-binding` |  | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`buckets set-iam-policy` |  | `storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`buckets update` |  | `storage.buckets.update`  
`storage.buckets.setIpFilter`14  
`buckets update` | `--no-requester-pays` | `storage.buckets.update`  
`resourcemanager.projects.createBillingAssignment`2  
`buckets update` | `--recovery-point-objective`  
`--rpo`  
`--[no-]uniform-bucket-level-access` | `storage.buckets.get`  
`storage.buckets.update`  
`buckets update` | `--clear-pap`  
`--clear-public-access-prevention`  
`--[no-]pap`  
`--[no-]public-access-prevention` | `storage.buckets.get`  
`storage.buckets.update`  
`storage.buckets.setIamPolicy`  
`cat` |  | `storage.objects.get`  
`cp` |  | `storage.objects.get` (for the source objects)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.list`4 (for the destination bucket)   
`storage.objects.delete`5 (for the destination bucket)   
`storage.buckets.get`12 (for the destination bucket)  
`du` |  | `storage.objects.list`  
`feature-configs create` |  | `storage.featureConfigs.create`  
`feature-configs delete` |  | `storage.featureConfigs.delete`  
`feature-configs describe` |  | `storage.featureConfigs.get`  
`feature-configs list` |  | `storage.featureConfigs.list`  
`feature-configs update` |  | `storage.featureConfigs.update`  
`folders create` |  | `storage.folders.create`  
`folders delete` |  | `storage.folders.delete`  
`folders describe` |  | `storage.folders.get`  
`folders list` |  | `storage.folders.list`  
`folders rename` |  | `storage.folders.rename` (for the source bucket)   
`storage.folders.create` (for the destination bucket)  
`hash` |  | `storage.objects.get`  
`hmac create` |  | `storage.hmacKeys.create`  
`hmac delete` |  | `storage.hmacKeys.delete`  
`hmac describe` |  | `storage.hmacKeys.get`  
`hmac list` |  | `storage.hmacKeys.list`  
`hmac update` |  | `storage.hmacKeys.update`  
`insights dataset-configs create` |  | `storageinsights.datasetConfigs.create`  
`insights dataset-configs create-link` |  | `storageinsights.datasetConfigs.linkDataset`  
`insights dataset-configs delete` |  | `storageinsights.datasetConfigs.delete`  
`insights dataset-configs delete-link` |  | `storageinsights.datasetConfigs.unlinkDataset`  
`insights dataset-configs describe` |  | `storageinsights.datasetConfigs.get`  
`insights dataset-configs list` |  | `storageinsights.datasetConfigs.list`  
`insights dataset-configs update` |  | `storageinsights.datasetConfigs.update`  
`insights inventory-reports create` |  | `storageinsights.reportConfigs.create`  
`insights inventory-reports delete` |  | `storageinsights.reportConfigs.delete`  
`insights inventory-reports details list` |  | `storageinsights.reportDetails.list`  
`insights inventory-reports details describe` |  | `storageinsights.reportDetails.get`  
`insights inventory-reports list` |  | `storageinsights.reportConfigs.list`  
`insights inventory-reports update` |  | `storageinsights.reportConfigs.get`  
`storageinsights.reportConfigs.update`  
`intelligence-configs describe` |  | `storage.intelligenceConfigs.get`  
`intelligence-configs disable` |  | `storage.intelligenceConfigs.update`  
`intelligence-configs enable` |  | `storage.intelligenceConfigs.update`  
`intelligence-configs update` |  | `storage.intelligenceConfigs.update`  
`ls` (for bucket listing) |  | `storage.buckets.list`  
`storage.buckets.getIamPolicy`6  
`ls` (for object listing) |  | `storage.objects.get`7  
`storage.objects.list`  
`storage.objects.getIamPolicy`8  
`ls` | `--buckets` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`6  
`mv` |  | `storage.objects.get` (for the source objects)   
`storage.objects.delete` (for the source bucket)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.list`4 (for the destination bucket)   
`storage.objects.delete`5 (for the destination bucket)   
`storage.buckets.get`12 (for the destination bucket)  
`objects compose` |  | `storage.objects.get`  
`storage.objects.create`  
`storage.objects.delete`9  
`objects describe` |  | `storage.objects.get`  
`storage.objects.getIamPolicy`8  
`objects list` |  | `storage.objects.list`  
`storage.objects.getIamPolicy`8  
`objects update` |  | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
`objects update` | `--storage-class`  
`--encryption-key`  
`--clear-encryption-key` | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.create`  
`storage.objects.delete`  
`objects update` | `--retention-mode`  
`--retain-until`  
`--clear-retention` | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
`storage.objects.setRetention`  
`storage.objects.overrideUnlockedRetention`11  
`operations cancel` |  | `storage.bucketOperations.cancel`  
`operations describe` |  | `storage.bucketOperations.get`  
`operations list` |  | `storage.bucketOperations.list`  
`restore` |  | `storage.objects.create`  
`storage.objects.delete`9  
`storage.objects.restore`  
`restore` | `--async` | `storage.objects.create`  
`storage.objects.delete`13  
`storage.objects.restore`  
`storage.buckets.restore`  
`rm` |  | `storage.buckets.delete`  
`storage.objects.delete`  
`storage.objects.list`  
`rsync` |  | `storage.objects.list` (for the source bucket)   
`storage.objects.get` (for the source objects)   
`storage.objects.list` (for the destination bucket)   
`storage.objects.get` (for the destination bucket)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete`10 (for the destination bucket)   
`storage.buckets.get`16 (for the destination bucket)  
`rsync` | `--dry-run` | `storage.objects.list` (for the source and destination buckets)  
`service-agent` |  | `resourceManager.projects.get`  
`sign-url` |  | None; however, the service account whose key is used as part of this command must have permission to perform the request being encoded into the signed URL.  
  
1This permission is only required if you want IAM policies included in the details.

2This permission is only required if you don't include a billing project in your request. See Requester Pays [Use and access requirements](https://docs.cloud.google.com/storage/docs/requester-pays#requirements) for more information.

3These permissions are not required if the topic already exists and the relevant service account has access to it.

4This permission is only required when the destination in the command contains an object path.

5This permission is only required if you use [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads) or if you don't use the `--no-clobber` flag but insert an object that has the same name as an object that already exists in the bucket.

6This permission is only required if you want IAM policies included in the details.

7This permission is only required if you use the `--fetch-encrypted-object-hashes` flag.

8This permission is only required if you want IAM policies included in the details, and it does not apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

9This permission is only required if the operation creates an object with the same name as an object that already exists in the bucket.

10This permission is only required if you use the `--delete-unmatched-destination-objects` flag or if you insert an object that has the same name as, but [different data](https://docs.cloud.google.com/storage/docs/data-validation#rsync) than, an object that already exists in the bucket.

11This permission is only required if the request also requires you to use the `--override-unlocked-retention` flag.

12This permission is required to perform [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads) if the gcloud CLI property `storage/parallel_composite_upload_compatibility_check` is set to `True`. When this property is set to `True`, the gcloud CLI performs a bucket-level compatibility check before performing the parallel composite upload. If the property `storage/parallel_composite_upload_compatibility_check` or `storage/parallel_composite_upload_enabled` is set to `False`, the compatibility check is skipped and this permission is not required, except for some cases.

13This permission is only required if the request includes the `--allow-overwrite` flag and the operation creates an object with the same name as an object that already exists in the bucket.

14This permission is only required if the request includes the flag `--ip-filter-file` to create, update or delete the IP filtering rules on a bucket.

15This permission is only required if you want to get the bucket's IP filter configuration as part of the response.

16This permission is required when the destination is a bucket root, such as `gs://BUCKET`, regardless of your parallel composite upload settings. When the destination includes a prefix, such as `gs://BUCKET/PREFIX`, running `rsync` requires the `storage.objects.list` permission instead. For more information, see [Troubleshooting for error 403](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads#objects-get-403-troubleshooting).

**Note:** The permissions listed in the previous table allow you to use the commands. Some commands set bucket configurations that won't work without additional permissions. For example, `buckets notification create` requires only `storage.buckets.get` and `storage.buckets.update` to use, but you must have [additional permissions](https://docs.cloud.google.com/storage/docs/reporting-changes#get-required-roles) for the feature to work properly.

## The `--billing-project` top-level flag

If you use the [`--billing-project` global flag](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project) to specify a project that should be billed for your request, you must have `serviceusage.services.use` permission for the project you specify. The `--billing-project` flag is used, for example, when accessing a bucket with [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled.

## Wildcards, regular expressions, and recursive flags

If you use [URI wildcards](https://docs.cloud.google.com/storage/docs/wildcards) or regular expressions to select multiple objects in a command, you must have `storage.objects.list` permission for the bucket containing the objects. Similarly, if you use URI wildcards or regular expressions to select multiple buckets in a command, you must have `storage.buckets.list` permission for the project(s) containing the buckets.

If you use the `--recursive` flag, you must have `storage.objects.list` permission for the relevant bucket, in addition to the permissions required for the specific command you are using.

## What's next

  * [Grant IAM roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) at the project and bucket level.
  * Review [IAM roles that contain Cloud Storage permissions](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
