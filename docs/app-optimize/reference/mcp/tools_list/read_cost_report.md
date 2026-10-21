---
url: https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report/
title: MCP Tools Reference: appoptimize.googleapis.com \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:13.277315+00:00
---

# MCP Tools Reference: appoptimize.googleapis.com  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  MCP Tools Reference: appoptimize.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `read_cost_report`

Reads and retrieves the actual data rows of a completed cost and utilization report (spend figures and resource usage). Call this tool after the report creation operation returned by `create_cost_report` has finished with `done: true`.

Row and column formatting rules: - Cost columns (`type: "RECORD"`) are formatted as `google.type.Money` objects with `currency_code` (string, e.g. `"USD"`), `units` (int64 serialized as a JSON string), and `nanos` (int32 billionths, `10^-9`), or `null` when no cost was recorded or applicable for that entity. - Utilization and usage/allocation metric columns (`type: "FLOAT64"`) are JSON numbers, or `null` when not applicable to the resource (e.g. persistent disks or snapshots). - Dimension columns (`type: "STRING"`) are JSON strings. - Returns at most 10,000 rows per page by default (25,000 maximum); paginate using `next_page_token`.

Empty results: When a report has zero matching cost or utilization records (for example, because the project or scope has no resources, usage, or billing charges for the configured time range and filter), the `rows` field is omitted from the JSON response and only `columns` is returned. A response containing `columns` without `rows` means the report succeeded and is validly empty — it is NOT corrupt or incomplete. Inform the user that no cost or usage data was recorded for that report's configuration, and do NOT call `create_cost_report` to recreate or test the report.

Required IAM on the scoped project: - `roles/appoptimize.viewer` or `roles/appoptimize.admin` to read report data.

The following code sample shows how to use `curl` to call the `read_cost_report` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://appoptimize.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "read_cost_report",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for the `ReadReport` method.

### ReadReportRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the report to query.Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`pageSize` |  `integer` Optional. The maximum number of rows to return. The service may return fewer than this value. If unspecified, at most 10,000 rows will be returned per page. The maximum allowed value is 25,000; values above 25,000 are coerced to 25,000.  
`pageToken` |  `string` Optional. A page token, received from a previous `ReadReport` call, to retrieve the subsequent page of results. When `page_token` is specified, `job_reference` must also be provided from the previous response, and the `statement` field must not be set.  
  
## Output Schema

Response message for the `ReadReport` method.

### ReadReportResponse

JSON representation  
---  
      
    
    {
      "rows": [
        array
      ],
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report#Output.Schema.Column))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`rows[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` A list of rows, where each row represents a record from the report.Each `ListValue` element in a row corresponds positionally (1-to-1) to the entry at the same index in `columns`. When a report has zero matching records, `rows` is omitted and only `columns` is returned.  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report#Output.Schema.Column)`)` The columns describing the structure and data types of the values in the `rows` field, ordered positionally to match each row's elements. Always populated, even when the report contains zero `rows`.  
`nextPageToken` |  `string` A token that can be sent as `page_token` in a subsequent `ReadReport` request to retrieve the next page of results. If this field is empty, there are no further pages.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Column

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "mode": string,
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report#Output.Schema.Column))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of the column.This field:

  * Contains only letters (a-z, A-Z), numbers (0-9), or underscores (_);
  * Start with a letter or underscore; and
  * Has a maximum length is 128 characters.

  
`type` |  `string` The data type of the column.Supported values include:

  * `STRING`
  * `INT64`
  * `FLOAT64`
  * `BOOLEAN`
  * `TIMESTAMP`
  * `RECORD`

`RECORD` indicates that the field contains a nested schema, described in the `columns` property of this `Column`.  
`mode` |  `string` The mode of the column, indicating if it is nullable, required, or repeated.Possible values:

  * `NULLABLE`: The column allows NULL values.
  * `REQUIRED`: The column does not allow NULL values.
  * `REPEATED`: The column contains an array of values.

  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report#Output.Schema.Column)`)` If the `type` of this column is `RECORD`, this sub-field describes the nested structure (for example, a cost column of type `RECORD` contains nested columns `currency_code` of type `STRING`, `units` of type `INT64`, and `nanos` of type `INT64`).  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
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
