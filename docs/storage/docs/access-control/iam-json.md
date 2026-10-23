---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-json/
title: IAM permissions for JSON methods \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:33.597564+00:00
---

# IAM permissions for JSON methods  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM permissions for JSON methods Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) permissions required to run each Cloud Storage [JSON method](https://docs.cloud.google.com/storage/docs/json_api/v1) on a given resource. IAM permissions are bundled together to make [roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). You [grant roles to users and groups](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

For additional methods that only apply to buckets with [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled, see the ACL methods table.

Resource | Method | Required IAM Permissions1  
---|---|---  
`AnywhereCache` | `create` | `storage.anywhereCaches.create`  
`AnywhereCache` | `disable` | `storage.anywhereCaches.disable`  
`AnywhereCache` | `get` | `storage.anywhereCaches.get`  
`AnywhereCache` | `list` | `storage.anywhereCaches.list`  
`AnywhereCache` | `pause` | `storage.anywhereCaches.pause`  
`AnywhereCache` | `resume` | `storage.anywhereCaches.resume`  
`AnywhereCache` | `update` | `storage.anywhereCaches.update`  
`Buckets` | `delete` | `storage.buckets.delete`  
`Buckets` | `get` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`2  
`storage.buckets.getIpFilter`13  
`storage.anywhereCaches.get`18  
`Buckets` | `getIamPolicy` | `storage.buckets.getIamPolicy`  
`Buckets` | `insert` | `storage.buckets.create`  
`storage.buckets.enableObjectRetention`3  
`storage.buckets.setIpFilter`14  
`Buckets` | `list` | `storage.buckets.list`  
`storage.buckets.getIamPolicy`2  
`storage.buckets.getIpFilter`13  
`storage.anywhereCaches.list`  
`Buckets` | `lockRetentionPolicy` | `storage.buckets.update`  
`Buckets` | `patch` | `storage.buckets.update`  
`storage.buckets.getIamPolicy`4  
`storage.buckets.setIamPolicy`5  
`storage.buckets.setIpFilter`14  
`storage.buckets.getIpFilter`13  
`Buckets` | `relocate` | `storage.buckets.relocate`  
`Buckets` | `setIamPolicy` | `storage.buckets.setIamPolicy`  
`Buckets` | `testIamPermissions` | None  
`Buckets` | `update` | `storage.buckets.update`  
`storage.buckets.getIamPolicy`4  
`storage.buckets.setIamPolicy`5  
`storage.buckets.setIpFilter`14  
`storage.buckets.getIpFilter`13  
`storage.anywhereCaches.update`  
`DatasetConfigs` | `delete` | `storageinsights.datasetConfigs.delete`  
`DatasetConfigs` | `get` | `storageinsights.datasetConfigs.get`  
`DatasetConfigs` | `insert` | `storageinsights.datasetConfigs.create`  
`DatasetConfigs` | `list` | `storageinsights.datasetConfigs.list`  
`DatasetConfigs` | `linkDataset` | `storageinsights.datasetConfigs.linkDataset`  
`DatasetConfigs` | `unlinkDataset` | `storageinsights.datasetConfigs.unlinkDataset`  
`DatasetConfigs` | `patch` | `storageinsights.datasetConfigs.update`  
`FeatureConfigs` | `create` | `storage.featureConfigs.create`  
`FeatureConfigs` | `delete` | `storage.featureConfigs.delete`  
`FeatureConfigs` | `get` | `storage.featureConfigs.get`  
`FeatureConfigs` | `list` | `storage.featureConfigs.list`  
`FeatureConfigs` | `update` | `storage.featureConfigs.update`  
`Folders` | `get` | `storage.folders.get`  
`Folders` | `insert` | `storage.folders.create`  
`Folders` | `list` | `storage.folders.list`  
`Folders` | `rename` | `storage.folders.rename` (for the source folder)   
`storage.folders.create` (for the destination folder)  
`Folders` | `delete` | `storage.folders.delete`  
`IntelligenceConfig` | `getIntelligenceConfig` | `storage.intelligenceConfigs.get`  
`IntelligenceConfig` | `updateIntelligenceConfig` | `storage.intelligenceConfigs.update`  
`IntelligenceFindings` | `get` | `storage.buckets.viewIntelligenceDetails`  
`IntelligenceFindings` | `list` | `storage.buckets.viewIntelligenceDetails`  
`IntelligenceFindings` | `summarize` | `storage.buckets.viewIntelligenceDetails`  
`IntelligenceFindings.revisions` | `get` | `storage.buckets.viewIntelligenceDetails`  
`IntelligenceFindings.revisions` | `list` | `storage.buckets.viewIntelligenceDetails`  
`Jobs` | `create` | `storagebatchoperations.jobs.create`  
`Jobs` | `get` | `storagebatchoperations.jobs.get`  
`storagebatchoperations.operations.get`  
`Jobs` | `list` | `storagebatchoperations.jobs.list`  
`storagebatchoperations.operations.list`  
`Jobs` | `cancel` | `storagebatchoperations.jobs.cancel`  
`storagebatchoperations.operations.cancel`  
`Jobs` | `delete` | `storagebatchoperations.jobs.delete`  
`ManagedFolders` | `delete` | `storage.managedfolders.delete`  
`storage.managedfolders.setIamPolicy`10  
`ManagedFolders` | `get` | `storage.managedfolders.get`  
`ManagedFolders` | `getIamPolicy` | `storage.managedfolders.getIamPolicy`  
`ManagedFolders` | `insert` | `storage.managedfolders.create`  
`ManagedFolders` | `list` | `storage.managedfolders.list`  
`ManagedFolders` | `update` | `storage.managedfolders.update`  
`ManagedFolders` | `setIamPolicy` | `storage.managedfolders.setIamPolicy`  
`Notifications` | `delete` | `storage.buckets.update`  
`Notifications` | `get` | `storage.buckets.get`  
`Notifications` | `insert` | `storage.buckets.update`  
`Notifications` | `list` | `storage.buckets.get`  
`Objects` | `bulkRestore` | `storage.buckets.restore`  
`storage.objects.create`  
`storage.objects.delete`11  
`storage.objects.restore`  
`storage.objects.setIamPolicy`6,12  
`Objects` | `compose` | `storage.objects.get`  
`storage.objects.create`  
`storage.objects.delete`7  
`storage.objects.getIamPolicy`2,6  
`storage.objects.setRetention`8  
`storage.objects.createContext`19  
`Objects` | `copy` | `storage.objects.get` (for the source bucket)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete` (for the destination bucket)7  
`storage.objects.setRetention` (for the destination bucket)8  
`storage.objects.createContext`19  
`Objects` | `delete` | `storage.objects.delete`  
`Objects` | `get` | `storage.objects.get`  
`storage.objects.getIamPolicy`2,6  
`Objects` | `insert` | `storage.objects.create`  
`storage.objects.delete`7  
`storage.objects.setRetention`8  
`storage.objects.createContext`19  
`Objects` | `list` | `storage.objects.list`  
`storage.objects.getIamPolicy`2,6  
`Objects` | `move` | `storage.objects.move`15 (for the source object)   
`storage.objects.delete`15 (for the source object)   
`storage.objects.get`15 (for the source object)   
`storage.objects.create` (for the destination object)   
`storage.objects.delete`16 (for the destination object)   
`storage.folders.create`17 (for the destination object)  
`Objects` | `patch` | `storage.objects.update`  
`storage.objects.setRetention`8  
`storage.objects.overrideUnlockedRetention`9  
`storage.objects.getIamPolicy`4,6  
`storage.objects.setIamPolicy`5,6  
`storage.objects.createContext`20  
`storage.objects.updateContext`21  
`storage.objects.deleteContext`22  
`Objects` | `restore` | `storage.objects.create`  
`storage.objects.delete`7  
`storage.objects.restore`  
`storage.objects.getIamPolicy`2,6  
`storage.objects.setIamPolicy`6,12  
`Objects` | `rewrite` | `storage.objects.get` (for the source bucket)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete` (for the destination bucket)7  
`storage.objects.setRetention` (for the destination bucket)8  
`storage.objects.createContext`19  
`Objects` | `update` | `storage.objects.update`  
`storage.objects.setRetention`8  
`storage.objects.overrideUnlockedRetention`9  
`storage.objects.getIamPolicy`4,6  
`storage.objects.setIamPolicy`5,6  
`storage.objects.createContext`20  
`storage.objects.updateContext`21  
`storage.objects.deleteContext`22  
`Objects` | `viewFullContext` | `storage.objects.viewFullContext`  
`Objects` | `watchAll` | `storage.buckets.update`  
`Projects.hmacKeys` | `create` | `storage.hmacKeys.create`  
`Projects.hmacKeys` | `delete` | `storage.hmacKeys.delete`  
`Projects.hmacKeys` | `get` | `storage.hmacKeys.get`  
`Projects.hmacKeys` | `list` | `storage.hmacKeys.list`  
`Projects.hmacKeys` | `update` | `storage.hmacKeys.update`  
`Projects.serviceAccount` | `get` | `resourceManager.projects.get`  
`ReportConfigs` | `delete` | `storageinsights.reportConfigs.delete`  
`ReportConfigs` | `get` | `storageinsights.reportConfigs.get`  
`ReportConfigs` | `list` | `storageinsights.reportConfigs.list`  
`ReportConfigs` | `insert` | `storageinsights.reportConfigs.create`  
`ReportConfigs` | `update` | `storageinsights.reportConfigs.update`  
`ReportDetails` | `get` | `storageinsights.reportDetails.get`  
`ReportDetails` | `list` | `storageinsights.reportDetails.list`  
  
1 If you use the `userProject` parameter or the [`x-goog-user-project` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject) in your request, you must have `serviceusage.services.use` permission for the project ID that you specify, in addition to the normal IAM permissions required to make the request.

2 This permission is only required if you want to include ACLs or IAM policies as part of a `full` projection. If you don't have this permission and request a `full` projection, you receive only a partial projection.

3 This permission is only required when the request includes the `enableObjectRetention` query parameter.

4 This permission is only required if you want to include ACLs as part of the response.

5 This permission is required if you want to include ACLs or changes to the [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) setting as part of the request.

6 This permission does not apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

7 This permission is only required if the request causes an object with the same name to be overwritten.

8 This permission is required when the request body includes the `retention` property or when making an [`UPDATE`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/update) request for an object that has an existing retention configuration.

9 This permission is only required when the request includes the query parameter `overrideUnlockedRetention=true`.

10 This permission is only required when the request includes the query parameter `allowNonEmpty=true`.

11 This permission is only required when the request includes the query parameter `allowOverwrite=true` and the request causes an object with the same name to be overwritten.

12 This permission is only required when the request includes the query parameter `copySourceAcl=true`.

13 This permission is only required if you want to include [bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) as part of the [Buckets: get](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request. If you don't have this permission, you receive only a partial projection.

14 This permission is only required if you want to create, list, delete, and update [bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).

15 To move an object within a bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled, you either need `storage.objects.delete` and `storage.objects.get` permissions, or `storage.objects.move` permission if you want to move it without granting read or delete access to the object.

16 This permission is required only if you want to replace an object.

17 This permission is required only if you want to automatically create any missing parent folders.

18 This permission is only required if you want to return caches created with Rapid Cache.

19 This permission is required only if the request includes either a non-empty `destination.contexts.custom` property to compose an object, or a non-empty `contexts.custom` property to copy, insert or rewrite an object.

20 This permission is only required if you want to add contexts to an object.

21 This permission is only required if you want to update contexts of an object.

22 This permission is only required if you want to delete contexts of an object.

#### ACL-related methods

The following table lists the IAM permissions required to run JSON methods that apply specifically to the management of ACLs. These methods only apply to buckets that have [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled.

Resource | Method | Required IAM Permissions1  
---|---|---  
`BucketAccessControls` | `delete` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`BucketAccessControls` | `get` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`BucketAccessControls` | `insert` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`BucketAccessControls` | `list` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`BucketAccessControls` | `patch` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`BucketAccessControls` | `update` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`DefaultObjectAccessControls` | `delete` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`DefaultObjectAccessControls` | `get` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`DefaultObjectAccessControls` | `insert` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`DefaultObjectAccessControls` | `list` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`DefaultObjectAccessControls` | `patch` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`DefaultObjectAccessControls` | `update` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`ObjectAccessControls` | `delete` | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
`ObjectAccessControls` | `get` | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`ObjectAccessControls` | `insert` | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
`ObjectAccessControls` | `list` | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`ObjectAccessControls` | `patch` | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
`ObjectAccessControls` | `update` | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
  
1 If you use the `userProject` parameter or the [`x-goog-user-project` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject) in your request, you must have `serviceusage.services.use` permission for the project ID that you specify, in addition to the normal IAM permissions required to make the request.

## What's next

  * For a list of roles and the permissions they contain, see [IAM Roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

  * [Assign IAM roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) at the project and bucket level.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
