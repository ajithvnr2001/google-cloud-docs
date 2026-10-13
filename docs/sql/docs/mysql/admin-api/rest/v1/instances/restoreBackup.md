---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup/
title: Method: instances.restoreBackup \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:56.126635+00:00
---

# Method: instances.restoreBackup  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: instances.restoreBackup Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesRestoreBackupRequest
    * JSON representation
  * RestoreBackupContext
    * JSON representation
  * Examples
  * Try it!



Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart.

### HTTP request

`POST https://sqladmin.googleapis.com/v1/projects/{project}/instances/{instance}/restoreBackup`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the project that contains the instance.  
`instance` |  `string` Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains an instance of `[InstancesRestoreBackupRequest](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup#InstancesRestoreBackupRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesRestoreBackupRequest

Database instance restore backup request.

JSON representation  
---  
      
    
    {
      "restoreBackupContext": {
        object ([RestoreBackupContext](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup#RestoreBackupContext))
      },
      "backup": string,
      "backupdrBackup": string,
      "restoreInstanceSettings": {
        object ([DatabaseInstance](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance))
      },
      "restoreInstanceClearOverridesFieldNames": [
        string
      ]
    }  
  
Fields  
---  
`restoreBackupContext` |  `object (`[RestoreBackupContext](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup#RestoreBackupContext)`)` Parameters required to perform the restore backup operation.  
`backup` |  `string` The name of the backup that's used to restore a Cloud SQL instance: Format: projects/{project-id}/backups/{backup-uid}. Only one of restoreBackupContext, backup, backupdrBackup can be passed to the input.  
`backupdrBackup` |  `string` The name of the backup that's used to restore a Cloud SQL instance: Format: "projects/{project-id}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup-uid}". Only one of restoreBackupContext, backup, backupdrBackup can be passed to the input.  
`restoreInstanceSettings` |  `object (`[DatabaseInstance](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance)`)` Optional. By using this parameter, Cloud SQL overrides any instance settings stored in the backup you are restoring from. You can't change the instance's major database version and you can only increase the disk size. You can use this field to restore new instances only. This field is not applicable for restore to existing instances.  
`restoreInstanceClearOverridesFieldNames[]` |  `string` Optional. This field has the same purpose as restoreInstanceSettings, changes any instance settings stored in the backup you are restoring from. With the difference that these fields are cleared in the settings.  
  
## RestoreBackupContext

Database instance restore from backup context. Backup context contains source instance id and project id.

JSON representation  
---  
      
    
    {
      "kind": string,
      "backupRunId": string,
      "instanceId": string,
      "project": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#restoreBackupContext`.  
`backupRunId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The ID of the backup run to restore from.  
`instanceId` |  `string` The ID of the instance that the backup was taken from.  
`project` |  `string` The full project ID of the source instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
