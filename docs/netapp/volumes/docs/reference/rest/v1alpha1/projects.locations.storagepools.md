---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1alpha1/projects.locations.storagepools
title: REST Resource: projects.locations.storagepools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:13.773186+00:00
---

# REST Resource: projects.locations.storagepools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1alpha1/projects.locations.storagepools




#  REST Resource: projects.locations.storagepools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: StoragePool
    * JSON representation
  * State
  * Methods



## Resource: StoragePool

Resources StoragePool StoragePool is a container for volumes with a service level and capacity. Volumes can be created in a pool of sufficient available capacity. StoragePool capacity is what you are billed for.

JSON representation  
---  
      
    
    {
      "name": string,
      "serviceLevel": enum ([ServiceLevel](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/ServiceLevel)),
      "capacityGib": string,
      "volumeCapacityGib": string,
      "volumeCount": integer,
      "state": enum ([State](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools#State)),
      "stateDetails": string,
      "createTime": string,
      "description": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the storage pool. Format: `projects/{project_number}/locations/{locationId}/storagepools/{storagePoolId}`.  
`serviceLevel` |  `enum (`[ServiceLevel](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/ServiceLevel)`)` Required. Service level of the storage pool  
`capacityGib` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Capacity in GIB of the pool  
`volumeCapacityGib` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Allocated size of all volumes in GIB in the storage pool  
`volumeCount` |  `integer` Output only. Volume count of the storage pool  
`state` |  `enum (`[State](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools#State)`)` Output only. State of the storage pool  
`stateDetails` |  `string` Output only. State details of the storage pool  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Create time of the storage poolA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`description` |  `string` Description of the storage pool  
`labels` |  `map (key: string, value: string)` Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## State

The Storage Pool States

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified Storage Pool State  
`READY` | Ready  
`CREATING` | Creating  
`DELETING` | Deleting  
`UPDATING` | Updating  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools/create)`

|  CreateStoragePoolCreates a new storage pool.  
  
### `[delete](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools/delete)`

|  DeleteStoragePoolWarning!  
  
### `[get](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools/get)`

|  GetStoragePoolReturns the description of the specified storage pool by poolId.  
  
### `[list](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools/list)`

|  ListStoragePoolsReturns descriptions of all storage pools owned by the caller.  
  
### `[patch](https://docs.cloud.google.com/netapp/docs/reference/rest/v1alpha1/projects.locations.storagepools/patch)`

|  UpdateStoragePoolUpdates the storage pool properties with the full spec  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-23 UTC."],[],[]] 
