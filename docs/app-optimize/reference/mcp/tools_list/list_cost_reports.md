---
url: https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/list_cost_reports/
title: MCP Tools Reference: appoptimize.googleapis.com \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:13.062162+00:00
---

# MCP Tools Reference: appoptimize.googleapis.com  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/list_cost_reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  MCP Tools Reference: appoptimize.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_cost_reports`

Lists all saved cost and utilization reports in the specified parent location. `location` is always `global` (aggregated listing `locations/-` is not supported). Supports pagination via `next_page_token`.

An empty list is normal: reports expire and are deleted automatically 24 hours after creation.

Required IAM on the scoped project: - `roles/appoptimize.viewer` or `roles/appoptimize.admin` to list reports.

The following code sample shows how to use `curl` to call the `list_cost_reports` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://appoptimize.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_cost_reports",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for the `ListReports` method.

### ListReportsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent project whose reports are to be listed.Format: `projects/{project}/locations/{location}`.  
`pageSize` |  `integer` Optional. The maximum number of reports to return. The service may return fewer than this value. If unspecified, the server will determine the number of results to return.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListReports` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListReports` must match the call that provided the page token.  
  
## Output Schema

Response message for the `ListReports` method.

### ListReportsResponse

JSON representation  
---  
      
    
    {
      "reports": [
        {
          object ([Report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Input.Schema.Report))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`reports[]` |  `object (`[Report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Input.Schema.Report)`)` The list of reports.  
`nextPageToken` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is empty, there are no subsequent pages.  
  
### Report

JSON representation  
---  
      
    
    {
      "name": string,
      "dimensions": [
        string
      ],
      "metrics": [
        string
      ],
      "scopes": [
        {
          object ([Scope](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Input.Schema.Scope))
        }
      ],
      "filter": string,
    
      // Union field expiration can be only one of the following:
      "expireTime": string
      // End of list of possible types for union field expiration.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of this report.  
`dimensions[]` |  `string` Required. A list of dimensions to include in the report. Supported values:

  * `project`
  * `application`
  * `service_or_workload`
  * `resource`
  * `resource_type`
  * `location`
  * `product_display_name`
  * `sku`
  * `month`
  * `day`
  * `hour`

To aggregate results by time, specify at least one time dimension (`month`, `day`, or `hour`). All time dimensions use Pacific Time, respect Daylight Saving Time (DST), and follow these ISO 8601 formats:

  * `month`: `YYYY-MM` (e.g., `2024-01`)
  * `day`: `YYYY-MM-DD` (e.g., `2024-01-10`)
  * `hour`: `YYYY-MM-DDTHH` (e.g., `2024-01-10T00`)

Supported dimension combinations:

  * `{project}`
  * `{product_display_name}`
  * `{product_display_name, project}`
  * `{product_display_name, resource}`
  * `{product_display_name, resource_type}`
  * `{application}`
  * `{application, product_display_name}`
  * `{location, product_display_name, project, sku}`
  * `{location, product_display_name, project, service_or_workload}`
  * `{location, product_display_name, project, resource, resource_type}`
  * `{location, product_display_name, project, resource, resource_type, sku}`

Any of the above combinations can optionally include one or more time dimensions (`month`, `day`, or `hour`).Metric constraints:

  * If `sku` is present in dimensions, only cost metrics are supported (CPU and memory utilization metrics are rejected).
  * `cpu_p95_utilization` and `memory_p95_utilization` require the `resource` dimension.

If the time range filter does not align with the selected time dimension, the range is expanded to encompass the full period of the finest-grained time dimension.For example, if the filter is `2026-01-10` through `2026-01-12` and the `month` dimension is selected, the effective time range expands to include all of January (`2026-01-01` to `2026-02-01`).  
`metrics[]` |  `string` Required. A list of metrics to include in the report. Supported values:

  * `cost`
  * `resource_cost`
  * `network_cost`
  * `network_cost_standard_internet`
  * `network_cost_premium_internet`
  * `network_cost_inter_region`
  * `network_cost_inter_zone`
  * `network_cost_load_balancing_inbound`
  * `network_cost_load_balancing_outbound`
  * `network_cost_interconnect_inbound`
  * `network_cost_interconnect_outbound`
  * `cpu_mean_utilization`
  * `cpu_usage_core_seconds`
  * `cpu_allocation_core_seconds`
  * `cpu_p95_utilization`
  * `memory_mean_utilization`
  * `memory_usage_byte_seconds`
  * `memory_allocation_byte_seconds`
  * `memory_p95_utilization`

  
`scopes[]` |  `object (`[Scope](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Input.Schema.Scope)`)` Optional. The resource containers for which to fetch data. Default is the project specified in the report's parent.No more than one scope is supported.  
`filter` |  `string` Optional. A Common Expression Language (CEL) expression used to filter the data for the report.Predicates may refer to any dimension. Filtering must conform to these constraints:

  * All string field predicates must use exact string matches.
  * Multiple predicates referring to the same string field must be joined using the logical OR operator ('||').
  * All other predicates must be joined using the logical AND operator (`&&`).
  * Time dimensions (`month`, `day`, `hour`) are typed as `google.protobuf.Timestamp`, NOT strings. Equality comparisons (`==`, `!=`, or `:`) and string literals (e.g., `month == '2024-01'`) are NOT supported.
  * A predicate on a time dimension (e.g., `day`) specifying the start time must use a greater-than-or-equal-to comparison (`>=`).
  * A predicate on a time dimension specifying the end time must use a less-than comparison (`<`).

Examples:

  1. Filter by a specific resource type: `"resource_type == 'compute.googleapis.com/Instance'"`
  2. Filter data points that fall within a specific absolute time interval: `"hour >= timestamp('2024-01-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"`
  3. Filter data points that fall within the past 72 hours: `"hour >= now - duration('72h')"`
  4. Combine string predicate with time interval predicate: `"(location == 'us-east1' || location == 'us-west1') && hour >= timestamp('2023-12-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"`
  5. Filter for a specific calendar month (e.g., August 2026): `"month >= month('2026-08') && month < month('2026-09')"`

If the filter omits time dimensions (`month`, `day`, `hour`), the report defaults to a 7-day range ending at the previous Pacific Time midnight, with Daylight Saving Time (DST) applied.For example, if the current Pacific Time is `2026-01-05T12:00:00`, the default range is `2025-12-29T00:00:00` to `2026-01-05T00:00:00` Pacific time.  
Union field `expiration`. Defines this report's expiration time. `expiration` can be only one of the following:  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp in UTC of when this report expires. Once the report expires, it will no longer be accessible and the report's underlying data will be deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### Scope

JSON representation  
---  
      
    
    {
    
      // Union field scope can be only one of the following:
      "project": string,
      "application": string
      // End of list of possible types for union field scope.
    }  
  
Fields  
---  
Union field `scope`.`scope` can be only one of the following:  
`project` |  `string` Required (oneof). A Google Cloud Platform project to fetch data from.Format: `"projects/{project}"`.Exactly one of `project` or `application` must be specified.  
`application` |  `string` Required (oneof). An App Hub Application to fetch data from.Format: `"projects/{project}/locations/{location}/applications/{application}"`.Exactly one of `project` or `application` must be specified.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
