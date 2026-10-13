---
url: https://docs.cloud.google.com/trace/docs/reference/mcp/mcp/tools_list/get_trace/
title: MCP Tools Reference: cloudtrace.googleapis.com \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:02.588180+00:00
---

# MCP Tools Reference: cloudtrace.googleapis.com  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/reference/mcp/mcp/tools_list/get_trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Reference ](https://docs.cloud.google.com/trace/docs/reference)



Send feedback 

#  MCP Tools Reference: cloudtrace.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_trace`

Use this as the primary tool to retrieve a single distributed trace from Google Cloud Trace. Traces provide a detailed view of the path of a request as it travels through your application's services. This is essential for understanding latency issues and debugging complex, multi-service workflows. This is often used as a follow on to list_traces to get full details on a specific trace.

The following code sample shows how to use `curl` to call the `get_trace` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudtrace.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_trace",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The request message for the `GetTrace` method.

### GetTraceRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "traceId": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. ID of the Cloud project where the trace data is stored.  
`traceId` |  `string` Required. ID of the trace to return.  
  
## Output Schema

A trace describes how long it takes for an application to perform an operation. It consists of a set of spans, each of which represent a single timed event within the operation.

### Trace

JSON representation  
---  
      
    
    {
      "projectId": string,
      "traceId": string,
      "spans": [
        {
          object ([TraceSpan](https://docs.cloud.google.com/trace/docs/reference/mcp/mcp/tools_list/list_traces#Output.Schema.TraceSpan))
        }
      ]
    }  
  
Fields  
---  
`projectId` |  `string` Required. Project ID of the Cloud project where the trace data is stored.  
`traceId` |  `string` Required. Globally unique identifier for the trace. This identifier is a 128-bit numeric value formatted as a 32-byte hex string. For example, `382d4f4c6b7bb2f4a972559d9085001d`. The numeric value should not be zero.  
`spans[]` |  `object (`[TraceSpan](https://docs.cloud.google.com/trace/docs/reference/mcp/mcp/tools_list/list_traces#Output.Schema.TraceSpan)`)` Collection of spans in the trace.  
  
### TraceSpan

JSON representation  
---  
      
    
    {
      "spanId": string,
      "kind": enum ([SpanKind](https://docs.cloud.google.com/trace/docs/reference/mcp/mcp/tools_list/list_traces#Output.Schema.SpanKind)),
      "name": string,
      "startTime": string,
      "endTime": string,
      "parentSpanId": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`spanId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Required. Identifier for the span. Must be a 64-bit integer other than 0 and unique within a trace. For example, `2205310701640571284`.  
`kind` |  `enum (`[SpanKind](https://docs.cloud.google.com/trace/docs/reference/mcp/mcp/tools_list/list_traces#Output.Schema.SpanKind)`)` Optional. Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using `RPC_CLIENT` and `RPC_SERVER` to identify queueing latency associated with the span.  
`name` |  `string` Required. Name of the span. Must be less than 128 bytes. The span name is sanitized and displayed in the Trace tool in the Google Cloud Platform Console. The name may be a method name or some other per-call site name. For the same executable and the same call point, a best practice is to use a consistent name, which makes it easier to correlate cross-trace spans.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Start time of the span in seconds and nanoseconds from the UNIX epoch.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. End time of the span in seconds and nanoseconds from the UNIX epoch.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`parentSpanId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Optional. ID of the parent span, if any.  
`labels` |  `map (key: string, value: string)` Optional. Collection of labels associated with the span. Label keys must be less than 128 bytes. Label values must be less than 16 KiB. Some keys might have predefined meaning, and you can also create your own.For more information, see [Cloud Trace labels](https://cloud.google.com/trace/docs/trace-labels).  
  
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
  
### SpanKind

Type of span. Can be used to specify additional relationships between spans in addition to a parent/child relationship.

Enums  
---  
`SPAN_KIND_UNSPECIFIED` | Unspecified.  
`RPC_SERVER` | Indicates that the span covers server-side handling of an RPC or other remote network request.  
`RPC_CLIENT` | Indicates that the span covers the client-side wrapper around an RPC or other remote request.  
  
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
