---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-roles/
title: IAM roles for Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:36.617777+00:00
---

# IAM roles for Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM roles for Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about Identity and Access Management (IAM) roles and permissions for Cloud Storage.

## Predefined roles

The following table describes [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) roles that are associated with Cloud Storage and lists the permissions that are contained in each role. Unless otherwise noted, these roles can be applied either to projects, buckets, or managed folders. However, you can [grant legacy roles only to individual buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

To learn how to control access to buckets, see [use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). To learn how to control access to managed folders, see [use IAM for managed folders](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders).

Role | Permissions  
---|---  
  
#### Storage Admin 

(`roles/storage.admin`) Grants full control of objects and buckets.  When applied to an individual **bucket** , control applies only to the specified bucket and objects within the bucket.  Lowest-level resources where you can grant this role:

  * Bucket 

|  `cloudaicompanion.instances.completeTask` `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `firebase.projects.get` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`orgpolicy.policy.get` `recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
#### Storage Bucket Viewer Beta

(`roles/storage.bucketViewer`) Grants permission to view buckets and their metadata, excluding IAM policies.  Lowest-level resources where you can grant this role:

  * Bucket

|  `storage.buckets.get` `storage.buckets.list`  
  
#### Storage Editor 

(`roles/storage.editor`) Editor role for storage  Lowest-level resources where you can grant this role:

  * Managed folder

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.list` `storage.buckets.listEffectiveTags` `storage.buckets.listTagBindings` `storage.buckets.viewIntelligenceDetails` `storage.buckets.viewSecurityIntelligenceDetails` `storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.hmacKeys.*`

  * `storage.hmacKeys.create`
  * `storage.hmacKeys.delete`
  * `storage.hmacKeys.get`
  * `storage.hmacKeys.list`
  * `storage.hmacKeys.update`

`storage.intelligenceConfigs.get`  
  
#### Storage Folder Admin 

(`roles/storage.folderAdmin`) Grants full control over folders and objects, including listing, creating, viewing, and deleting objects.  Lowest-level resources where you can grant this role:

  * Managed folder

|  `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

  
  
#### Storage Legacy Bucket Owner 

(`roles/storage.legacyBucketOwner`) Grants permission to create, overwrite, and delete objects; list objects in a bucket and read object metadata, excluding allow policies, when listing; and read and edit bucket metadata, including allow policies.  Use of this role is also reflected in the bucket's ACLs. For more information, see [ IAM relation to ACLs](https://docs.cloud.google.com/storage/docs/access-control/iam#acls).  Lowest-level resources where you can grant this role:

  * Bucket 

|  `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.createTagBinding` `storage.buckets.deleteTagBinding` `storage.buckets.enableObjectRetention` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.getIpFilter` `storage.buckets.listEffectiveTags` `storage.buckets.listTagBindings` `storage.buckets.relocate` `storage.buckets.restore` `storage.buckets.setIamPolicy` `storage.buckets.setIpFilter` `storage.buckets.update` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.createContext` `storage.objects.delete` `storage.objects.deleteContext` `storage.objects.list` `storage.objects.restore` `storage.objects.setRetention` `storage.objects.updateContext`  
  
#### Storage Legacy Bucket Reader 

(`roles/storage.legacyBucketReader`) Grants permission to list a bucket's contents and read bucket metadata, excluding allow policies. Also grants permission to read object metadata, excluding allow policies, when listing objects.  Use of this role is also reflected in the bucket's ACLs. For more information, see [ IAM relation to ACLs](https://docs.cloud.google.com/storage/docs/access-control/iam#acls).  Lowest-level resources where you can grant this role:

  * Bucket 

|  `storage.buckets.get` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.multipartUploads.list` `storage.objects.list`  
  
#### Storage Legacy Bucket Writer 

(`roles/storage.legacyBucketWriter`) Grants permission to create, overwrite, and delete objects; list objects in a bucket and read object metadata, excluding allow policies, when listing; and read bucket metadata, excluding allow policies.  Use of this role is also reflected in the bucket's ACLs. For more information, see [ IAM relation to ACLs](https://docs.cloud.google.com/storage/docs/access-control/iam#acls).  Lowest-level resources where you can grant this role:

  * Bucket 

|  `storage.buckets.get` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.createContext` `storage.objects.delete` `storage.objects.list` `storage.objects.restore` `storage.objects.setRetention`  
  
#### Storage Legacy Object Owner 

(`roles/storage.legacyObjectOwner`) Grants permission to view and edit objects and their metadata, including ACLs.  Lowest-level resources where you can grant this role:

  * Managed folder 

|  `storage.objects.createContext` `storage.objects.deleteContext` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.overrideUnlockedRetention` `storage.objects.setIamPolicy` `storage.objects.setRetention` `storage.objects.update` `storage.objects.updateContext`  
  
#### Storage Legacy Object Reader 

(`roles/storage.legacyObjectReader`) Grants permission to view objects and their metadata, excluding ACLs.  Lowest-level resources where you can grant this role:

  * Managed folder 

|  `storage.objects.get`  
  
#### Storage Object Admin 

(`roles/storage.objectAdmin`) Grants full control of objects, including listing, creating, viewing, and deleting objects.  Lowest-level resources where you can grant this role:

  * Managed folder 

|  `monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

  
  
#### Storage Object Creator 

(`roles/storage.objectCreator`) Allows users to create objects. Does not give permission to view, delete, or overwrite objects.  Lowest-level resources where you can grant this role:

  * Managed folder 

|  `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.create` `storage.managedFolders.create` `storage.multipartUploads.abort` `storage.multipartUploads.create` `storage.multipartUploads.listParts` `storage.objects.create` `storage.objects.createContext`  
  
#### Storage Object User 

(`roles/storage.objectUser`) Access to create, read, update and delete objects and multipart uploads in GCS.  Lowest-level resources where you can grant this role:

  * Managed folder

|  `monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.createContext` `storage.objects.delete` `storage.objects.deleteContext` `storage.objects.get` `storage.objects.list` `storage.objects.move` `storage.objects.restore` `storage.objects.update` `storage.objects.updateContext`  
  
#### Storage Object Viewer 

(`roles/storage.objectViewer`) Grants access to view objects and their metadata, excluding ACLs. Can also list the objects in a bucket.  Lowest-level resources where you can grant this role:

  * Managed folder 

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.objects.get` `storage.objects.list`  
  
#### Storage Viewer 

(`roles/storage.viewer`) Viewer role for storage  Lowest-level resources where you can grant this role:

  * Managed folder

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.buckets.list` `storage.buckets.listEffectiveTags` `storage.buckets.listTagBindings` `storage.buckets.viewIntelligenceDetails` `storage.buckets.viewSecurityIntelligenceDetails` `storage.featureConfigs.get` `storage.featureConfigs.list` `storage.folders.get` `storage.folders.list` `storage.hmacKeys.get` `storage.hmacKeys.list` `storage.intelligenceConfigs.get`  
  
#### Storage Annotation Generator Service Beta

(`roles/storage.annotationGeneratorService`) Grants all permissions needed to generate annotations for objects in a bucket.  Lowest-level resources where you can grant this role:

  * Managed folder

|  `storage.objects.createContext` `storage.objects.deleteContext` `storage.objects.get` `storage.objects.list` `storage.objects.update` `storage.objects.updateContext`  
  
#### Storage Express Mode Service Input Beta

(`roles/storage.expressModeServiceInput`) Grants permission to Express Mode service accounts at a managed folder so they can create objects but not read them on input folders.  Lowest-level resources where you can grant this role:

  * Managed folder

|  `storage.objects.create` `storage.objects.delete` `storage.objects.list` `storage.objects.update`  
  
#### Storage Express Mode Service Output Beta

(`roles/storage.expressModeServiceOutput`) Grants permission to Express Mode service accounts at a managed folder so they can read objects but not write them on output folders.  Lowest-level resources where you can grant this role:

  * Managed folder

|  `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
#### Storage Express Mode User Access Beta

(`roles/storage.expressModeUserAccess`) Grants permission to Express Mode accounts at the project level so they can read, list, create and delete any object in any of their buckets in Express Mode.  Lowest-level resources where you can grant this role:

  * Project

|  `orgpolicy.policy.get` `storage.buckets.get` `storage.buckets.list` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.restore` `storage.objects.update`  
  
#### Storage HMAC Key Admin 

(`roles/storage.hmacKeyAdmin`) Full control of Cloud Storage HMAC keys.  Lowest-level resources where you can grant this role:

  * Project

|  `firebase.projects.get` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.hmacKeys.*`

  * `storage.hmacKeys.create`
  * `storage.hmacKeys.delete`
  * `storage.hmacKeys.get`
  * `storage.hmacKeys.list`
  * `storage.hmacKeys.update`

  
  
#### Storage Insights Collector Service 

(`roles/storage.insightsCollectorService`) Read-only access to Cloud Storage Inventory metadata for Storage Insights.  Lowest-level resources where you can grant this role:

  * Bucket

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.buckets.get` `storage.buckets.getObjectInsights`  
**Note:** Consider the following for permissions: 

  * The `orgpolicy.policy.get` permission allows principals to know the [organization policy constraints](https://docs.cloud.google.com/storage/docs/org-policy-constraints) that a project is subject to. This permission is only effective if the role is [granted at the project level](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) or above.
  * For more information about the `resourcemanager.projects.*` permissions, see [Access control for projects with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj).
  * The `storagebatchoperations.jobs.*` and `storagebatchoperations.operations.*` permissions allow you to [create and manage storage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs). These permissions are effective only if the role is [granted at the project level](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).



### Predefined Storage Insights roles

The following table describes [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam) roles that are associated with Storage Insights and lists the permissions that are contained in each role.

Role | Permissions  
---|---  
  
#### Storage Insights Admin 

(`roles/storageinsights.admin`) Full access to Storage Insights resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storageinsights.*`

  * `storageinsights.datasetConfigs.create`
  * `storageinsights.datasetConfigs.delete`
  * `storageinsights.datasetConfigs.get`
  * `storageinsights.datasetConfigs.linkDataset`
  * `storageinsights.datasetConfigs.list`
  * `storageinsights.datasetConfigs.unlinkDataset`
  * `storageinsights.datasetConfigs.update`
  * `storageinsights.locations.get`
  * `storageinsights.locations.list`
  * `storageinsights.operations.cancel`
  * `storageinsights.operations.delete`
  * `storageinsights.operations.get`
  * `storageinsights.operations.list`
  * `storageinsights.reportConfigs.create`
  * `storageinsights.reportConfigs.delete`
  * `storageinsights.reportConfigs.get`
  * `storageinsights.reportConfigs.list`
  * `storageinsights.reportConfigs.update`
  * `storageinsights.reportDetails.get`
  * `storageinsights.reportDetails.list`

  
  
#### Storage Insights Viewer 

(`roles/storageinsights.viewer`) Read-only access to Storage Insights resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storageinsights.datasetConfigs.get` `storageinsights.datasetConfigs.list` `storageinsights.locations.*`

  * `storageinsights.locations.get`
  * `storageinsights.locations.list`

`storageinsights.operations.get` `storageinsights.operations.list` `storageinsights.reportConfigs.get` `storageinsights.reportConfigs.list` `storageinsights.reportDetails.*`

  * `storageinsights.reportDetails.get`
  * `storageinsights.reportDetails.list`

  
  
#### Storage Insights Analyst 

(`roles/storageinsights.analyst`) Data access to Storage Insights.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storageinsights.datasetConfigs.get` `storageinsights.datasetConfigs.linkDataset` `storageinsights.datasetConfigs.list` `storageinsights.datasetConfigs.unlinkDataset` `storageinsights.locations.*`

  * `storageinsights.locations.get`
  * `storageinsights.locations.list`

`storageinsights.operations.get` `storageinsights.operations.list` `storageinsights.reportConfigs.get` `storageinsights.reportConfigs.list` `storageinsights.reportDetails.*`

  * `storageinsights.reportDetails.get`
  * `storageinsights.reportDetails.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### StorageInsights Service Agent 

(`roles/storageinsights.serviceAgent`) Permissions for Insights to write reports into customer project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `serviceusage.services.use` `storageinsights.reportDetails.list`  
  
## Basic roles

**Note:** You should minimize the use of basic roles if possible, and in production environments, don't grant basic roles unless there is no alternative. Basic roles contain a wide range of permissions across all Google Cloud services and have potentially surprising behavior in Cloud Storage as described in this section.

Basic roles are roles that existed prior to IAM. These roles have unique characteristics:

  * Basic roles can only be granted for an entire project, not for individual buckets within the project. Like other roles that you grant for a project, basic roles apply to all buckets and objects in the project.

  * Basic roles contain additional permissions for other Google Cloud services that are not covered in this section. See [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for a general discussion of the permissions that basic roles grant.

  * Each basic role has a [_convenience value_](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values) that lets you use the basic role as if it were a group. When used in this way, any principal that has the basic role is considered to be part of the group. Everyone in the group gets additional access for resources based on the access the convenience value has.

    * Convenience values can be used when granting roles for buckets.

    * Convenience values can be used when setting ACLs on objects.

  * Basic roles don't intrinsically give all of the access to Cloud Storage resources that their names imply. Instead, they give a portion of the expected access intrinsically and the rest of the expected access through the use of convenience values. Because convenience values can be manually added or removed like any other IAM principal, it is possible to revoke access that principals might otherwise expect to have.

For a discussion of additional access that principals with basic roles typically gain due to convenience values, see modifiable behavior.




### Intrinsic permissions

The following table describes the Cloud Storage permissions that are always associated with each basic role.

Role | Description | Cloud Storage Permissions  
---|---|---  
**Viewer** (`roles/viewer`) | Grants permission to list buckets in the project; view bucket metadata when listing (excluding ACLs); and list and get HMAC keys in the project. | `storage.buckets.getIpFilter`  
`storage.buckets.list`  
`storage.hmacKeys.get`  
`storage.hmacKeys.list`  
**Editor** (`roles/editor`) | Grants permission to create, list, and delete buckets in the project; view bucket metadata when listing (excluding ACLs); and control HMAC keys in the project. | `storage.buckets.create`  
`storage.buckets.delete`  
`storage.buckets.getIpFilter`  
`storage.buckets.list`  
`storage.hmacKeys.*`  
**Owner** (`roles/owner`) | Grants permission to create, list, and delete buckets in the project; view bucket metadata when listing (excluding ACLs); create, delete, and list tag bindings; and control HMAC keys in the project; Enable, disable, update, and get the Storage Intelligence configuration on a project, a folder, or an organization. Within Google Cloud more generally, principals with this role can perform administrative tasks such as changing principals' roles for the project or changing billing. | `storage.buckets.create`  
`storage.buckets.delete`  
`storage.buckets.list`  
`storage.buckets.createTagBinding`  
`storage.buckets.deleteTagBinding`  
`storage.buckets.getIpFilter`  
`storage.buckets.listEffectiveTags`  
`storage.buckets.listTagBindings`  
`storage.buckets.setIpFilter`  
`storage.hmacKeys.*`  
`storage.intelligenceConfigs.get`  
`storage.intelligenceConfigs.update`  
  
### Modifiable behavior

Principals granted basic roles often have additional access to a project's buckets and objects due to [_convenience values_](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values). When a bucket is created, convenience values are granted certain bucket-level access, but you can later edit your bucket IAM policies and your object ACLs to remove or change the access.

When you create a bucket that has [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled, the following access is granted via convenience values:

  * Principals granted `roles/viewer` gain the `roles/storage.legacyBucketReader` and `roles/storage.legacyObjectReader` roles for the bucket.

  * Principals granted `roles/editor` gain the `roles/storage.legacyBucketOwner` and `roles/storage.legacyObjectOwner` roles for the bucket.

  * Principals granted `roles/owner` gain the `roles/storage.legacyBucketOwner` and `roles/storage.legacyObjectOwner` roles for the bucket.




When you create a bucket that does not have uniform bucket-level access enabled, the following access is granted using convenience values:

  * Principals granted `roles/viewer` gain the `roles/storage.legacyBucketReader` role for the bucket.

  * Principals granted `roles/editor` gain the `roles/storage.legacyBucketOwner` role for the bucket.

  * Principals granted `roles/owner` gain the `roles/storage.legacyBucketOwner` role for the bucket.

  * Additionally, the bucket has a [default object Access Control List (ACL)](https://docs.cloud.google.com/storage/docs/access-control/lists#defaultobjects). This default ACL is often applied to new objects in the bucket and often grants additional access to convenience values.




## Custom roles

You might want to define your own roles which contain bundles of permissions that you specify. To support this, IAM offers [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## What's next

  * [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to control access to buckets and objects.

  * Learn about each [IAM permission for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions).

  * See available [IAM references for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-reference), such as which IAM permissions allow users to perform actions with various tools and APIs.

  * For a reference of other Google Cloud roles, see [Understanding Roles](https://docs.cloud.google.com/iam/docs/understanding-roles).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
