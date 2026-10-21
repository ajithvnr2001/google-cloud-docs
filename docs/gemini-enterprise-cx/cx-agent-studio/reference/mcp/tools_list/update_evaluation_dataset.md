---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_evaluation_dataset/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:09:48.125352+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_evaluation_dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_evaluation_dataset`

Updates the specified evaluation dataset Make sure to always pass an update mask in the input.

The following code sample shows how to use `curl` to call the `update_evaluation_dataset` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_evaluation_dataset",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `EvaluationService.UpdateEvaluationDataset`.

### UpdateEvaluationDatasetRequest

JSON representation  
---  
      
    
    {
      "evaluationDataset": {
        object ([EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation_dataset#Input.Schema.EvaluationDataset))
      },
      "updateMask": string
    }  
  
Fields  
---  
`evaluationDataset` |  `object (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation_dataset#Input.Schema.EvaluationDataset)`)` Required. The evaluation dataset to update.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### EvaluationDataset

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "evaluations": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "createdBy": string,
      "lastUpdatedBy": string,
      "aggregatedMetrics": {
        object ([AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation dataset. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`displayName` |  `string` Required. User-defined display name of the evaluation dataset. Unique within an App.  
`evaluations[]` |  `string` Optional. Evaluations that are included in this dataset.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation dataset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation dataset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`createdBy` |  `string` Output only. The user who created the evaluation dataset.  
`lastUpdatedBy` |  `string` Output only. The user who last updated the evaluation dataset.  
`aggregatedMetrics` |  `object (`[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics)`)` Output only. The aggregated metrics for this evaluation dataset across all runs.  
  
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
  
## Output Schema

An evaluation dataset represents a set of evaluations that are grouped together basaed on shared tags.

### EvaluationDataset

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "evaluations": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "createdBy": string,
      "lastUpdatedBy": string,
      "aggregatedMetrics": {
        object ([AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation dataset. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`displayName` |  `string` Required. User-defined display name of the evaluation dataset. Unique within an App.  
`evaluations[]` |  `string` Optional. Evaluations that are included in this dataset.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation dataset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation dataset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`createdBy` |  `string` Output only. The user who created the evaluation dataset.  
`lastUpdatedBy` |  `string` Output only. The user who last updated the evaluation dataset.  
`aggregatedMetrics` |  `object (`[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation#Input.Schema.AggregatedMetrics)`)` Output only. The aggregated metrics for this evaluation dataset across all runs.  
  
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
