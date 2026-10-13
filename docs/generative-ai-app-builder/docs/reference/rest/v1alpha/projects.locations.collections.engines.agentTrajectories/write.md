---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write/
title: Method: projects.locations.collections.engines.agentTrajectories.write \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:39.973084+00:00
---

# Method: projects.locations.collections.engines.agentTrajectories.write  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.engines.agentTrajectories.write Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AgentTrajectory
    * JSON representation
  * Span
    * JSON representation
  * SpanKind
  * Event
    * JSON representation



Writes the execution trajectory of a single agent turn for internal observability logging. This method is used by first-party agent clients (for example, the Gemini Enterprise desktop Cowork agent). Logging is gated on the engine's ObservabilityConfig; content-bearing attributes are redacted unless sensitive-content logging is enabled, and the trajectory is written as a JSON object to a fixed Google-internal GCS bucket for debugging (never to a customer project). It is NOT persisted to the user event or recommendation store.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/agentTrajectories:write`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines#Engine)` the trajectory belongs to, in the form `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`. Observability logging is gated on this engine's `ObservabilityConfig`: the trajectory is only logged (written as a JSON object to a fixed Google-internal GCS bucket) when observability is enabled for the engine, and content-bearing attributes are only included when sensitive logging is enabled.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "agentTrajectory": {
        object ([AgentTrajectory](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#AgentTrajectory))
      }
    }  
  
Fields  
---  
`agentTrajectory` |  `object (`[AgentTrajectory](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#AgentTrajectory)`)` Required. The agent trajectory to log.  
  
### Response body

Response message for `UserEventService.WriteAgentTrajectory` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "acceptedSpanCount": integer
    }  
  
Fields  
---  
`acceptedSpanCount` |  `integer` The number of spans that were accepted for observability logging.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.engines.createEngineUserData`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AgentTrajectory

AgentTrajectory captures the execution trace of a single agent turn, modeled on OpenTelemetry GenAI semantic conventions. It is reported by first-party clients (e.g. the Gemini Enterprise desktop Cowork agent) for internal observability logging only; it is not persisted to the user event / recommendation store.

The server gates logging on the engine's ObservabilityConfig, redacts content-bearing attributes unless sensitive-content logging is enabled, and writes the trajectory as a JSON object to a fixed Google-internal GCS bucket for debugging (never to a customer project).

JSON representation  
---  
      
    
    {
      "spans": [
        {
          object ([Span](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#Span))
        }
      ],
      "sessionId": string,
      "resourceAttributes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`spans[]` |  `object (`[Span](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#Span)`)` Required. The spans that make up this agent turn. All spans MUST share the same `[Span.trace_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#Span.FIELDS.trace_id)`.  
`sessionId` |  `string` Optional. A unique identifier for the agent session this turn belongs to.  
`resourceAttributes` |  `map (key: string, value: string)` Optional. Resource-level attributes shared by all spans, following OpenTelemetry resource semantic conventions (e.g. `service.name`, `gen_ai.agent.name`, `gen_ai.agent.id`). These are opted in to observability logging by default.  
  
## Span

A single span within the agent trajectory, aligned with the OpenTelemetry span data model.

JSON representation  
---  
      
    
    {
      "traceId": string,
      "spanId": string,
      "parentSpanId": string,
      "displayName": string,
      "spanKind": enum ([SpanKind](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#SpanKind)),
      "startTime": string,
      "endTime": string,
      "attributes": {
        string: string,
        ...
      },
      "contentAttributes": {
        string: string,
        ...
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "events": [
        {
          object ([Event](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#Event))
        }
      ]
    }  
  
Fields  
---  
`traceId` |  `string` Required. A 32 hex-character (16-byte) trace ID shared by all spans of the turn.  
`spanId` |  `string` Required. A 16 hex-character (8-byte) span ID that uniquely identifies this span within the trace.  
`parentSpanId` |  `string` Optional. The span ID of this span's parent, if any. Empty for the root span.  
`displayName` |  `string` Required. A human-readable name for the span (e.g. `invoke_agent`, `generate_content`, `execute_tool <toolName>`).  
`spanKind` |  `enum (`[SpanKind](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#SpanKind)`)` Optional. The kind of the span.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The start time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The end time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: string)` Optional. Non-content span attributes following OpenTelemetry GenAI semantic conventions (e.g. `gen_ai.system`, `gen_ai.operation.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`). Numeric values are string-encoded. These are opted in to observability logging by default.  
`contentAttributes` |  `map (key: string, value: string)` Optional. Content-bearing attributes (e.g. prompts, responses, tool arguments and results). These are opted OUT of observability logging by default and are only logged when the customer has enabled sensitive-content logging.  
`status` |  `object (`[Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Optional. The status of the span. `code` is a `google.rpc.Code`; `OK` (0) indicates success and any non-zero code indicates an error.  
`events[]` |  `object (`[Event](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.agentTrajectories/write#Event)`)` Optional. Timed events that occurred during the span.  
  
## SpanKind

The kind of the span, aligned with OpenTelemetry SpanKind.

Enums  
---  
`SPAN_KIND_UNSPECIFIED` | Unspecified. Treated as INTERNAL.  
`INTERNAL` | An internal operation within the agent (e.g. invoke_agent).  
`SERVER` | A synchronous incoming request handler.  
`CLIENT` | A synchronous outgoing request (e.g. a model or tool call).  
`PRODUCER` | An asynchronous producer of a message.  
`CONSUMER` | An asynchronous consumer of a message.  
  
## Event

A timed event that occurred during the span (e.g. a streamed chunk).

JSON representation  
---  
      
    
    {
      "displayName": string,
      "eventTime": string,
      "attributes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`displayName` |  `string` Required. A human-readable name for the event.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The wall-clock time the event occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: string)` Optional. Non-content attributes describing the event.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
