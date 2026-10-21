---
url: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/update_user/
title: MCP Tools Reference: cloud-sql \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:06.048423+00:00
---

# MCP Tools Reference: cloud-sql  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/update_user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  MCP Tools Reference: cloud-sql Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_user`

Update a database user for a Cloud SQL instance. A common use case for the `update_user` is to grant a user the `cloudsqlsuperuser` role, which can provide a user with many required permissions.

This tool only supports updating users to assign database roles.

  * This tool returns a long-running operation. Use the `get_operation` tool to poll its status until the operation completes.
  * Before calling the `update_user` tool, always check the existing configuration of the user such as the user type with `list_users` tool.
  * As a special case for MySQL, if the `list_users` tool returns a full email address for the `iamEmail` field, for example `{name=test-account, iamEmail=test-account@project-id.iam.gserviceaccount.com}`, then in your `update_user` request, use the full email address in the `iamEmail` field in the `name` field of your toolrequest. For example, `name=test-account@project-id.iam.gserviceaccount.com`.



Key parameters for updating user roles:

  * `database_roles`: A list of database roles to be assigned to the user.
  * `revokeExistingRoles`: A boolean field (default: false) that controls how existing roles are handled.



How role updates work:

  1. **If`revokeExistingRoles` is true:**

     * Any existing roles granted to the user but NOT in the provided `database_roles` list will be REVOKED.
     * Revoking only applies to non-system roles. System roles like `cloudsqliamuser` etc won't be revoked.
     * Any roles in the `database_roles` list that the user does NOT already have will be GRANTED.
     * If `database_roles` is empty, then ALL existing non-system roles are revoked.
  2. **If`revokeExistingRoles` is false (default):**

     * Any roles in the `database_roles` list that the user does NOT already have will be GRANTED.
     * Existing roles NOT in the `database_roles` list are KEPT.
     * If `database_roles` is empty, then there is no change to the user's roles.



Examples:

  * Existing Roles: `[roleA, roleB]`

    * Request: `database_roles: [roleB, roleC], revokeExistingRoles: true`
    * Result: Revokes `roleA`, Grants `roleC`. User roles become `[roleB, roleC]`.
    * Request: `database_roles: [roleB, roleC], revokeExistingRoles: false`
    * Result: Grants `roleC`. User roles become `[roleA, roleB, roleC]`.
    * Request: `database_roles: [], revokeExistingRoles: true`
    * Result: Revokes `roleA`, Revokes `roleB`. User roles become `[]`.
    * Request: `database_roles: [], revokeExistingRoles: false`
    * Result: No change. User roles remain `[roleA, roleB]`.



The following code sample shows how to use `curl` to call the `update_user` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://sqladmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_user",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

User update request for MCP.

### SqlUsersUpdateMcpRequest

JSON representation  
---  
      
    
    {
      "host": string,
      "instance": string,
      "name": string,
      "project": string,
      "databaseRoles": [
        string
      ],
      "type": enum ([SqlUserType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_user#Input.Schema.SqlUserType)),
    
      // Union field _revoke_existing_roles can be only one of the following:
      "revokeExistingRoles": boolean
      // End of list of possible types for union field _revoke_existing_roles.
    }  
  
Fields  
---  
`host` |  `string` Optional. Host of the user in the instance.  
`instance` |  `string` Required. Database instance ID. This does not include the project ID.  
`name` |  `string` Required. Name of the user in the instance.  
`project` |  `string` Required. Project ID of the project that contains the instance.  
`databaseRoles[]` |  `string` Optional. List of database roles to grant to the user. body.database_roles will be ignored for update request.  
`type` |  `enum (`[SqlUserType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_user#Input.Schema.SqlUserType)`)` Required. The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.  
Union field `_revoke_existing_roles`.`_revoke_existing_roles` can be only one of the following:  
`revokeExistingRoles` |  `boolean` Optional. revoke the existing roles granted to the user.  
  
### SqlUserType

The user type.

Enums  
---  
`BUILT_IN` | The database's built-in user type.  
`CLOUD_IAM_USER` | Cloud IAM user.  
`CLOUD_IAM_SERVICE_ACCOUNT` | Cloud IAM service account.  
`CLOUD_IAM_GROUP` | Cloud IAM group. Not used for login.  
`CLOUD_IAM_GROUP_USER` | Read-only. Login for a user that belongs to the Cloud IAM group.  
`CLOUD_IAM_GROUP_SERVICE_ACCOUNT` | Read-only. Login for a service account that belongs to the Cloud IAM group.  
`CLOUD_IAM_WORKFORCE_IDENTITY` | Cloud IAM workforce identity managed by Workforce Identity Federation.  
`ENTRAID_USER` | Microsoft Entra ID user.  
  
## Output Schema

An Operation resource. For successful operations that return an Operation resource, only the fields relevant to the operation are populated in the resource.

### Operation

JSON representation  
---  
      
    
    {
      "kind": string,
      "targetLink": string,
      "status": enum ([SqlOperationStatus](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlOperationStatus)),
      "user": string,
      "insertTime": string,
      "startTime": string,
      "endTime": string,
      "error": {
        object ([OperationErrors](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.OperationErrors))
      },
      "apiWarning": {
        object ([ApiWarning](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances#Output.Schema.ApiWarning))
      },
      "operationType": enum ([SqlOperationType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlOperationType)),
      "importContext": {
        object ([ImportContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.ImportContext))
      },
      "exportContext": {
        object ([ExportContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.ExportContext))
      },
      "backupContext": {
        object ([BackupContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.BackupContext))
      },
      "preCheckMajorVersionUpgradeContext": {
        object ([PreCheckMajorVersionUpgradeContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PreCheckMajorVersionUpgradeContext))
      },
      "startWorkloadCaptureContext": {
        object ([StartWorkloadCaptureContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.StartWorkloadCaptureContext))
      },
      "stopWorkloadCaptureContext": {
        object ([StopWorkloadCaptureContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.StopWorkloadCaptureContext))
      },
      "startWorkloadReplayContext": {
        object ([StartWorkloadReplayContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.StartWorkloadReplayContext))
      },
      "stopWorkloadReplayContext": {
        object (StopWorkloadReplayContext)
      },
      "name": string,
      "targetId": string,
      "selfLink": string,
      "targetProject": string,
      "acquireSsrsLeaseContext": {
        object ([AcquireSsrsLeaseContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.AcquireSsrsLeaseContext))
      },
      "subOperationType": {
        object ([SqlSubOperationType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlSubOperationType))
      }
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#operation`.  
`targetLink` |  `string`  
`status` |  `enum (`[SqlOperationStatus](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlOperationStatus)`)` The status of an operation.  
`user` |  `string` The email address of the user who initiated this operation.  
`insertTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[OperationErrors](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.OperationErrors)`)` If errors occurred during processing of this operation, this field will be populated.  
`apiWarning` |  `object (`[ApiWarning](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances#Output.Schema.ApiWarning)`)` An Admin API warning message.  
`operationType` |  `enum (`[SqlOperationType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlOperationType)`)` The type of the operation. Valid values are: * `CREATE` * `DELETE` * `UPDATE` * `RESTART` * `IMPORT` * `EXPORT` * `BACKUP_VOLUME` * `RESTORE_VOLUME` * `CREATE_USER` * `DELETE_USER` * `CREATE_DATABASE` * `DELETE_DATABASE`  
`importContext` |  `object (`[ImportContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.ImportContext)`)` The context for import operation, if applicable.  
`exportContext` |  `object (`[ExportContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.ExportContext)`)` The context for export operation, if applicable.  
`backupContext` |  `object (`[BackupContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.BackupContext)`)` The context for backup operation, if applicable.  
`preCheckMajorVersionUpgradeContext` |  `object (`[PreCheckMajorVersionUpgradeContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PreCheckMajorVersionUpgradeContext)`)` This field is only populated when the operation_type is PRE_CHECK_MAJOR_VERSION_UPGRADE. The PreCheckMajorVersionUpgradeContext message itself contains the details for that pre-check, such as the target database version for the upgrade and the results of the check (including any warnings or errors found).  
`startWorkloadCaptureContext` |  `object (`[StartWorkloadCaptureContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.StartWorkloadCaptureContext)`)` The context for the `StartWorkloadCapture` operation, which contains details to start recording the workload (SQL queries) on a Cloud SQL instance.  
`stopWorkloadCaptureContext` |  `object (`[StopWorkloadCaptureContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.StopWorkloadCaptureContext)`)` The context for the `StopWorkloadCapture` operation, which contains details to stop recording the workload (SQL queries) on a Cloud SQL instance.  
`startWorkloadReplayContext` |  `object (`[StartWorkloadReplayContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.StartWorkloadReplayContext)`)` The context for the `StartWorkloadReplay` operation, which contains details about starting the execution of a captured workload (recorded read and write SQL queries) on a replay instance (the Cloud SQL instance where the recorded SQL queries are executed).  
`stopWorkloadReplayContext` |  `object (`StopWorkloadReplayContext`)` The context for the `StopWorkloadReplay` operation, which contains details about stopping the execution of a captured workload (recorded read and write SQL queries) on a replay instance.  
`name` |  `string` An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation.  
`targetId` |  `string` Name of the resource on which this operation runs.  
`selfLink` |  `string` The URI of this resource.  
`targetProject` |  `string` The project ID of the target instance related to this operation.  
`acquireSsrsLeaseContext` |  `object (`[AcquireSsrsLeaseContext](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.AcquireSsrsLeaseContext)`)` The context for acquire SSRS lease operation, if applicable.  
`subOperationType` |  `object (`[SqlSubOperationType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlSubOperationType)`)` Optional. The sub operation based on the operation type.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### OperationErrors

JSON representation  
---  
      
    
    {
      "kind": string,
      "errors": [
        {
          object ([OperationError](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.OperationError))
        }
      ]
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#operationErrors`.  
`errors[]` |  `object (`[OperationError](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.OperationError)`)` The list of errors encountered while processing this operation.  
  
### OperationError

JSON representation  
---  
      
    
    {
      "kind": string,
      "code": string,
      "message": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#operationError`.  
`code` |  `string` Identifies the specific error that occurred.  
`message` |  `string` Additional information about the error encountered.  
  
### ApiWarning

JSON representation  
---  
      
    
    {
      "code": enum ([SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances#Output.Schema.SqlApiWarningCode)),
      "message": string,
      "region": string
    }  
  
Fields  
---  
`code` |  `enum (`[SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances#Output.Schema.SqlApiWarningCode)`)` Code to uniquely identify the warning type.  
`message` |  `string` The warning message.  
`region` |  `string` The region name for REGION_UNREACHABLE warning.  
  
### ImportContext

JSON representation  
---  
      
    
    {
      "uri": string,
      "database": string,
      "kind": string,
      "fileType": enum ([SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlFileType)),
      "csvImportOptions": {
        object ([SqlCsvImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlCsvImportOptions))
      },
      "importUser": string,
      "bakImportOptions": {
        object ([SqlBakImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlBakImportOptions))
      },
      "sqlImportOptions": {
        object ([SqlImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlImportOptions))
      },
      "tdeImportOptions": {
        object ([SqlTdeImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlTdeImportOptions))
      }
    }  
  
Fields  
---  
`uri` |  `string` Path to the import file in Cloud Storage, in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are supported when `fileType` is `SQL`. The instance must have write permissions to the bucket and read access to the file.  
`database` |  `string` The target database for the import. If `fileType` is `SQL`, this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. For entire instance parallel import operations, the database is overridden by the database name stored in subdirectory name. If `fileType` is `CSV`, one database must be specified.  
`kind` |  `string` This is always `sql#importContext`.  
`fileType` |  `enum (`[SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlFileType)`)` The file type for the specified uri.`SQL`: The file contains SQL statements. \`CSV`: The file contains CSV data.  
`csvImportOptions` |  `object (`[SqlCsvImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlCsvImportOptions)`)` Options for importing data as CSV.  
`importUser` |  `string` The PostgreSQL user for this import operation. PostgreSQL instances only.  
`bakImportOptions` |  `object (`[SqlBakImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlBakImportOptions)`)` Import parameters specific to SQL Server .BAK files  
`sqlImportOptions` |  `object (`[SqlImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlImportOptions)`)` Optional. Options for importing data from SQL statements.  
`tdeImportOptions` |  `object (`[SqlTdeImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlTdeImportOptions)`)` Optional. Import parameters specific to SQL Server TDE certificates  
  
### SqlCsvImportOptions

JSON representation  
---  
      
    
    {
      "table": string,
      "columns": [
        string
      ],
      "escapeCharacter": string,
      "quoteCharacter": string,
      "fieldsTerminatedBy": string,
      "linesTerminatedBy": string
    }  
  
Fields  
---  
`table` |  `string` The table to which CSV data is imported.  
`columns[]` |  `string` The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.  
`escapeCharacter` |  `string` Specifies the character that should appear before a data character that needs to be escaped.  
`quoteCharacter` |  `string` Specifies the quoting character to be used when a data value is quoted.  
`fieldsTerminatedBy` |  `string` Specifies the character that separates columns within each row (line) of the file.  
`linesTerminatedBy` |  `string` This is used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values.  
  
### SqlBakImportOptions

JSON representation  
---  
      
    
    {
      "encryptionOptions": {
        object ([EncryptionOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.EncryptionOptions))
      },
      "striped": boolean,
      "noRecovery": boolean,
      "recoveryOnly": boolean,
      "bakType": enum ([BakType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.BakType)),
      "stopAt": string,
      "stopAtMark": string
    }  
  
Fields  
---  
`encryptionOptions` |  `object (`[EncryptionOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.EncryptionOptions)`)`  
`striped` |  `boolean` Whether or not the backup set being restored is striped. Applies only to Cloud SQL for SQL Server.  
`noRecovery` |  `boolean` Whether or not the backup importing will restore database with NORECOVERY option. Applies only to Cloud SQL for SQL Server.  
`recoveryOnly` |  `boolean` Whether or not the backup importing request will just bring database online without downloading Bak content only one of "no_recovery" and "recovery_only" can be true otherwise error will return. Applies only to Cloud SQL for SQL Server.  
`bakType` |  `enum (`[BakType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.BakType)`)` Type of the bak content, FULL or DIFF  
`stopAt` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The timestamp when the import should stop. This timestamp is in the [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, `2023-10-01T16:19:00.094`). This field is equivalent to the STOPAT keyword and applies to Cloud SQL for SQL Server only.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stopAtMark` |  `string` Optional. The marked transaction where the import should stop. This field is equivalent to the STOPATMARK keyword and applies to Cloud SQL for SQL Server only.  
  
### EncryptionOptions

JSON representation  
---  
      
    
    {
      "certPath": string,
      "pvkPath": string,
      "pvkPassword": string,
      "keepEncrypted": boolean
    }  
  
Fields  
---  
`certPath` |  `string` Path to the Certificate (.cer) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`pvkPath` |  `string` Path to the Certificate Private Key (.pvk) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`pvkPassword` |  `string` Password that encrypts the private key  
`keepEncrypted` |  `boolean` Optional. Whether the imported file remains encrypted.  
  
### BoolValue

JSON representation  
---  
      
    
    {
      "value": boolean
    }  
  
Fields  
---  
`value` |  `boolean` The bool value.  
  
### SqlImportOptions

JSON representation  
---  
      
    
    {
      "threads": integer,
      "parallel": boolean,
      "postgresImportOptions": {
        object ([PostgresImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PostgresImportOptions))
      }
    }  
  
Fields  
---  
`threads` |  `integer` Optional. The number of threads to use for parallel import.  
`parallel` |  `boolean` Optional. Whether or not the import should be parallel.  
`postgresImportOptions` |  `object (`[PostgresImportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PostgresImportOptions)`)` Optional. Options for importing from a Cloud SQL for PostgreSQL instance.  
  
### Int32Value

JSON representation  
---  
      
    
    {
      "value": integer
    }  
  
Fields  
---  
`value` |  `integer` The int32 value.  
  
### PostgresImportOptions

JSON representation  
---  
      
    
    {
      "clean": boolean,
      "ifExists": boolean
    }  
  
Fields  
---  
`clean` |  `boolean` Optional. The --clean flag for the pg_restore utility. This flag applies only if you enabled Cloud SQL to import files in parallel.  
`ifExists` |  `boolean` Optional. The --if-exists flag for the pg_restore utility. This flag applies only if you enabled Cloud SQL to import files in parallel.  
  
### SqlTdeImportOptions

JSON representation  
---  
      
    
    {
      "certificatePath": string,
      "privateKeyPath": string,
      "privateKeyPassword": string,
      "name": string
    }  
  
Fields  
---  
`certificatePath` |  `string` Required. Path to the TDE certificate public key in the form gs://bucketName/fileName. The instance must have read access to the file. Applicable only for SQL Server instances.  
`privateKeyPath` |  `string` Required. Path to the TDE certificate private key in the form gs://bucketName/fileName. The instance must have read access to the file. Applicable only for SQL Server instances.  
`privateKeyPassword` |  `string` Required. Password that encrypts the private key.  
`name` |  `string` Required. Certificate name. Applicable only for SQL Server instances.  
  
### ExportContext

JSON representation  
---  
      
    
    {
      "uri": string,
      "databases": [
        string
      ],
      "kind": string,
      "sqlExportOptions": {
        object ([SqlExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlExportOptions))
      },
      "csvExportOptions": {
        object ([SqlCsvExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlCsvExportOptions))
      },
      "fileType": enum ([SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlFileType)),
      "offload": boolean,
      "bakExportOptions": {
        object ([SqlBakExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlBakExportOptions))
      },
      "tdeExportOptions": {
        object ([SqlTdeExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlTdeExportOptions))
      }
    }  
  
Fields  
---  
`uri` |  `string` The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form `gs://bucketName/fileName`. If the file already exists, the request succeeds, but the operation fails. If `fileType` is `SQL` and the filename ends with .gz, the contents are compressed.  
`databases[]` |  `string` Databases to be exported.   
`MySQL instances:` If `fileType` is `SQL` and no database is specified, all databases are exported, except for the `mysql` system database. If `fileType` is `CSV`, you can specify one database, either by using this property or by using the `csvExportOptions.selectQuery` property, which takes precedence over this property.   
`PostgreSQL instances:` If you don't specify a database by name, all user databases in the instance are exported. This excludes system databases and Cloud SQL databases used to manage internal operations. Exporting all user databases is only available for directory-formatted parallel export. If `fileType` is `CSV`, this database must match the one specified in the `csvExportOptions.selectQuery` property.   
`SQL Server instances:` You must specify one database to be exported, and the `fileType` must be `BAK`.  
`kind` |  `string` This is always `sql#exportContext`.  
`sqlExportOptions` |  `object (`[SqlExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlExportOptions)`)` Options for exporting data as SQL statements.  
`csvExportOptions` |  `object (`[SqlCsvExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlCsvExportOptions)`)` Options for exporting data as CSV. `MySQL` and `PostgreSQL` instances only.  
`fileType` |  `enum (`[SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlFileType)`)` The file type for the specified uri.  
`offload` |  `boolean` Whether to perform a serverless export.  
`bakExportOptions` |  `object (`[SqlBakExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlBakExportOptions)`)` Options for exporting data as BAK files.  
`tdeExportOptions` |  `object (`[SqlTdeExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlTdeExportOptions)`)` Optional. Export parameters specific to SQL Server TDE certificates  
  
### SqlExportOptions

JSON representation  
---  
      
    
    {
      "tables": [
        string
      ],
      "schemaOnly": boolean,
      "mysqlExportOptions": {
        object ([MysqlExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.MysqlExportOptions))
      },
      "threads": integer,
      "parallel": boolean,
      "postgresExportOptions": {
        object ([PostgresExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PostgresExportOptions))
      }
    }  
  
Fields  
---  
`tables[]` |  `string` Tables to export, or that were exported, from the specified database. If you specify tables, specify one and only one database. For PostgreSQL instances, you can specify only one table.  
`schemaOnly` |  `boolean` Export only schemas.  
`mysqlExportOptions` |  `object (`[MysqlExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.MysqlExportOptions)`)`  
`threads` |  `integer` Optional. The number of threads to use for parallel export.  
`parallel` |  `boolean` Optional. Whether or not the export should be parallel.  
`postgresExportOptions` |  `object (`[PostgresExportOptions](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PostgresExportOptions)`)` Optional. Options for exporting from a Cloud SQL for PostgreSQL instance.  
  
### MysqlExportOptions

JSON representation  
---  
      
    
    {
      "masterData": integer
    }  
  
Fields  
---  
`masterData` |  `integer` Option to include SQL statement required to set up replication. If set to `1`, the dump file includes a CHANGE MASTER TO statement with the binary log coordinates, and --set-gtid-purged is set to ON. If set to `2`, the CHANGE MASTER TO statement is written as a SQL comment and has no effect. If set to any value other than `1`, --set-gtid-purged is set to OFF.  
  
### PostgresExportOptions

JSON representation  
---  
      
    
    {
      "clean": boolean,
      "ifExists": boolean
    }  
  
Fields  
---  
`clean` |  `boolean` Optional. Use this option to include DROP `<object>` SQL statements. Use these statements to delete database objects before running the import operation.  
`ifExists` |  `boolean` Optional. Option to include an IF EXISTS SQL statement with each DROP statement produced by clean.  
  
### SqlCsvExportOptions

JSON representation  
---  
      
    
    {
      "selectQuery": string,
      "escapeCharacter": string,
      "quoteCharacter": string,
      "fieldsTerminatedBy": string,
      "linesTerminatedBy": string
    }  
  
Fields  
---  
`selectQuery` |  `string` The select query used to extract the data.  
`escapeCharacter` |  `string` Specifies the character that should appear before a data character that needs to be escaped.  
`quoteCharacter` |  `string` Specifies the quoting character to be used when a data value is quoted.  
`fieldsTerminatedBy` |  `string` Specifies the character that separates columns within each row (line) of the file.  
`linesTerminatedBy` |  `string` This is used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values.  
  
### SqlBakExportOptions

JSON representation  
---  
      
    
    {
      "striped": boolean,
      "stripeCount": integer,
      "bakType": enum ([BakType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.BakType)),
      "copyOnly": boolean,
      "differentialBase": boolean,
      "exportLogStartTime": string,
      "exportLogEndTime": string
    }  
  
Fields  
---  
`striped` |  `boolean` Whether or not the export should be striped.  
`stripeCount` |  `integer` Option for specifying how many stripes to use for the export. If blank, and the value of the striped field is true, the number of stripes is automatically chosen.  
`bakType` |  `enum (`[BakType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.BakType)`)` Type of this bak file will be export, FULL or DIFF, SQL Server only  
`copyOnly  
**(deprecated)**` |  `boolean` This item is deprecated!Deprecated: copy_only is deprecated. Use differential_base instead  
`differentialBase` |  `boolean` Whether or not the backup can be used as a differential base copy_only backup can not be served as differential base  
`exportLogStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The begin timestamp when transaction log will be included in the export operation. [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, `2023-10-01T16:19:00.094`) in UTC. When omitted, all available logs from the beginning of retention period will be included. Only applied to Cloud SQL for SQL Server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`exportLogEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The end timestamp when transaction log will be included in the export operation. [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, `2023-10-01T16:19:00.094`) in UTC. When omitted, all available logs until current time will be included. Only applied to Cloud SQL for SQL Server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SqlTdeExportOptions

JSON representation  
---  
      
    
    {
      "certificatePath": string,
      "privateKeyPath": string,
      "privateKeyPassword": string,
      "name": string
    }  
  
Fields  
---  
`certificatePath` |  `string` Required. Path to the TDE certificate public key in the form gs://bucketName/fileName. The instance must have write access to the bucket. Applicable only for SQL Server instances.  
`privateKeyPath` |  `string` Required. Path to the TDE certificate private key in the form gs://bucketName/fileName. The instance must have write access to the location. Applicable only for SQL Server instances.  
`privateKeyPassword` |  `string` Required. Password that encrypts the private key.  
`name` |  `string` Required. Certificate name. Applicable only for SQL Server instances.  
  
### BackupContext

JSON representation  
---  
      
    
    {
      "backupId": string,
      "kind": string,
      "name": string
    }  
  
Fields  
---  
`backupId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The identifier of the backup.  
`kind` |  `string` This is always `sql#backupContext`.  
`name` |  `string` The name of the backup. Format: projects/{project}/backups/{backup}  
  
### PreCheckMajorVersionUpgradeContext

JSON representation  
---  
      
    
    {
      "targetDatabaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_instance#Output.Schema.SqlDatabaseVersion)),
      "preCheckResponse": [
        {
          object ([PreCheckResponse](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PreCheckResponse))
        }
      ],
      "kind": string,
    
      // Union field _max_runtime can be only one of the following:
      "maxRuntime": string
      // End of list of possible types for union field _max_runtime.
    }  
  
Fields  
---  
`targetDatabaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_instance#Output.Schema.SqlDatabaseVersion)`)` Required. The target database version to upgrade to.  
`preCheckResponse[]` |  `object (`[PreCheckResponse](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.PreCheckResponse)`)` Output only. The responses from the precheck operation.  
`kind` |  `string` Optional. This is always `sql#preCheckMajorVersionUpgradeContext`.  
Union field `_max_runtime`.`_max_runtime` can be only one of the following:  
`maxRuntime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The maximum allowed runtime for the precheck operation.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### PreCheckResponse

JSON representation  
---  
      
    
    {
      "actionsRequired": [
        string
      ],
    
      // Union field _message can be only one of the following:
      "message": string
      // End of list of possible types for union field _message.
    
      // Union field _message_type can be only one of the following:
      "messageType": enum ([MessageType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.MessageType))
      // End of list of possible types for union field _message_type.
    }  
  
Fields  
---  
`actionsRequired[]` |  `string` The actions that the user needs to take. Use repeated for multiple actions.  
Union field `_message`.`_message` can be only one of the following:  
`message` |  `string` The message to be displayed to the user.  
Union field `_message_type`.`_message_type` can be only one of the following:  
`messageType` |  `enum (`[MessageType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.MessageType)`)` The type of message whether it is an info, warning, or error.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### StartWorkloadCaptureContext

JSON representation  
---  
      
    
    {
      "enableLiveReplay": boolean,
    
      // Union field _replay_instance can be only one of the following:
      "replayInstance": string
      // End of list of possible types for union field _replay_instance.
    }  
  
Fields  
---  
`enableLiveReplay` |  `boolean` Optional. If true, the captured workload is simultaneously executed on a separate, ephemeral Cloud SQL instance. This "live replay" instance is automatically provisioned and is cloned from the source instance. If false (the default), the workload is only stored and no live replay occurs. It can be replayed later using a separate `StartWorkloadReplayRequest`. Note: The workload capture runs continuously until an explicit `StopWorkloadCaptureRequest` is issued.  
Union field `_replay_instance`.`_replay_instance` can be only one of the following:  
`replayInstance` |  `string` Optional. Required if `enable_live_replay` is true. The name of the Cloud SQL instance where the captured workload (SQL queries) is being executed, excluding the project ID (for example, `my-replay-instance`). The instance name must start with a lowercase letter and contain only lowercase letters, numbers, and hyphens. The combined length of `project-ID:instance-name` must be 98 characters or less.  
  
### StopWorkloadCaptureContext

JSON representation  
---  
      
    
    {
      "abortLiveReplay": boolean
    }  
  
Fields  
---  
`abortLiveReplay` |  `boolean` Optional. If true, immediately aborts the concurrent live replay and discards any un-replayed traffic alongside stopping the capture. If false (the default), the capture stops recording new traffic, but the live replay will continue executing until the entire backlog of captured traffic has been replayed.  
  
### StartWorkloadReplayContext

JSON representation  
---  
      
    
    {
      "replayInstance": string,
      "workloadId": string
    }  
  
Fields  
---  
`replayInstance` |  `string` Required. The name of the Cloud SQL instance where the captured workload (SQL queries) is being executed, excluding the project ID (for example, `my-replay-instance`). The instance name must start with a lowercase letter and contain only lowercase letters, numbers, and hyphens. The combined length of `project-ID:instance-name` must be 98 characters or less.  
`workloadId` |  `string` Output only. The ID of the workload to start executing on the replay instance. Each workload capture generates a unique ID in the format `workload-<epoch_timestamp>` (for example, `workload-1786046400`). Use this ID to start executing the recorded SQL queries.  
  
### AcquireSsrsLeaseContext

JSON representation  
---  
      
    
    {
    
      // Union field _setup_login can be only one of the following:
      "setupLogin": string
      // End of list of possible types for union field _setup_login.
    
      // Union field _service_login can be only one of the following:
      "serviceLogin": string
      // End of list of possible types for union field _service_login.
    
      // Union field _report_database can be only one of the following:
      "reportDatabase": string
      // End of list of possible types for union field _report_database.
    
      // Union field _duration can be only one of the following:
      "duration": string
      // End of list of possible types for union field _duration.
    }  
  
Fields  
---  
Union field `_setup_login`.`_setup_login` can be only one of the following:  
`setupLogin` |  `string` The username to be used as the setup login to connect to the database server for SSRS setup.  
Union field `_service_login`.`_service_login` can be only one of the following:  
`serviceLogin` |  `string` The username to be used as the service login to connect to the report database for SSRS setup.  
Union field `_report_database`.`_report_database` can be only one of the following:  
`reportDatabase` |  `string` The report database to be used for SSRS setup.  
Union field `_duration`.`_duration` can be only one of the following:  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Lease duration needed for SSRS setup.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### SqlSubOperationType

JSON representation  
---  
      
    
    {
    
      // Union field sub_operation_details can be only one of the following:
      "maintenanceType": enum ([SqlMaintenanceType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlMaintenanceType))
      // End of list of possible types for union field sub_operation_details.
    }  
  
Fields  
---  
Union field `sub_operation_details`. Sub operation details corresponding to the operation type. `sub_operation_details` can be only one of the following:  
`maintenanceType` |  `enum (`[SqlMaintenanceType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance#Output.Schema.SqlMaintenanceType)`)` The type of maintenance to be performed on the instance.  
  
### SqlOperationStatus

The status of an operation.

Enums  
---  
`SQL_OPERATION_STATUS_UNSPECIFIED` | The state of the operation is unknown.  
`PENDING` | The operation has been queued, but has not started yet.  
`RUNNING` | The operation is running.  
`DONE` | The operation completed.  
  
### SqlApiWarningCode

Enums  
---  
`SQL_API_WARNING_CODE_UNSPECIFIED` | An unknown or unset warning type from Cloud SQL API.  
`REGION_UNREACHABLE` | Warning when one or more regions are not reachable. The returned result set may be incomplete.  
`MAX_RESULTS_EXCEEDS_LIMIT` | Warning when user provided maxResults parameter exceeds the limit. The returned result set may be incomplete.  
`COMPROMISED_CREDENTIALS` | Warning when user tries to create/update a user with credentials that have previously been compromised by a public data breach.  
`INTERNAL_STATE_FAILURE` | Warning when the operation succeeds but some non-critical workflow state failed.  
  
### SqlOperationType

The type of Cloud SQL operation.

Enums  
---  
`SQL_OPERATION_TYPE_UNSPECIFIED` | Unknown operation type.  
`IMPORT` | Imports data into a Cloud SQL instance.  
`EXPORT` | Exports data from a Cloud SQL instance to a Cloud Storage bucket.  
`CREATE` | Creates a new Cloud SQL instance.  
`UPDATE` | Updates the settings of a Cloud SQL instance.  
`DELETE` | Deletes a Cloud SQL instance.  
`RESTART` | Restarts the Cloud SQL instance.  
`BACKUP` |   
`SNAPSHOT` |   
`BACKUP_VOLUME` | Performs instance backup.  
`DELETE_VOLUME` | Deletes an instance backup.  
`RESTORE_VOLUME` | Restores an instance backup.  
`INJECT_USER` | Injects a privileged user in mysql for MOB instances.  
`CLONE` | Clones a Cloud SQL instance.  
`STOP_REPLICA` | Stops replication on a Cloud SQL read replica instance.  
`START_REPLICA` | Starts replication on a Cloud SQL read replica instance.  
`PROMOTE_REPLICA` | Promotes a Cloud SQL replica instance.  
`CREATE_REPLICA` | Creates a Cloud SQL replica instance.  
`CREATE_USER` | Creates a new user in a Cloud SQL instance.  
`DELETE_USER` | Deletes a user from a Cloud SQL instance.  
`UPDATE_USER` | Updates an existing user in a Cloud SQL instance. If a user with the specified username doesn't exist, a new user is created.  
`CREATE_DATABASE` | Creates a database in the Cloud SQL instance.  
`DELETE_DATABASE` | Deletes a database in the Cloud SQL instance.  
`UPDATE_DATABASE` | Updates a database in the Cloud SQL instance.  
`FAILOVER` | Performs failover of an HA-enabled Cloud SQL failover replica.  
`DELETE_BACKUP` | Deletes the backup taken by a backup run.  
`RECREATE_REPLICA` |   
`TRUNCATE_LOG` | Truncates a general or slow log table in MySQL.  
`DEMOTE_MASTER` | Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.  
`MAINTENANCE` | Indicates that the instance is currently in maintenance. Maintenance typically causes the instance to be unavailable for 1-3 minutes.  
`ENABLE_PRIVATE_IP` | This field is deprecated, and will be removed in future version of API.  
`DEFER_MAINTENANCE` |   
`CREATE_CLONE` | Creates clone instance.  
`RESCHEDULE_MAINTENANCE` | Reschedule maintenance to another time.  
`START_EXTERNAL_SYNC` | Starts external sync of a Cloud SQL EM replica to an external primary instance.  
`LOG_CLEANUP` | Recovers logs from an instance's old data disk.  
`AUTO_RESTART` | Performs auto-restart of an HA-enabled Cloud SQL database for auto recovery.  
`REENCRYPT` | Re-encrypts CMEK instances with latest key version.  
`SWITCHOVER` | Switches the roles of the primary and replica pair. The target instance should be the replica.  
`UPDATE_BACKUP` | Update a backup.  
`ACQUIRE_SSRS_LEASE` | Acquire a lease for the setup of SQL Server Reporting Services (SSRS).  
`RELEASE_SSRS_LEASE` | Release a lease for the setup of SQL Server Reporting Services (SSRS).  
`RECONFIGURE_OLD_PRIMARY` | Reconfigures old primary after a promote replica operation. Effect of a promote operation to the old primary is executed in this operation, asynchronously from the promote replica operation executed to the replica.  
`CLUSTER_MAINTENANCE` | Indicates that the instance, its read replicas, and its cascading replicas are in maintenance. Maintenance typically gets initiated on groups of replicas first, followed by the primary instance. For each instance, maintenance typically causes the instance to be unavailable for 1-3 minutes.  
`SELF_SERVICE_MAINTENANCE` | Indicates that the instance (and any of its replicas) are currently in maintenance. This is initiated as a self-service request by using SSM. Maintenance typically causes the instance to be unavailable for 1-3 minutes.  
`SWITCHOVER_TO_REPLICA` | Switches a primary instance to a replica. This operation runs as part of a switchover operation to the original primary instance.  
`MAJOR_VERSION_UPGRADE` | Updates the major version of a Cloud SQL instance.  
`ADVANCED_BACKUP` | Deprecated: ADVANCED_BACKUP is deprecated. Use ENHANCED_BACKUP instead.  
`MANAGE_BACKUP` | Changes the BackupTier of a Cloud SQL instance.  
`ENHANCED_BACKUP` | Creates a backup for an Enhanced BackupTier Cloud SQL instance.  
`REPAIR_READ_POOL` | Repairs entire read pool or specified read pool nodes in the read pool.  
`CREATE_READ_POOL` | Creates a Cloud SQL read pool instance.  
`PRE_CHECK_MAJOR_VERSION_UPGRADE` | Pre-checks the major version upgrade operation.  
`SETUP_MIGRATION` | This operation type represents individual steps in a multi-step setup migration workflow: including configuration, replication, switchover/back, and data reseeding, as defined by operation's intent.  
`CREATE_BLUE_GREEN_DEPLOYMENT` | Creates a new Blue-Green deployment.  
`SWITCHOVER_BLUE_GREEN_DEPLOYMENT` | Switches over a Blue-Green deployment.  
`DELETE_BLUE_GREEN_DEPLOYMENT` | Deletes a Blue-Green deployment.  
  
### SqlFileType

Enums  
---  
`SQL_FILE_TYPE_UNSPECIFIED` | Unknown file type.  
`SQL` | File containing SQL statements.  
`CSV` | File in CSV format.  
`BAK` |   
`TDE` | TDE certificate.  
  
### BakType

Enums  
---  
`BAK_TYPE_UNSPECIFIED` | Default type.  
`FULL` | Full backup.  
`DIFF` | Differential backup.  
`TLOG` | Transaction Log backup  
  
### SqlDatabaseVersion

The database engine type and version.

Enums  
---  
`SQL_DATABASE_VERSION_UNSPECIFIED` | This is an unknown database version.  
`MYSQL_5_1` | The database version is MySQL 5.1.  
`MYSQL_5_5` | The database version is MySQL 5.5.  
`MYSQL_5_6` | The database version is MySQL 5.6.  
`MYSQL_5_7` | The database version is MySQL 5.7.  
`MYSQL_8_0` | The database version is MySQL 8.  
`MYSQL_8_0_18` | The database major version is MySQL 8.0 and the minor version is 18.  
`MYSQL_8_0_26` | The database major version is MySQL 8.0 and the minor version is 26.  
`MYSQL_8_0_27` | The database major version is MySQL 8.0 and the minor version is 27.  
`MYSQL_8_0_28` | The database major version is MySQL 8.0 and the minor version is 28.  
`MYSQL_8_0_29` | The database major version is MySQL 8.0 and the minor version is 29.  
`MYSQL_8_0_30` | The database major version is MySQL 8.0 and the minor version is 30.  
`MYSQL_8_0_31` | The database major version is MySQL 8.0 and the minor version is 31.  
`MYSQL_8_0_32` | The database major version is MySQL 8.0 and the minor version is 32.  
`MYSQL_8_0_33` | The database major version is MySQL 8.0 and the minor version is 33.  
`MYSQL_8_0_34` | The database major version is MySQL 8.0 and the minor version is 34.  
`MYSQL_8_0_35` | The database major version is MySQL 8.0 and the minor version is 35.  
`MYSQL_8_0_36` | The database major version is MySQL 8.0 and the minor version is 36.  
`MYSQL_8_0_37` | The database major version is MySQL 8.0 and the minor version is 37.  
`MYSQL_8_0_39` | The database major version is MySQL 8.0 and the minor version is 39.  
`MYSQL_8_0_40` | The database major version is MySQL 8.0 and the minor version is 40.  
`MYSQL_8_0_41` | The database major version is MySQL 8.0 and the minor version is 41.  
`MYSQL_8_0_42` | The database major version is MySQL 8.0 and the minor version is 42.  
`MYSQL_8_0_43` | The database major version is MySQL 8.0 and the minor version is 43.  
`MYSQL_8_0_44` | The database major version is MySQL 8.0 and the minor version is 44.  
`MYSQL_8_0_45` | The database major version is MySQL 8.0 and the minor version is 45.  
`MYSQL_8_0_46` | The database major version is MySQL 8.0 and the minor version is 46.  
`MYSQL_8_4` | The database version is MySQL 8.4.  
`MYSQL_9_7` | The database version is MySQL 9.7.  
`SQLSERVER_2017_STANDARD` | The database version is SQL Server 2017 Standard.  
`SQLSERVER_2017_ENTERPRISE` | The database version is SQL Server 2017 Enterprise.  
`SQLSERVER_2017_EXPRESS` | The database version is SQL Server 2017 Express.  
`SQLSERVER_2017_WEB` | The database version is SQL Server 2017 Web.  
`POSTGRES_9_6` | The database version is PostgreSQL 9.6.  
`POSTGRES_10` | The database version is PostgreSQL 10.  
`POSTGRES_11` | The database version is PostgreSQL 11.  
`POSTGRES_12` | The database version is PostgreSQL 12.  
`POSTGRES_13` | The database version is PostgreSQL 13.  
`POSTGRES_14` | The database version is PostgreSQL 14.  
`POSTGRES_15` | The database version is PostgreSQL 15.  
`POSTGRES_16` | The database version is PostgreSQL 16.  
`POSTGRES_17` | The database version is PostgreSQL 17.  
`POSTGRES_18` | The database version is PostgreSQL 18.  
`POSTGRES_19` | The database version is PostgreSQL 19.  
`POSTGRES_20` | The database version is PostgreSQL 20.  
`SQLSERVER_2019_STANDARD` | The database version is SQL Server 2019 Standard.  
`SQLSERVER_2019_ENTERPRISE` | The database version is SQL Server 2019 Enterprise.  
`SQLSERVER_2019_EXPRESS` | The database version is SQL Server 2019 Express.  
`SQLSERVER_2019_WEB` | The database version is SQL Server 2019 Web.  
`SQLSERVER_2022_STANDARD` | The database version is SQL Server 2022 Standard.  
`SQLSERVER_2022_ENTERPRISE` | The database version is SQL Server 2022 Enterprise.  
`SQLSERVER_2022_EXPRESS` | The database version is SQL Server 2022 Express.  
`SQLSERVER_2022_WEB` | The database version is SQL Server 2022 Web.  
`SQLSERVER_2025_STANDARD` | The database version is SQL Server 2025 Standard.  
`SQLSERVER_2025_ENTERPRISE` | The database version is SQL Server 2025 Enterprise.  
`SQLSERVER_2025_EXPRESS` | The database version is SQL Server 2025 Express.  
  
### MessageType

The type of message which can be an info, a warning, or an error that requires user intervention.

Enums  
---  
`MESSAGE_TYPE_UNSPECIFIED` | Default unspecified value to prevent unintended behavior changes.  
`INFO` | General informational messages that don't require action.  
`WARNING` | Warnings that might impact the upgrade but don't block it.  
`ERROR` | Errors that a user must resolve before proceeding with the upgrade.  
  
### SqlMaintenanceType

The type of maintenance to be performed on the instance.

Enums  
---  
`SQL_MAINTENANCE_TYPE_UNSPECIFIED` | Maintenance type is unspecified.  
`INSTANCE_MAINTENANCE` | Indicates that a standalone instance is undergoing maintenance. The instance can be either a primary instance or a replica.  
`REPLICA_INCLUDED_MAINTENANCE` | Indicates that the primary instance and all of its replicas, including cascading replicas, are undergoing maintenance. Maintenance is performed on groups of replicas first, followed by the primary instance.  
`INSTANCE_SELF_SERVICE_MAINTENANCE` | Indicates that the standalone instance is undergoing maintenance, initiated by self-service. The instance can be either a primary instance or a replica.  
`REPLICA_INCLUDED_SELF_SERVICE_MAINTENANCE` | Indicates that the primary instance and all of its replicas are undergoing maintenance, initiated by self-service. Maintenance is performed on groups of replicas first, followed by the primary instance.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
