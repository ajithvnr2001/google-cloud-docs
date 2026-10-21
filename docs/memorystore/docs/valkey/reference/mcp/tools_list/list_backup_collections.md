---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backup_collections/
title: MCP Tools Reference: memorystore.googleapis.com \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:49.361804+00:00
---

# MCP Tools Reference: memorystore.googleapis.com  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backup_collections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  MCP Tools Reference: memorystore.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_backup_collections`

List all Memorystore for Valkey backup collections.

The following sample demonstrate how to use `curl` to invoke the `list_backup_collections` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://memorystore.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_backup_collections",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for `ListBackupCollections`.

### ListBackupCollectionsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the backupCollection location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
`pageSize` |  `integer` Optional. The maximum number of items to return.If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more clusters left to be queried.  
`pageToken` |  `string` Optional. The `next_page_token` value returned from a previous `ListBackupCollections` request, if any.  
  
## Output Schema

Response for `ListBackupCollections`.

### ListBackupCollectionsResponse

JSON representation  
---  
      
    
    {
      "backupCollections": [
        {
          object ([BackupCollection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backup_collections#Output.Schema.BackupCollection))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backupCollections[]` |  `object (`[BackupCollection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_backup_collections#Output.Schema.BackupCollection)`)` A list of backupCollections in the project.If the `location_id` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder backupCollection entry is included in the response with the `name` field set to a value of the form `projects/{project_id}/locations/{location_id}/backupCollections/`\- and the `status` field set to ERROR and `status_message` field set to "location not available for ListBackupCollections".  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### BackupCollection

JSON representation  
---  
      
    
    {
      "name": string,
      "instanceUid": string,
      "instance": string,
      "kmsKey": string,
      "uid": string,
      "createTime": string,
      "totalBackupSizeBytes": string,
      "totalBackupCount": string,
      "lastBackupTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Full resource path of the backup collection.  
`instanceUid` |  `string` Output only. The instance uid of the backup collection.  
`instance` |  `string` Output only. The full resource path of the instance the backup collection belongs to. Example: projects/{project}/locations/{location}/instances/{instance}  
`kmsKey` |  `string` Output only. The KMS key used to encrypt the backups under this backup collection.  
`uid` |  `string` Output only. System assigned unique identifier of the backup collection.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup collection was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`totalBackupSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total size of all backups in the backup collection.  
`totalBackupCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total number of backups in the backup collection.  
`lastBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time a backup was created in the backup collection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
