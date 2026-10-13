---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/CopyBackupMetadata/
title: CopyBackupMetadata \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:29.268646+00:00
---

# CopyBackupMetadata  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/CopyBackupMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  CopyBackupMetadata Stay organized with collections  Save and categorize content based on your preferences. 

Metadata type for the google.longrunning.Operation returned by `[backups.copy](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/copy#google.bigtable.admin.v2.BigtableTableAdmin.CopyBackup)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "sourceBackupInfo": {
        object ([BackupInfo](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#BackupInfo))
      },
      "progress": {
        object ([OperationProgress](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/OperationProgress))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the backup being created through the copy operation. Values are of the form `projects/<project>/instances/<instance>/clusters/<cluster>/backups/<backup>`.  
`sourceBackupInfo` |  `object (`[BackupInfo](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#BackupInfo)`)` Information about the source backup that is being copied from.  
`progress` |  `object (`[OperationProgress](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/OperationProgress)`)` The progress of the `[backups.copy](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/copy#google.bigtable.admin.v2.BigtableTableAdmin.CopyBackup)` operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-03 UTC."],[],[]] 
