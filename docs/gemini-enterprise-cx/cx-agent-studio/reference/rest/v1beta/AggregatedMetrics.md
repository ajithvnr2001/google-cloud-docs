---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics/
title: AggregatedMetrics \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:00:06.846449+00:00
---

# AggregatedMetrics  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  AggregatedMetrics Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AggregatedMetrics.MetricsByAppVersion
    * JSON representation
  * AggregatedMetrics.ToolMetrics
    * JSON representation
  * AggregatedMetrics.SemanticSimilarityMetrics
    * JSON representation
  * AggregatedMetrics.HallucinationMetrics
    * JSON representation
  * AggregatedMetrics.ToolCallLatencyMetrics
    * JSON representation
  * AggregatedMetrics.TurnLatencyMetrics
    * JSON representation
  * AggregatedMetrics.MetricsByTurn
    * JSON representation



Aggregated metrics for an evaluation or evaluation dataset.

JSON representation  
---  
      
    
    {
      "metricsByAppVersion": [
        {
          object ([AggregatedMetrics.MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.MetricsByAppVersion))
        }
      ]
    }  
  
Fields  
---  
`metricsByAppVersion[]` |  `object (`[AggregatedMetrics.MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.MetricsByAppVersion)`)` Output only. Aggregated metrics, grouped by app version ID.  
  
## AggregatedMetrics.MetricsByAppVersion

Metrics aggregated per app version.

JSON representation  
---  
      
    
    {
      "appVersionId": string,
      "toolMetrics": [
        {
          object ([AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolMetrics))
        }
      ],
      "semanticSimilarityMetrics": [
        {
          object ([AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.SemanticSimilarityMetrics))
        }
      ],
      "hallucinationMetrics": [
        {
          object ([AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.HallucinationMetrics))
        }
      ],
      "toolCallLatencyMetrics": [
        {
          object ([AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolCallLatencyMetrics))
        }
      ],
      "turnLatencyMetrics": [
        {
          object ([AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.TurnLatencyMetrics))
        }
      ],
      "passCount": integer,
      "failCount": integer,
      "metricsByTurn": [
        {
          object ([AggregatedMetrics.MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.MetricsByTurn))
        }
      ]
    }  
  
Fields  
---  
`appVersionId` |  `string` Output only. The app version ID.  
`toolMetrics[]` |  `object (`[AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolMetrics)`)` Output only. Metrics for each tool within this app version.  
`semanticSimilarityMetrics[]` |  `object (`[AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.SemanticSimilarityMetrics)`)` Output only. Metrics for semantic similarity within this app version.  
`hallucinationMetrics[]` |  `object (`[AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.HallucinationMetrics)`)` Output only. Metrics for hallucination within this app version.  
`toolCallLatencyMetrics[]` |  `object (`[AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolCallLatencyMetrics)`)` Output only. Metrics for tool call latency within this app version.  
`turnLatencyMetrics[]` |  `object (`[AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.TurnLatencyMetrics)`)` Output only. Metrics for turn latency within this app version.  
`passCount` |  `integer` Output only. The number of times the evaluation passed.  
`failCount` |  `integer` Output only. The number of times the evaluation failed.  
`metricsByTurn[]` |  `object (`[AggregatedMetrics.MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.MetricsByTurn)`)` Output only. Metrics aggregated per turn within this app version.  
  
## AggregatedMetrics.ToolMetrics

Metrics for a single tool.

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
  
## AggregatedMetrics.SemanticSimilarityMetrics

Metrics for semantic similarity results.

JSON representation  
---  
      
    
    {
      "score": number
    }  
  
Fields  
---  
`score` |  `number` Output only. The average semantic similarity score (0-4).  
  
## AggregatedMetrics.HallucinationMetrics

Metrics for hallucination results.

JSON representation  
---  
      
    
    {
      "score": number
    }  
  
Fields  
---  
`score` |  `number` Output only. The average hallucination score (0 to 1).  
  
## AggregatedMetrics.ToolCallLatencyMetrics

Metrics for tool call latency.

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
  
## AggregatedMetrics.TurnLatencyMetrics

Metrics for turn latency.

JSON representation  
---  
      
    
    {
      "averageLatency": string
    }  
  
Fields  
---  
`averageLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The average latency of the turns.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## AggregatedMetrics.MetricsByTurn

Metrics aggregated per turn.

JSON representation  
---  
      
    
    {
      "turnIndex": integer,
      "toolMetrics": [
        {
          object ([AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolMetrics))
        }
      ],
      "semanticSimilarityMetrics": [
        {
          object ([AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.SemanticSimilarityMetrics))
        }
      ],
      "hallucinationMetrics": [
        {
          object ([AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.HallucinationMetrics))
        }
      ],
      "toolCallLatencyMetrics": [
        {
          object ([AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolCallLatencyMetrics))
        }
      ],
      "turnLatencyMetrics": [
        {
          object ([AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.TurnLatencyMetrics))
        }
      ]
    }  
  
Fields  
---  
`turnIndex` |  `integer` Output only. The turn index (0-based).  
`toolMetrics[]` |  `object (`[AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolMetrics)`)` Output only. Metrics for each tool within this turn.  
`semanticSimilarityMetrics[]` |  `object (`[AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.SemanticSimilarityMetrics)`)` Output only. Metrics for semantic similarity within this turn.  
`hallucinationMetrics[]` |  `object (`[AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.HallucinationMetrics)`)` Output only. Metrics for hallucination within this turn.  
`toolCallLatencyMetrics[]` |  `object (`[AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.ToolCallLatencyMetrics)`)` Output only. Metrics for tool call latency within this turn.  
`turnLatencyMetrics[]` |  `object (`[AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics#AggregatedMetrics.TurnLatencyMetrics)`)` Output only. Metrics for turn latency within this turn.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
