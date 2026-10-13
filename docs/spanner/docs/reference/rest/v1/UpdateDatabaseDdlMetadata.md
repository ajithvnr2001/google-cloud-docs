---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateDatabaseDdlMetadata/
title: UpdateDatabaseDdlMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:23.942354+00:00
---

# UpdateDatabaseDdlMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateDatabaseDdlMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  UpdateDatabaseDdlMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata type for the operation returned by `[databases.updateDdl](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)`.

JSON representation  
---  
      
    
    {
      "database": string,
      "statements": [
        string
      ],
      "commitTimestamps": [
        string
      ],
      "throttled": boolean,
      "progress": [
        {
          object ([OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress))
        }
      ],
      "actions": [
        {
          object ([DdlStatementActionInfo](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DdlStatementActionInfo))
        }
      ]
    }  
  
Fields  
---  
`database` |  `string` The database being modified.  
`statements[]` |  `string` For an update this list contains all the statements. For an individual statement, this list contains only that statement.  
`commitTimestamps[]` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Reports the commit timestamps of all statements that have succeeded so far, where `commitTimestamps[i]` is the commit timestamp for the statement `statements[i]`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`throttled` |  `boolean` Output only. When true, indicates that the operation is throttled, for example, due to resource constraints. When resources become available the operation will resume and this field will be false again.  
`progress[]` |  `object (`[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress)`)` The progress of the `[databases.updateDdl](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)` operations. All DDL statements will have continuously updating progress, and `progress[i]` is the operation progress for `statements[i]`. Also, `progress[i]` will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed.  
`actions[]` |  `object (`[DdlStatementActionInfo](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DdlStatementActionInfo)`)` The brief action info for the DDL statements. `actions[i]` is the brief info for `statements[i]`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
