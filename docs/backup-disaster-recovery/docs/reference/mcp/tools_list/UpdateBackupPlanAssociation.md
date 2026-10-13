---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/UpdateBackupPlanAssociation/
title: MCP Tools Reference: backupdr.googleapis.com \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:31.402164+00:00
---

# MCP Tools Reference: backupdr.googleapis.com  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/UpdateBackupPlanAssociation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  MCP Tools Reference: backupdr.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `UpdateBackupPlanAssociation`

Updates an existing BackupPlanAssociation.

The following sample demonstrate how to use `curl` to invoke the `UpdateBackupPlanAssociation` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://backupdr.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "UpdateBackupPlanAssociation",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for updating a backup plan association.

### UpdateBackupPlanAssociationRequest

JSON representation  
---  
      
    
    {
      "backupPlanAssociation": {
        object ([BackupPlanAssociation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.BackupPlanAssociation))
      },
      "updateMask": string,
      "requestId": string
    }  
  
Fields  
---  
`backupPlanAssociation` |  `object (`[BackupPlanAssociation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.BackupPlanAssociation)`)` Required. The resource being updated  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlanAssociation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently backup_plan_association.backup_plan is the only supported field.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### BackupPlanAssociation

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceType": string,
      "resource": string,
      "backupPlan": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.State)),
      "rulesConfigInfo": [
        {
          object ([RuleConfigInfo](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.RuleConfigInfo))
        }
      ],
      "dataSource": string,
      "backupPlanRevisionId": string,
      "backupPlanRevisionName": string,
    
      // Union field resource_properties can be only one of the following:
      "cloudSqlInstanceBackupPlanAssociationProperties": {
        object ([CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.CloudSqlInstanceBackupPlanAssociationProperties))
      },
      "filestoreInstanceBackupPlanAssociationProperties": {
        object ([FilestoreInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.FilestoreInstanceBackupPlanAssociationProperties))
      },
      "alloydbClusterBackupPlanAssociationProperties": {
        object ([AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.AlloyDBClusterBackupPlanAssociationProperties))
      }
      // End of list of possible types for union field resource_properties.
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}  
`resourceType` |  `string` Required. Immutable. Resource type of workload on which backupplan is applied  
`resource` |  `string` Required. Immutable. Resource name of workload on which the backup plan is applied.The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance").  
`backupPlan` |  `string` Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.State)`)` Output only. The BackupPlanAssociation resource state.  
`rulesConfigInfo[]` |  `object (`[RuleConfigInfo](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.RuleConfigInfo)`)` Output only. The config info related to backup rules.  
`dataSource` |  `string` Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}  
`backupPlanRevisionId` |  `string` Output only. The user friendly revision ID of the `BackupPlanRevision`.Example: v0, v1, v2, etc.  
`backupPlanRevisionName` |  `string` Output only. The resource id of the `BackupPlanRevision`.Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`  
Union field `resource_properties`. Properties of the protected Google Cloud resource. `resource_properties` can be only one of the following:  
`cloudSqlInstanceBackupPlanAssociationProperties` |  `object (`[CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.CloudSqlInstanceBackupPlanAssociationProperties)`)` Output only. Cloud SQL instance's backup plan association properties.  
`filestoreInstanceBackupPlanAssociationProperties` |  `object (`[FilestoreInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.FilestoreInstanceBackupPlanAssociationProperties)`)` Output only. Filestore instance's backup plan association properties.  
`alloydbClusterBackupPlanAssociationProperties` |  `object (`[AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.AlloyDBClusterBackupPlanAssociationProperties)`)` Output only. AlloyDB cluster's backup plan association properties.  
  
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
  
### RuleConfigInfo

JSON representation  
---  
      
    
    {
      "ruleId": string,
      "lastBackupState": enum ([LastBackupState](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.LastBackupState)),
      "lastBackupError": {
        object ([Status](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/CreateBackupPlan#Output.Schema.Status))
      },
      "lastSuccessfulBackupConsistencyTime": string
    }  
  
Fields  
---  
`ruleId` |  `string` Output only. Backup Rule id fetched from backup plan.  
`lastBackupState` |  `enum (`[LastBackupState](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlanAssociations#Output.Schema.LastBackupState)`)` Output only. The last backup state for rule.  
`lastBackupError` |  `object (`[Status](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/CreateBackupPlan#Output.Schema.Status)`)` Output only. google.rpc.Status object to store the last backup error.  
`lastSuccessfulBackupConsistencyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The point in time when the last successful backup was captured from the source.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### CloudSqlInstanceBackupPlanAssociationProperties

JSON representation  
---  
      
    
    {
      "instanceCreateTime": string
    }  
  
Fields  
---  
`instanceCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### FilestoreInstanceBackupPlanAssociationProperties

JSON representation  
---  
      
    
    {
      "instanceCreateTime": string
    }  
  
Fields  
---  
`instanceCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### AlloyDBClusterBackupPlanAssociationProperties

JSON representation  
---  
      
    
    {
      "clusterUid": string
    }  
  
Fields  
---  
`clusterUid` |  `string` Output only. The cluster UID of the AlloyDB cluster.  
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
### State

Enum for State of BackupPlan Association

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | The resource is being created.  
`ACTIVE` | The resource has been created and is fully usable.  
`DELETING` | The resource is being deleted.  
`INACTIVE` | The resource has been created but is not usable.  
`UPDATING` | The resource is being updated.  
  
### LastBackupState

Enum for LastBackupState

Enums  
---  
`LAST_BACKUP_STATE_UNSPECIFIED` | State not set.  
`FIRST_BACKUP_PENDING` | The first backup is pending.  
`PERMISSION_DENIED` | The most recent backup could not be run/failed because of the lack of permissions.  
`SUCCEEDED` | The last backup operation succeeded.  
`FAILED` | The last backup operation failed.  
  
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
        object ([Status](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/CreateBackupPlan#Output.Schema.Status))
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
`error` |  `object (`[Status](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/CreateBackupPlan#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
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

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
