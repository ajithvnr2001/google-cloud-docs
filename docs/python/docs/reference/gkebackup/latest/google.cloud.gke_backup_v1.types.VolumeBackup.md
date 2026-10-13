---
url: https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.VolumeBackup
title: Class VolumeBackup (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:01.434060+00:00
---

# Class VolumeBackup (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.VolumeBackup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class VolumeBackup (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.19  0.4.4  0.3.0  0.2.2  0.1.1 
    
    
    VolumeBackup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the backup of a specific persistent volume as a component of a Backup - both the record of the operation and a pointer to the underlying storage-specific artifacts.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The full name of the VolumeBackup resource. Format: `projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*`.   
`uid` |  `str`   
Output only. Server generated global unique identifier of `UUID `__ format.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when this VolumeBackup resource was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when this VolumeBackup resource was last updated.   
`source_pvc` |  `[google.cloud.gke_backup_v1.types.NamespacedName](https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.NamespacedName)`   
Output only. A reference to the source Kubernetes PVC from which this VolumeBackup was created.   
`volume_backup_handle` |  `str`   
Output only. A storage system-specific opaque handle to the underlying volume backup.   
`format_` |  `[google.cloud.gke_backup_v1.types.VolumeBackup.VolumeBackupFormat](https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.VolumeBackup.VolumeBackupFormat)`   
Output only. The format used for the volume backup.   
`storage_bytes` |  `int`   
Output only. The aggregate size of the underlying artifacts associated with this VolumeBackup in the backup storage. This may change over time when multiple backups of the same volume share the same backup storage location. In particular, this is likely to increase in size when the immediately preceding backup of the same volume is deleted.   
`disk_size_bytes` |  `int`   
Output only. The minimum size of the disk to which this VolumeBackup can be restored.   
`complete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the associated underlying volume backup operation completed.   
`state` |  `[google.cloud.gke_backup_v1.types.VolumeBackup.State](https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.VolumeBackup.State)`   
Output only. The current state of this VolumeBackup.   
`state_message` |  `str`   
Output only. A human readable message explaining why the VolumeBackup is in its current state. This field is only meant for human consumption and should not be used programmatically as this field is not guaranteed to be consistent.   
`etag` |  `str`   
Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume backup updates in order to avoid race conditions.   
`satisfies_pzs` |  `bool`   
Output only. [Output Only] Reserved for future use.   
`satisfies_pzi` |  `bool`   
Output only. [Output Only] Reserved for future use.   
  
## Classes 

### State
    
    
    State(value)

The current state of a VolumeBackup

### VolumeBackupFormat
    
    
    VolumeBackupFormat(value)

Identifies the format used for the volume backup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
