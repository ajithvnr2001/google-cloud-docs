---
url: https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances/
title: MCP Tools Reference: maintenance.googleapis.com \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:41.339451+00:00
---

# MCP Tools Reference: maintenance.googleapis.com  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Reference ](https://docs.cloud.google.com/unified-maintenance/docs/apis)



Send feedback 

#  MCP Tools Reference: maintenance.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `summarize_maintenances`

Summarizes maintenances for a given project and location by providing aggregated statistics.

**Parameters**

  * `parent` (string, Required): The parent of the resource maintenance, in the format `projects/{project}/locations/{location}`.
  * `page_size` (integer, Optional): The maximum number of resource maintenances to send per page.
  * `page_token` (string, Optional): A page token, received from a previous `SummarizeMaintenances` call.
  * `filter` (string, Optional): Filter the list as specified in <https://google.aip.dev/160>.
  * `order_by` (string, Optional): Order results as specified in <https://google.aip.dev/132>.



**Return Value**

The method returns a SummarizeMaintenancesResponse object, which contains:

  * `maintenances`: A list of maintenance summaries.
  * `next_page_token`: A token that can be sent as `page_token` in a subsequent request to retrieve the next page of results.



**Notes**

  * Use '-' as location for a global summary across all regions.



The following sample demonstrate how to use `curl` to invoke the `summarize_maintenances` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://maintenance.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "summarize_maintenances",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for SummarizeMaintenances custom method.

### SummarizeMaintenancesRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent of the resource maintenance. eg. `projects/123/locations/*`  
`pageSize` |  `integer` The maximum number of resource maintenances to send per page. The default page size is 20 and the maximum is 1000.  
`pageToken` |  `string` The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.  
`filter` |  `string` Filter the list as specified in <https://google.aip.dev/160>. Supported fields include: - `maintenance.maintenanceName` Examples: - `maintenance.maintenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1"`  
`orderBy` |  `string` Order results as specified in <https://google.aip.dev/132>.  
  
## Output Schema

Request message for SummarizeMaintenances custom method.

### SummarizeMaintenancesResponse

JSON representation  
---  
      
    
    {
      "maintenances": [
        {
          object ([MaintenanceSummary](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances#Output.Schema.MaintenanceSummary))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`maintenances[]` |  `object (`[MaintenanceSummary](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances#Output.Schema.MaintenanceSummary)`)` The resulting summaries.  
`nextPageToken` |  `string` If present, the next page token can be provided to a subsequent SummarizeMaintenances call to list the next page. If empty, there are no more pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### MaintenanceSummary

JSON representation  
---  
      
    
    {
      "maintenanceName": string,
      "title": string,
      "description": string,
      "category": enum ([MaintenanceCategory](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/list_resource_maintenances#Output.Schema.MaintenanceCategory)),
      "maintenanceScheduledStartTime": string,
      "maintenanceScheduledEndTime": string,
      "maintenanceStartTime": string,
      "maintenanceEndTime": string,
      "userControllable": boolean,
      "controls": [
        {
          object ([MaintenanceControl](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/list_resource_maintenances#Output.Schema.MaintenanceControl))
        }
      ],
      "stats": [
        {
          object ([Stats](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances#Output.Schema.Stats))
        }
      ]
    }  
  
Fields  
---  
`maintenanceName` |  `string` Output only. The name of the maintenance.  
`title` |  `string` Output only. The title of the maintenance.  
`description` |  `string` Output only. The description of the maintenance.  
`category` |  `enum (`[MaintenanceCategory](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/list_resource_maintenances#Output.Schema.MaintenanceCategory)`)` Output only. The category of the maintenance event.  
`maintenanceScheduledStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Scheduled start time of the maintenance. The maintenance will start at `maintenanceScheduledStartTime` or later, with best effort to finish before `maintenanceScheduledEndTime`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maintenanceScheduledEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. An estimated (best effort, not guaranteed) end time of the scheduled maintenance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maintenanceStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Actual date when the maintenance started. Field present only after the state changed to `RUNNING`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maintenanceEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Actual date when the maintenance successfully completed. Field present only after the state changed to `SUCCEEDED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userControllable` |  `boolean` Output only. Indicates whether the user has some control over that maintenance, either proactively before maintenance was scheduled with maintenance policy or with reactive controls after it was scheduled (see controls field).  
`controls[]` |  `object (`[MaintenanceControl](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/list_resource_maintenances#Output.Schema.MaintenanceControl)`)` Output only. Control available for that Maintenance (might not be available for every resource that maintenance is applied to).  
`stats[]` |  `object (`[Stats](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances#Output.Schema.Stats)`)` Output only. Stats is a field of ResourceMaintenance used to aggregate the stats.  
  
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
  
### MaintenanceControl

JSON representation  
---  
      
    
    {
      "control": enum ([Control](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/list_resource_maintenances#Output.Schema.Control)),
      "isCustom": boolean,
      "documentation": string
    }  
  
Fields  
---  
`control` |  `enum (`[Control](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/list_resource_maintenances#Output.Schema.Control)`)` The control of the resource maintenance.  
`isCustom` |  `boolean` Indicates whether the control is available only in Service Producer API (not through Unified Maintenance).  
`documentation` |  `string` Link to Service Producer documentation about maintenance control. Provided only when `isCustom` is `true`.  
  
### Stats

JSON representation  
---  
      
    
    {
      "groupBy": string,
      "aggregates": [
        {
          object ([Aggregate](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances#Output.Schema.Aggregate))
        }
      ]
    }  
  
Fields  
---  
`groupBy` |  `string` groupBy specifies the type of aggregate. For example a group_by might be `"state"`  
`aggregates[]` |  `object (`[Aggregate](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp/tools_list/summarize_maintenances#Output.Schema.Aggregate)`)` Aggregates is a list <group, count> pairs. For example, if the group_by is `"state"` a possible tuple in the aggregates list could be "SCHEDULED" : `11`,  
  
### Aggregate

JSON representation  
---  
      
    
    {
      "group": string,
      "count": string
    }  
  
Fields  
---  
`group` |  `string` Specifies what specific value of the group_by the count represents. For example if group_by is `"state"` its corresponding group could be `"SCHEDULED"`.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of the group.  
  
### MaintenanceCategory

The Category of the maintenance.

Enums  
---  
`MAINTENANCE_CATEGORY_UNSPECIFIED` | Unspecified category.  
`INFRASTRUCTURE` | Infrastructure maintenance events are times that Google Cloud performs regular maintenance on network equipment e.g. Google Cloud Interconnect These events are usually scheduled in advance and we provide notification, when possible, so that users can plan for the infrastructure maintenance event and prevent downtime. Infrastructure maintenance events don't have a set interval between occurrences, but generally occur several times a year.  
`SERVICE_UPDATE` | Updates that can include bug fixes, changes, or new features that are backward compatible with existing versions (including patches). Some SPs allow users to control the scheduling of these maintenance events using maintenance windows and/or deny maintenance features.  
  
### Control

Sets the type of control supported. comment (as in logs).

Enums  
---  
`CONTROL_UNSPECIFIED` | Unspecified control.  
`APPLY` | Apply control.  
`MANAGE_POLICY` | Manage policy control.  
`RESCHEDULE` | Reschedule control.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
