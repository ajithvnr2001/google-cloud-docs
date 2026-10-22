---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-krm-api/
title: Storage KRM API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:31.074593+00:00
---

# Storage KRM API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-krm-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Storage KRM API Stay organized with collections  Save and categorize content based on your preferences. 

## object.gdc.goog/v1alpha1

Package v1alpha1 contains API Schema definitions for the object.gdc.goog v1alpha1 API group

### Bucket

Bucket is the Schema for the buckets API

_Appears in:_ \- BucketList

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1alpha1`  
`kind` _string_ | `Bucket`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketSpec_ |   
`status` _BucketStatus_ |   
  
### BucketList

BucketList contains a list of Bucket

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1alpha1`  
`kind` _string_ | `BucketList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Bucket_ |   
  
### BucketPolicy

_Appears in:_ \- BucketSpec

Field | Description  
---|---  
`lockingPolicy` _LockingPolicy_ | Policy for object locking. When set, object versioning is enabled and all objects stored in the bucket will be subject to this policy. A locked object cannot be deleted until the lock expires. LockingPolicy has to be enabled when creating the bucket and cannot be disabled afterwards. When unset, object locking and versioning is disabled and cannot be enabled.  
  
### BucketSpec

BucketSpec defines the desired state of the Bucket Resource.

_Appears in:_ \- Bucket

Field | Description  
---|---  
_description_ _string_ | Description of bucket contents.  
_storageClass_ _ObjectStorageClass_ | Available options are: - Standard - Good for **hot** data that is accessed frequently, including websites, streaming videos, and mobile apps  
_bucketPolicy_ _BucketPolicy_ | Defines policies of the bucket resource. If unspecified, default policies will be applied.  
  
### BucketStatus

BucketStatus defines the observed state of Bucket

_Appears in:_ \- Bucket

Field | Description  
---|---  
`fullyQualifiedName` _string_ | FullyQualifiedName is the name of the provisioned bucket. This name should be used to refer to the bucket when using external tools and libraries.  
`conditions` _Conditions_ | Conditions specify the status of the bucket. Supported conditions include: - BucketReady: true indicates if the bucket has been provisioned and is ready for use  
`endpoint` _string_ | The DNS endpoint at which the bucket is reachable.  
`region` _string_ | The region where the bucket is stored.  
  
### LockingPolicy

LockingPolicy defines the strategy for locking the objects of the bucket.

_Appears in:_ \- BucketPolicy

Field | Description  
---|---  
`defaultObjectRetentionDays` _integer_ | DefaultObjectRetentionDays specifies the minimum number of days that each version of every object will be retained. An object cannot be deleted during the retention period. If a bucket contains any object, it cannot be deleted either. When unspecified, no default object retention period is set. DefaultObjectRetentionDays can be modified after creation, however the change will only take effect for new objects and versions. Existing objects and versions will still use the previous value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
