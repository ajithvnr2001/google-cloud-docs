---
url: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage/
title: Configure a Cloud Storage bucket \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:30:06.181568+00:00
---

# Configure a Cloud Storage bucket  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage lets you store and retrieve any amount of data world-wide at any time. You can use Cloud Storage for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download. For more information, see [Product overview of Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction).

This document describes the connections and parameters you can configure when using App Design Center to create a Cloud Storage bucket. The configuration parameters are based on the [terraform-google-cloud-storage](https://github.com/terraform-google-modules/terraform-google-cloud-storage/tree/main/modules/simple_bucket) Terraform module.

## Component connections

The following table includes the components that you can connect to a Cloud Storage bucket, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can control bucket objects, including listing, creating, viewing, and deleting objects.
  * The `roles/storage.objectAdmin` role is assigned to the Compute Engine instance template service account.

| [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)  
[service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can manage objects in the Cloud Storage bucket.
  * The service account IAM information is added to the Cloud Storage bucket.
  * The `roles/storage.objectAdmin` role is assigned to the service account.

| [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can manage objects in the Cloud Storage bucket.
  * The Cloud Run service account IAM information is added to the Cloud Storage bucket.
  * The `roles/storage.objectAdmin` role is assigned to the Cloud Run service account.

| [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services)  
[Pub/Sub](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub) | 

  * The Pub/Sub subscription can write messages to the Cloud Storage bucket.
  * The Cloud Storage bucket information is added to the Pub/Sub subscription fields.

| [Cloud Storage subscriptions](https://docs.cloud.google.com/pubsub/docs/cloudstorage)  
  
## Required configuration parameters

If your template includes a Cloud Storage component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Cloud Storage resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | [location](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#location) | [Bucket locations](https://docs.cloud.google.com/storage/docs/locations)  
**Name** | [name](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#name) | [Bucket Names](https://docs.cloud.google.com/storage/docs/buckets#naming)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Storage Class** | [storageClass](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#storageClass) | [Storage Classes](https://docs.cloud.google.com/storage/docs/storage-classes)  
| **Bucket Policy Only** | [iamConfiguration.uniformBucketLevelAccess](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#iamConfiguration.uniformBucketLevelAccess) | [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access)  
| **Versioning** | [versioning.enabled](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#versioning.enabled) | [Object versioning](https://docs.cloud.google.com/storage/docs/object-versioning)  
| **Autoclass** | [autoclass.enabled](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#autoclass.enabled) | [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass)  
Retention Policy | **Is Locked** | [retentionPolicy.isLocked](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#retentionPolicy.isLocked) | [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock)  
**Retention period** | [retentionPolicy.retentionPeriod](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#retentionPolicy.retentionPeriod) | [Retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy)  
Encryption | **Default KMS Key Name** | [encryption.defaultKmsKeyName](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#encryption.defaultKmsKeyName) | [Use customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys)  
Lifecycle Rules | **Type** | [lifecycle.rule[].action.type](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.action.type) | [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)  
**Storage Class** | [lifecycle.rule[].action.storageClass](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.action.storageClass) | [setStorageClass](https://docs.cloud.google.com/storage/docs/lifecycle#setstorageclass)  
**Age** | [lifecycle.rule[].condition.age](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.age) | [age](https://docs.cloud.google.com/storage/docs/lifecycle#age)  
**Send Age If Zero** | [send_age_if_zero](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#send_age_if_zero-1) | [lifecycle_rules](https://github.com/terraform-google-modules/terraform-google-cloud-storage/tree/main/modules/simple_bucket#inputs)  
**Created Before** | [lifecycle.rule[].condition.createdBefore](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.createdBefore) | [createdBefore](https://docs.cloud.google.com/storage/docs/lifecycle#createdbefore)  
**With State** | [with_state](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#with_state-1) | [lifecycle_rules](https://github.com/terraform-google-modules/terraform-google-cloud-storage/tree/main/modules/simple_bucket#inputs)  
**Matches Storage Class** | [lifecycle.rule[].condition.matchesStorageClass[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.matchesStorageClass) | [matchesStorageClass](https://docs.cloud.google.com/storage/docs/lifecycle#matchesstorageclass)  
**Matches Prefix** | [lifecycle.rule[].condition.matchesPrefix[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.matchesPrefix) | [matchesPrefix and matchesSuffix](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix)  
**Matches Suffix** | [lifecycle.rule[].condition.matchesSuffix[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.matchesSuffix) | [matchesPrefix and matchesSuffix](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix)  
**Num Newer Versions** | [lifecycle.rule[].condition.numNewerVersions](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.numNewerVersions) | [numNewerVersions](https://docs.cloud.google.com/storage/docs/lifecycle#numnewerversions)  
**Custom Time Before** | [lifecycle.rule[].condition.customTimeBefore](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.customTimeBefore) | [customTimeBefore](https://docs.cloud.google.com/storage/docs/lifecycle#customtimebefore)  
**Days Since Custom Time** | [lifecycle.rule[].condition.daysSinceCustomTime](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.daysSinceCustomTime) | [daysSinceCustomTime](https://docs.cloud.google.com/storage/docs/lifecycle#dayssincecustomtime)  
**Days Since Noncurrent Time** | [lifecycle.rule[].condition.daysSinceNoncurrentTime](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.daysSinceNoncurrentTime) | [daysSinceNoncurrentTime](https://docs.cloud.google.com/storage/docs/lifecycle#dayssincenoncurrenttime)  
**Noncurrent Time Before** | [lifecycle.rule[].condition.noncurrentTimeBefore](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle.rule.condition.noncurrentTimeBefore) | [noncurrentTimeBefore](https://docs.cloud.google.com/storage/docs/lifecycle#noncurrenttimebefore)  
Internal Encryption Config | **Create Encryption Key** | To create a Cloud Key Management Service key ring and key, select the checkbox. | [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)  
**Prevent Destroy** | To prevent the destruction of the Cloud KMS key, select the checkbox. | [Key versions and locked objects](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#locked-objects)  
**Key Destroy Scheduled Duration** | [destroyScheduledDuration](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.destroy_scheduled_duration) | [Key versions and locked objects](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#locked-objects)  
**Key Rotation Period** | [rotationPeriod](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period) | [Key rotation](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#key-rotation)  
| **Force Destroy** | To delete all contained objects when you delete a bucket, select the checkbox. | [force_destroy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket.html#force_destroy-1)  
IAM Members | **Role** | The collection of permissions that you want to grant. | [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#rest-apis)  
**Member** | The principals that are granted the role. | [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#rest-apis)  
Labels | **Key** | [labels](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#labels) | [Tags and labels](https://docs.cloud.google.com/storage/docs/tags-and-labels)  
**Value** | [labels](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#labels) | [Tags and labels](https://docs.cloud.google.com/storage/docs/tags-and-labels)  
Custom Placement Config | **Data Locations** | [customPlacementConfig.dataLocations[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#dataLocations) | [Dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr)  
CORS | **Origin** | [cors[].origin[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#cors.origin) | [Cross-origin resource sharing (CORS)](https://docs.cloud.google.com/storage/docs/cross-origin)  
**Method** | [cors[].method[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#cors.method) | [How CORS works](https://docs.cloud.google.com/storage/docs/cross-origin#overview)  
**Response Header** | [cors[].responseHeader[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#cors.responseHeader) | [Components of a CORS configuration](https://docs.cloud.google.com/storage/docs/cross-origin#cors-components)  
**Max Age Seconds** | [cors[].maxAgeSeconds[]](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#cors.maxAgeSeconds) | [Components of a CORS configuration](https://docs.cloud.google.com/storage/docs/cross-origin#cors-components)  
| **Log Bucket** | [logging.logBucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#logging.logBucket) | [Usage logs & storage logs](https://docs.cloud.google.com/storage/docs/access-logs)  
| **Log Object Prefix** | [logging.logObjectPrefix](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#logging.logObjectPrefix) | [Usage logs & storage logs](https://docs.cloud.google.com/storage/docs/access-logs)  
Website | **Main Page Suffix** | [website.mainPageSuffix](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#website.mainPageSuffix) | [Recommended: assign specialty pages](https://docs.cloud.google.com/storage/docs/hosting-static-website#specialty-pages)  
**Not Found Page** | [website.notFoundPage](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#website.notFoundPage) | [Recommended: assign specialty pages](https://docs.cloud.google.com/storage/docs/hosting-static-website#specialty-pages)  
| **Public Access Prevention** | [iamConfiguration.publicAccessPrevention](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#iamConfiguration.publicAccessPrevention) | [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)  
Soft Delete Policy | **Retention Duration Seconds** | [softDeletePolicy.retentionDurationSeconds](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#softDeletePolicy.retentionDurationSeconds) | [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
