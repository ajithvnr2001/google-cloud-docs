---
url: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert/
title: MCP Tools Reference: monitoring.googleapis.com \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:11.418316+00:00
---

# MCP Tools Reference: monitoring.googleapis.com  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  MCP Tools Reference: monitoring.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_alert`

Use this as the primary tool to get information about a specific alert. An alert is the representation of a violation of an alert policy. This is useful for understanding the details of a specific alert.

The following code sample shows how to use `curl` to call the `get_alert` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://monitoring.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_alert",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The `GetAlert` request.

### GetAlertRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the alert.The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alerts/[ALERT_ID]
    

The `[ALERT_ID]` is a system-assigned unique identifier for the alert.  
  
## Output Schema

An alert is the representation of a violation of an alert policy. It is a read-only resource that cannot be modified by the accompanied API.

### Alert

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert#Output.Schema.State)),
      "openTime": string,
      "closeTime": string,
      "resource": {
        object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResource))
      },
      "metadata": {
        object ([MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResourceMetadata))
      },
      "metric": {
        object ([Metric](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Metric))
      },
      "log": {
        object ([LogMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert#Output.Schema.LogMetadata))
      },
      "policy": {
        object ([PolicySnapshot](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert#Output.Schema.PolicySnapshot))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the alert.The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alerts/[ALERT_ID]
    

The `[ALERT_ID]` is a system-assigned unique identifier for the alert.  
`state` |  `enum (`[State](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert#Output.Schema.State)`)` Output only. The current state of the alert.  
`openTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the alert was opened.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`closeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the alert was closed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resource` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResource)`)` The monitored resource type and any monitored resource labels preserved from the incident's generating condition.  
`metadata` |  `object (`[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResourceMetadata)`)` The metadata of the monitored resource.  
`metric` |  `object (`[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Metric)`)` The metric type and any metric labels preserved from the incident's generating condition.  
`log` |  `object (`[LogMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert#Output.Schema.LogMetadata)`)` The log information associated with the alert. This field is only populated for log-based alerts.  
`policy` |  `object (`[PolicySnapshot](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert#Output.Schema.PolicySnapshot)`)` The snapshot of the alert policy that generated this alert.  
  
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
  
### MonitoredResource

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`type` |  `string` Required. The monitored resource type. This field must match the `type` field of a `MonitoredResourceDescriptor` object. For example, the type of a Compute Engine VM instance is `gce_instance`. For a list of types, see [Monitoring resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list).  
`labels` |  `map (key: string, value: string)` Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels `"project_id"`, `"instance_id"`, and `"zone"`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
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
  
### MonitoredResourceMetadata

JSON representation  
---  
      
    
    {
      "systemLabels": {
        object
      },
      "userLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`systemLabels` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example:
    
    
    { "name": "my-test-instance",
      "security_group": ["a", "b", "c"],
      "spot_instance": false }
      
  
`userLabels` |  `map (key: string, value: string)` Output only. A map of user-defined metadata labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
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
  
### UserLabelsEntry

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
  
### Metric

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`type` |  `string` An existing metric type, see `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptor)`. For example, `custom.googleapis.com/invoice/paid/amount`.  
`labels` |  `map (key: string, value: string)` The set of label values that uniquely identify this metric. All labels listed in the `MetricDescriptor` must be assigned values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
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
  
### LogMetadata

JSON representation  
---  
      
    
    {
      "extractedLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`extractedLabels` |  `map (key: string, value: string)` The labels extracted from the log.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### ExtractedLabelsEntry

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
  
### PolicySnapshot

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "severity": enum ([Severity](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Severity)),
      "userLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the alert policy resource. In the form of "projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]".  
`displayName` |  `string` The display name of the alert policy.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Severity)`)` The severity of the alert policy.  
`userLabels` |  `map (key: string, value: string)` The user labels for the alert policy.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### UserLabelsEntry

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

The enumeration of possible states for an alert.

Enums  
---  
`STATE_UNSPECIFIED` | The alert state is unspecified.  
`OPEN` | The alert is open.  
`CLOSED` | The alert is closed.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Severity

An enumeration of possible severity level for an alerting policy.

Enums  
---  
`SEVERITY_UNSPECIFIED` | No severity is specified. This is the default value.  
`CRITICAL` | This is the highest severity level. Use this if the problem could cause significant damage or downtime.  
`ERROR` | This is the medium severity level. Use this if the problem could cause minor damage or downtime.  
`WARNING` | This is the lowest severity level. Use this if the problem is not causing any damage or downtime, but could potentially lead to a problem in the future.  
  
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

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
