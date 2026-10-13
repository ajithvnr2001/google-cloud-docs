---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:54.966215+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_autonomous_database`

Create an Autonomous Database (ADB). This request can be used to create a new ADB instance or a clone of an existing ADB or an ADB Disaster Recovery (DR) instance. If the source config is not specified, a new ADB instance is created. If the source config is specified, a clone of the source is created. If the source is specified and the source is an ADB DR instance, then a new ADB DR instance is created. While creating a new ADB instance, it can have Public IP support or Private IP support. In case of Private IP support, the request should contain the ODBSubnetwork details. If a request is Public IP mLTS is required mandatorily.

The following sample demonstrate how to use `curl` to invoke the `create_autonomous_database` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_autonomous_database",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for CreateAutonomousDatabase.

### CreateAutonomousDatabaseRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "autonomousDatabase": {
        object ([AutonomousDatabase](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Input.Schema.AutonomousDatabase))
      },
      "autonomousDatabaseId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the project to create the ADB in. Format: `projects/{project}/locations/{location}`  
`autonomousDatabase` |  `object (`[AutonomousDatabase](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Input.Schema.AutonomousDatabase)`)` Required. The ADB to create.  
`autonomousDatabaseId` |  `string` Required. The ID to use for the ADB that is being created.  
  
### AutonomousDatabase

JSON representation  
---  
      
    
    {
      "name": string,
      "database": string,
      "displayName": string,
      "adminPasswordSecretVersion": string,
      "odbSubnet": string,
      "sourceConfig": {
        object ([SourceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Input.Schema.SourceConfig))
      },
      "computeCount": number,
      "dataStorageSizeTb": integer,
      "dataStorageSizeGb": integer,
      "dbWorkload": enum (DBWorkload),
      "dbEdition": enum (DatabaseEdition),
      "characterSet": string,
      "nCharacterSet": string,
      "dbVersion": string,
      "isAutoScalingEnabled": boolean,
      "isStorageAutoScalingEnabled": boolean,
      "licenseType": enum (LicenseType),
      "mtlsConnectionRequired": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the ADB. Format: `projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}`  
`database` |  `string` Optional. Immutable. The name of the Autonomous Database. The database name must be unique in the project. The name must begin with a letter and can contain a maximum of 30 alphanumeric characters.  
`displayName` |  `string` Optional. Immutable. The display name for the Autonomous Database. The name does not have to be unique within your project.  
`adminPasswordSecretVersion` |  `string` Optional. Immutable. The resource name of a secret version in Secret Manager which contains the database admin user's password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
`odbSubnet` |  `string` Optional. Immutable. The name of the OdbSubnet associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`sourceConfig` |  `object (`[SourceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Input.Schema.SourceConfig)`)` Optional. Immutable. The source Autonomous Database configuration for the standby Autonomous Database. The source Autonomous Database is configured while creating the Peer Autonomous Database or a clone and can't be updated after creation.  
`computeCount` |  `number` Optional. Immutable. The number of compute servers for the Autonomous Database.  
`dataStorageSizeTb` |  `integer` Optional. Immutable. The size of the data stored in the database, in terabytes.  
`dataStorageSizeGb` |  `integer` Optional. Immutable. The size of the data stored in the database, in gigabytes.  
`dbWorkload` |  `enum (`DBWorkload`)` Optional. Immutable. The workload type of the Autonomous Database.  
`dbEdition` |  `enum (`DatabaseEdition`)` Optional. Immutable. The edition of the Autonomous Databases.  
`characterSet` |  `string` Optional. Immutable. The character set for the Autonomous Database. The default is AL32UTF8.  
`nCharacterSet` |  `string` Optional. Immutable. The national character set for the Autonomous Database. The default is AL16UTF16.  
`dbVersion` |  `string` Optional. Immutable. The Oracle Database version for the Autonomous Database.  
`isAutoScalingEnabled` |  `boolean` Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database CPU core count.  
`isStorageAutoScalingEnabled` |  `boolean` Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database storage.  
`licenseType` |  `enum (`LicenseType`)` Required. Immutable. The license type used for the Autonomous Database.  
`mtlsConnectionRequired` |  `boolean` Optional. Immutable. This field specifies if the Autonomous Database requires mTLS connections.  
  
### SourceConfig

JSON representation  
---  
      
    
    {
      "autonomousDatabase": string,
      "automaticBackupsReplicationEnabled": boolean,
      "sourceType": enum (SourceType),
      "cloneType": enum (CloneType),
      "refreshableMode": enum (RefreshableMode),
      "autoRefreshFrequencySeconds": integer,
      "autoRefreshPointLagSeconds": integer,
      "autoRefreshStartTime": string,
      "autonomousDatabaseBackup": string,
      "backupTime": string,
      "useLatestAvailableBackup": boolean
    }  
  
Fields  
---  
`autonomousDatabase` |  `string` Optional. The name of the primary Autonomous Database that is used to create a Peer Autonomous Database from a source.  
`automaticBackupsReplicationEnabled` |  `boolean` Optional. This field specifies if the replication of automatic backups is enabled when creating a Data Guard.  
`sourceType` |  `enum (`SourceType`)` Optional. The source type of the Autonomous Database.  
`cloneType` |  `enum (`CloneType`)` Optional. The clone type of the Autonomous Database. This field is only applicable in case of cloning  
`refreshableMode` |  `enum (`RefreshableMode`)` Optional. The refresh mode of the clone.  
`autoRefreshFrequencySeconds` |  `integer` Optional. The frequency in seconds a refreshable clone is refreshed after auto-refresh is enabled.  
`autoRefreshPointLagSeconds` |  `integer` Optional. The time, in seconds, the data of the automatic refreshable clone lags the primary database at the point of refresh.  
`autoRefreshStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The date and time that auto-refreshing will begin for an Autonomous Database refreshable clone. This value controls only the start time for the first refresh operation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`autonomousDatabaseBackup` |  `string` Optional. The name of the Autonomous Database Backup resource with the format: projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomous_database_backup} Required when source_type is BACKUP_FROM_ID.  
`backupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The timestamp specified for the point-in-time clone of the source Autonomous Database. This field is only applicable in case of BACKUP_FROM_TIMESTAMP source type and when use_latest_available_backup is false.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`useLatestAvailableBackup` |  `boolean` Optional. Clone from latest available backup timestamp. This field is only applicable in case of BACKUP_FROM_TIMESTAMP source type.  
  
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
  
## Output Schema

This resource represents a long-running operation that is the result of a network API call.

### Operation

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Output.Schema.Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
