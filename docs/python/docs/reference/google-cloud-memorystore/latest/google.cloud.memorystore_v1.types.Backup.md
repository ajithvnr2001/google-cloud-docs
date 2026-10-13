---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.Backup
title: Class Backup (0.5.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:55.034887+00:00
---

# Class Backup (0.5.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Backup (0.5.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.5 (latest)  0.5.4  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    Backup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Backup of an instance.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]\\_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the backup was created.   
`instance` |  `str`   
Output only. Instance resource path of this backup.   
`instance_uid` |  `str`   
Output only. Instance uid of this backup.   
`total_size_bytes` |  `int`   
Output only. Total size of the backup in bytes.   
`expire_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the backup will expire.   
`engine_version` |  `str`   
Output only. valkey-7.5/valkey-8.0, etc.   
`backup_files` |  `MutableSequence[[google.cloud.memorystore_v1.types.BackupFile](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.BackupFile)]`   
Output only. List of backup files of the backup.   
`node_type` |  `[google.cloud.memorystore_v1.types.Instance.NodeType](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.Instance.NodeType)`   
Output only. Node type of the instance.   
`replica_count` |  `int`   
Output only. Number of replicas for the instance.   
`shard_count` |  `int`   
Output only. Number of shards for the instance.   
`backup_type` |  `[google.cloud.memorystore_v1.types.Backup.BackupType](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.Backup.BackupType)`   
Output only. Type of the backup.   
`state` |  `[google.cloud.memorystore_v1.types.Backup.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.Backup.State)`   
Output only. State of the backup.   
`encryption_info` |  `[google.cloud.memorystore_v1.types.EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1.types.EncryptionInfo)`   
Output only. Encryption information of the backup.   
`uid` |  `str`   
Output only. System assigned unique identifier of the backup.   
  
## Classes 

### BackupType
    
    
    BackupType(value)

Type of the backup.

### State
    
    
    State(value)

State of the backup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
