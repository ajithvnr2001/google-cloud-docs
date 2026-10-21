---
url: https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report/
title: MCP Tools Reference: appoptimize.googleapis.com \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:13.144714+00:00
---

# MCP Tools Reference: appoptimize.googleapis.com  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  MCP Tools Reference: appoptimize.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_cost_report`

Creates a saved, reusable cost and utilization report for Google Cloud — spend and CPU/memory usage for a project or App Hub application. This initiates an asynchronous long-running operation (LRO). Poll the operation status using `get_report_operation` until `done: true`, then read data using `read_cost_report`. Cost-only reports complete in under a minute; reports with utilization metrics take ~9-10 minutes (pulling from Cloud Monitoring).

Scope: To query a specific project, set `scopes: [{"project": "projects/{project}"}]`. To query an App Hub application, set `scopes: [{"application": "projects/{project}/locations/{location}/applications/{application}"}]`. Do not specify both. If omitted, defaults to the parent project. Reports are deleted automatically 24 hours after creation.

Required IAM on the scoped project: - `roles/appoptimize.admin` is required to create reports. - Role `billing.resourceCosts.get` (e.g. `roles/cloudhub.operator`, `roles/reader`, or `roles/viewer`) if any cost metrics are requested. - Role `roles/monitoring.viewer` if any utilization metrics are requested. - Role `roles/apphub.appManagementViewer` on the host project if an App Hub scope is requested.

The following code sample shows how to use `curl` to call the `create_cost_report` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://appoptimize.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_cost_report",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for the `CreateReport` method.

### CreateReportRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "reportId": string,
      "report": {
        object ([Report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Input.Schema.Report))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent Google Cloud project that will own the report.This value does not define the scope of the report data. See `Report.scope` for setting the data scope.Format: `projects/{project}/locations/{location}`.  
`reportId` |  `string` Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`report` |  `object (`[Report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Input.Schema.Report)`)` Required. The report resource to create.  
  
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
        object ([Status](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Output.Schema.Status))
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
`error` |  `object (`[Status](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
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

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
