---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/mcp/tools_list/list_snapshots/
title: MCP Tools Reference: netapp.googleapis.com \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:41.041849+00:00
---

# MCP Tools Reference: netapp.googleapis.com  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/mcp/tools_list/list_snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Reference ](https://docs.cloud.google.com/netapp/volumes/docs/apis)



Send feedback 

#  MCP Tools Reference: netapp.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_snapshots`

List snapshots in a given project and location.

The following sample demonstrates how to use `curl` to invoke the `list_snapshots` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://netapp.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_snapshots",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

ListSnapshotsRequest lists snapshots.

### ListSnapshotsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "orderBy": string,
      "filter": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The volume for which to retrieve snapshot information, in the format `projects/{project}/locations/{location}/volumes/{volume_id}`.  
`pageSize` |  `integer` The maximum number of items to return.  
`pageToken` |  `string` The next_page_token value to use if there are additional results to retrieve for this list request.  
`orderBy` |  `string` Sort results. Supported values are "name", "name desc" or "" (unsorted).  
`filter` |  `string` List filter.  
  
## Output Schema

ListSnapshotsResponse is the result of ListSnapshotsRequest.

### ListSnapshotsResponse

JSON representation  
---  
      
    
    {
      "snapshots": [
        {
          object ([Snapshot](https://docs.cloud.google.com/netapp/volumes/docs/reference/mcp/tools_list/list_snapshots#Output.Schema.Snapshot))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`snapshots[]` |  `object (`[Snapshot](https://docs.cloud.google.com/netapp/volumes/docs/reference/mcp/tools_list/list_snapshots#Output.Schema.Snapshot)`)` A list of snapshots in the project for the specified volume.  
`nextPageToken` |  `string` The token you can use to retrieve the next page of results. Not returned if there are no more results in the list.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Snapshot

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/netapp/volumes/docs/reference/mcp/tools_list/list_snapshots#Output.Schema.State)),
      "stateDetails": string,
      "description": string,
      "usedBytes": number,
      "createTime": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the snapshot. Format: `projects/{project}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/netapp/volumes/docs/reference/mcp/tools_list/list_snapshots#Output.Schema.State)`)` Output only. The snapshot state.  
`stateDetails` |  `string` Output only. State details of the storage pool  
`description` |  `string` A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected.  
`usedBytes` |  `number` Output only. Current storage usage for the snapshot in bytes.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the snapshot was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
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
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### State

The Snapshot States

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified Snapshot State  
`READY` | Snapshot State is Ready  
`CREATING` | Snapshot State is Creating  
`DELETING` | Snapshot State is Deleting  
`UPDATING` | Snapshot State is Updating  
`DISABLED` | Snapshot State is Disabled  
`ERROR` | Snapshot State is Error  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
