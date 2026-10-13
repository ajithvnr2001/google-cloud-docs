---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools
title: REST Resource: projects.locations.clusters.nodePools \u00a0|\u00a0 Google Distributed Cloud connected, version 1.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:10.745755+00:00
---

# REST Resource: projects.locations.clusters.nodePools  |  Google Distributed Cloud connected, version 1.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/apis)



Send feedback 

#  REST Resource: projects.locations.clusters.nodePools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NodePool
    * JSON representation
  * LocalDiskEncryption
    * JSON representation
  * NodeConfig
    * JSON representation
  * Methods



## Resource: NodePool

A set of Kubernetes nodes in a cluster with common configuration and specification.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "nodeLocation": string,
      "nodeCount": integer,
      "machineFilter": string,
      "localDiskEncryption": {
        object ([LocalDiskEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools#LocalDiskEncryption))
      },
      "nodeVersion": string,
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools#NodeConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the node pool.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the node pool was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the node pool was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodeLocation` |  `string` Name of the Google Distributed Cloud Edge zone where this node pool will be created. For example: `us-central1-edge-customer-a`.  
`nodeCount` |  `integer` Required. The number of nodes in the pool.  
`machineFilter` |  `string` Only machines matching this filter will be allowed to join the node pool. The filtering language accepts strings like "name=", and is documented in more detail in [AIP-160](https://google.aip.dev/160).  
`localDiskEncryption` |  `object (`[LocalDiskEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools#LocalDiskEncryption)`)` Optional. Local disk encryption options. This field is only used when enabling CMEK support.  
`nodeVersion` |  `string` Output only. The lowest release version among all worker nodes.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools#NodeConfig)`)` Optional. Configuration for each node in the NodePool  
  
## LocalDiskEncryption

Configuration for CMEK support for edge machine local disk encryption.

JSON representation  
---  
      
    
    {
      "kmsKey": string,
      "kmsKeyActiveVersion": string,
      "kmsKeyState": enum ([KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/KmsKeyState)),
      "kmsStatus": {
        object ([Status](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/Status))
      }
    }  
  
Fields  
---  
`kmsKey` |  `string` Optional. The Cloud KMS CryptoKey e.g. projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} to use for protecting node local disks. If not specified, a Google-managed key will be used instead.  
`kmsKeyActiveVersion` |  `string` Output only. The Cloud KMS CryptoKeyVersion currently in use for protecting node local disks. Only applicable if kmsKey is set.  
`kmsKeyState` |  `enum (`[KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/KmsKeyState)`)` Output only. Availability of the Cloud KMS CryptoKey. If not `KEY_AVAILABLE`, then nodes may go offline as they cannot access their local data. This can be caused by a lack of permissions to use the key, or if the key is disabled or deleted.  
`kmsStatus` |  `object (`[Status](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/Status)`)` Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kmsKeyState` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.  
  
## NodeConfig

Configuration for each node in the NodePool

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` Optional. The Kubernetes node labelsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/create)`

|  Creates a new NodePool in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/delete)`

|  Deletes a single NodePool.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/get)`

|  Gets details of a single NodePool.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/list)`

|  Lists NodePools in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/patch)`

|  Updates the parameters of a single NodePool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
