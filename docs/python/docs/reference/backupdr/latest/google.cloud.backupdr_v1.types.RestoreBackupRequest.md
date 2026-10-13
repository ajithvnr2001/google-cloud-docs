---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupRequest
title: Class RestoreBackupRequest (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:08.519741+00:00
---

# Class RestoreBackupRequest (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RestoreBackupRequest (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    RestoreBackupRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for restoring from a Backup.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.   
`request_id` |  `str`   
Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
`compute_instance_target_environment` |  `[google.cloud.backupdr_v1.types.ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceTargetEnvironment)`   
Compute Engine target environment to be used during restore. This field is a member of `oneof`_ `target_environment`.   
`disk_target_environment` |  `[google.cloud.backupdr_v1.types.DiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskTargetEnvironment)`   
Disk target environment to be used during restore. This field is a member of `oneof`_ `target_environment`.   
`region_disk_target_environment` |  `[google.cloud.backupdr_v1.types.RegionDiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RegionDiskTargetEnvironment)`   
Region disk target environment to be used during restore. This field is a member of `oneof`_ `target_environment`.   
`compute_instance_restore_properties` |  `[google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties)`   
Compute Engine instance properties to be overridden during restore. This field is a member of `oneof`_ `instance_properties`.   
`disk_restore_properties` |  `[google.cloud.backupdr_v1.types.DiskRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties)`   
Disk properties to be overridden during restore. This field is a member of `oneof`_ `instance_properties`.   
`clear_overrides_field_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof. When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field. The most common current use case is clearing default encryption keys. Examples of field mask paths: \- Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key` \- Single Disk: `disk_restore_properties.disk_encryption_key` This field is a member of `oneof`_ `_clear_overrides_field_mask`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
