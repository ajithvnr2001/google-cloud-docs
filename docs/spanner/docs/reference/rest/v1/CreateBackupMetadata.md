---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata/
title: CreateBackupMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:16.201494+00:00
---

# CreateBackupMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  CreateBackupMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata type for the operation returned by `[backups.create](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/create#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "database": string,
      "progress": {
        object ([OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress))
      },
      "cancelTime": string
    }  
  
Fields  
---  
`name` |  `string` The name of the backup being created.  
`database` |  `string` The name of the database the backup is created from.  
`progress` |  `object (`[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress)`)` The progress of the `[backups.create](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/create#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` operation.  
`cancelTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which cancellation of this operation was received. `[Operations.CancelOperation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.operations/cancel#google.longrunning.Operations.CancelOperation)` starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.operations/get#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `[Operation.error](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation.FIELDS.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status#FIELDS.code)` of 1, corresponding to `Code.CANCELLED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
