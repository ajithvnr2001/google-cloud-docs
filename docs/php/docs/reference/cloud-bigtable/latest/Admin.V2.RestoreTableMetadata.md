---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreTableMetadata
title: Cloud Bigtable V2 Client - Class RestoreTableMetadata (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:53.098093+00:00
---

# Cloud Bigtable V2 Client - Class RestoreTableMetadata (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreTableMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class RestoreTableMetadata (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class RestoreTableMetadata.

Metadata type for the long-running operation returned by [RestoreTable](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__restoreTable__).

Generated from protobuf message `google.bigtable.admin.v2.RestoreTableMetadata`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Name of the table being created and restored to.  
`↳ source_type` |  `int`   
The type of the restore source.  
`↳ backup_info` |  `[BackupInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.BackupInfo)`   
  
`↳ optimize_table_operation_name` |  `string`   
If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored table. The metadata type of the long-running operation is OptimizeRestoreTableMetadata. The response type is Empty. This long-running operation may be automatically created by the system if applicable after the RestoreTable long-running operation completes successfully. This operation may not be created if the table is already optimized or the restore was not successful.  
`↳ progress` |  `[OperationProgress](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.OperationProgress)`   
The progress of the [RestoreTable](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__restoreTable__) operation.  
  
### getName

Name of the table being created and restored to.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Name of the table being created and restored to.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceType

The type of the restore source.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [RestoreSourceType](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreSourceType).  
  
### setSourceType

The type of the restore source.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [RestoreSourceType](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreSourceType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupInfo

Generated from protobuf field `.google.bigtable.admin.v2.BackupInfo backup_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BackupInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.BackupInfo)|null` |   
  
### hasBackupInfo

### setBackupInfo

Generated from protobuf field `.google.bigtable.admin.v2.BackupInfo backup_info = 3;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BackupInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.BackupInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOptimizeTableOperationName

If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored table. The metadata type of the long-running operation is OptimizeRestoreTableMetadata. The response type is Empty. This long-running operation may be automatically created by the system if applicable after the RestoreTable long-running operation completes successfully. This operation may not be created if the table is already optimized or the restore was not successful.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOptimizeTableOperationName

If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored table. The metadata type of the long-running operation is OptimizeRestoreTableMetadata. The response type is Empty. This long-running operation may be automatically created by the system if applicable after the RestoreTable long-running operation completes successfully. This operation may not be created if the table is already optimized or the restore was not successful.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProgress

The progress of the [RestoreTable](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__restoreTable__) operation.

**Returns**  
---  
**Type** | **Description**  
`[OperationProgress](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.OperationProgress)|null` |   
  
### hasProgress

### clearProgress

### setProgress

The progress of the [RestoreTable](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__restoreTable__) operation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[OperationProgress](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.OperationProgress)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceInfo

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
