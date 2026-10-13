---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RestoreDatabaseMetadata/
title: RestoreDatabaseMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:21.904904+00:00
---

# RestoreDatabaseMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RestoreDatabaseMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  RestoreDatabaseMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata type for the long-running operation returned by `[databases.restore](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "sourceType": enum ([RestoreSourceType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#RestoreSourceType)),
      "progress": {
        object ([OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress))
      },
      "cancelTime": string,
      "optimizeDatabaseOperationName": string,
    
      // Union field source_info can be only one of the following:
      "backupInfo": {
        object ([BackupInfo](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#BackupInfo))
      }
      // End of list of possible types for union field source_info.
    }  
  
Fields  
---  
`name` |  `string` Name of the database being created and restored to.  
`sourceType` |  `enum (`[RestoreSourceType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#RestoreSourceType)`)` The type of the restore source.  
`progress` |  `object (`[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress)`)` The progress of the `[databases.restore](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase)` operation.  
`cancelTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which cancellation of this operation was received. `[Operations.CancelOperation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.operations/cancel#google.longrunning.Operations.CancelOperation)` starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.operations/get#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a `[google.rpc.Status.code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status#FIELDS.code)` of 1, corresponding to `Code.CANCELLED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`optimizeDatabaseOperationName` |  `string` If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored database, and remove the dependency on the restore source. The name is of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>` where the  is the name of database being created and restored to. The metadata type of the long-running operation is `[OptimizeRestoredDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OptimizeRestoredDatabaseMetadata)`. This long-running operation will be automatically created by the system after the databases.restore long-running operation completes successfully. This operation will not be created if the restore was not successful.  
Union field `source_info`. Information about the source used to restore the database, as specified by `source` in `RestoreDatabaseRequest`. `source_info` can be only one of the following:  
`backupInfo` |  `object (`[BackupInfo](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#BackupInfo)`)` Information about the backup used to restore the database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
