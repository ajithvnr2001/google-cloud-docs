---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/storage/
title: Cloud Storage roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:52.578031+00:00
---

# Cloud Storage roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Storage roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Storage. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Storage roles

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
  
## Cloud Storage permissions

Permission | Included in roles  
---|---  
  
#### `storage.anywhereCaches.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.anywhereCaches.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.anywhereCaches.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.anywhereCaches.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.anywhereCaches.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.anywhereCaches.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.anywhereCaches.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.bucketOperations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.bucketOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.bucketOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [CA Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.admin) (`roles/privateca.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Backup and DR Cloud Storage Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [CA Service Operation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.caManager) (`roles/privateca.caManager`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Edge Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiedgeportal#aiedgeportal.serviceAgent) (`roles/aiedgeportal.serviceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine Standard Environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) (`roles/appengine.serviceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.serviceAgent) (`roles/stream.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.enableObjectRetention`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Bucket Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Backup and DR Cloud Storage Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dataflow Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)  [Dataplex Storage Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataOwner) (`roles/dataplex.storageDataOwner`)  [Dataplex Storage Data Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataReader) (`roles/dataplex.storageDataReader`)  [Dataproc Hub Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.hubAgent) (`roles/dataproc.hubAgent`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  [Storage Insights Collector Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.insightsCollectorService) (`roles/storage.insightsCollectorService`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Edge Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiedgeportal#aiedgeportal.serviceAgent) (`roles/aiedgeportal.serviceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine Standard Environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) (`roles/appengine.serviceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 
  * [AutoML Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.serviceAgent) (`roles/automl.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent) (`roles/cloudoptimization.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataplex Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryServiceAgent) (`roles/dataplex.discoveryServiceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Data Studio Managed Storage Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.managedStorageServiceAgent) (`roles/datastudio.managedStorageServiceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Firebase Telemetry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasetelemetry#firebasetelemetry.serviceAgent) (`roles/firebasetelemetry.serviceAgent`) 
  * [Firestore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#firestore.serviceAgent) (`roles/firestore.serviceAgent`) 
  * [Generative Language Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/generativelanguage#generativelanguage.serviceAgent) (`roles/generativelanguage.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Route Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.serviceAgent) (`roles/routeoptimization.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Google Cloud Security Response Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityResponseServiceAgent) (`roles/securitycenter.securityResponseServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent) (`roles/speech.serviceAgent`) 
  * [Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.serviceAgent) (`roles/stream.serviceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.getIpFilter`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.getObjectInsights`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Storage Insights Collector Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.insightsCollectorService) (`roles/storage.insightsCollectorService`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Bucket Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Edge Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiedgeportal#aiedgeportal.serviceAgent) (`roles/aiedgeportal.serviceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 
  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent) (`roles/speech.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.relocate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.setIpFilter`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Google Cloud Security Response Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityResponseServiceAgent) (`roles/securitycenter.securityResponseServiceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.viewIntelligenceDetails`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.buckets.viewSecurityIntelligenceDetails`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.featureConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.featureConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.featureConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.featureConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.featureConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.folders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.folders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Database Migration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.serviceAgent) (`roles/datamigration.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.folders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Environment and Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectUser) (`roles/composer.environmentAndStorageObjectUser`)  [Environment and Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectViewer) (`roles/composer.environmentAndStorageObjectViewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.folders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Environment and Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectUser) (`roles/composer.environmentAndStorageObjectUser`)  [Environment and Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectViewer) (`roles/composer.environmentAndStorageObjectViewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.folders.rename`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.hmacKeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage HMAC Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.hmacKeyAdmin) (`roles/storage.hmacKeyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `storage.hmacKeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage HMAC Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.hmacKeyAdmin) (`roles/storage.hmacKeyAdmin`)   
  
#### `storage.hmacKeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage HMAC Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.hmacKeyAdmin) (`roles/storage.hmacKeyAdmin`)   
  
#### `storage.hmacKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage HMAC Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.hmacKeyAdmin) (`roles/storage.hmacKeyAdmin`)   
  
#### `storage.hmacKeys.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage HMAC Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.hmacKeyAdmin) (`roles/storage.hmacKeyAdmin`)   
  
#### `storage.intelligenceConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.editor) (`roles/storage.editor`)  [Storage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.viewer) (`roles/storage.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.intelligenceConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Environment and Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectUser) (`roles/composer.environmentAndStorageObjectUser`)  [Environment and Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectViewer) (`roles/composer.environmentAndStorageObjectViewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Environment and Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectUser) (`roles/composer.environmentAndStorageObjectUser`)  [Environment and Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectViewer) (`roles/composer.environmentAndStorageObjectViewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.managedFolders.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.multipartUploads.abort`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.multipartUploads.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.multipartUploads.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.multipartUploads.listParts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Backup and DR Cloud Storage Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`)  [Task Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.worker) (`roles/bigquerymigration.worker`)  [Cloud Deploy Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.jobRunner) (`roles/clouddeploy.jobRunner`)  [Velostrata Storage Access](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.storageaccess) (`roles/cloudmigration.storageaccess`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dataflow Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)  [Dataplex Storage Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataOwner) (`roles/dataplex.storageDataOwner`)  [Dataplex Storage Data Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataWriter) (`roles/dataplex.storageDataWriter`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Express Mode Service Input](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceInput) (`roles/storage.expressModeServiceInput`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Edge Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiedgeportal#aiedgeportal.serviceAgent) (`roles/aiedgeportal.serviceAgent`) 
  * [Vertex AI Agent Sandbox Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentSandboxServiceAgent) (`roles/aiplatform.agentSandboxServiceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [AutoML Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.serviceAgent) (`roles/automl.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent) (`roles/cloudoptimization.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.serviceAgent) (`roles/compute.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Data Studio Managed Storage Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.managedStorageServiceAgent) (`roles/datastudio.managedStorageServiceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Firestore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#firestore.serviceAgent) (`roles/firestore.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Live Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.serviceAgent) (`roles/livestream.serviceAgent`) 
  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Route Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.serviceAgent) (`roles/routeoptimization.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent) (`roles/speech.serviceAgent`) 
  * [Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.serviceAgent) (`roles/stream.serviceAgent`) 
  * [Transcoder Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.serviceAgent) (`roles/transcoder.serviceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.createContext`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Annotation Generator Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.annotationGeneratorService) (`roles/storage.annotationGeneratorService`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Backup and DR Cloud Storage Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`)  [Velostrata Storage Access](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.storageaccess) (`roles/cloudmigration.storageaccess`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dataplex Storage Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataOwner) (`roles/dataplex.storageDataOwner`)  [Dataplex Storage Data Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataWriter) (`roles/dataplex.storageDataWriter`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Storage Express Mode Service Input](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceInput) (`roles/storage.expressModeServiceInput`)  [Storage Express Mode Service Output](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceOutput) (`roles/storage.expressModeServiceOutput`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Edge Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiedgeportal#aiedgeportal.serviceAgent) (`roles/aiedgeportal.serviceAgent`) 
  * [Vertex AI Agent Sandbox Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentSandboxServiceAgent) (`roles/aiplatform.agentSandboxServiceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [AutoML Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.serviceAgent) (`roles/automl.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent) (`roles/cloudoptimization.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Data Studio Managed Storage Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.managedStorageServiceAgent) (`roles/datastudio.managedStorageServiceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Firestore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#firestore.serviceAgent) (`roles/firestore.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Live Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.serviceAgent) (`roles/livestream.serviceAgent`) 
  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Transcoder Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.serviceAgent) (`roles/transcoder.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.deleteContext`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Storage Annotation Generator Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.annotationGeneratorService) (`roles/storage.annotationGeneratorService`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Legacy Object Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectReader) (`roles/storage.legacyObjectReader`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Container Registry -> Artifact Registry Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.containerRegistryMigrationAdmin) (`roles/artifactregistry.containerRegistryMigrationAdmin`)  [Backup and DR Cloud Storage Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`)  [Task Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.worker) (`roles/bigquerymigration.worker`)  [Cloud Deploy Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.jobRunner) (`roles/clouddeploy.jobRunner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Velostrata Storage Access](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.storageaccess) (`roles/cloudmigration.storageaccess`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Environment and Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectUser) (`roles/composer.environmentAndStorageObjectUser`)  [Environment and Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectViewer) (`roles/composer.environmentAndStorageObjectViewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dataflow Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)  [Dataplex Storage Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataOwner) (`roles/dataplex.storageDataOwner`)  [Dataplex Storage Data Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataReader) (`roles/dataplex.storageDataReader`)  [Dataproc Hub Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.hubAgent) (`roles/dataproc.hubAgent`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Storage Annotation Generator Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.annotationGeneratorService) (`roles/storage.annotationGeneratorService`)  [Storage Express Mode Service Output](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceOutput) (`roles/storage.expressModeServiceOutput`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  [Wiz Serverless & Container Image Registry Scanner](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.serverlessImageRegistryScanner) (`roles/wiz.serverlessImageRegistryScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Edge Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiedgeportal#aiedgeportal.serviceAgent) (`roles/aiedgeportal.serviceAgent`) 
  * [Vertex AI Agent Sandbox Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentSandboxServiceAgent) (`roles/aiplatform.agentSandboxServiceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Extension Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionServiceAgent) (`roles/aiplatform.extensionServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [AutoML Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.serviceAgent) (`roles/automl.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent) (`roles/cloudoptimization.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.serviceAgent) (`roles/compute.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [[Deprecated] Kubernetes Engine Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.nodeServiceAgent) (`roles/container.nodeServiceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Registry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerregistry#containerregistry.ServiceAgent) (`roles/containerregistry.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [Database Migration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.serviceAgent) (`roles/datamigration.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataplex Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryServiceAgent) (`roles/dataplex.discoveryServiceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Data Studio Managed Storage Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.managedStorageServiceAgent) (`roles/datastudio.managedStorageServiceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Enterprise Knowledge Graph Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.serviceAgent) (`roles/enterpriseknowledgegraph.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Firebase Telemetry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasetelemetry#firebasetelemetry.serviceAgent) (`roles/firebasetelemetry.serviceAgent`) 
  * [Firestore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#firestore.serviceAgent) (`roles/firestore.serviceAgent`) 
  * [Generative Language Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/generativelanguage#generativelanguage.serviceAgent) (`roles/generativelanguage.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Live Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.serviceAgent) (`roles/livestream.serviceAgent`) 
  * [Managed Flink Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.serviceAgent) (`roles/managedflink.serviceAgent`) 
  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Migration Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.serviceAgent) (`roles/migrationcenter.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Route Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.serviceAgent) (`roles/routeoptimization.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent) (`roles/speech.serviceAgent`) 
  * [Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.serviceAgent) (`roles/stream.serviceAgent`) 
  * [Transcoder Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.serviceAgent) (`roles/transcoder.serviceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Registry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerregistry#containerregistry.ServiceAgent) (`roles/containerregistry.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Container Registry -> Artifact Registry Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.containerRegistryMigrationAdmin) (`roles/artifactregistry.containerRegistryMigrationAdmin`)  [Backup and DR Cloud Storage Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`)  [Task Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.orchestrator) (`roles/bigquerymigration.orchestrator`)  [Task Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.worker) (`roles/bigquerymigration.worker`)  [Cloud Deploy Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.jobRunner) (`roles/clouddeploy.jobRunner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Velostrata Storage Access](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.storageaccess) (`roles/cloudmigration.storageaccess`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Environment and Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectUser) (`roles/composer.environmentAndStorageObjectUser`)  [Environment and Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectViewer) (`roles/composer.environmentAndStorageObjectViewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dataplex Storage Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataOwner) (`roles/dataplex.storageDataOwner`)  [Dataplex Storage Data Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataReader) (`roles/dataplex.storageDataReader`)  [Dataproc Hub Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.hubAgent) (`roles/dataproc.hubAgent`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Storage Annotation Generator Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.annotationGeneratorService) (`roles/storage.annotationGeneratorService`)  [Storage Express Mode Service Input](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceInput) (`roles/storage.expressModeServiceInput`)  [Storage Express Mode Service Output](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceOutput) (`roles/storage.expressModeServiceOutput`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Wiz Data Security Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.dataSecurityScanner) (`roles/wiz.dataSecurityScanner`)  [Wiz Serverless & Container Image Registry Scanner](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.serverlessImageRegistryScanner) (`roles/wiz.serverlessImageRegistryScanner`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Agent Sandbox Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentSandboxServiceAgent) (`roles/aiplatform.agentSandboxServiceAgent`) 
  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [AutoML Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.serviceAgent) (`roles/automl.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent) (`roles/cloudoptimization.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.serviceAgent) (`roles/compute.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [[Deprecated] Kubernetes Engine Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.nodeServiceAgent) (`roles/container.nodeServiceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Registry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerregistry#containerregistry.ServiceAgent) (`roles/containerregistry.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [Database Migration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.serviceAgent) (`roles/datamigration.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataplex Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryServiceAgent) (`roles/dataplex.discoveryServiceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Data Studio Managed Storage Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.managedStorageServiceAgent) (`roles/datastudio.managedStorageServiceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Enterprise Knowledge Graph Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.serviceAgent) (`roles/enterpriseknowledgegraph.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Firestore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#firestore.serviceAgent) (`roles/firestore.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Live Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.serviceAgent) (`roles/livestream.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Route Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.serviceAgent) (`roles/routeoptimization.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 
  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 
  * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent) (`roles/speech.serviceAgent`) 
  * [Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.serviceAgent) (`roles/stream.serviceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.move`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.overrideUnlockedRetention`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.setRetention`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Velostrata Storage Access](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.storageaccess) (`roles/cloudmigration.storageaccess`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dataplex Storage Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataOwner) (`roles/dataplex.storageDataOwner`)  [Dataplex Storage Data Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.storageDataWriter) (`roles/dataplex.storageDataWriter`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Storage Annotation Generator Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.annotationGeneratorService) (`roles/storage.annotationGeneratorService`)  [Storage Express Mode Service Input](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeServiceInput) (`roles/storage.expressModeServiceInput`)  [Storage Express Mode User Access](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.expressModeUserAccess) (`roles/storage.expressModeUserAccess`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Batch Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent) (`roles/aiplatform.batchPredictionServiceAgent`) 
  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 
  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Vertex AI Model Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent) (`roles/aiplatform.modelMonitoringServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Vertex AI Tuning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent) (`roles/aiplatform.tuningServiceAgent`) 
  * [AutoML Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.serviceAgent) (`roles/automl.serviceAgent`) 
  * [Recommendations AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent) (`roles/automlrecommendations.serviceAgent`) 
  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent) (`roles/cloudoptimization.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.serviceAgent) (`roles/compute.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Cloud Storage for Firebase Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent) (`roles/firebasestorage.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Live Stream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.serviceAgent) (`roles/livestream.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Retail Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.serviceAgent) (`roles/retail.serviceAgent`) 
  * [Route Optimization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.serviceAgent) (`roles/routeoptimization.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent) (`roles/speech.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storage.objects.updateContext`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Folder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`)  [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)  [Storage Legacy Object Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`)  [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)  [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)  [Environment and Storage Object Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Storage Annotation Generator Service](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.annotationGeneratorService) (`roles/storage.annotationGeneratorService`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Extension Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent) (`roles/aiplatform.extensionCustomCodeServiceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
