---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:24:42.241014+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_evaluation_run`

Gets details of the specified evaluation run.

The following code sample shows how to use `curl` to call the `get_evaluation_run` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_evaluation_run",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `EvaluationService.GetEvaluationRun`.

### GetEvaluationRunRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the evaluation run to retrieve.  
  
## Output Schema

An evaluation run represents an all the evaluation results from an evaluation execution.

### EvaluationRun

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "evaluationResults": [
        string
      ],
      "createTime": string,
      "initiatedBy": string,
      "appVersion": string,
      "appVersionDisplayName": string,
      "changelog": string,
      "changelogCreateTime": string,
      "evaluations": [
        string
      ],
      "evaluationDataset": string,
      "evaluationType": enum ([EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationType)),
      "state": enum ([EvaluationRunState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationRunState)),
      "progress": {
        object ([Progress](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.Progress))
      },
      "config": {
        object ([EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationConfig))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app#Output.Schema.Status))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo))
      },
      "evaluationRunSummaries": {
        string: {
          object ([EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationRunSummary))
        },
        ...
      },
      "latencyReport": {
        object ([LatencyReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyReport))
      },
      "runCount": integer,
      "personaRunConfigs": [
        {
          object ([PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.PersonaRunConfig))
        }
      ],
      "optimizationConfig": {
        object ([OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.OptimizationConfig))
      },
      "scheduledEvaluationRun": string,
      "goldenRunMethod": enum ([GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenRunMethod)),
      "operation": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`displayName` |  `string` Optional. User-defined display name of the evaluation run. default: " run - ".  
`evaluationResults[]` |  `string` Output only. The evaluation results that are part of this run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation run was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`initiatedBy` |  `string` Output only. The user who initiated the evaluation run.  
`appVersion` |  `string` Output only. The app version to evaluate. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`appVersionDisplayName` |  `string` Output only. The display name of the `app_version` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelogCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`evaluations[]` |  `string` Output only. The evaluations that are part of this run. The list may contain evaluations of either type. This field is mutually exclusive with `evaluation_dataset`. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`evaluationDataset` |  `string` Output only. The evaluation dataset that this run is associated with. This field is mutually exclusive with `evaluations`. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`evaluationType` |  `enum (`[EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationType)`)` Output only. The type of the evaluations in this run.  
`state` |  `enum (`[EvaluationRunState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationRunState)`)` Output only. The state of the evaluation run.  
`progress` |  `object (`[Progress](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.Progress)`)` Output only. The progress of the evaluation run.  
`config` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationConfig)`)` Output only. The configuration used in the run.  
`error  
**(deprecated)**` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app#Output.Schema.Status)`)` This item is deprecated!Output only. Deprecated: Use error_info instead. Errors encountered during execution.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo)`)` Output only. Error information for the evaluation run.  
`evaluationRunSummaries` |  `map (key: string, value: object (`[EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationRunSummary)`))` Output only. Map of evaluation name to EvaluationRunSummary.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`latencyReport` |  `object (`[LatencyReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyReport)`)` Output only. Latency report for the evaluation run.  
`runCount` |  `integer` Output only. The number of times the evaluations inside the run were run.  
`personaRunConfigs[]` |  `object (`[PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.PersonaRunConfig)`)` Output only. The configuration to use for the run per persona.  
`optimizationConfig` |  `object (`[OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.OptimizationConfig)`)` Optional. Configuration for running the optimization step after the evaluation run. If not set, the optimization step will not be run.  
`scheduledEvaluationRun` |  `string` Output only. The scheduled evaluation run resource name that created this evaluation run. This field is only set if the evaluation run was created by a scheduled evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}`  
`goldenRunMethod` |  `enum (`[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenRunMethod)`)` Output only. The method used to run the evaluation.  
`operation` |  `string` Output only. The operation that created this evaluation run. Format: `projects/{project}/locations/{location}/operations/{operation}`  
  
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
  
### Progress

JSON representation  
---  
      
    
    {
      "totalCount": integer,
      "failedCount": integer,
      "errorCount": integer,
      "completedCount": integer,
      "passedCount": integer,
      "cancelledCount": integer
    }  
  
Fields  
---  
`totalCount` |  `integer` Output only. Total number of evaluation results in this run.  
`failedCount` |  `integer` Output only. Number of completed evaluation results with an outcome of FAIL. (EvaluationResult.execution_state is COMPLETED and EvaluationResult.evaluation_status is FAIL).  
`errorCount` |  `integer` Output only. Number of evaluation results that failed to execute. (EvaluationResult.execution_state is ERROR).  
`completedCount` |  `integer` Output only. Number of evaluation results that finished successfully. (EvaluationResult.execution_state is COMPLETED).  
`passedCount` |  `integer` Output only. Number of completed evaluation results with an outcome of PASS. (EvaluationResult.execution_state is COMPLETED and EvaluationResult.evaluation_status is PASS).  
`cancelledCount` |  `integer` Output only. Number of evaluation results that were cancelled. (EvaluationResult.execution_state is CANCELLED).  
  
### EvaluationConfig

JSON representation  
---  
      
    
    {
      "inputAudioConfig": {
        object ([InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.InputAudioConfig))
      },
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OutputAudioConfig))
      },
      "evaluationChannel": enum ([EvaluationChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationChannel)),
      "toolCallBehaviour": enum ([EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationToolCallBehaviour))
    }  
  
Fields  
---  
`inputAudioConfig` |  `object (`[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.InputAudioConfig)`)` Optional. Configuration for processing the input audio.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OutputAudioConfig)`)` Optional. Configuration for generating the output audio.  
`evaluationChannel` |  `enum (`[EvaluationChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationChannel)`)` Optional. The channel to evaluate.  
`toolCallBehaviour` |  `enum (`[EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationToolCallBehaviour)`)` Optional. Specifies whether the evaluation should use real tool calls or fake tools.  
  
### InputAudioConfig

JSON representation  
---  
      
    
    {
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AudioEncoding)),
      "sampleRateHertz": integer,
      "noiseSuppressionLevel": string
    }  
  
Fields  
---  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AudioEncoding)`)` Required. The encoding of the input audio data.  
`sampleRateHertz` |  `integer` Required. The sample rate (in Hertz) of the input audio data.  
`noiseSuppressionLevel` |  `string` Optional. Whether to enable noise suppression on the input audio. Available values are "low", "moderate", "high", "very_high".  
  
### OutputAudioConfig

JSON representation  
---  
      
    
    {
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AudioEncoding)),
      "sampleRateHertz": integer
    }  
  
Fields  
---  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AudioEncoding)`)` Required. The encoding of the output audio data.  
`sampleRateHertz` |  `integer` Required. The sample rate (in Hertz) of the output audio data.  
  
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
  
### EvaluationErrorInfo

JSON representation  
---  
      
    
    {
      "errorType": enum ([ErrorType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ErrorType)),
      "errorMessage": string,
      "sessionId": string,
      "userFacingErrorMessage": string
    }  
  
Fields  
---  
`errorType` |  `enum (`[ErrorType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ErrorType)`)` Output only. The type of error.  
`errorMessage` |  `string` Output only. The error message.  
`sessionId` |  `string` Output only. The session ID for the conversation that caused the error.  
`userFacingErrorMessage` |  `string` Output only. The user facing error message.  
  
### EvaluationRunSummariesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationRunSummary))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.EvaluationRunSummary)`)`  
  
### EvaluationRunSummary

JSON representation  
---  
      
    
    {
      "passedCount": integer,
      "failedCount": integer,
      "errorCount": integer
    }  
  
Fields  
---  
`passedCount` |  `integer` Output only. Number of passed results for the associated Evaluation in this run.  
`failedCount` |  `integer` Output only. Number of failed results for the associated Evaluation in this run.  
`errorCount` |  `integer` Output only. Number of error results for the associated Evaluation in this run.  
  
### LatencyReport

JSON representation  
---  
      
    
    {
      "toolLatencies": [
        {
          object ([ToolLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.ToolLatency))
        }
      ],
      "callbackLatencies": [
        {
          object ([CallbackLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.CallbackLatency))
        }
      ],
      "guardrailLatencies": [
        {
          object ([GuardrailLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.GuardrailLatency))
        }
      ],
      "llmCallLatencies": [
        {
          object ([LlmCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LlmCallLatency))
        }
      ],
      "sessionCount": integer
    }  
  
Fields  
---  
`toolLatencies[]` |  `object (`[ToolLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.ToolLatency)`)` Output only. Unordered list. Latency metrics for each tool.  
`callbackLatencies[]` |  `object (`[CallbackLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.CallbackLatency)`)` Output only. Unordered list. Latency metrics for each callback.  
`guardrailLatencies[]` |  `object (`[GuardrailLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.GuardrailLatency)`)` Output only. Unordered list. Latency metrics for each guardrail.  
`llmCallLatencies[]` |  `object (`[LlmCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LlmCallLatency)`)` Output only. Unordered list. Latency metrics for each LLM call.  
`sessionCount` |  `integer` Output only. The total number of sessions considered in the latency report.  
  
### ToolLatency

JSON representation  
---  
      
    
    {
      "toolDisplayName": string,
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics))
      },
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`toolDisplayName` |  `string` Output only. The display name of the tool.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics)`)` Output only. The latency metrics for the tool.  
Union field `tool_identifier`. The identifier of the tool. `tool_identifier` can be only one of the following:  
`tool` |  `string` Output only. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`.  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Output only. The toolset tool identifier.  
  
### ToolsetTool

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolId": string
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the Toolset from which this tool is derived. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolId` |  `string` Optional. The tool ID to filter the tools to retrieve the schema for.  
  
### LatencyMetrics

JSON representation  
---  
      
    
    {
      "p50Latency": string,
      "p90Latency": string,
      "p99Latency": string,
      "callCount": integer
    }  
  
Fields  
---  
`p50Latency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The 50th percentile latency.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`p90Latency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The 90th percentile latency.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`p99Latency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The 99th percentile latency.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`callCount` |  `integer` Output only. The number of times the resource was called.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### CallbackLatency

JSON representation  
---  
      
    
    {
      "stage": string,
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics))
      }
    }  
  
Fields  
---  
`stage` |  `string` Output only. The stage of the callback.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics)`)` Output only. The latency metrics for the callback.  
  
### GuardrailLatency

JSON representation  
---  
      
    
    {
      "guardrail": string,
      "guardrailDisplayName": string,
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics))
      }
    }  
  
Fields  
---  
`guardrail` |  `string` Output only. The name of the guardrail. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`.  
`guardrailDisplayName` |  `string` Output only. The display name of the guardrail.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics)`)` Output only. The latency metrics for the guardrail.  
  
### LlmCallLatency

JSON representation  
---  
      
    
    {
      "model": string,
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics))
      }
    }  
  
Fields  
---  
`model` |  `string` Output only. The name of the model.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.LatencyMetrics)`)` Output only. The latency metrics for the LLM call.  
  
### PersonaRunConfig

JSON representation  
---  
      
    
    {
      "persona": string,
      "taskCount": integer
    }  
  
Fields  
---  
`persona` |  `string` Optional. The persona to use for the evaluation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}`  
`taskCount` |  `integer` Optional. The number of tasks to run for the persona.  
  
### OptimizationConfig

JSON representation  
---  
      
    
    {
      "generateLossReport": boolean,
      "assistantSession": string,
      "reportSummary": string,
      "shouldSuggestFix": boolean,
      "status": enum ([OptimizationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.OptimizationStatus)),
      "errorMessage": string,
      "lossReport": {
        object
      }
    }  
  
Fields  
---  
`generateLossReport` |  `boolean` Optional. Whether to generate a loss report.  
`assistantSession` |  `string` Output only. The assistant session to use for the optimization based on this evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}`  
`reportSummary` |  `string` Output only. The summary of the loss report.  
`shouldSuggestFix` |  `boolean` Output only. Whether to suggest a fix for the losses.  
`status` |  `enum (`[OptimizationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run#Output.Schema.OptimizationStatus)`)` Output only. The status of the optimization run.  
`errorMessage` |  `string` Output only. The error message if the optimization run failed.  
`lossReport` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The generated loss report.  
  
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
  
### EvaluationType

The type of the evaluations in this run. Additional values may be added in the future.

Enums  
---  
`EVALUATION_TYPE_UNSPECIFIED` | Evaluation type is not specified.  
`GOLDEN` | Golden evaluation.  
`SCENARIO` | Scenario evaluation.  
`MIXED` | Indicates the run includes a mix of golden and scenario evaluations.  
  
### EvaluationRunState

The state of the evaluation run.

Enums  
---  
`EVALUATION_RUN_STATE_UNSPECIFIED` | Evaluation run state is not specified.  
`QUEUED` | Indicates the evaluation run is queued.  
`RUNNING` | Evaluation run is running.  
`COMPLETED` | Evaluation run has completed.  
`ERROR` | The evaluation run has an error.  
`CANCELLED` | Evaluation run was cancelled.  
  
### AudioEncoding

AudioEncoding specifies the encoding format for audio data.

Enums  
---  
`AUDIO_ENCODING_UNSPECIFIED` | Unspecified audio encoding.  
`LINEAR16` | 16-bit linear PCM audio encoding.  
`MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`ALAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/A-law.  
  
### EvaluationChannel

The channel to evaluate.

Enums  
---  
`EVALUATION_CHANNEL_UNSPECIFIED` | Unspecified evaluation channel.  
`TEXT` | Text-only evaluation channel.  
`AUDIO` | Audio evaluation channel.  
  
### EvaluationToolCallBehaviour

Configures the tool call behaviour for evaluation runs.

Enums  
---  
`EVALUATION_TOOL_CALL_BEHAVIOUR_UNSPECIFIED` | Unspecified tool call behavior. Will default to real tool calls.  
`REAL` | Use real tool calls.  
`FAKE` | Use fake tool calls.  
  
### ErrorType

The type of error

Enums  
---  
`ERROR_TYPE_UNSPECIFIED` | Unspecified error type.  
`RUNTIME_FAILURE` | Failure during runtime execution.  
`CONVERSATION_RETRIEVAL_FAILURE` | Failure to retrieve conversation from CES Runtime.  
`METRIC_CALCULATION_FAILURE` | Failure to calculate a metric / outcome.  
`EVALUATION_UPDATE_FAILURE` | Failure to update the evaluation.  
`QUOTA_EXHAUSTED` | Ran out of quota.  
`USER_SIMULATION_FAILURE` | Failure during user simulation.  
  
### OptimizationStatus

The status of the optimization run.

Enums  
---  
`OPTIMIZATION_STATUS_UNSPECIFIED` | Optimization status is not specified.  
`RUNNING` | Optimization is running.  
`COMPLETED` | Optimization has completed.  
`ERROR` | Optimization failed due to an internal error.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### GoldenRunMethod

The method used to run the evaluation.

Enums  
---  
`GOLDEN_RUN_METHOD_UNSPECIFIED` | Run method is not specified.  
`STABLE` | Run the evaluation as stable replay, where each turn is a unique session with the previous expected turns injected as context.  
`NAIVE` | Run the evaluation as naive replay, where the run is a single session with no context injected.  
  
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

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
