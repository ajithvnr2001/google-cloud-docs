---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/v1/global-object-v1/
title: KRM API object.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:08.427296+00:00
---

# KRM API object.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/v1/global-object-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API object.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## object.global.gdc.goog/v1

### AsyncDualZoneSpec

_Appears in:_ \- BucketLocationSpec \- LocationInfo

Field | Description  
---|---  
`zoneNames` _string array_ | Slice of 2 location.mz.global.private.gdc.goog/v1alpha1 Zone resources.  
`combinationPrefix` _string_ | 2-character prefix used in the BucketPrefix resource  
  
### Bucket

Defines the schema for the Buckets API.

_Appears in:_ \- BucketList

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `Bucket`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketSpec_ |   
`status` _BucketStatus_ |   
  
### BucketList

Contains a list of Buckets.

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Bucket array_ |   
  
### BucketLocation

Defines the schema for the BucketLocation API.

_Appears in:_ \- BucketLocationList

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketLocation`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketLocationSpec_ |   
`status` _BucketLocationStatus_ |   
  
### BucketLocationClusterStatus

Provides the status of a BucketLocation rolling out to a particular cluster. Follows pkg/apis/common/global/v1alpha1 ZoneStatus

_Appears in:_ \- BucketLocationConfigStatus

Field | Description  
---|---  
`name` _string_ | The name of the cluster where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the cluster.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The reconciliation status of the replica collected from the cluster. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### BucketLocationConfig

Defines the schema for the BucketLocationConfig API.

_Appears in:_ \- BucketLocationConfigList

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketLocationConfig`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketLocationSpec_ |   
`status` _BucketLocationConfigStatus_ |   
  
### BucketLocationConfigList

Contains a list of BucketLocationConfigs.

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketLocationConfigList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BucketLocationConfig array_ |   
  
### BucketLocationConfigStatus

Defines the observed state of the BucketLocationConfig.

_Appears in:_ \- BucketLocationConfig

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`clusters` _BucketLocationClusterStatus array_ | The list of cluster statuses where the resource is rolled out to.  
  
### BucketLocationList

Contains a list of BucketLocations.

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketLocationList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BucketLocation array_ |   
  
### BucketLocationReplica

Defines the schema for the BucketLocationReplica API.

_Appears in:_ \- BucketLocationReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketLocationReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketLocationSpec_ |   
`status` _BucketLocationReplicaStatus_ |   
  
### BucketLocationReplicaList

Contains a list of BucketLocationReplicas.

Field | Description  
---|---  
`apiVersion` _string_ | `object.global.gdc.goog/v1`  
`kind` _string_ | `BucketLocationReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BucketLocationReplica array_ |   
  
### BucketLocationReplicaStatus

_Appears in:_ \- BucketLocationReplica \- BucketLocationZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this bucket location's overall state.  
  
### BucketLocationSpec

BucketLocationSpec defines the desired state of the BucketLocation Resource.

_Appears in:_ \- BucketLocation \- BucketLocationConfig \- BucketLocationReplica

Field | Description  
---|---  
`asyncDualZone` _AsyncDualZoneSpec_ | BucketLocation configuration specific to AsyncDualZone buckets. Must be present if LocationType = AsyncDualZone  
`syncDualZone` _SyncDualZoneSpec_ | BucketLocation configuration specific to SyncDualZone buckets. Must be present if LocationType = SyncDualZone  
`locationType` _BucketLocationType_ | Supported types include: [ AsyncDualZone, SyncDualZone ].  
`active` _boolean_ | If active = false, new buckets cannot be created with this BucketLocation.  
  
### BucketLocationStatus

Defines the observed state of the BucketLocation.

_Appears in:_ \- BucketLocation

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _BucketLocationZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### BucketLocationZoneStatus

Provides the status of a BucketLocation rolling out to a particular zone.

_Appears in:_ \- BucketLocationStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _BucketLocationReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### BucketSpec

Defines the desired state of the Bucket Resource.

_Appears in:_ \- Bucket

Field | Description  
---|---  
`description` _string_ | The description of bucket contents.  
`storageClass` _ObjectStorageClass_ | The storage class of the bucket. Defines how frequently data needs to be accessed. The available options include `Standard` and `Nearline`. `Standard` is appropriate for hot data that is accessed frequently, such as websites, streaming videos, and mobile apps. It is used for data that can be stored for at least 30 days. `Nearline` is appropriate for data that can be stored for at least 60 days, including data backup and long-tail multimedia content.  
`bucketPolicy` _GlobalBucketPolicy_ | The policies of the bucket resource. If unspecified, default policies are applied.  
`location` _string_ | The physical place where object data in the bucket resides. This must map to the name of an existing `ObjectStorageLocation` resource.  
  
### BucketStatus

Defines the observed state of the Bucket.

_Appears in:_ \- Bucket

Field | Description  
---|---  
`fullyQualifiedName` _string_ | The name of the provisioned bucket. This name is used to refer to the bucket when using external tools and libraries.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The conditions of the bucket. Supported conditions include `BucketReady`. If BucketReady is `True`, it indicates the bucket has been provisioned and is ready for use.  
`zonalEndpoints` _string array_ | Zonal endpoints at which the bucket is reachable. Use these endpoints if a customized failover is required.  
`globalEndpoint` _string_ | Global endpoint which will dynamically route traffic to any zone which contains data for this bucket. Use this endpoint if automatic failover is required.  
`region` _string_ | The region where the bucket is stored.  
`encryption` _EncryptionStatus_ | The status of the encryption on the bucket.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with the observed times included.  
  
### LocationInfo

Only one of its members should be specified.

_Appears in:_ \- BucketLocationSpec

Field | Description  
---|---  
`asyncDualZone` _AsyncDualZoneSpec_ | BucketLocation configuration specific to AsyncDualZone buckets. Must be present if LocationType = AsyncDualZone  
`syncDualZone` _SyncDualZoneSpec_ | BucketLocation configuration specific to SyncDualZone buckets. Must be present if LocationType = SyncDualZone  
  
### SyncDualZoneSpec

_Appears in:_ \- BucketLocationSpec \- LocationInfo

Field | Description  
---|---  
`zoneNames` _string array_ | Slice of 2 location.mz.global.private.gdc.goog/v1alpha1 Zone resources.  
`combinationPrefix` _string_ | 2-character prefix used in the BucketPrefix resource  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
