---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections
title: REST Resource: projects.locations.backupCollections \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:42.253834+00:00
---

# REST Resource: projects.locations.backupCollections  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  REST Resource: projects.locations.backupCollections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackupCollection
    * JSON representation
  * Methods



## Resource: BackupCollection

BackupCollection of a cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "clusterUid": string,
      "cluster": string,
      "kmsKey": string,
      "uid": string,
      "createTime": string,
      "totalBackupSizeBytes": string,
      "totalBackupCount": string,
      "lastBackupTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Full resource path of the backup collection.  
`clusterUid` |  `string` Output only. The cluster uid of the backup collection.  
`cluster` |  `string` Output only. The full resource path of the cluster the backup collection belongs to. Example: projects/{project}/locations/{location}/clusters/{cluster}  
`kmsKey` |  `string` Output only. The KMS key used to encrypt the backups under this backup collection.  
`uid` |  `string` Output only. System assigned unique identifier of the backup collection.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup collection was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`totalBackupSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total size of all backups in the backup collection.  
`totalBackupCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total number of backups in the backup collection.  
`lastBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time a backup was created in the backup collection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections/get)`

|  Get a backup collection.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections/list)`

|  Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
