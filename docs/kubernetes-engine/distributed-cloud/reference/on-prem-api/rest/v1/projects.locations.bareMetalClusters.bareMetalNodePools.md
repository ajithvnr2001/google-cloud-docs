---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools
title: REST Resource: projects.locations.bareMetalClusters.bareMetalNodePools \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:13.781425+00:00
---

# REST Resource: projects.locations.bareMetalClusters.bareMetalNodePools  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  REST Resource: projects.locations.bareMetalClusters.bareMetalNodePools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BareMetalNodePool
    * JSON representation
  * State
  * BareMetalNodePoolUpgradePolicy
    * JSON representation
  * BareMetalParallelUpgradeConfig
    * JSON representation
  * Methods



## Resource: BareMetalNodePool

Resource that represents a bare metal node pool.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#State)),
      "reconciling": boolean,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "etag": string,
      "annotations": {
        string: string,
        ...
      },
      "nodePoolConfig": {
        object ([BareMetalNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig))
      },
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      },
      "upgradePolicy": {
        object ([BareMetalNodePoolUpgradePolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#BareMetalNodePoolUpgradePolicy))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. The bare metal node pool resource name.  
`displayName` |  `string` The display name for the bare metal node pool.  
`uid` |  `string` Output only. The unique identifier of the bare metal node pool.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#State)`)` Output only. The current state of the bare metal node pool.  
`reconciling` |  `boolean` Output only. If set, there are currently changes in flight to the bare metal node pool.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this bare metal node pool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this bare metal node pool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this bare metal node pool was deleted. If the resource is not deleted, this must be emptyUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.  
`annotations` |  `map (key: string, value: string)` Annotations on the bare metal node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodePoolConfig` |  `object (`[BareMetalNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig)`)` Required. Node pool configuration.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. ResourceStatus representing the detailed node pool status.  
`upgradePolicy` |  `object (`[BareMetalNodePoolUpgradePolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#BareMetalNodePoolUpgradePolicy)`)` The worker node pool upgrade policy.  
  
## State

The lifecycle state of the bare metal node pool.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the bare metal node pool is being created.  
`RUNNING` | The RUNNING state indicates the bare metal node pool has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that the bare metal node pool is being updated. It remains available, but potentially with degraded performance.  
`STOPPING` | The STOPPING state indicates the bare metal node pool is being deleted.  
`ERROR` | The ERROR state indicates the bare metal node pool is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the bare metal node pool requires user action to restore full functionality.  
  
## BareMetalNodePoolUpgradePolicy

BareMetalNodePoolUpgradePolicy defines the node pool upgrade policy.

JSON representation  
---  
      
    
    {
      "parallelUpgradeConfig": {
        object ([BareMetalParallelUpgradeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#BareMetalParallelUpgradeConfig))
      }
    }  
  
Fields  
---  
`parallelUpgradeConfig` |  `object (`[BareMetalParallelUpgradeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#BareMetalParallelUpgradeConfig)`)` The parallel upgrade settings for worker node pools.  
  
## BareMetalParallelUpgradeConfig

BareMetalParallelUpgradeConfig defines the parallel upgrade settings for worker node pools.

JSON representation  
---  
      
    
    {
      "concurrentNodes": integer,
      "minimumAvailableNodes": integer
    }  
  
Fields  
---  
`concurrentNodes` |  `integer` The maximum number of nodes that can be upgraded at once.  
`minimumAvailableNodes` |  `integer` The minimum number of nodes that should be healthy and available during an upgrade. If set to the default value of 0, it is possible that none of the nodes will be available during an upgrade.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/create)`

|  Creates a new bare metal node pool in a given project, location and Bare Metal cluster.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/delete)`

|  Deletes a single bare metal node pool.  
  
### `[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/enroll)`

|  Enrolls an existing bare metal node pool to the Anthos On-Prem API within a given project and location.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/get)`

|  Gets details of a single bare metal node pool.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/list)`

|  Lists bare metal node pools in a given project, location and bare metal cluster.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/patch)`

|  Updates the parameters of a single bare metal node pool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
