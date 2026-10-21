---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation
title: Evaluation.GoldenExpectation \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:59:35.389682+00:00
---

# Evaluation.GoldenExpectation  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Evaluation.GoldenExpectation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationMetricsConfig.HallucinationMetricsConfig
    * JSON representation
  * EvaluationMetricsConfig.ComparisonType



Represents a single, checkable requirement.

JSON representation  
---  
      
    
    {
      "note": string,
      "skipEvaluation": boolean,
      "expectationLevelMetricsThresholdsOverride": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds))
      },
      "agentResponseSemanticSimilarityMetricsConfigOverride": {
        object ([EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig.SemanticSimilarityMetricsConfig))
      },
      "agentResponseHallucinationMetricsConfigOverride": {
        object ([EvaluationMetricsConfig.HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation#EvaluationMetricsConfig.HallucinationMetricsConfig))
      },
      "comparisonType": enum ([EvaluationMetricsConfig.ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation#EvaluationMetricsConfig.ComparisonType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
      },
      "agentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "mockToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
      },
      "noToolCalls": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`note` |  `string` Optional. A note for this requirement, useful in reporting when specific checks fail. E.g., "Check_Payment_Tool_Called".  
`skipEvaluation` |  `boolean` Optional. If set to true, this specific expectation will not be evaluated.  
`expectationLevelMetricsThresholdsOverride` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)`)` Optional. Overrides metrics at the step level.  
`agentResponseSemanticSimilarityMetricsConfigOverride` |  `object (`[EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig.SemanticSimilarityMetricsConfig)`)` Optional. Overrides for agentResponse semantic similarity metrics.  
`agentResponseHallucinationMetricsConfigOverride` |  `object (`[EvaluationMetricsConfig.HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation#EvaluationMetricsConfig.HallucinationMetricsConfig)`)` Optional. Overrides for agentResponse hallucination metrics.  
`comparisonType` |  `enum (`[EvaluationMetricsConfig.ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation#EvaluationMetricsConfig.ComparisonType)`)` Optional. The comparison type to use for the expectation check.  
The actual check to perform. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall)`)` Optional. Check that a specific tool was called with the parameters.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Optional. Check that a specific tool had the expected response.  
`agentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message)`)` Optional. Check that the agent responded with the correct response. The role "agent" is implied.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentTransfer)`)` Optional. Check that the agent transferred the conversation to a different agent.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Check that the agent updated the session variables to the expected values. Used to also capture agent variable updates for golden evals.  
`mockToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Optional. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`noToolCalls` |  `boolean` Optional. Check that no tools were called during this turn.  
End of mutually exclusive fields.  
  
## EvaluationMetricsConfig.HallucinationMetricsConfig

Configuration for the hallucination metrics for the evaluation. To disable the metric, set the message but do not set the `enableHallucinationMetrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

JSON representation  
---  
      
    
    {
      "enableHallucinationMetrics": boolean
    }  
  
Fields  
---  
`enableHallucinationMetrics` |  `boolean` Optional. Whether to calculate hallucination metrics for the evaluation.  
  
## EvaluationMetricsConfig.ComparisonType

Supported comparison types for checking the agent's response.

Enums  
---  
`COMPARISON_TYPE_UNSPECIFIED` | Unspecified comparison type. Behavior defaults to SEMANTIC_SIMILARITY for agent responses and tool calls.  
`EQUALS` | Exact string match.  
`CONTAINS` | Substring match (checks if the expected string is contained in the actual response).  
`SEMANTIC_SIMILARITY` | Semantic similarity match (evaluates meaning similarity using an LLM).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
