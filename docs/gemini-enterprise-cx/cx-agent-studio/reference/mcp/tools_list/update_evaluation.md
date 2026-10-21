---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_evaluation/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:33:17.847389+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_evaluation`

Updates the specified evaluation. Make sure to always pass an update mask in the input.

The following code sample shows how to use `curl` to call the `update_evaluation` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_evaluation",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `EvaluationService.UpdateEvaluation`.

### UpdateEvaluationRequest

JSON representation  
---  
      
    
    {
      "evaluation": {
        object ([Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Evaluation))
      },
      "updateMask": string
    }  
  
Fields  
---  
`evaluation` |  `object (`[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Evaluation)`)` Required. The evaluation to update.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Evaluation

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "tags": [
        string
      ],
      "evaluationDatasets": [
        string
      ],
      "createTime": string,
      "createdBy": string,
      "updateTime": string,
      "lastUpdatedBy": string,
      "evaluationRuns": [
        string
      ],
      "etag": string,
      "aggregatedMetrics": {
        object ([AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics))
      },
      "lastCompletedResult": {
        object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult))
      },
      "invalid": boolean,
      "lastTenResults": [
        {
          object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult))
        }
      ],
      "evaluationMetricsThresholdOverride": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds))
      },
      "evaluationMetricsConfigOverride": {
        object ([EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsConfig))
      },
    
      // Union field inputs can be only one of the following:
      "golden": {
        object ([Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Golden))
      },
      "scenario": {
        object ([Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Scenario))
      }
      // End of list of possible types for union field inputs.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`displayName` |  `string` Required. User-defined display name of the evaluation. Unique within an App.  
`description` |  `string` Optional. User-defined description of the evaluation.  
`tags[]` |  `string` Optional. User defined tags to categorize the evaluation.  
`evaluationDatasets[]` |  `string` Output only. List of evaluation datasets the evaluation belongs to. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createdBy` |  `string` Output only. The user who created the evaluation.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdatedBy` |  `string` Output only. The user who last updated the evaluation.  
`evaluationRuns[]` |  `string` Output only. The EvaluationRuns that this Evaluation is associated with.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`aggregatedMetrics` |  `object (`[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics)`)` Output only. The aggregated metrics for this evaluation across all runs.  
`lastCompletedResult` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult)`)` Output only. The latest evaluation result for this evaluation.  
`invalid` |  `boolean` Output only. Whether the evaluation is invalid. This can happen if an evaluation is referencing a tool, toolset, or agent that has since been deleted.  
`lastTenResults[]` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult)`)` Output only. The last 10 evaluation results for this evaluation. This is only populated if include_last_ten_results is set to true in the ListEvaluationsRequest or GetEvaluationRequest.  
`evaluationMetricsThresholdOverride` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds)`)` Optional. Overrides metrics thresholds for this specific evaluation.  
`evaluationMetricsConfigOverride` |  `object (`[EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsConfig)`)` Optional. Overrides metrics config for this specific evaluation.  
Union field `inputs`. The inputs for the evaluation `inputs` can be only one of the following:  
`golden` |  `object (`[Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Golden)`)` Optional. The golden steps to be evaluated.  
`scenario` |  `object (`[Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Scenario)`)` Optional. The config for a scenario.  
  
### Golden

JSON representation  
---  
      
    
    {
      "turns": [
        {
          object ([GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenTurn))
        }
      ],
      "evaluationExpectations": [
        string
      ]
    }  
  
Fields  
---  
`turns[]` |  `object (`[GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenTurn)`)` Required. The golden turns required to replay a golden conversation. The maximum number of allowed turns is 100.  
`evaluationExpectations[]` |  `string` Optional. The evaluation expectations to evaluate the replayed conversation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
  
### GoldenTurn

JSON representation  
---  
      
    
    {
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Step))
        }
      ],
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span))
      },
      "turnLevelMetricsThresholdsOverride": {
        object ([TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds))
      },
      "hallucinationMetricBehaviorOverride": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Step)`)` Required. The steps required to replay a golden conversation.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span)`)` Optional. The root span of the golden turn for processing and maintaining audio information. The uri for the audio must contain audio saved in 16Khz sample rate.  
`turnLevelMetricsThresholdsOverride` |  `object (`[TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds)`)` Optional. Overrides for turn-level metric thresholds.  
`hallucinationMetricBehaviorOverride` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` Optional. Override for turn-level hallucination metric behavior.  
  
### Step

JSON representation  
---  
      
    
    {
    
      // Union field step can be only one of the following:
      "userInput": {
        object ([SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SessionInput))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "expectation": {
        object ([GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation))
      }
      // End of list of possible types for union field step.
    }  
  
Fields  
---  
Union field `step`. The step to perform. `step` can be only one of the following:  
`userInput` |  `object (`[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SessionInput)`)` Optional. User input for the conversation.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Optional. Transfer the conversation to a different agent.  
`expectation` |  `object (`[GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation)`)` Optional. Executes an expectation on the current turn.  
  
### SessionInput

JSON representation  
---  
      
    
    {
      "willContinue": boolean,
    
      // Union field input_type can be only one of the following:
      "text": string,
      "dtmf": string,
      "audio": string,
      "toolResponses": {
        object ([ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponses))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image))
      },
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob))
      },
      "variables": {
        object
      },
      "event": {
        object ([Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Event))
      }
      // End of list of possible types for union field input_type.
    }  
  
Fields  
---  
`willContinue` |  `boolean` Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session.When set to `true`, the agent defers processing until it receives a subsequent message where `will_continue` is `false`, or until the system detects an endpoint in the audio input.NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.  
Union field `input_type`. The type of the input. `input_type` can be only one of the following:  
`text` |  `string` Optional. Text data from the end user.  
`dtmf` |  `string` Optional. DTMF digits from the end user.  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Audio data from the end user.A base64-encoded string.  
`toolResponses` |  `object (`[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponses)`)` Optional. Execution results for the tool calls from the client.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image)`)` Optional. Image data from the end user.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob)`)` Optional. Blob data from the end user.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters.  
`event` |  `object (`[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Event)`)` Optional. Event input.  
  
### ToolResponses

JSON representation  
---  
      
    
    {
      "toolResponses": [
        {
          object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
        }
      ]
    }  
  
Fields  
---  
`toolResponses[]` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. The list of tool execution results.  
  
### ToolResponse

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "response": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)` the response is for.  
`displayName` |  `string` Output only. Display name of the tool.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Optional. The toolset tool that got executed.  
  
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
  
### Image

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "altText": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data. Supported image types includes: * image/png * image/jpeg * image/webp  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the image.A base64-encoded string.  
`altText` |  `string` Optional. The alternative text for the image.  
  
### Blob

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the blob.A base64-encoded string.  
  
### Event

JSON representation  
---  
      
    
    {
      "event": string,
      "variables": {
        object
      }
    }  
  
Fields  
---  
`event` |  `string` Required. The name of the event.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Additional variables associated with the event.  
  
### AgentTransfer

JSON representation  
---  
      
    
    {
      "targetAgent": string,
      "displayName": string
    }  
  
Fields  
---  
`targetAgent` |  `string` Required. The agent to which the conversation is being transferred. The agent will handle the conversation from this point forward. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Output only. Display name of the agent.  
  
### GoldenExpectation

JSON representation  
---  
      
    
    {
      "note": string,
      "skipEvaluation": boolean,
      "expectationLevelMetricsThresholdsOverride": {
        object ([ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds))
      },
      "agentResponseSemanticSimilarityMetricsConfigOverride": {
        object ([SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig))
      },
      "agentResponseHallucinationMetricsConfigOverride": {
        object ([HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricsConfig))
      },
      "comparisonType": enum ([ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ComparisonType)),
    
      // Union field condition can be only one of the following:
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "agentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "mockToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "noToolCalls": boolean
      // End of list of possible types for union field condition.
    }  
  
Fields  
---  
`note` |  `string` Optional. A note for this requirement, useful in reporting when specific checks fail. E.g., "Check_Payment_Tool_Called".  
`skipEvaluation` |  `boolean` Optional. If set to true, this specific expectation will not be evaluated.  
`expectationLevelMetricsThresholdsOverride` |  `object (`[ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds)`)` Optional. Overrides metrics at the step level.  
`agentResponseSemanticSimilarityMetricsConfigOverride` |  `object (`[SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig)`)` Optional. Overrides for agent_response semantic similarity metrics.  
`agentResponseHallucinationMetricsConfigOverride` |  `object (`[HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricsConfig)`)` Optional. Overrides for agent_response hallucination metrics.  
`comparisonType` |  `enum (`[ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ComparisonType)`)` Optional. The comparison type to use for the expectation check.  
Union field `condition`. The actual check to perform. `condition` can be only one of the following:  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Optional. Check that a specific tool was called with the parameters.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. Check that a specific tool had the expected response.  
`agentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Optional. Check that the agent responded with the correct response. The role "agent" is implied.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Optional. Check that the agent transferred the conversation to a different agent.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Check that the agent updated the session variables to the expected values. Used to also capture agent variable updates for golden evals.  
`mockToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`noToolCalls` |  `boolean` Optional. Check that no tools were called during this turn.  
  
### ToolCall

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "args": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `ToolResponse`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Optional. The toolset tool to execute.  
  
### Message

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Chunk))
        }
      ],
      "eventTime": string
    }  
  
Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Chunk)`)` Optional. Content of the message as a series of chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `example`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Chunk

JSON representation  
---  
      
    
    {
    
      // Union field data can be only one of the following:
      "text": string,
      "transcript": string,
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "defaultVariables": {
        object
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
Union field `data`. Chunk data. `data` can be only one of the following:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob)`)` Optional. Blob data.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom payload data.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image)`)` Optional. Image data.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Optional. Tool execution request.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. Tool execution response.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Optional. Agent transfer event.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`defaultVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
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
  
### ExpectationLevelMetricsThresholds

JSON representation  
---  
      
    
    {
    
      // Union field _tool_invocation_parameter_correctness_threshold can be only one
      // of the following:
      "toolInvocationParameterCorrectnessThreshold": number
      // End of list of possible types for union field
      // _tool_invocation_parameter_correctness_threshold.
    }  
  
Fields  
---  
Union field `_tool_invocation_parameter_correctness_threshold`.`_tool_invocation_parameter_correctness_threshold` can be only one of the following:  
`toolInvocationParameterCorrectnessThreshold` |  `number` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### SemanticSimilarityMetricsConfig

JSON representation  
---  
      
    
    {
      "enableSemanticSimilarityMetrics": boolean
    }  
  
Fields  
---  
`enableSemanticSimilarityMetrics` |  `boolean` Optional. Whether to calculate semantic similarity metrics for the evaluation.  
  
### HallucinationMetricsConfig

JSON representation  
---  
      
    
    {
      "enableHallucinationMetrics": boolean
    }  
  
Fields  
---  
`enableHallucinationMetrics` |  `boolean` Optional. Whether to calculate hallucination metrics for the evaluation.  
  
### Span

JSON representation  
---  
      
    
    {
      "name": string,
      "startTime": string,
      "endTime": string,
      "duration": string,
      "attributes": {
        object
      },
      "childSpans": [
        {
          object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the span.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the span.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`attributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Key-value attributes associated with the span.  
`childSpans[]` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span)`)` Output only. The child spans that are nested under this span.  
  
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
  
### TurnLevelMetricsThresholds

JSON representation  
---  
      
    
    {
      "semanticSimilarityChannel": enum ([SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityChannel)),
    
      // Union field _semantic_similarity_success_threshold can be only one of the
      // following:
      "semanticSimilaritySuccessThreshold": integer
      // End of list of possible types for union field
      // _semantic_similarity_success_threshold.
    
      // Union field _overall_tool_invocation_correctness_threshold can be only one
      // of the following:
      "overallToolInvocationCorrectnessThreshold": number
      // End of list of possible types for union field
      // _overall_tool_invocation_correctness_threshold.
    }  
  
Fields  
---  
`semanticSimilarityChannel` |  `enum (`[SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityChannel)`)` Optional. The semantic similarity channel to use for evaluation.  
Union field `_semantic_similarity_success_threshold`.`_semantic_similarity_success_threshold` can be only one of the following:  
`semanticSimilaritySuccessThreshold` |  `integer` Optional. The success threshold for semantic similarity. Must be an integer between 0 and 4. Default is >= 3.  
Union field `_overall_tool_invocation_correctness_threshold`.`_overall_tool_invocation_correctness_threshold` can be only one of the following:  
`overallToolInvocationCorrectnessThreshold` |  `number` Optional. The success threshold for overall tool invocation correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### Scenario

JSON representation  
---  
      
    
    {
      "task": string,
      "userFacts": [
        {
          object ([UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact))
        }
      ],
      "maxTurns": integer,
      "rubrics": [
        string
      ],
      "scenarioExpectations": [
        {
          object ([ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation))
        }
      ],
      "variableOverrides": {
        object
      },
      "taskCompletionBehavior": enum ([TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionBehavior)),
      "userGoalBehavior": enum ([UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalBehavior)),
      "evaluationExpectations": [
        string
      ],
      "scenarioExecutionMode": enum ([ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExecutionMode))
    }  
  
Fields  
---  
`task` |  `string` Required. The task to be targeted by the scenario.  
`userFacts[]` |  `object (`[UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact)`)` Optional. The user facts to be used by the scenario.  
`maxTurns` |  `integer` Optional. The maximum number of turns to simulate. The maximum allowed value is 100. The default value is 100.  
`rubrics[]` |  `string` Required. The rubrics to score the scenario against.  
`scenarioExpectations[]` |  `object (`[ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation)`)` Required. The ScenarioExpectations to evaluate the conversation produced by the user simulation.  
`variableOverrides` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Variables / Session Parameters as context for the session, keyed by variable names. Members of this struct will override any default values set by the system.Note, these are different from user facts, which are facts known to the user. Variables are parameters known to the agent: i.e. MDN (phone number) passed by the telephony system.  
`taskCompletionBehavior  
**(deprecated)**` |  `enum (`[TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionBehavior)`)` This item is deprecated!Optional. Deprecated. Use user_goal_behavior instead.  
`userGoalBehavior` |  `enum (`[UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalBehavior)`)` Optional. The expected behavior of the user goal.  
`evaluationExpectations[]` |  `string` Optional. The evaluation expectations to evaluate the conversation produced by the simulation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
`scenarioExecutionMode` |  `enum (`[ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExecutionMode)`)` Optional. The execution mode for scenario evaluations.  
  
### UserFact

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the user fact.  
`value` |  `string` Required. The value of the user fact.  
  
### ScenarioExpectation

JSON representation  
---  
      
    
    {
    
      // Union field expectation can be only one of the following:
      "toolExpectation": {
        object ([ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolExpectation))
      },
      "agentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      }
      // End of list of possible types for union field expectation.
    }  
  
Fields  
---  
Union field `expectation`. The expectation to evaluate the conversation produced by the simulation. `expectation` can be only one of the following:  
`toolExpectation` |  `object (`[ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolExpectation)`)` Optional. The tool call and response pair to be evaluated.  
`agentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Optional. The agent response to be evaluated.  
  
### ToolExpectation

JSON representation  
---  
      
    
    {
      "expectedToolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "mockToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      }
    }  
  
Fields  
---  
`expectedToolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Required. The expected tool call, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`mockToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Required. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
  
### AggregatedMetrics

JSON representation  
---  
      
    
    {
      "metricsByAppVersion": [
        {
          object ([MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByAppVersion))
        }
      ]
    }  
  
Fields  
---  
`metricsByAppVersion[]` |  `object (`[MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByAppVersion)`)` Output only. Aggregated metrics, grouped by app version ID.  
  
### MetricsByAppVersion

JSON representation  
---  
      
    
    {
      "appVersionId": string,
      "toolMetrics": [
        {
          object ([ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics))
        }
      ],
      "semanticSimilarityMetrics": [
        {
          object ([SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics))
        }
      ],
      "hallucinationMetrics": [
        {
          object ([HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics))
        }
      ],
      "toolCallLatencyMetrics": [
        {
          object ([ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics))
        }
      ],
      "turnLatencyMetrics": [
        {
          object ([TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics))
        }
      ],
      "passCount": integer,
      "failCount": integer,
      "metricsByTurn": [
        {
          object ([MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByTurn))
        }
      ]
    }  
  
Fields  
---  
`appVersionId` |  `string` Output only. The app version ID.  
`toolMetrics[]` |  `object (`[ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics)`)` Output only. Metrics for each tool within this app version.  
`semanticSimilarityMetrics[]` |  `object (`[SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics)`)` Output only. Metrics for semantic similarity within this app version.  
`hallucinationMetrics[]` |  `object (`[HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics)`)` Output only. Metrics for hallucination within this app version.  
`toolCallLatencyMetrics[]` |  `object (`[ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics)`)` Output only. Metrics for tool call latency within this app version.  
`turnLatencyMetrics[]` |  `object (`[TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics)`)` Output only. Metrics for turn latency within this app version.  
`passCount` |  `integer` Output only. The number of times the evaluation passed.  
`failCount` |  `integer` Output only. The number of times the evaluation failed.  
`metricsByTurn[]` |  `object (`[MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByTurn)`)` Output only. Metrics aggregated per turn within this app version.  
  
### ToolMetrics

JSON representation  
---  
      
    
    {
      "tool": string,
      "passCount": integer,
      "failCount": integer
    }  
  
Fields  
---  
`tool` |  `string` Output only. The name of the tool.  
`passCount` |  `integer` Output only. The number of times the tool passed.  
`failCount` |  `integer` Output only. The number of times the tool failed.  
  
### SemanticSimilarityMetrics

JSON representation  
---  
      
    
    {
      "score": number
    }  
  
Fields  
---  
`score` |  `number` Output only. The average semantic similarity score (0-4).  
  
### HallucinationMetrics

JSON representation  
---  
      
    
    {
      "score": number
    }  
  
Fields  
---  
`score` |  `number` Output only. The average hallucination score (0 to 1).  
  
### ToolCallLatencyMetrics

JSON representation  
---  
      
    
    {
      "tool": string,
      "averageLatency": string
    }  
  
Fields  
---  
`tool` |  `string` Output only. The name of the tool.  
`averageLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The average latency of the tool calls.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### TurnLatencyMetrics

JSON representation  
---  
      
    
    {
      "averageLatency": string
    }  
  
Fields  
---  
`averageLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The average latency of the turns.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### MetricsByTurn

JSON representation  
---  
      
    
    {
      "turnIndex": integer,
      "toolMetrics": [
        {
          object ([ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics))
        }
      ],
      "semanticSimilarityMetrics": [
        {
          object ([SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics))
        }
      ],
      "hallucinationMetrics": [
        {
          object ([HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics))
        }
      ],
      "toolCallLatencyMetrics": [
        {
          object ([ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics))
        }
      ],
      "turnLatencyMetrics": [
        {
          object ([TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics))
        }
      ]
    }  
  
Fields  
---  
`turnIndex` |  `integer` Output only. The turn index (0-based).  
`toolMetrics[]` |  `object (`[ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics)`)` Output only. Metrics for each tool within this turn.  
`semanticSimilarityMetrics[]` |  `object (`[SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics)`)` Output only. Metrics for semantic similarity within this turn.  
`hallucinationMetrics[]` |  `object (`[HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics)`)` Output only. Metrics for hallucination within this turn.  
`toolCallLatencyMetrics[]` |  `object (`[ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics)`)` Output only. Metrics for tool call latency within this turn.  
`turnLatencyMetrics[]` |  `object (`[TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics)`)` Output only. Metrics for turn latency within this turn.  
  
### EvaluationResult

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "evaluationStatus": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "evaluationRun": string,
      "persona": {
        object ([EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationPersona))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app#Output.Schema.Status))
      },
      "initiatedBy": string,
      "appVersion": string,
      "appVersionDisplayName": string,
      "changelog": string,
      "changelogCreateTime": string,
      "executionState": enum ([ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExecutionState)),
      "evaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds))
      },
      "config": {
        object ([EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationConfig))
      },
      "goldenRunMethod": enum ([GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenRunMethod)),
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span))
      },
      "outcomeMetadata": enum ([OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OutcomeMetadata)),
    
      // Union field result can be only one of the following:
      "goldenResult": {
        object ([GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenResult))
      },
      "scenarioResult": {
        object ([ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioResult))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`  
`displayName` |  `string` Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: " result - ".  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation result was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`evaluationStatus` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the evaluation. Only populated if execution_state is COMPLETE.  
`evaluationRun` |  `string` Output only. The evaluation run that produced this result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`persona` |  `object (`[EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationPersona)`)` Output only. The persona used to generate the conversation for the evaluation result.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo)`)` Output only. Error information for the evaluation result.  
`error  
**(deprecated)**` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app#Output.Schema.Status)`)` This item is deprecated!Output only. Deprecated: Use `error_info` instead. Errors encountered during execution.  
`initiatedBy` |  `string` Output only. The user who initiated the evaluation run that resulted in this result.  
`appVersion` |  `string` Output only. The app version used to generate the conversation that resulted in this result. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`appVersionDisplayName` |  `string` Output only. The display name of the `app_version` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelogCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionState` |  `enum (`[ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExecutionState)`)` Output only. The state of the evaluation result execution.  
`evaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds)`)` Output only. The evaluation thresholds for the result.  
`config` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationConfig)`)` Output only. The configuration used in the evaluation run that resulted in this result.  
`goldenRunMethod` |  `enum (`[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenRunMethod)`)` Output only. The method used to run the golden evaluation.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span)`)` Output only. The root span of the evaluation execution, which includes information about each step of the evaluation.  
`outcomeMetadata` |  `enum (`[OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OutcomeMetadata)`)` Output only. The outcome metadata of the evaluation. Only populated if execution_state is COMPLETE.  
Union field `result`. The result of the evaluation. Only populated when the execution_state is COMPLETED. `result` can be only one of the following:  
`goldenResult` |  `object (`[GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenResult)`)` Output only. The outcome of a golden evaluation.  
`scenarioResult` |  `object (`[ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioResult)`)` Output only. The outcome of a scenario evaluation.  
  
### GoldenResult

JSON representation  
---  
      
    
    {
      "turnReplayResults": [
        {
          object ([TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnReplayResult))
        }
      ],
      "evaluationExpectationResults": [
        {
          object ([EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult))
        }
      ]
    }  
  
Fields  
---  
`turnReplayResults[]` |  `object (`[TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnReplayResult)`)` Output only. The result of running each turn of the golden conversation.  
`evaluationExpectationResults[]` |  `object (`[EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult)`)` Output only. The results of the evaluation expectations.  
  
### TurnReplayResult

JSON representation  
---  
      
    
    {
      "conversation": string,
      "expectationOutcome": [
        {
          object ([GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectationOutcome))
        }
      ],
      "hallucinationResult": {
        object ([HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult))
      },
      "toolInvocationScore": number,
      "turnLatency": string,
      "toolCallLatencies": [
        {
          object ([ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency))
        }
      ],
      "semanticSimilarityResult": {
        object ([SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult))
      },
      "overallToolInvocationResult": {
        object ([OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OverallToolInvocationResult))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo))
      },
      "spanLatencies": [
        {
          object ([SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency))
        }
      ],
    
      // Union field _tool_ordered_invocation_score can be only one of the following:
      "toolOrderedInvocationScore": number
      // End of list of possible types for union field
      // _tool_ordered_invocation_score.
    }  
  
Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated for this turn.  
`expectationOutcome[]` |  `object (`[GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectationOutcome)`)` Output only. The outcome of each expectation.  
`hallucinationResult` |  `object (`[HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult)`)` Output only. The result of the hallucination check.  
`toolInvocationScore  
**(deprecated)**` |  `number` This item is deprecated!Output only. Deprecated. Use OverallToolInvocationResult instead.  
`turnLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Duration of the turn.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`toolCallLatencies[]` |  `object (`[ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency)`)` Output only. The latency of each tool call in the turn.  
`semanticSimilarityResult` |  `object (`[SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult)`)` Output only. The result of the semantic similarity check.  
`overallToolInvocationResult` |  `object (`[OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OverallToolInvocationResult)`)` Output only. The result of the overall tool invocation check.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo)`)` Output only. Information about the error that occurred during this turn.  
`spanLatencies[]` |  `object (`[SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency)`)` Output only. The latency of spans in the turn.  
Union field `_tool_ordered_invocation_score`.`_tool_ordered_invocation_score` can be only one of the following:  
`toolOrderedInvocationScore` |  `number` Output only. The overall tool ordered invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked in the expected order.  
  
### GoldenExpectationOutcome

JSON representation  
---  
      
    
    {
      "expectation": {
        object ([GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation))
      },
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "semanticSimilarityResult": {
        object ([SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult))
      },
      "toolInvocationResult": {
        object ([ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolInvocationResult))
      },
    
      // Union field result can be only one of the following:
      "observedToolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "observedToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "observedAgentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      },
      "observedAgentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "observedPayload": {
        object
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`expectation` |  `object (`[GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation)`)` Output only. The expectation that was evaluated.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the expectation.  
`semanticSimilarityResult  
**(deprecated)**` |  `object (`[SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult)`)` This item is deprecated!Output only. The result of the semantic similarity check.  
`toolInvocationResult` |  `object (`[ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolInvocationResult)`)` Output only. The result of the tool invocation check.  
Union field `result`. The result of the expectation. `result` can be only one of the following:  
`observedToolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Output only. The result of the tool call expectation.  
`observedToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Output only. The result of the tool response expectation.  
`observedAgentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Output only. The result of the agent response expectation.  
`observedAgentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Output only. The result of the agent transfer expectation.  
`observedPayload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. An observed custom payload. There are no expectations for custom payloads. This is only used for metrics calculation. The outcome is always SKIPPED.  
  
### SemanticSimilarityResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 4: Fully Consistent Score 3: Mostly Consistent Score 2: Partially Consistent (Minor Omissions) Score 1: Largely Inconsistent (Major Omissions) Score 0: Completely Inconsistent / Contradictory  
`explanation` |  `string` Output only. The explanation for the semantic similarity score.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the semantic similarity check. This is determined by comparing the score to the semantic_similarity_success_threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The semantic similarity score. Can be 0, 1, 2, 3, or 4.  
  
### ToolInvocationResult

JSON representation  
---  
      
    
    {
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "explanation": string,
    
      // Union field _parameter_correctness_score can be only one of the following:
      "parameterCorrectnessScore": number
      // End of list of possible types for union field _parameter_correctness_score.
    }  
  
Fields  
---  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the tool invocation check. This is determined by comparing the parameter_correctness_score to the threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`explanation` |  `string` Output only. A free text explanation for the tool invocation result.  
Union field `_parameter_correctness_score`.`_parameter_correctness_score` can be only one of the following:  
`parameterCorrectnessScore` |  `number` Output only. The tool invocation parameter correctness score. This indicates the percent of parameters from the expected tool call that were also present in the actual tool call.  
  
### HallucinationResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Justified Score 0: Not Justified Score -1: No Claim To Assess  
`explanation` |  `string` Output only. The explanation for the hallucination score.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The hallucination score. Can be -1, 0, 1.  
  
### ToolCallLatency

JSON representation  
---  
      
    
    {
      "tool": string,
      "displayName": string,
      "startTime": string,
      "endTime": string,
      "executionLatency": string
    }  
  
Fields  
---  
`tool` |  `string` Output only. The name of the tool that got executed. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`.  
`displayName` |  `string` Output only. The display name of the tool.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the tool call execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the tool call execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The latency of the tool call execution.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### OverallToolInvocationResult

JSON representation  
---  
      
    
    {
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
    
      // Union field _tool_invocation_score can be only one of the following:
      "toolInvocationScore": number
      // End of list of possible types for union field _tool_invocation_score.
    }  
  
Fields  
---  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the tool invocation check. This is determined by comparing the tool_invocation_score to the overall_tool_invocation_correctness_threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
Union field `_tool_invocation_score`.`_tool_invocation_score` can be only one of the following:  
`toolInvocationScore` |  `number` The overall tool invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked.  
  
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
  
### SpanLatency

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Type)),
      "displayName": string,
      "startTime": string,
      "endTime": string,
      "executionLatency": string,
    
      // Union field identifier can be only one of the following:
      "resource": string,
      "toolset": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      },
      "model": string,
      "callback": string
      // End of list of possible types for union field identifier.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Type)`)` Output only. The type of span.  
`displayName` |  `string` Output only. The display name of the span. Applicable to tool and guardrail spans.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The latency of span.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
Union field `identifier`. The identifier of the specific item based on its type. `identifier` can be only one of the following:  
`resource` |  `string` Output only. The resource name of the guardrail or tool spans.  
`toolset` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Output only. The toolset tool identifier.  
`model` |  `string` Output only. The name of the LLM span.  
`callback` |  `string` Output only. The name of the user callback span.  
  
### EvaluationExpectationResult

JSON representation  
---  
      
    
    {
      "evaluationExpectation": string,
      "prompt": string,
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "explanation": string
    }  
  
Fields  
---  
`evaluationExpectation` |  `string` Output only. The evaluation expectation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluation_expectation}`  
`prompt` |  `string` Output only. The prompt that was used for the evaluation.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the evaluation expectation.  
`explanation` |  `string` Output only. The explanation for the result.  
  
### ScenarioResult

JSON representation  
---  
      
    
    {
      "conversation": string,
      "task": string,
      "userFacts": [
        {
          object ([UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact))
        }
      ],
      "expectationOutcomes": [
        {
          object ([ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectationOutcome))
        }
      ],
      "rubricOutcomes": [
        {
          object ([ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioRubricOutcome))
        }
      ],
      "hallucinationResult": [
        {
          object ([HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult))
        }
      ],
      "taskCompletionResult": {
        object ([TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionResult))
      },
      "toolCallLatencies": [
        {
          object ([ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency))
        }
      ],
      "userGoalSatisfactionResult": {
        object ([UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalSatisfactionResult))
      },
      "spanLatencies": [
        {
          object ([SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency))
        }
      ],
      "evaluationExpectationResults": [
        {
          object ([EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult))
        }
      ],
    
      // Union field _all_expectations_satisfied can be only one of the following:
      "allExpectationsSatisfied": boolean
      // End of list of possible types for union field _all_expectations_satisfied.
    
      // Union field _task_completed can be only one of the following:
      "taskCompleted": boolean
      // End of list of possible types for union field _task_completed.
    }  
  
Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated in the scenario.  
`task` |  `string` Output only. The task that was used when running the scenario for this result.  
`userFacts[]` |  `object (`[UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact)`)` Output only. The user facts that were used by the scenario for this result.  
`expectationOutcomes[]` |  `object (`[ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectationOutcome)`)` Output only. The outcome of each expectation.  
`rubricOutcomes[]` |  `object (`[ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioRubricOutcome)`)` Output only. The outcome of the rubric.  
`hallucinationResult[]` |  `object (`[HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult)`)` Output only. The result of the hallucination check. There will be one hallucination result for each turn in the conversation.  
`taskCompletionResult  
**(deprecated)**` |  `object (`[TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionResult)`)` This item is deprecated!Output only. The result of the task completion check.  
`toolCallLatencies[]` |  `object (`[ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency)`)` Output only. The latency of each tool call execution in the conversation.  
`userGoalSatisfactionResult` |  `object (`[UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalSatisfactionResult)`)` Output only. The result of the user goal satisfaction check.  
`spanLatencies[]` |  `object (`[SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency)`)` Output only. The latency of spans in the conversation.  
`evaluationExpectationResults[]` |  `object (`[EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult)`)` Output only. The results of the evaluation expectations.  
Union field `_all_expectations_satisfied`.`_all_expectations_satisfied` can be only one of the following:  
`allExpectationsSatisfied` |  `boolean` Output only. Whether all expectations were satisfied for this turn.  
Union field `_task_completed`.`_task_completed` can be only one of the following:  
`taskCompleted` |  `boolean` Output only. Whether the task was completed for this turn. This is a composite of all expectations satisfied, no hallucinations, and user goal satisfaction.  
  
### ScenarioExpectationOutcome

JSON representation  
---  
      
    
    {
      "expectation": {
        object ([ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation))
      },
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
    
      // Union field result can be only one of the following:
      "observedToolCall": {
        object ([ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ObservedToolCall))
      },
      "observedAgentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`expectation` |  `object (`[ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation)`)` Output only. The expectation that was evaluated.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the ScenarioExpectation.  
Union field `result`. The result of the expectation. `result` can be only one of the following:  
`observedToolCall` |  `object (`[ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ObservedToolCall)`)` Output only. The observed tool call.  
`observedAgentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Output only. The observed agent response.  
  
### ObservedToolCall

JSON representation  
---  
      
    
    {
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      }
    }  
  
Fields  
---  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Output only. The observed tool call.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Output only. The observed tool response.  
  
### ScenarioRubricOutcome

JSON representation  
---  
      
    
    {
      "rubric": string,
      "scoreExplanation": string,
    
      // Union field _score can be only one of the following:
      "score": number
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`rubric` |  `string` Output only. The rubric that was used to evaluate the conversation.  
`scoreExplanation` |  `string` Output only. The rater's response to the rubric.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `number` Output only. The score of the conversation against the rubric.  
  
### TaskCompletionResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Task Completed Score 0: Task Not Completed Score -1: User Goal Undefined  
`explanation` |  `string` Output only. The explanation for the task completion score.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The task completion score. Can be -1, 0, 1  
  
### UserGoalSatisfactionResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 2: Graceful Handoff Score 1: User Task Satisfied Score 0: User Task Not Satisfied Score -1: User Task Unspecified  
`explanation` |  `string` Output only. The explanation for the user task satisfaction score.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The user task satisfaction score. Can be -1, 0, 1, 2.  
  
### EvaluationPersona

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "displayName": string,
      "personality": string,
      "speechConfig": {
        object ([SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpeechConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The unique identifier of the persona. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}`  
`description` |  `string` Optional. The description of the persona.  
`displayName` |  `string` Required. The display name of the persona. Unique within an app.  
`personality` |  `string` Required. An instruction for the agent on how to behave in the evaluation.  
`speechConfig` |  `object (`[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpeechConfig)`)` Optional. Configuration for how the persona sounds (TTS settings).  
  
### SpeechConfig

JSON representation  
---  
      
    
    {
      "speakingRate": number,
      "environment": enum ([BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.BackgroundEnvironment)),
      "voiceId": string
    }  
  
Fields  
---  
`speakingRate` |  `number` Optional. The speaking rate. 1.0 is normal. Lower is slower (e.g., 0.8), higher is faster (e.g., 1.5). Useful for testing how the agent handles fast talkers.  
`environment` |  `enum (`[BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.BackgroundEnvironment)`)` Optional. The simulated audio environment.  
`voiceId` |  `string` Optional. The specific voice identifier/accent to use. Example: "en-US-Wavenet-D" or "en-GB-Standard-A"  
  
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
  
### EvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "goldenEvaluationMetricsThresholds": {
        object ([GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenEvaluationMetricsThresholds))
      },
      "hallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)),
      "goldenHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)),
      "scenarioHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`goldenEvaluationMetricsThresholds` |  `object (`[GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenEvaluationMetricsThresholds)`)` Optional. The golden evaluation metrics thresholds.  
`hallucinationMetricBehavior  
**(deprecated)**` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` This item is deprecated!Optional. Deprecated: Use `golden_hallucination_metric_behavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`goldenHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for golden evaluations.  
`scenarioHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for scenario evaluations.  
  
### GoldenEvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "turnLevelMetricsThresholds": {
        object ([TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds))
      },
      "expectationLevelMetricsThresholds": {
        object ([ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds))
      },
      "toolMatchingSettings": {
        object ([ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMatchingSettings))
      }
    }  
  
Fields  
---  
`turnLevelMetricsThresholds` |  `object (`[TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds)`)` Optional. The turn level metrics thresholds.  
`expectationLevelMetricsThresholds` |  `object (`[ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds)`)` Optional. The expectation level metrics thresholds.  
`toolMatchingSettings` |  `object (`[ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMatchingSettings)`)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
### ToolMatchingSettings

JSON representation  
---  
      
    
    {
      "extraToolCallBehavior": enum ([ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExtraToolCallBehavior))
    }  
  
Fields  
---  
`extraToolCallBehavior` |  `enum (`[ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExtraToolCallBehavior)`)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
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
  
### EvaluationMetricsConfig

JSON representation  
---  
      
    
    {
      "goldenMetricsConfig": {
        object ([GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenMetricsConfig))
      },
      "scenarioMetricsConfig": {
        object ([ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioMetricsConfig))
      }
    }  
  
Fields  
---  
`goldenMetricsConfig` |  `object (`[GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenMetricsConfig)`)` Optional. Configuration for the golden metrics for the evaluation.  
`scenarioMetricsConfig` |  `object (`[ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioMetricsConfig)`)` Optional. Configuration for the scenario metrics for the evaluation.  
  
### GoldenMetricsConfig

JSON representation  
---  
      
    
    {
      "semanticSimilarityMetricsConfig": {
        object ([SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig))
      },
      "toolCorrectnessMetricsConfig": {
        object ([ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig))
      },
      "stepToolCorrectnessMetricsConfig": {
        object ([ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig))
      }
    }  
  
Fields  
---  
`semanticSimilarityMetricsConfig` |  `object (`[SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig)`)` Optional. Global configuration for semantic similarity metrics.  
`toolCorrectnessMetricsConfig` |  `object (`[ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig)`)` Optional. Configuration for turn level tool correctness metrics.  
`stepToolCorrectnessMetricsConfig` |  `object (`[ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig)`)` Optional. Configuration for step level tool correctness metrics.  
  
### ToolCorrectnessMetricsConfig

JSON representation  
---  
      
    
    {
      "enableToolCorrectnessMetrics": boolean
    }  
  
Fields  
---  
`enableToolCorrectnessMetrics` |  `boolean` Optional. Whether to calculate tool correctness metrics for the evaluation.  
  
### ScenarioMetricsConfig

JSON representation  
---  
      
    
    {
      "userGoalMetMetricsConfig": {
        object ([UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalMetMetricsConfig))
      },
      "expectationsMetMetricsConfig": {
        object ([ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationsMetMetricsConfig))
      }
    }  
  
Fields  
---  
`userGoalMetMetricsConfig` |  `object (`[UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalMetMetricsConfig)`)` Optional. Configuration for user goal met metrics.  
`expectationsMetMetricsConfig` |  `object (`[ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationsMetMetricsConfig)`)` Optional. Configuration for expectation level metrics.  
  
### UserGoalMetMetricsConfig

JSON representation  
---  
      
    
    {
      "enableUserGoalMetMetrics": boolean
    }  
  
Fields  
---  
`enableUserGoalMetMetrics` |  `boolean` Optional. Whether to calculate the user goal met metrics for the evaluation.  
  
### ExpectationsMetMetricsConfig

JSON representation  
---  
      
    
    {
      "enableExpectationsMetMetrics": boolean
    }  
  
Fields  
---  
`enableExpectationsMetMetrics` |  `boolean` Optional. Whether to calculate the expectation level metrics for the evaluation.  
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### ComparisonType

Supported comparison types for checking the agent's response.

Enums  
---  
`COMPARISON_TYPE_UNSPECIFIED` | Unspecified comparison type. Behavior defaults to SEMANTIC_SIMILARITY for agent responses and tool calls.  
`EQUALS` | Exact string match.  
`CONTAINS` | Substring match (checks if the expected string is contained in the actual response).  
`SEMANTIC_SIMILARITY` | Semantic similarity match (evaluates meaning similarity using an LLM).  
  
### SemanticSimilarityChannel

Semantic similarity channel to use.

Enums  
---  
`SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED` | Metric unspecified. Defaults to TEXT.  
`TEXT` | Use text semantic similarity.  
`AUDIO` | Use audio semantic similarity.  
  
### HallucinationMetricBehavior

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

Enums  
---  
`HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED` | Unspecified hallucination metric behavior.  
`DISABLED` | Disable hallucination metric.  
`ENABLED` | Enable hallucination metric.  
  
### TaskCompletionBehavior

The expected behavior of the user task. This is used to determine whether the scenario is successful.

Enums  
---  
`TASK_COMPLETION_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to TASK_SATISFIED.  
`TASK_SATISFIED` | The user task should be completed successfully.  
`TASK_REJECTED` | The user task should be rejected.  
  
### UserGoalBehavior

The expected behavior of the user goal. This is used to determine whether the scenario is successful.

Enums  
---  
`USER_GOAL_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to USER_GOAL_SATISFIED.  
`USER_GOAL_SATISFIED` | The user goal should be completed successfully.  
`USER_GOAL_REJECTED` | The user goal should be rejected.  
`USER_GOAL_IGNORED` | Ignore the user goal status.  
  
### ScenarioExecutionMode

The execution mode for scenario evaluations.

Enums  
---  
`SCENARIO_EXECUTION_MODE_UNSPECIFIED` | Unspecified execution mode. Defaults to QUALITY_OPTIMIZED.  
`QUALITY_OPTIMIZED` | Quality optimized mode.  
`SPEED_OPTIMIZED` | Speed optimized mode.  
  
### Outcome

The outcome of the evaluation or expectation.

Enums  
---  
`OUTCOME_UNSPECIFIED` | Evaluation outcome is not specified.  
`PASS` | Evaluation/Expectation passed. In the case of an evaluation, this means that all expectations were met.  
`FAIL` | Evaluation/Expectation failed. In the case of an evaluation, this means that at least one expectation was not met.  
`SKIPPED` | Evaluation/Expectation was skipped.  
  
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
  
### Type

The type of span. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TOOL` | Tool call span.  
`USER_CALLBACK` | User callback span.  
`GUARDRAIL` | Guardrail span.  
`LLM` | LLM span.  
  
### BackgroundEnvironment

Simulated audio environment.

Enums  
---  
`BACKGROUND_ENVIRONMENT_UNSPECIFIED` | Background environment unspecified.  
`CALL_CENTER` | Call center environment.  
`TRAFFIC` | Traffic noise environment.  
`KIDS_NOISE` | Kids noise environment.  
`CAFE` | Cafe environment.  
  
### ExecutionState

The state of the evaluation result execution.

Enums  
---  
`EXECUTION_STATE_UNSPECIFIED` | Evaluation result execution state is not specified.  
`QUEUED` | Evaluation result execution is queued.  
`RUNNING` | Evaluation result execution is running.  
`COMPLETED` | Evaluation result execution has completed.  
`ERROR` | Evaluation result execution failed due to an internal error.  
`CANCELLED` | Evaluation result execution was cancelled.  
  
### ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
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
  
### GoldenRunMethod

The method used to run the evaluation.

Enums  
---  
`GOLDEN_RUN_METHOD_UNSPECIFIED` | Run method is not specified.  
`STABLE` | Run the evaluation as stable replay, where each turn is a unique session with the previous expected turns injected as context.  
`NAIVE` | Run the evaluation as naive replay, where the run is a single session with no context injected.  
  
### OutcomeMetadata

Metadata about the outcome of the evaluation.

Enums  
---  
`OUTCOME_METADATA_UNSPECIFIED` | Unspecified outcome metadata.  
`GRACEFUL_HANDOFF` | The evaluation resulted in a graceful handoff to a human representative.  
  
## Output Schema

An evaluation represents all of the information needed to simulate and evaluate an agent.

### Evaluation

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "tags": [
        string
      ],
      "evaluationDatasets": [
        string
      ],
      "createTime": string,
      "createdBy": string,
      "updateTime": string,
      "lastUpdatedBy": string,
      "evaluationRuns": [
        string
      ],
      "etag": string,
      "aggregatedMetrics": {
        object ([AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics))
      },
      "lastCompletedResult": {
        object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult))
      },
      "invalid": boolean,
      "lastTenResults": [
        {
          object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult))
        }
      ],
      "evaluationMetricsThresholdOverride": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds))
      },
      "evaluationMetricsConfigOverride": {
        object ([EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsConfig))
      },
    
      // Union field inputs can be only one of the following:
      "golden": {
        object ([Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Golden))
      },
      "scenario": {
        object ([Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Scenario))
      }
      // End of list of possible types for union field inputs.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`displayName` |  `string` Required. User-defined display name of the evaluation. Unique within an App.  
`description` |  `string` Optional. User-defined description of the evaluation.  
`tags[]` |  `string` Optional. User defined tags to categorize the evaluation.  
`evaluationDatasets[]` |  `string` Output only. List of evaluation datasets the evaluation belongs to. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createdBy` |  `string` Output only. The user who created the evaluation.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdatedBy` |  `string` Output only. The user who last updated the evaluation.  
`evaluationRuns[]` |  `string` Output only. The EvaluationRuns that this Evaluation is associated with.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`aggregatedMetrics` |  `object (`[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics)`)` Output only. The aggregated metrics for this evaluation across all runs.  
`lastCompletedResult` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult)`)` Output only. The latest evaluation result for this evaluation.  
`invalid` |  `boolean` Output only. Whether the evaluation is invalid. This can happen if an evaluation is referencing a tool, toolset, or agent that has since been deleted.  
`lastTenResults[]` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationResult)`)` Output only. The last 10 evaluation results for this evaluation. This is only populated if include_last_ten_results is set to true in the ListEvaluationsRequest or GetEvaluationRequest.  
`evaluationMetricsThresholdOverride` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds)`)` Optional. Overrides metrics thresholds for this specific evaluation.  
`evaluationMetricsConfigOverride` |  `object (`[EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsConfig)`)` Optional. Overrides metrics config for this specific evaluation.  
Union field `inputs`. The inputs for the evaluation `inputs` can be only one of the following:  
`golden` |  `object (`[Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Golden)`)` Optional. The golden steps to be evaluated.  
`scenario` |  `object (`[Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Scenario)`)` Optional. The config for a scenario.  
  
### Golden

JSON representation  
---  
      
    
    {
      "turns": [
        {
          object ([GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenTurn))
        }
      ],
      "evaluationExpectations": [
        string
      ]
    }  
  
Fields  
---  
`turns[]` |  `object (`[GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenTurn)`)` Required. The golden turns required to replay a golden conversation. The maximum number of allowed turns is 100.  
`evaluationExpectations[]` |  `string` Optional. The evaluation expectations to evaluate the replayed conversation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
  
### GoldenTurn

JSON representation  
---  
      
    
    {
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Step))
        }
      ],
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span))
      },
      "turnLevelMetricsThresholdsOverride": {
        object ([TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds))
      },
      "hallucinationMetricBehaviorOverride": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Step)`)` Required. The steps required to replay a golden conversation.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span)`)` Optional. The root span of the golden turn for processing and maintaining audio information. The uri for the audio must contain audio saved in 16Khz sample rate.  
`turnLevelMetricsThresholdsOverride` |  `object (`[TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds)`)` Optional. Overrides for turn-level metric thresholds.  
`hallucinationMetricBehaviorOverride` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` Optional. Override for turn-level hallucination metric behavior.  
  
### Step

JSON representation  
---  
      
    
    {
    
      // Union field step can be only one of the following:
      "userInput": {
        object ([SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SessionInput))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "expectation": {
        object ([GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation))
      }
      // End of list of possible types for union field step.
    }  
  
Fields  
---  
Union field `step`. The step to perform. `step` can be only one of the following:  
`userInput` |  `object (`[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SessionInput)`)` Optional. User input for the conversation.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Optional. Transfer the conversation to a different agent.  
`expectation` |  `object (`[GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation)`)` Optional. Executes an expectation on the current turn.  
  
### SessionInput

JSON representation  
---  
      
    
    {
      "willContinue": boolean,
    
      // Union field input_type can be only one of the following:
      "text": string,
      "dtmf": string,
      "audio": string,
      "toolResponses": {
        object ([ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponses))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image))
      },
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob))
      },
      "variables": {
        object
      },
      "event": {
        object ([Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Event))
      }
      // End of list of possible types for union field input_type.
    }  
  
Fields  
---  
`willContinue` |  `boolean` Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session.When set to `true`, the agent defers processing until it receives a subsequent message where `will_continue` is `false`, or until the system detects an endpoint in the audio input.NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.  
Union field `input_type`. The type of the input. `input_type` can be only one of the following:  
`text` |  `string` Optional. Text data from the end user.  
`dtmf` |  `string` Optional. DTMF digits from the end user.  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Audio data from the end user.A base64-encoded string.  
`toolResponses` |  `object (`[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponses)`)` Optional. Execution results for the tool calls from the client.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image)`)` Optional. Image data from the end user.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob)`)` Optional. Blob data from the end user.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters.  
`event` |  `object (`[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Event)`)` Optional. Event input.  
  
### ToolResponses

JSON representation  
---  
      
    
    {
      "toolResponses": [
        {
          object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
        }
      ]
    }  
  
Fields  
---  
`toolResponses[]` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. The list of tool execution results.  
  
### ToolResponse

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "response": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)` the response is for.  
`displayName` |  `string` Output only. Display name of the tool.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Optional. The toolset tool that got executed.  
  
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
  
### Image

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "altText": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data. Supported image types includes: * image/png * image/jpeg * image/webp  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the image.A base64-encoded string.  
`altText` |  `string` Optional. The alternative text for the image.  
  
### Blob

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the blob.A base64-encoded string.  
  
### Event

JSON representation  
---  
      
    
    {
      "event": string,
      "variables": {
        object
      }
    }  
  
Fields  
---  
`event` |  `string` Required. The name of the event.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Additional variables associated with the event.  
  
### AgentTransfer

JSON representation  
---  
      
    
    {
      "targetAgent": string,
      "displayName": string
    }  
  
Fields  
---  
`targetAgent` |  `string` Required. The agent to which the conversation is being transferred. The agent will handle the conversation from this point forward. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Output only. Display name of the agent.  
  
### GoldenExpectation

JSON representation  
---  
      
    
    {
      "note": string,
      "skipEvaluation": boolean,
      "expectationLevelMetricsThresholdsOverride": {
        object ([ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds))
      },
      "agentResponseSemanticSimilarityMetricsConfigOverride": {
        object ([SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig))
      },
      "agentResponseHallucinationMetricsConfigOverride": {
        object ([HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricsConfig))
      },
      "comparisonType": enum ([ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ComparisonType)),
    
      // Union field condition can be only one of the following:
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "agentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "mockToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "noToolCalls": boolean
      // End of list of possible types for union field condition.
    }  
  
Fields  
---  
`note` |  `string` Optional. A note for this requirement, useful in reporting when specific checks fail. E.g., "Check_Payment_Tool_Called".  
`skipEvaluation` |  `boolean` Optional. If set to true, this specific expectation will not be evaluated.  
`expectationLevelMetricsThresholdsOverride` |  `object (`[ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds)`)` Optional. Overrides metrics at the step level.  
`agentResponseSemanticSimilarityMetricsConfigOverride` |  `object (`[SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig)`)` Optional. Overrides for agent_response semantic similarity metrics.  
`agentResponseHallucinationMetricsConfigOverride` |  `object (`[HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricsConfig)`)` Optional. Overrides for agent_response hallucination metrics.  
`comparisonType` |  `enum (`[ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ComparisonType)`)` Optional. The comparison type to use for the expectation check.  
Union field `condition`. The actual check to perform. `condition` can be only one of the following:  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Optional. Check that a specific tool was called with the parameters.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. Check that a specific tool had the expected response.  
`agentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Optional. Check that the agent responded with the correct response. The role "agent" is implied.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Optional. Check that the agent transferred the conversation to a different agent.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Check that the agent updated the session variables to the expected values. Used to also capture agent variable updates for golden evals.  
`mockToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`noToolCalls` |  `boolean` Optional. Check that no tools were called during this turn.  
  
### ToolCall

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "args": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `ToolResponse`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Optional. The toolset tool to execute.  
  
### Message

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Chunk))
        }
      ],
      "eventTime": string
    }  
  
Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Chunk)`)` Optional. Content of the message as a series of chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `example`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Chunk

JSON representation  
---  
      
    
    {
    
      // Union field data can be only one of the following:
      "text": string,
      "transcript": string,
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "defaultVariables": {
        object
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
Union field `data`. Chunk data. `data` can be only one of the following:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Blob)`)` Optional. Blob data.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom payload data.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Image)`)` Optional. Image data.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Optional. Tool execution request.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Optional. Tool execution response.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Optional. Agent transfer event.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`defaultVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
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
  
### ExpectationLevelMetricsThresholds

JSON representation  
---  
      
    
    {
    
      // Union field _tool_invocation_parameter_correctness_threshold can be only one
      // of the following:
      "toolInvocationParameterCorrectnessThreshold": number
      // End of list of possible types for union field
      // _tool_invocation_parameter_correctness_threshold.
    }  
  
Fields  
---  
Union field `_tool_invocation_parameter_correctness_threshold`.`_tool_invocation_parameter_correctness_threshold` can be only one of the following:  
`toolInvocationParameterCorrectnessThreshold` |  `number` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### SemanticSimilarityMetricsConfig

JSON representation  
---  
      
    
    {
      "enableSemanticSimilarityMetrics": boolean
    }  
  
Fields  
---  
`enableSemanticSimilarityMetrics` |  `boolean` Optional. Whether to calculate semantic similarity metrics for the evaluation.  
  
### HallucinationMetricsConfig

JSON representation  
---  
      
    
    {
      "enableHallucinationMetrics": boolean
    }  
  
Fields  
---  
`enableHallucinationMetrics` |  `boolean` Optional. Whether to calculate hallucination metrics for the evaluation.  
  
### Span

JSON representation  
---  
      
    
    {
      "name": string,
      "startTime": string,
      "endTime": string,
      "duration": string,
      "attributes": {
        object
      },
      "childSpans": [
        {
          object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the span.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the span.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`attributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Key-value attributes associated with the span.  
`childSpans[]` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span)`)` Output only. The child spans that are nested under this span.  
  
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
  
### TurnLevelMetricsThresholds

JSON representation  
---  
      
    
    {
      "semanticSimilarityChannel": enum ([SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityChannel)),
    
      // Union field _semantic_similarity_success_threshold can be only one of the
      // following:
      "semanticSimilaritySuccessThreshold": integer
      // End of list of possible types for union field
      // _semantic_similarity_success_threshold.
    
      // Union field _overall_tool_invocation_correctness_threshold can be only one
      // of the following:
      "overallToolInvocationCorrectnessThreshold": number
      // End of list of possible types for union field
      // _overall_tool_invocation_correctness_threshold.
    }  
  
Fields  
---  
`semanticSimilarityChannel` |  `enum (`[SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityChannel)`)` Optional. The semantic similarity channel to use for evaluation.  
Union field `_semantic_similarity_success_threshold`.`_semantic_similarity_success_threshold` can be only one of the following:  
`semanticSimilaritySuccessThreshold` |  `integer` Optional. The success threshold for semantic similarity. Must be an integer between 0 and 4. Default is >= 3.  
Union field `_overall_tool_invocation_correctness_threshold`.`_overall_tool_invocation_correctness_threshold` can be only one of the following:  
`overallToolInvocationCorrectnessThreshold` |  `number` Optional. The success threshold for overall tool invocation correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### Scenario

JSON representation  
---  
      
    
    {
      "task": string,
      "userFacts": [
        {
          object ([UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact))
        }
      ],
      "maxTurns": integer,
      "rubrics": [
        string
      ],
      "scenarioExpectations": [
        {
          object ([ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation))
        }
      ],
      "variableOverrides": {
        object
      },
      "taskCompletionBehavior": enum ([TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionBehavior)),
      "userGoalBehavior": enum ([UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalBehavior)),
      "evaluationExpectations": [
        string
      ],
      "scenarioExecutionMode": enum ([ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExecutionMode))
    }  
  
Fields  
---  
`task` |  `string` Required. The task to be targeted by the scenario.  
`userFacts[]` |  `object (`[UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact)`)` Optional. The user facts to be used by the scenario.  
`maxTurns` |  `integer` Optional. The maximum number of turns to simulate. The maximum allowed value is 100. The default value is 100.  
`rubrics[]` |  `string` Required. The rubrics to score the scenario against.  
`scenarioExpectations[]` |  `object (`[ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation)`)` Required. The ScenarioExpectations to evaluate the conversation produced by the user simulation.  
`variableOverrides` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Variables / Session Parameters as context for the session, keyed by variable names. Members of this struct will override any default values set by the system.Note, these are different from user facts, which are facts known to the user. Variables are parameters known to the agent: i.e. MDN (phone number) passed by the telephony system.  
`taskCompletionBehavior  
**(deprecated)**` |  `enum (`[TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionBehavior)`)` This item is deprecated!Optional. Deprecated. Use user_goal_behavior instead.  
`userGoalBehavior` |  `enum (`[UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalBehavior)`)` Optional. The expected behavior of the user goal.  
`evaluationExpectations[]` |  `string` Optional. The evaluation expectations to evaluate the conversation produced by the simulation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
`scenarioExecutionMode` |  `enum (`[ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExecutionMode)`)` Optional. The execution mode for scenario evaluations.  
  
### UserFact

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the user fact.  
`value` |  `string` Required. The value of the user fact.  
  
### ScenarioExpectation

JSON representation  
---  
      
    
    {
    
      // Union field expectation can be only one of the following:
      "toolExpectation": {
        object ([ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolExpectation))
      },
      "agentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      }
      // End of list of possible types for union field expectation.
    }  
  
Fields  
---  
Union field `expectation`. The expectation to evaluate the conversation produced by the simulation. `expectation` can be only one of the following:  
`toolExpectation` |  `object (`[ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolExpectation)`)` Optional. The tool call and response pair to be evaluated.  
`agentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Optional. The agent response to be evaluated.  
  
### ToolExpectation

JSON representation  
---  
      
    
    {
      "expectedToolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "mockToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      }
    }  
  
Fields  
---  
`expectedToolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Required. The expected tool call, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`mockToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Required. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
  
### AggregatedMetrics

JSON representation  
---  
      
    
    {
      "metricsByAppVersion": [
        {
          object ([MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByAppVersion))
        }
      ]
    }  
  
Fields  
---  
`metricsByAppVersion[]` |  `object (`[MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByAppVersion)`)` Output only. Aggregated metrics, grouped by app version ID.  
  
### MetricsByAppVersion

JSON representation  
---  
      
    
    {
      "appVersionId": string,
      "toolMetrics": [
        {
          object ([ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics))
        }
      ],
      "semanticSimilarityMetrics": [
        {
          object ([SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics))
        }
      ],
      "hallucinationMetrics": [
        {
          object ([HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics))
        }
      ],
      "toolCallLatencyMetrics": [
        {
          object ([ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics))
        }
      ],
      "turnLatencyMetrics": [
        {
          object ([TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics))
        }
      ],
      "passCount": integer,
      "failCount": integer,
      "metricsByTurn": [
        {
          object ([MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByTurn))
        }
      ]
    }  
  
Fields  
---  
`appVersionId` |  `string` Output only. The app version ID.  
`toolMetrics[]` |  `object (`[ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics)`)` Output only. Metrics for each tool within this app version.  
`semanticSimilarityMetrics[]` |  `object (`[SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics)`)` Output only. Metrics for semantic similarity within this app version.  
`hallucinationMetrics[]` |  `object (`[HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics)`)` Output only. Metrics for hallucination within this app version.  
`toolCallLatencyMetrics[]` |  `object (`[ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics)`)` Output only. Metrics for tool call latency within this app version.  
`turnLatencyMetrics[]` |  `object (`[TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics)`)` Output only. Metrics for turn latency within this app version.  
`passCount` |  `integer` Output only. The number of times the evaluation passed.  
`failCount` |  `integer` Output only. The number of times the evaluation failed.  
`metricsByTurn[]` |  `object (`[MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.MetricsByTurn)`)` Output only. Metrics aggregated per turn within this app version.  
  
### ToolMetrics

JSON representation  
---  
      
    
    {
      "tool": string,
      "passCount": integer,
      "failCount": integer
    }  
  
Fields  
---  
`tool` |  `string` Output only. The name of the tool.  
`passCount` |  `integer` Output only. The number of times the tool passed.  
`failCount` |  `integer` Output only. The number of times the tool failed.  
  
### SemanticSimilarityMetrics

JSON representation  
---  
      
    
    {
      "score": number
    }  
  
Fields  
---  
`score` |  `number` Output only. The average semantic similarity score (0-4).  
  
### HallucinationMetrics

JSON representation  
---  
      
    
    {
      "score": number
    }  
  
Fields  
---  
`score` |  `number` Output only. The average hallucination score (0 to 1).  
  
### ToolCallLatencyMetrics

JSON representation  
---  
      
    
    {
      "tool": string,
      "averageLatency": string
    }  
  
Fields  
---  
`tool` |  `string` Output only. The name of the tool.  
`averageLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The average latency of the tool calls.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### TurnLatencyMetrics

JSON representation  
---  
      
    
    {
      "averageLatency": string
    }  
  
Fields  
---  
`averageLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The average latency of the turns.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### MetricsByTurn

JSON representation  
---  
      
    
    {
      "turnIndex": integer,
      "toolMetrics": [
        {
          object ([ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics))
        }
      ],
      "semanticSimilarityMetrics": [
        {
          object ([SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics))
        }
      ],
      "hallucinationMetrics": [
        {
          object ([HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics))
        }
      ],
      "toolCallLatencyMetrics": [
        {
          object ([ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics))
        }
      ],
      "turnLatencyMetrics": [
        {
          object ([TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics))
        }
      ]
    }  
  
Fields  
---  
`turnIndex` |  `integer` Output only. The turn index (0-based).  
`toolMetrics[]` |  `object (`[ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMetrics)`)` Output only. Metrics for each tool within this turn.  
`semanticSimilarityMetrics[]` |  `object (`[SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetrics)`)` Output only. Metrics for semantic similarity within this turn.  
`hallucinationMetrics[]` |  `object (`[HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetrics)`)` Output only. Metrics for hallucination within this turn.  
`toolCallLatencyMetrics[]` |  `object (`[ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatencyMetrics)`)` Output only. Metrics for tool call latency within this turn.  
`turnLatencyMetrics[]` |  `object (`[TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLatencyMetrics)`)` Output only. Metrics for turn latency within this turn.  
  
### EvaluationResult

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "evaluationStatus": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "evaluationRun": string,
      "persona": {
        object ([EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationPersona))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app#Output.Schema.Status))
      },
      "initiatedBy": string,
      "appVersion": string,
      "appVersionDisplayName": string,
      "changelog": string,
      "changelogCreateTime": string,
      "executionState": enum ([ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExecutionState)),
      "evaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds))
      },
      "config": {
        object ([EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationConfig))
      },
      "goldenRunMethod": enum ([GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenRunMethod)),
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span))
      },
      "outcomeMetadata": enum ([OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OutcomeMetadata)),
    
      // Union field result can be only one of the following:
      "goldenResult": {
        object ([GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenResult))
      },
      "scenarioResult": {
        object ([ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioResult))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`  
`displayName` |  `string` Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: " result - ".  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation result was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`evaluationStatus` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the evaluation. Only populated if execution_state is COMPLETE.  
`evaluationRun` |  `string` Output only. The evaluation run that produced this result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`persona` |  `object (`[EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationPersona)`)` Output only. The persona used to generate the conversation for the evaluation result.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo)`)` Output only. Error information for the evaluation result.  
`error  
**(deprecated)**` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app#Output.Schema.Status)`)` This item is deprecated!Output only. Deprecated: Use `error_info` instead. Errors encountered during execution.  
`initiatedBy` |  `string` Output only. The user who initiated the evaluation run that resulted in this result.  
`appVersion` |  `string` Output only. The app version used to generate the conversation that resulted in this result. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`appVersionDisplayName` |  `string` Output only. The display name of the `app_version` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelogCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionState` |  `enum (`[ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExecutionState)`)` Output only. The state of the evaluation result execution.  
`evaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationMetricsThresholds)`)` Output only. The evaluation thresholds for the result.  
`config` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationConfig)`)` Output only. The configuration used in the evaluation run that resulted in this result.  
`goldenRunMethod` |  `enum (`[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenRunMethod)`)` Output only. The method used to run the golden evaluation.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Span)`)` Output only. The root span of the evaluation execution, which includes information about each step of the evaluation.  
`outcomeMetadata` |  `enum (`[OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OutcomeMetadata)`)` Output only. The outcome metadata of the evaluation. Only populated if execution_state is COMPLETE.  
Union field `result`. The result of the evaluation. Only populated when the execution_state is COMPLETED. `result` can be only one of the following:  
`goldenResult` |  `object (`[GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenResult)`)` Output only. The outcome of a golden evaluation.  
`scenarioResult` |  `object (`[ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioResult)`)` Output only. The outcome of a scenario evaluation.  
  
### GoldenResult

JSON representation  
---  
      
    
    {
      "turnReplayResults": [
        {
          object ([TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnReplayResult))
        }
      ],
      "evaluationExpectationResults": [
        {
          object ([EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult))
        }
      ]
    }  
  
Fields  
---  
`turnReplayResults[]` |  `object (`[TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnReplayResult)`)` Output only. The result of running each turn of the golden conversation.  
`evaluationExpectationResults[]` |  `object (`[EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult)`)` Output only. The results of the evaluation expectations.  
  
### TurnReplayResult

JSON representation  
---  
      
    
    {
      "conversation": string,
      "expectationOutcome": [
        {
          object ([GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectationOutcome))
        }
      ],
      "hallucinationResult": {
        object ([HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult))
      },
      "toolInvocationScore": number,
      "turnLatency": string,
      "toolCallLatencies": [
        {
          object ([ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency))
        }
      ],
      "semanticSimilarityResult": {
        object ([SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult))
      },
      "overallToolInvocationResult": {
        object ([OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OverallToolInvocationResult))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo))
      },
      "spanLatencies": [
        {
          object ([SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency))
        }
      ],
    
      // Union field _tool_ordered_invocation_score can be only one of the following:
      "toolOrderedInvocationScore": number
      // End of list of possible types for union field
      // _tool_ordered_invocation_score.
    }  
  
Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated for this turn.  
`expectationOutcome[]` |  `object (`[GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectationOutcome)`)` Output only. The outcome of each expectation.  
`hallucinationResult` |  `object (`[HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult)`)` Output only. The result of the hallucination check.  
`toolInvocationScore  
**(deprecated)**` |  `number` This item is deprecated!Output only. Deprecated. Use OverallToolInvocationResult instead.  
`turnLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Duration of the turn.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`toolCallLatencies[]` |  `object (`[ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency)`)` Output only. The latency of each tool call in the turn.  
`semanticSimilarityResult` |  `object (`[SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult)`)` Output only. The result of the semantic similarity check.  
`overallToolInvocationResult` |  `object (`[OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.OverallToolInvocationResult)`)` Output only. The result of the overall tool invocation check.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationErrorInfo)`)` Output only. Information about the error that occurred during this turn.  
`spanLatencies[]` |  `object (`[SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency)`)` Output only. The latency of spans in the turn.  
Union field `_tool_ordered_invocation_score`.`_tool_ordered_invocation_score` can be only one of the following:  
`toolOrderedInvocationScore` |  `number` Output only. The overall tool ordered invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked in the expected order.  
  
### GoldenExpectationOutcome

JSON representation  
---  
      
    
    {
      "expectation": {
        object ([GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation))
      },
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "semanticSimilarityResult": {
        object ([SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult))
      },
      "toolInvocationResult": {
        object ([ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolInvocationResult))
      },
    
      // Union field result can be only one of the following:
      "observedToolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "observedToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      },
      "observedAgentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      },
      "observedAgentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer))
      },
      "observedPayload": {
        object
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`expectation` |  `object (`[GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenExpectation)`)` Output only. The expectation that was evaluated.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the expectation.  
`semanticSimilarityResult  
**(deprecated)**` |  `object (`[SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityResult)`)` This item is deprecated!Output only. The result of the semantic similarity check.  
`toolInvocationResult` |  `object (`[ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolInvocationResult)`)` Output only. The result of the tool invocation check.  
Union field `result`. The result of the expectation. `result` can be only one of the following:  
`observedToolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Output only. The result of the tool call expectation.  
`observedToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Output only. The result of the tool response expectation.  
`observedAgentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Output only. The result of the agent response expectation.  
`observedAgentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AgentTransfer)`)` Output only. The result of the agent transfer expectation.  
`observedPayload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. An observed custom payload. There are no expectations for custom payloads. This is only used for metrics calculation. The outcome is always SKIPPED.  
  
### SemanticSimilarityResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 4: Fully Consistent Score 3: Mostly Consistent Score 2: Partially Consistent (Minor Omissions) Score 1: Largely Inconsistent (Major Omissions) Score 0: Completely Inconsistent / Contradictory  
`explanation` |  `string` Output only. The explanation for the semantic similarity score.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the semantic similarity check. This is determined by comparing the score to the semantic_similarity_success_threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The semantic similarity score. Can be 0, 1, 2, 3, or 4.  
  
### ToolInvocationResult

JSON representation  
---  
      
    
    {
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "explanation": string,
    
      // Union field _parameter_correctness_score can be only one of the following:
      "parameterCorrectnessScore": number
      // End of list of possible types for union field _parameter_correctness_score.
    }  
  
Fields  
---  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the tool invocation check. This is determined by comparing the parameter_correctness_score to the threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`explanation` |  `string` Output only. A free text explanation for the tool invocation result.  
Union field `_parameter_correctness_score`.`_parameter_correctness_score` can be only one of the following:  
`parameterCorrectnessScore` |  `number` Output only. The tool invocation parameter correctness score. This indicates the percent of parameters from the expected tool call that were also present in the actual tool call.  
  
### HallucinationResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Justified Score 0: Not Justified Score -1: No Claim To Assess  
`explanation` |  `string` Output only. The explanation for the hallucination score.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The hallucination score. Can be -1, 0, 1.  
  
### ToolCallLatency

JSON representation  
---  
      
    
    {
      "tool": string,
      "displayName": string,
      "startTime": string,
      "endTime": string,
      "executionLatency": string
    }  
  
Fields  
---  
`tool` |  `string` Output only. The name of the tool that got executed. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`.  
`displayName` |  `string` Output only. The display name of the tool.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the tool call execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the tool call execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The latency of the tool call execution.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### OverallToolInvocationResult

JSON representation  
---  
      
    
    {
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
    
      // Union field _tool_invocation_score can be only one of the following:
      "toolInvocationScore": number
      // End of list of possible types for union field _tool_invocation_score.
    }  
  
Fields  
---  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the tool invocation check. This is determined by comparing the tool_invocation_score to the overall_tool_invocation_correctness_threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
Union field `_tool_invocation_score`.`_tool_invocation_score` can be only one of the following:  
`toolInvocationScore` |  `number` The overall tool invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked.  
  
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
  
### SpanLatency

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Type)),
      "displayName": string,
      "startTime": string,
      "endTime": string,
      "executionLatency": string,
    
      // Union field identifier can be only one of the following:
      "resource": string,
      "toolset": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool))
      },
      "model": string,
      "callback": string
      // End of list of possible types for union field identifier.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Type)`)` Output only. The type of span.  
`displayName` |  `string` Output only. The display name of the span. Applicable to tool and guardrail spans.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The latency of span.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
Union field `identifier`. The identifier of the specific item based on its type. `identifier` can be only one of the following:  
`resource` |  `string` Output only. The resource name of the guardrail or tool spans.  
`toolset` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolsetTool)`)` Output only. The toolset tool identifier.  
`model` |  `string` Output only. The name of the LLM span.  
`callback` |  `string` Output only. The name of the user callback span.  
  
### EvaluationExpectationResult

JSON representation  
---  
      
    
    {
      "evaluationExpectation": string,
      "prompt": string,
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
      "explanation": string
    }  
  
Fields  
---  
`evaluationExpectation` |  `string` Output only. The evaluation expectation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluation_expectation}`  
`prompt` |  `string` Output only. The prompt that was used for the evaluation.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the evaluation expectation.  
`explanation` |  `string` Output only. The explanation for the result.  
  
### ScenarioResult

JSON representation  
---  
      
    
    {
      "conversation": string,
      "task": string,
      "userFacts": [
        {
          object ([UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact))
        }
      ],
      "expectationOutcomes": [
        {
          object ([ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectationOutcome))
        }
      ],
      "rubricOutcomes": [
        {
          object ([ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioRubricOutcome))
        }
      ],
      "hallucinationResult": [
        {
          object ([HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult))
        }
      ],
      "taskCompletionResult": {
        object ([TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionResult))
      },
      "toolCallLatencies": [
        {
          object ([ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency))
        }
      ],
      "userGoalSatisfactionResult": {
        object ([UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalSatisfactionResult))
      },
      "spanLatencies": [
        {
          object ([SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency))
        }
      ],
      "evaluationExpectationResults": [
        {
          object ([EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult))
        }
      ],
    
      // Union field _all_expectations_satisfied can be only one of the following:
      "allExpectationsSatisfied": boolean
      // End of list of possible types for union field _all_expectations_satisfied.
    
      // Union field _task_completed can be only one of the following:
      "taskCompleted": boolean
      // End of list of possible types for union field _task_completed.
    }  
  
Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated in the scenario.  
`task` |  `string` Output only. The task that was used when running the scenario for this result.  
`userFacts[]` |  `object (`[UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserFact)`)` Output only. The user facts that were used by the scenario for this result.  
`expectationOutcomes[]` |  `object (`[ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectationOutcome)`)` Output only. The outcome of each expectation.  
`rubricOutcomes[]` |  `object (`[ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioRubricOutcome)`)` Output only. The outcome of the rubric.  
`hallucinationResult[]` |  `object (`[HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationResult)`)` Output only. The result of the hallucination check. There will be one hallucination result for each turn in the conversation.  
`taskCompletionResult  
**(deprecated)**` |  `object (`[TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TaskCompletionResult)`)` This item is deprecated!Output only. The result of the task completion check.  
`toolCallLatencies[]` |  `object (`[ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCallLatency)`)` Output only. The latency of each tool call execution in the conversation.  
`userGoalSatisfactionResult` |  `object (`[UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalSatisfactionResult)`)` Output only. The result of the user goal satisfaction check.  
`spanLatencies[]` |  `object (`[SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpanLatency)`)` Output only. The latency of spans in the conversation.  
`evaluationExpectationResults[]` |  `object (`[EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.EvaluationExpectationResult)`)` Output only. The results of the evaluation expectations.  
Union field `_all_expectations_satisfied`.`_all_expectations_satisfied` can be only one of the following:  
`allExpectationsSatisfied` |  `boolean` Output only. Whether all expectations were satisfied for this turn.  
Union field `_task_completed`.`_task_completed` can be only one of the following:  
`taskCompleted` |  `boolean` Output only. Whether the task was completed for this turn. This is a composite of all expectations satisfied, no hallucinations, and user goal satisfaction.  
  
### ScenarioExpectationOutcome

JSON representation  
---  
      
    
    {
      "expectation": {
        object ([ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation))
      },
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)),
    
      // Union field result can be only one of the following:
      "observedToolCall": {
        object ([ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ObservedToolCall))
      },
      "observedAgentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`expectation` |  `object (`[ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioExpectation)`)` Output only. The expectation that was evaluated.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Outcome)`)` Output only. The outcome of the ScenarioExpectation.  
Union field `result`. The result of the expectation. `result` can be only one of the following:  
`observedToolCall` |  `object (`[ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ObservedToolCall)`)` Output only. The observed tool call.  
`observedAgentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.Message)`)` Output only. The observed agent response.  
  
### ObservedToolCall

JSON representation  
---  
      
    
    {
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse))
      }
    }  
  
Fields  
---  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCall)`)` Output only. The observed tool call.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolResponse)`)` Output only. The observed tool response.  
  
### ScenarioRubricOutcome

JSON representation  
---  
      
    
    {
      "rubric": string,
      "scoreExplanation": string,
    
      // Union field _score can be only one of the following:
      "score": number
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`rubric` |  `string` Output only. The rubric that was used to evaluate the conversation.  
`scoreExplanation` |  `string` Output only. The rater's response to the rubric.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `number` Output only. The score of the conversation against the rubric.  
  
### TaskCompletionResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Task Completed Score 0: Task Not Completed Score -1: User Goal Undefined  
`explanation` |  `string` Output only. The explanation for the task completion score.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The task completion score. Can be -1, 0, 1  
  
### UserGoalSatisfactionResult

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
    
      // Union field _score can be only one of the following:
      "score": integer
      // End of list of possible types for union field _score.
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 2: Graceful Handoff Score 1: User Task Satisfied Score 0: User Task Not Satisfied Score -1: User Task Unspecified  
`explanation` |  `string` Output only. The explanation for the user task satisfaction score.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `integer` Output only. The user task satisfaction score. Can be -1, 0, 1, 2.  
  
### EvaluationPersona

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "displayName": string,
      "personality": string,
      "speechConfig": {
        object ([SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpeechConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The unique identifier of the persona. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}`  
`description` |  `string` Optional. The description of the persona.  
`displayName` |  `string` Required. The display name of the persona. Unique within an app.  
`personality` |  `string` Required. An instruction for the agent on how to behave in the evaluation.  
`speechConfig` |  `object (`[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SpeechConfig)`)` Optional. Configuration for how the persona sounds (TTS settings).  
  
### SpeechConfig

JSON representation  
---  
      
    
    {
      "speakingRate": number,
      "environment": enum ([BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.BackgroundEnvironment)),
      "voiceId": string
    }  
  
Fields  
---  
`speakingRate` |  `number` Optional. The speaking rate. 1.0 is normal. Lower is slower (e.g., 0.8), higher is faster (e.g., 1.5). Useful for testing how the agent handles fast talkers.  
`environment` |  `enum (`[BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.BackgroundEnvironment)`)` Optional. The simulated audio environment.  
`voiceId` |  `string` Optional. The specific voice identifier/accent to use. Example: "en-US-Wavenet-D" or "en-GB-Standard-A"  
  
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
  
### EvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "goldenEvaluationMetricsThresholds": {
        object ([GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenEvaluationMetricsThresholds))
      },
      "hallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)),
      "goldenHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)),
      "scenarioHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`goldenEvaluationMetricsThresholds` |  `object (`[GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenEvaluationMetricsThresholds)`)` Optional. The golden evaluation metrics thresholds.  
`hallucinationMetricBehavior  
**(deprecated)**` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` This item is deprecated!Optional. Deprecated: Use `golden_hallucination_metric_behavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`goldenHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for golden evaluations.  
`scenarioHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for scenario evaluations.  
  
### GoldenEvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "turnLevelMetricsThresholds": {
        object ([TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds))
      },
      "expectationLevelMetricsThresholds": {
        object ([ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds))
      },
      "toolMatchingSettings": {
        object ([ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMatchingSettings))
      }
    }  
  
Fields  
---  
`turnLevelMetricsThresholds` |  `object (`[TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.TurnLevelMetricsThresholds)`)` Optional. The turn level metrics thresholds.  
`expectationLevelMetricsThresholds` |  `object (`[ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationLevelMetricsThresholds)`)` Optional. The expectation level metrics thresholds.  
`toolMatchingSettings` |  `object (`[ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolMatchingSettings)`)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
### ToolMatchingSettings

JSON representation  
---  
      
    
    {
      "extraToolCallBehavior": enum ([ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExtraToolCallBehavior))
    }  
  
Fields  
---  
`extraToolCallBehavior` |  `enum (`[ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExtraToolCallBehavior)`)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
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
  
### EvaluationMetricsConfig

JSON representation  
---  
      
    
    {
      "goldenMetricsConfig": {
        object ([GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenMetricsConfig))
      },
      "scenarioMetricsConfig": {
        object ([ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioMetricsConfig))
      }
    }  
  
Fields  
---  
`goldenMetricsConfig` |  `object (`[GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.GoldenMetricsConfig)`)` Optional. Configuration for the golden metrics for the evaluation.  
`scenarioMetricsConfig` |  `object (`[ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ScenarioMetricsConfig)`)` Optional. Configuration for the scenario metrics for the evaluation.  
  
### GoldenMetricsConfig

JSON representation  
---  
      
    
    {
      "semanticSimilarityMetricsConfig": {
        object ([SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig))
      },
      "toolCorrectnessMetricsConfig": {
        object ([ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig))
      },
      "stepToolCorrectnessMetricsConfig": {
        object ([ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig))
      }
    }  
  
Fields  
---  
`semanticSimilarityMetricsConfig` |  `object (`[SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.SemanticSimilarityMetricsConfig)`)` Optional. Global configuration for semantic similarity metrics.  
`toolCorrectnessMetricsConfig` |  `object (`[ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig)`)` Optional. Configuration for turn level tool correctness metrics.  
`stepToolCorrectnessMetricsConfig` |  `object (`[ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ToolCorrectnessMetricsConfig)`)` Optional. Configuration for step level tool correctness metrics.  
  
### ToolCorrectnessMetricsConfig

JSON representation  
---  
      
    
    {
      "enableToolCorrectnessMetrics": boolean
    }  
  
Fields  
---  
`enableToolCorrectnessMetrics` |  `boolean` Optional. Whether to calculate tool correctness metrics for the evaluation.  
  
### ScenarioMetricsConfig

JSON representation  
---  
      
    
    {
      "userGoalMetMetricsConfig": {
        object ([UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalMetMetricsConfig))
      },
      "expectationsMetMetricsConfig": {
        object ([ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationsMetMetricsConfig))
      }
    }  
  
Fields  
---  
`userGoalMetMetricsConfig` |  `object (`[UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.UserGoalMetMetricsConfig)`)` Optional. Configuration for user goal met metrics.  
`expectationsMetMetricsConfig` |  `object (`[ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.ExpectationsMetMetricsConfig)`)` Optional. Configuration for expectation level metrics.  
  
### UserGoalMetMetricsConfig

JSON representation  
---  
      
    
    {
      "enableUserGoalMetMetrics": boolean
    }  
  
Fields  
---  
`enableUserGoalMetMetrics` |  `boolean` Optional. Whether to calculate the user goal met metrics for the evaluation.  
  
### ExpectationsMetMetricsConfig

JSON representation  
---  
      
    
    {
      "enableExpectationsMetMetrics": boolean
    }  
  
Fields  
---  
`enableExpectationsMetMetrics` |  `boolean` Optional. Whether to calculate the expectation level metrics for the evaluation.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### ComparisonType

Supported comparison types for checking the agent's response.

Enums  
---  
`COMPARISON_TYPE_UNSPECIFIED` | Unspecified comparison type. Behavior defaults to SEMANTIC_SIMILARITY for agent responses and tool calls.  
`EQUALS` | Exact string match.  
`CONTAINS` | Substring match (checks if the expected string is contained in the actual response).  
`SEMANTIC_SIMILARITY` | Semantic similarity match (evaluates meaning similarity using an LLM).  
  
### SemanticSimilarityChannel

Semantic similarity channel to use.

Enums  
---  
`SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED` | Metric unspecified. Defaults to TEXT.  
`TEXT` | Use text semantic similarity.  
`AUDIO` | Use audio semantic similarity.  
  
### HallucinationMetricBehavior

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

Enums  
---  
`HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED` | Unspecified hallucination metric behavior.  
`DISABLED` | Disable hallucination metric.  
`ENABLED` | Enable hallucination metric.  
  
### TaskCompletionBehavior

The expected behavior of the user task. This is used to determine whether the scenario is successful.

Enums  
---  
`TASK_COMPLETION_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to TASK_SATISFIED.  
`TASK_SATISFIED` | The user task should be completed successfully.  
`TASK_REJECTED` | The user task should be rejected.  
  
### UserGoalBehavior

The expected behavior of the user goal. This is used to determine whether the scenario is successful.

Enums  
---  
`USER_GOAL_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to USER_GOAL_SATISFIED.  
`USER_GOAL_SATISFIED` | The user goal should be completed successfully.  
`USER_GOAL_REJECTED` | The user goal should be rejected.  
`USER_GOAL_IGNORED` | Ignore the user goal status.  
  
### ScenarioExecutionMode

The execution mode for scenario evaluations.

Enums  
---  
`SCENARIO_EXECUTION_MODE_UNSPECIFIED` | Unspecified execution mode. Defaults to QUALITY_OPTIMIZED.  
`QUALITY_OPTIMIZED` | Quality optimized mode.  
`SPEED_OPTIMIZED` | Speed optimized mode.  
  
### Outcome

The outcome of the evaluation or expectation.

Enums  
---  
`OUTCOME_UNSPECIFIED` | Evaluation outcome is not specified.  
`PASS` | Evaluation/Expectation passed. In the case of an evaluation, this means that all expectations were met.  
`FAIL` | Evaluation/Expectation failed. In the case of an evaluation, this means that at least one expectation was not met.  
`SKIPPED` | Evaluation/Expectation was skipped.  
  
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
  
### Type

The type of span. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TOOL` | Tool call span.  
`USER_CALLBACK` | User callback span.  
`GUARDRAIL` | Guardrail span.  
`LLM` | LLM span.  
  
### BackgroundEnvironment

Simulated audio environment.

Enums  
---  
`BACKGROUND_ENVIRONMENT_UNSPECIFIED` | Background environment unspecified.  
`CALL_CENTER` | Call center environment.  
`TRAFFIC` | Traffic noise environment.  
`KIDS_NOISE` | Kids noise environment.  
`CAFE` | Cafe environment.  
  
### ExecutionState

The state of the evaluation result execution.

Enums  
---  
`EXECUTION_STATE_UNSPECIFIED` | Evaluation result execution state is not specified.  
`QUEUED` | Evaluation result execution is queued.  
`RUNNING` | Evaluation result execution is running.  
`COMPLETED` | Evaluation result execution has completed.  
`ERROR` | Evaluation result execution failed due to an internal error.  
`CANCELLED` | Evaluation result execution was cancelled.  
  
### ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
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
  
### GoldenRunMethod

The method used to run the evaluation.

Enums  
---  
`GOLDEN_RUN_METHOD_UNSPECIFIED` | Run method is not specified.  
`STABLE` | Run the evaluation as stable replay, where each turn is a unique session with the previous expected turns injected as context.  
`NAIVE` | Run the evaluation as naive replay, where the run is a single session with no context injected.  
  
### OutcomeMetadata

Metadata about the outcome of the evaluation.

Enums  
---  
`OUTCOME_METADATA_UNSPECIFIED` | Unspecified outcome metadata.  
`GRACEFUL_HANDOFF` | The evaluation resulted in a graceful handoff to a human representative.  
  
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

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
