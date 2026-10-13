---
url: https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/restore_cluster/
title: MCP Tools Reference: alloydb \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:12.918328+00:00
---

# MCP Tools Reference: alloydb  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/restore_cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Reference ](https://docs.cloud.google.com/alloydb/docs/reference/rest)



Send feedback 

#  MCP Tools Reference: alloydb Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `restore_cluster`

Restores an AlloyDB cluster from a given backup or a source cluster and a timestamp.

**_Requirements_**

  * Depending on the source type, the requirements are different.
  * For a backup source, the backup resource must exist. The backup resource can be created on-demand or from an automated system.
  * For a continuous backup (also known as PITR) source, the source cluster must exist and have continuous backup enabled.
  * For a backup and disaster recovery source, the backup resource must exist inside the backup vault.
  * For a backup and disaster recovery point in time recovery source, the data source must exist inside the backup vault.



**_Usage_**

  1. Call `create_backup` to create an on-demand backup if needed.
  2. Call `restore_cluster` to restore a cluster from a given backup or a source cluster and a timestamp.
  3. This will return a long-running operation that indicates the progress of the cluster restoration. The time taken for the operation to complete depends on the size of the backup or the source cluster.
  4. You can poll the status of the operation using the `get_operation` tool.
  5. Once the long-running operation is complete, the new cluster will be in a READY state.



The following sample demonstrate how to use `curl` to invoke the `restore_cluster` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://alloydb.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "restore_cluster",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Message for restoring a Cluster from a backup or another cluster at a given point in time.

### RestoreClusterRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "clusterId": string,
    
      // Union field source can be only one of the following:
      "backupSource": {
        object ([BackupSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/list_clusters#Output.Schema.BackupSource))
      },
      "continuousBackupSource": {
        object ([ContinuousBackupSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/restore_cluster#Input.Schema.ContinuousBackupSource))
      },
      "backupdrBackupSource": {
        object ([BackupDrBackupSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/list_clusters#Output.Schema.BackupDrBackupSource))
      },
      "backupdrPitrSource": {
        object ([BackupDrPitrSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/restore_cluster#Input.Schema.BackupDrPitrSource))
      }
      // End of list of possible types for union field source.
    
      // Union field _psc_enabled can be only one of the following:
      "pscEnabled": boolean
      // End of list of possible types for union field _psc_enabled.
    
      // Union field _network can be only one of the following:
      "network": string
      // End of list of possible types for union field _network.
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent resource in which to create the backup. The value must have a format of projects/{project}/locations/{location}. - {project} is the project that the backup resides in. This field can be specified either as: - Project ID: An alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. - Project number: A valid base-10 encoded positive integer. - {location} is the Google Cloud region that the backup resides in. Regions will have format like "us-central1" or "us-west2". The field is REQUIRED.  
`clusterId` |  `string` Required. The cluster ID is the unique user-assigned ID of the restored cluster. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash characters ("-"). This field is REQUIRED.  
Union field `source`. The source to restore the cluster from. This field is REQUIRED. `source` can be only one of the following:  
`backupSource` |  `object (`[BackupSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/list_clusters#Output.Schema.BackupSource)`)` AlloyDB backup to restore from. This must either be the full backup name or the backup_id. In the second case, the project and location are assumed to be the same as the restored clusters that is being created. If using the full backup name, then it must be in the format of projects/{project}/locations/{location}/backups/{backup_id}. - {project} is the project that the backup resides in. This field can be specified either as: - Project ID: An alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. - Project number: A valid base-10 encoded positive integer. - {location} is the Google Cloud region that the backup resides in. Regions will have format like "us-central1" or "us-west2". - {backup_id} is the ID of the backup. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ('-') characters.  
`continuousBackupSource` |  `object (`[ContinuousBackupSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/restore_cluster#Input.Schema.ContinuousBackupSource)`)` The continuous backup source can be specified to use a source cluster from which to restore, and the point in time to restore to. Continuous backup needs to be enabled in the source cluster for this operation to succeed. The source cluster needs to be in the format of projects/{project}/locations/{location}/clusters/{cluster_id}. - {project} is the project that the cluster resides in. This field can be specified either as: - Project ID: An alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. - Project number: A valid base-10 encoded positive integer. - {location} is the Google Cloud region that the cluster resides in. Regions will have format like "us-central1" or "us-west2". - {cluster_id} is the ID of the cluster. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ('-') characters. The point in time to restore to needs to in RFC 3339 format where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30".  
`backupdrBackupSource` |  `object (`[BackupDrBackupSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/list_clusters#Output.Schema.BackupDrBackupSource)`)` Backup and Disaster Recovery backup source. The name of the backup resource must be in the format of projects/{project}/locations/{location}/backupVaults/{backupvault_id}/dataSources/{datasource_id}/backups/{backup_id}. - {project} is the project that the backup resides in. This field can be specified either as: - Project ID: An alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. - Project number: A valid base-10 encoded positive integer. - {location} is the Google Cloud region that the backup resides in. Regions will have format like "us-central1" or "us-west2". - {backupvault_id} is the ID of the backup vault. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. It must be between 3-63 characters long. - {datasource_id} is the ID of the data source. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. It must be between 3-63 characters long. - {backup_id} is the ID of the backup. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ('-') characters.  
`backupdrPitrSource` |  `object (`[BackupDrPitrSource](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/restore_cluster#Input.Schema.BackupDrPitrSource)`)` Backup and Disaster Recovery source used for point in time recovery. The name of the backup resource with the format: projects/{project}/locations/{location}/backupVaults/{backupvault_id}/dataSources/{datasource_id}. - {project} is the project that the backup resides in. This field can be specified either as: - Project ID: An alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. - Project number: A valid base-10 encoded positive integer. - {location} is the Google Cloud region that the backup resides in. Regions will have format like "us-central1" or "us-west2". - {backupvault_id} is the ID of the backup vault. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. It must be between 3-63 characters long. - {datasource_id} is the ID of the data source. It should be an alphanumeric string that can consist of lowercase letters, numerical digits, or dash ("-") characters. It must be between 3-63 characters long. The point in time to restore to needs to in RFC 3339 format where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z", "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30".  
Union field `_psc_enabled`.`_psc_enabled` can be only one of the following:  
`pscEnabled` |  `boolean` Configures whether Private Service Connect is enabled for the cluster. This field is OPTIONAL. If neither network nor psc_enabled is specified, the default behavior will be to enable Private Service Connect.  
Union field `_network`.`_network` can be only one of the following:  
`network` |  `string` The network is the VPC network that the cluster will reside in. Specifying this field will enable Private Google Access. This field is OPTIONAL, and if specified, it should have format like "projects/{project}/global/networks/{network_id}". This field should not be specified if psc_enabled is true.  
  
### BackupSource

JSON representation  
---  
      
    
    {
      "backupUid": string,
      "backupName": string
    }  
  
Fields  
---  
`backupUid` |  `string` Output only. The system-generated UID of the backup which was used to create this resource. The UID is generated when the backup is created, and it is retained until the backup is deleted.  
`backupName` |  `string` Required. The name of the backup resource with the format: * projects/{project}/locations/{region}/backups/{backup_id}  
  
### ContinuousBackupSource

JSON representation  
---  
      
    
    {
      "cluster": string,
      "pointInTime": string
    }  
  
Fields  
---  
`cluster` |  `string` Required. The source cluster from which to restore. This cluster must have continuous backup enabled for this operation to succeed. For the required format, see the comment on the Cluster.name field.  
`pointInTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The point in time to restore to.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### BackupDrBackupSource

JSON representation  
---  
      
    
    {
      "backup": string
    }  
  
Fields  
---  
`backup` |  `string` Required. The name of the backup resource with the format: * projects/{project}/locations/{location}/backupVaults/{backupvault_id}/dataSources/{datasource_id}/backups/{backup_id}  
  
### BackupDrPitrSource

JSON representation  
---  
      
    
    {
      "dataSource": string,
      "pointInTime": string
    }  
  
Fields  
---  
`dataSource` |  `string` Required. The name of the backup resource with the format: * projects/{project}/locations/{location}/backupVaults/{backupvault_id}/dataSources/{datasource_id}  
`pointInTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The point in time to restore to.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
        object ([Status](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/create_cluster#Output.Schema.Status))
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
`error` |  `object (`[Status](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/create_cluster#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
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

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
