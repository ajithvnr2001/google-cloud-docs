---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backups/
title: MCP Tools Reference: memorystore.googleapis.com \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:49.970542+00:00
---

# MCP Tools Reference: memorystore.googleapis.com  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  MCP Tools Reference: memorystore.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_backups`

List all Memorystore for Valkey backups.

The following sample demonstrate how to use `curl` to invoke the `list_backups` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://memorystore.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_backups",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for `ListBackups`.

### ListBackupsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}`  
`pageSize` |  `integer` Optional. The maximum number of items to return.If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more clusters left to be queried.  
`pageToken` |  `string` Optional. The `next_page_token` value returned from a previous `ListBackupCollections` request, if any.  
  
## Output Schema

Response for `ListBackups`.

### ListBackupsResponse

JSON representation  
---  
      
    
    {
      "backups": [
        {
          object ([Backup](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backups#Output.Schema.Backup))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backups[]` |  `object (`[Backup](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backups#Output.Schema.Backup)`)` A list of backups in the project.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Backups that could not be reached.  
  
### Backup

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "instance": string,
      "instanceUid": string,
      "totalSizeBytes": string,
      "expireTime": string,
      "engineVersion": string,
      "backupFiles": [
        {
          object ([BackupFile](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backups#Output.Schema.BackupFile))
        }
      ],
      "nodeType": enum (NodeType),
      "replicaCount": integer,
      "shardCount": integer,
      "backupType": enum (BackupType),
      "state": enum (State),
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.EncryptionInfo))
      },
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`instance` |  `string` Output only. Instance resource path of this backup.  
`instanceUid` |  `string` Output only. Instance uid of this backup.  
`totalSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total size of the backup in bytes.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup will expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`engineVersion` |  `string` Output only. valkey-7.5/valkey-8.0, etc.  
`backupFiles[]` |  `object (`[BackupFile](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backups#Output.Schema.BackupFile)`)` Output only. List of backup files of the backup.  
`nodeType` |  `enum (`NodeType`)` Output only. Node type of the instance.  
`replicaCount` |  `integer` Output only. Number of replicas for the instance.  
`shardCount` |  `integer` Output only. Number of shards for the instance.  
`backupType` |  `enum (`BackupType`)` Output only. Type of the backup.  
`state` |  `enum (`State`)` Output only. State of the backup.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.EncryptionInfo)`)` Output only. Encryption information of the backup.  
`uid` |  `string` Output only. System assigned unique identifier of the backup.  
  
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
  
### BackupFile

JSON representation  
---  
      
    
    {
      "fileName": string,
      "sizeBytes": string,
      "createTime": string
    }  
  
Fields  
---  
`fileName` |  `string` Output only. e.g: .rdb  
`sizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size of the backup file in bytes.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup file was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### EncryptionInfo

JSON representation  
---  
      
    
    {
      "encryptionType": enum (Type),
      "kmsKeyVersions": [
        string
      ],
      "kmsKeyPrimaryState": enum (KmsKeyState),
      "lastUpdateTime": string
    }  
  
Fields  
---  
`encryptionType` |  `enum (`Type`)` Output only. Type of encryption.  
`kmsKeyVersions[]` |  `string` Output only. KMS key versions that are being used to protect the data at-rest.  
`kmsKeyPrimaryState` |  `enum (`KmsKeyState`)` Output only. The state of the primary version of the KMS key perceived by the system. This field is not populated in backups.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time when the encryption info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
