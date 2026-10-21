---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results
title: REST Resource: projects.locations.apps.evaluations.results \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:33:42.601837+00:00
---

# REST Resource: projects.locations.apps.evaluations.results  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.evaluations.results Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationResult
    * JSON representation
    * EvaluationResult.GoldenResult
      * JSON representation
    * EvaluationResult.GoldenResult.TurnReplayResult
      * JSON representation
    * EvaluationResult.GoldenExpectationOutcome
      * JSON representation
    * EvaluationResult.Outcome
    * EvaluationResult.SemanticSimilarityResult
      * JSON representation
    * EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult
      * JSON representation
    * EvaluationResult.HallucinationResult
      * JSON representation
    * EvaluationResult.ToolCallLatency
      * JSON representation
    * EvaluationResult.OverallToolInvocationResult
      * JSON representation
    * EvaluationResult.SpanLatency
      * JSON representation
    * EvaluationResult.SpanLatency.Type
    * EvaluationResult.EvaluationExpectationResult
      * JSON representation
    * EvaluationResult.ScenarioResult
      * JSON representation
    * EvaluationResult.ScenarioExpectationOutcome
      * JSON representation
    * EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall
      * JSON representation
    * EvaluationResult.ScenarioRubricOutcome
      * JSON representation
    * EvaluationResult.TaskCompletionResult
      * JSON representation
    * EvaluationResult.UserGoalSatisfactionResult
      * JSON representation
    * EvaluationResult.ExecutionState
    * EvaluationResult.OutcomeMetadata
  * Methods



## Resource: EvaluationResult

An evaluation result represents the output of running an Evaluation.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "evaluationStatus": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
      "evaluationRun": string,
      "persona": {
        object ([EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status))
      },
      "initiatedBy": string,
      "appVersion": string,
      "appVersionDisplayName": string,
      "changelog": string,
      "changelogCreateTime": string,
      "executionState": enum ([EvaluationResult.ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ExecutionState)),
      "evaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds))
      },
      "config": {
        object ([EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig))
      },
      "goldenRunMethod": enum ([GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoldenRunMethod)),
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Span))
      },
      "outcomeMetadata": enum ([EvaluationResult.OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.OutcomeMetadata)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "goldenResult": {
        object ([EvaluationResult.GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenResult))
      },
      "scenarioResult": {
        object ([EvaluationResult.ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`  
`displayName` |  `string` Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: " result - ".  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation result was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`evaluationStatus` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the evaluation. Only populated if executionState is COMPLETE.  
`evaluationRun` |  `string` Output only. The evaluation run that produced this result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`persona` |  `object (`[EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona)`)` Output only. The persona used to generate the conversation for the evaluation result.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo)`)` Output only. Error information for the evaluation result.  
`error  
**(deprecated)**` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status)`)` This item is deprecated!Output only. Deprecated: Use `errorInfo` instead. Errors encountered during execution.  
`initiatedBy` |  `string` Output only. The user who initiated the evaluation run that resulted in this result.  
`appVersion` |  `string` Output only. The app version used to generate the conversation that resulted in this result. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`appVersionDisplayName` |  `string` Output only. The display name of the `appVersion` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelogCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionState` |  `enum (`[EvaluationResult.ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ExecutionState)`)` Output only. The state of the evaluation result execution.  
`evaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds)`)` Output only. The evaluation thresholds for the result.  
`config` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig)`)` Output only. The configuration used in the evaluation run that resulted in this result.  
`goldenRunMethod` |  `enum (`[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoldenRunMethod)`)` Output only. The method used to run the golden evaluation.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Span)`)` Output only. The root span of the evaluation execution, which includes information about each step of the evaluation.  
`outcomeMetadata` |  `enum (`[EvaluationResult.OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.OutcomeMetadata)`)` Output only. The outcome metadata of the evaluation. Only populated if executionState is COMPLETE.  
The result of the evaluation. Only populated when the execution_state is COMPLETED. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`goldenResult` |  `object (`[EvaluationResult.GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenResult)`)` Output only. The outcome of a golden evaluation.  
`scenarioResult` |  `object (`[EvaluationResult.ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioResult)`)` Output only. The outcome of a scenario evaluation.  
End of mutually exclusive fields.  
  
### EvaluationResult.GoldenResult

The result of a golden evaluation.

JSON representation  
---  
      
    
    {
      "turnReplayResults": [
        {
          object ([EvaluationResult.GoldenResult.TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenResult.TurnReplayResult))
        }
      ],
      "evaluationExpectationResults": [
        {
          object ([EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.EvaluationExpectationResult))
        }
      ]
    }  
  
Fields  
---  
`turnReplayResults[]` |  `object (`[EvaluationResult.GoldenResult.TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenResult.TurnReplayResult)`)` Output only. The result of running each turn of the golden conversation.  
`evaluationExpectationResults[]` |  `object (`[EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.EvaluationExpectationResult)`)` Output only. The results of the evaluation expectations.  
  
### EvaluationResult.GoldenResult.TurnReplayResult

The result of running a single turn of the golden conversation.

JSON representation  
---  
      
    
    {
      "conversation": string,
      "expectationOutcome": [
        {
          object ([EvaluationResult.GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenExpectationOutcome))
        }
      ],
      "hallucinationResult": {
        object ([EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.HallucinationResult))
      },
      "toolInvocationScore": number,
      "turnLatency": string,
      "toolCallLatencies": [
        {
          object ([EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ToolCallLatency))
        }
      ],
      "semanticSimilarityResult": {
        object ([EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SemanticSimilarityResult))
      },
      "overallToolInvocationResult": {
        object ([EvaluationResult.OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.OverallToolInvocationResult))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo))
      },
      "spanLatencies": [
        {
          object ([EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SpanLatency))
        }
      ],
      "toolOrderedInvocationScore": number
    }  
  
Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated for this turn.  
`expectationOutcome[]` |  `object (`[EvaluationResult.GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenExpectationOutcome)`)` Output only. The outcome of each expectation.  
`hallucinationResult` |  `object (`[EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.HallucinationResult)`)` Output only. The result of the hallucination check.  
`toolInvocationScore  
**(deprecated)**` |  `number` This item is deprecated!Output only. Deprecated. Use OverallToolInvocationResult instead.  
`turnLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Duration of the turn.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`toolCallLatencies[]` |  `object (`[EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ToolCallLatency)`)` Output only. The latency of each tool call in the turn.  
`semanticSimilarityResult` |  `object (`[EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SemanticSimilarityResult)`)` Output only. The result of the semantic similarity check.  
`overallToolInvocationResult` |  `object (`[EvaluationResult.OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.OverallToolInvocationResult)`)` Output only. The result of the overall tool invocation check.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo)`)` Output only. Information about the error that occurred during this turn.  
`spanLatencies[]` |  `object (`[EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SpanLatency)`)` Output only. The latency of spans in the turn.  
`toolOrderedInvocationScore` |  `number` Output only. The overall tool ordered invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked in the expected order.  
  
### EvaluationResult.GoldenExpectationOutcome

Specifies the expectation and the result of that expectation.

JSON representation  
---  
      
    
    {
      "expectation": {
        object ([Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation))
      },
      "outcome": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
      "semanticSimilarityResult": {
        object ([EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SemanticSimilarityResult))
      },
      "toolInvocationResult": {
        object ([EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "observedToolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall))
      },
      "observedToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
      },
      "observedAgentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message))
      },
      "observedAgentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentTransfer))
      },
      "observedPayload": {
        object
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`expectation` |  `object (`[Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation)`)` Output only. The expectation that was evaluated.  
`outcome` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the expectation.  
`semanticSimilarityResult  
**(deprecated)**` |  `object (`[EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SemanticSimilarityResult)`)` This item is deprecated!Output only. The result of the semantic similarity check.  
`toolInvocationResult` |  `object (`[EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult)`)` Output only. The result of the tool invocation check.  
The result of the expectation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`observedToolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall)`)` Output only. The result of the tool call expectation.  
`observedToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Output only. The result of the tool response expectation.  
`observedAgentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message)`)` Output only. The result of the agent response expectation.  
`observedAgentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentTransfer)`)` Output only. The result of the agent transfer expectation.  
`observedPayload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. An observed custom payload. There are no expectations for custom payloads. This is only used for metrics calculation. The outcome is always SKIPPED.  
End of mutually exclusive fields.  
  
### EvaluationResult.Outcome

The outcome of the evaluation or expectation.

Enums  
---  
`OUTCOME_UNSPECIFIED` | Evaluation outcome is not specified.  
`PASS` | Evaluation/Expectation passed. In the case of an evaluation, this means that all expectations were met.  
`FAIL` | Evaluation/Expectation failed. In the case of an evaluation, this means that at least one expectation was not met.  
`SKIPPED` | Evaluation/Expectation was skipped.  
  
### EvaluationResult.SemanticSimilarityResult

The result of the semantic similarity check.

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
      "outcome": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
      "score": integer
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 4: Fully Consistent Score 3: Mostly Consistent Score 2: Partially Consistent (Minor Omissions) Score 1: Largely Inconsistent (Major Omissions) Score 0: Completely Inconsistent / Contradictory  
`explanation` |  `string` Output only. The explanation for the semantic similarity score.  
`outcome` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the semantic similarity check. This is determined by comparing the score to the semanticSimilaritySuccessThreshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`score` |  `integer` Output only. The semantic similarity score. Can be 0, 1, 2, 3, or 4.  
  
### EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult

The result of the tool invocation check.

JSON representation  
---  
      
    
    {
      "outcome": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
      "explanation": string,
      "parameterCorrectnessScore": number
    }  
  
Fields  
---  
`outcome` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the tool invocation check. This is determined by comparing the parameterCorrectnessScore to the threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`explanation` |  `string` Output only. A free text explanation for the tool invocation result.  
`parameterCorrectnessScore` |  `number` Output only. The tool invocation parameter correctness score. This indicates the percent of parameters from the expected tool call that were also present in the actual tool call.  
  
### EvaluationResult.HallucinationResult

The result of the hallucination check for a single turn.

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
      "score": integer
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Justified Score 0: Not Justified Score -1: No Claim To Assess  
`explanation` |  `string` Output only. The explanation for the hallucination score.  
`score` |  `integer` Output only. The hallucination score. Can be -1, 0, 1.  
  
### EvaluationResult.ToolCallLatency

The latency of a tool call execution.

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
  
### EvaluationResult.OverallToolInvocationResult

The result of the overall tool invocation check.

JSON representation  
---  
      
    
    {
      "outcome": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
      "toolInvocationScore": number
    }  
  
Fields  
---  
`outcome` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the tool invocation check. This is determined by comparing the toolInvocationScore to the overallToolInvocationCorrectnessThreshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`toolInvocationScore` |  `number` The overall tool invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked.  
  
### EvaluationResult.SpanLatency

The latency of a span execution.

JSON representation  
---  
      
    
    {
      "type": enum ([EvaluationResult.SpanLatency.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SpanLatency.Type)),
      "displayName": string,
      "startTime": string,
      "endTime": string,
      "executionLatency": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "resource": string,
      "toolset": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool))
      },
      "model": string,
      "callback": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`type` |  `enum (`[EvaluationResult.SpanLatency.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SpanLatency.Type)`)` Output only. The type of span.  
`displayName` |  `string` Output only. The display name of the span. Applicable to tool and guardrail spans.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`executionLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The latency of span.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
The identifier of the specific item based on its type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`resource` |  `string` Output only. The resource name of the guardrail or tool spans.  
`toolset` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool)`)` Output only. The toolset tool identifier.  
`model` |  `string` Output only. The name of the LLM span.  
`callback` |  `string` Output only. The name of the user callback span.  
End of mutually exclusive fields.  
  
### EvaluationResult.SpanLatency.Type

The type of span. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TOOL` | Tool call span.  
`USER_CALLBACK` | User callback span.  
`GUARDRAIL` | Guardrail span.  
`LLM` | LLM span.  
  
### EvaluationResult.EvaluationExpectationResult

The result of a single evaluation expectation.

JSON representation  
---  
      
    
    {
      "evaluationExpectation": string,
      "prompt": string,
      "outcome": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
      "explanation": string
    }  
  
Fields  
---  
`evaluationExpectation` |  `string` Output only. The evaluation expectation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
`prompt` |  `string` Output only. The prompt that was used for the evaluation.  
`outcome` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the evaluation expectation.  
`explanation` |  `string` Output only. The explanation for the result.  
  
### EvaluationResult.ScenarioResult

The outcome of a scenario evaluation.

JSON representation  
---  
      
    
    {
      "conversation": string,
      "task": string,
      "userFacts": [
        {
          object ([Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.Scenario.UserFact))
        }
      ],
      "expectationOutcomes": [
        {
          object ([EvaluationResult.ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioExpectationOutcome))
        }
      ],
      "rubricOutcomes": [
        {
          object ([EvaluationResult.ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioRubricOutcome))
        }
      ],
      "hallucinationResult": [
        {
          object ([EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.HallucinationResult))
        }
      ],
      "taskCompletionResult": {
        object ([EvaluationResult.TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.TaskCompletionResult))
      },
      "toolCallLatencies": [
        {
          object ([EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ToolCallLatency))
        }
      ],
      "userGoalSatisfactionResult": {
        object ([EvaluationResult.UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.UserGoalSatisfactionResult))
      },
      "spanLatencies": [
        {
          object ([EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SpanLatency))
        }
      ],
      "evaluationExpectationResults": [
        {
          object ([EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.EvaluationExpectationResult))
        }
      ],
      "allExpectationsSatisfied": boolean,
      "taskCompleted": boolean
    }  
  
Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated in the scenario.  
`task` |  `string` Output only. The task that was used when running the scenario for this result.  
`userFacts[]` |  `object (`[Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.Scenario.UserFact)`)` Output only. The user facts that were used by the scenario for this result.  
`expectationOutcomes[]` |  `object (`[EvaluationResult.ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioExpectationOutcome)`)` Output only. The outcome of each expectation.  
`rubricOutcomes[]` |  `object (`[EvaluationResult.ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioRubricOutcome)`)` Output only. The outcome of the rubric.  
`hallucinationResult[]` |  `object (`[EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.HallucinationResult)`)` Output only. The result of the hallucination check. There will be one hallucination result for each turn in the conversation.  
`taskCompletionResult  
**(deprecated)**` |  `object (`[EvaluationResult.TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.TaskCompletionResult)`)` This item is deprecated!Output only. The result of the task completion check.  
`toolCallLatencies[]` |  `object (`[EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ToolCallLatency)`)` Output only. The latency of each tool call execution in the conversation.  
`userGoalSatisfactionResult` |  `object (`[EvaluationResult.UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.UserGoalSatisfactionResult)`)` Output only. The result of the user goal satisfaction check.  
`spanLatencies[]` |  `object (`[EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.SpanLatency)`)` Output only. The latency of spans in the conversation.  
`evaluationExpectationResults[]` |  `object (`[EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.EvaluationExpectationResult)`)` Output only. The results of the evaluation expectations.  
`allExpectationsSatisfied` |  `boolean` Output only. Whether all expectations were satisfied for this turn.  
`taskCompleted` |  `boolean` Output only. Whether the task was completed for this turn. This is a composite of all expectations satisfied, no hallucinations, and user goal satisfaction.  
  
### EvaluationResult.ScenarioExpectationOutcome

The outcome of a scenario expectation.

JSON representation  
---  
      
    
    {
      "expectation": {
        object ([Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation))
      },
      "outcome": enum ([EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "observedToolCall": {
        object ([EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall))
      },
      "observedAgentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`expectation` |  `object (`[Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation)`)` Output only. The expectation that was evaluated.  
`outcome` |  `enum (`[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.Outcome)`)` Output only. The outcome of the ScenarioExpectation.  
The result of the expectation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`observedToolCall` |  `object (`[EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult.EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall)`)` Output only. The observed tool call.  
`observedAgentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message)`)` Output only. The observed agent response.  
End of mutually exclusive fields.  
  
### EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall

The observed tool call and response.

JSON representation  
---  
      
    
    {
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
      }
    }  
  
Fields  
---  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall)`)` Output only. The observed tool call.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Output only. The observed tool response.  
  
### EvaluationResult.ScenarioRubricOutcome

The outcome of the evaluation against the rubric.

JSON representation  
---  
      
    
    {
      "rubric": string,
      "scoreExplanation": string,
      "score": number
    }  
  
Fields  
---  
`rubric` |  `string` Output only. The rubric that was used to evaluate the conversation.  
`scoreExplanation` |  `string` Output only. The rater's response to the rubric.  
`score` |  `number` Output only. The score of the conversation against the rubric.  
  
### EvaluationResult.TaskCompletionResult

The result of the task completion check for the conversation.

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
      "score": integer
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Task Completed Score 0: Task Not Completed Score -1: User Goal Undefined  
`explanation` |  `string` Output only. The explanation for the task completion score.  
`score` |  `integer` Output only. The task completion score. Can be -1, 0, 1  
  
### EvaluationResult.UserGoalSatisfactionResult

The result of a user goal satisfaction check for a conversation.

JSON representation  
---  
      
    
    {
      "label": string,
      "explanation": string,
      "score": integer
    }  
  
Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 2: Graceful Handoff Score 1: User Task Satisfied Score 0: User Task Not Satisfied Score -1: User Task Unspecified  
`explanation` |  `string` Output only. The explanation for the user task satisfaction score.  
`score` |  `integer` Output only. The user task satisfaction score. Can be -1, 0, 1, 2.  
  
### EvaluationResult.ExecutionState

The state of the evaluation result execution.

Enums  
---  
`EXECUTION_STATE_UNSPECIFIED` | Evaluation result execution state is not specified.  
`QUEUED` | Evaluation result execution is queued.  
`RUNNING` | Evaluation result execution is running.  
`COMPLETED` | Evaluation result execution has completed.  
`ERROR` | Evaluation result execution failed due to an internal error.  
`CANCELLED` | Evaluation result execution was cancelled.  
  
### EvaluationResult.OutcomeMetadata

Metadata about the outcome of the evaluation.

Enums  
---  
`OUTCOME_METADATA_UNSPECIFIED` | Unspecified outcome metadata.  
`GRACEFUL_HANDOFF` | The evaluation resulted in a graceful handoff to a human representative.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/delete)`

|  Deletes an evaluation result.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/export)`

|  Exports evaluations results.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/get)`

|  Gets details of the specified evaluation result.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list)`

|  Lists all evaluation results for a given evaluation.  
  
### `[runEvaluationResultMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/runEvaluationResultMetrics)`

|  Runs metrics on an existing evaluation result.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
