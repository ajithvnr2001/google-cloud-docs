---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlMetadata
title: Cloud Spanner V1 Client - Class UpdateDatabaseDdlMetadata (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:45.345156+00:00
---

# Cloud Spanner V1 Client - Class UpdateDatabaseDdlMetadata (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner V1 Client - Class UpdateDatabaseDdlMetadata (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner V1 Client class UpdateDatabaseDdlMetadata.

Metadata type for the operation returned by [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__).

Generated from protobuf message `google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata`

## Namespace

Google \ Cloud \ Spanner \ Admin \ Database \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ database` |  `string`   
The database being modified.  
`↳ statements` |  `string[]`   
For an update this list contains all the statements. For an individual statement, this list contains only that statement.  
`↳ commit_timestamps` |  `array<Google\Protobuf\Timestamp>`   
Reports the commit timestamps of all statements that have succeeded so far, where `commit_timestamps[i]` is the commit timestamp for the statement `statements[i]`.  
`↳ throttled` |  `bool`   
Output only. When true, indicates that the operation is throttled e.g. due to resource constraints. When resources become available the operation will resume and this field will be false again.  
`↳ progress` |  `array<[OperationProgress](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.OperationProgress)>`   
The progress of the [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) operations. All DDL statements will have continuously updating progress, and `progress[i]` is the operation progress for `statements[i]`. Also, `progress[i]` will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed.  
`↳ actions` |  `array<[DdlStatementActionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.DdlStatementActionInfo)>`   
The brief action info for the DDL statements. `actions[i]` is the brief info for `statements[i]`.  
  
### getDatabase

The database being modified.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDatabase

The database being modified.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStatements

For an update this list contains all the statements. For an individual statement, this list contains only that statement.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setStatements

For an update this list contains all the statements. For an individual statement, this list contains only that statement.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCommitTimestamps

Reports the commit timestamps of all statements that have succeeded so far, where `commit_timestamps[i]` is the commit timestamp for the statement `statements[i]`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<Google\Protobuf\Timestamp>` |   
  
### setCommitTimestamps

Reports the commit timestamps of all statements that have succeeded so far, where `commit_timestamps[i]` is the commit timestamp for the statement `statements[i]`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<Google\Protobuf\Timestamp>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getThrottled

Output only. When true, indicates that the operation is throttled e.g.

due to resource constraints. When resources become available the operation will resume and this field will be false again.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setThrottled

Output only. When true, indicates that the operation is throttled e.g.

due to resource constraints. When resources become available the operation will resume and this field will be false again.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProgress

The progress of the [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) operations. All DDL statements will have continuously updating progress, and `progress[i]` is the operation progress for `statements[i]`. Also, `progress[i]` will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[OperationProgress](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.OperationProgress)>` |   
  
### setProgress

The progress of the [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) operations. All DDL statements will have continuously updating progress, and `progress[i]` is the operation progress for `statements[i]`. Also, `progress[i]` will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[OperationProgress](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.OperationProgress)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getActions

The brief action info for the DDL statements.

`actions[i]` is the brief info for `statements[i]`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[DdlStatementActionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.DdlStatementActionInfo)>` |   
  
### setActions

The brief action info for the DDL statements.

`actions[i]` is the brief info for `statements[i]`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[DdlStatementActionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.DdlStatementActionInfo)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
