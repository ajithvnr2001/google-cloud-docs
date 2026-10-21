---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations
title: REST Resource: projects.locations.apps.evaluations \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:49:37.614931+00:00
---

# REST Resource: projects.locations.apps.evaluations  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.evaluations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Evaluation
    * JSON representation
  * Evaluation.Golden
    * JSON representation
  * Evaluation.GoldenTurn
    * JSON representation
  * Evaluation.Step
    * JSON representation
  * SessionInput
    * JSON representation
  * ToolResponses
    * JSON representation
  * Event
    * JSON representation
  * Evaluation.Scenario
    * JSON representation
  * Evaluation.Scenario.TaskCompletionBehavior
  * Evaluation.Scenario.UserGoalBehavior
  * Methods



## Resource: Evaluation

An evaluation represents all of the information needed to simulate and evaluate an agent.

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
        object ([AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics))
      },
      "lastCompletedResult": {
        object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult))
      },
      "invalid": boolean,
      "lastTenResults": [
        {
          object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult))
        }
      ],
      "evaluationMetricsThresholdOverride": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds))
      },
      "evaluationMetricsConfigOverride": {
        object ([EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "golden": {
        object ([Evaluation.Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Golden))
      },
      "scenario": {
        object ([Evaluation.Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Scenario))
      }
      // End of mutually exclusive fields.
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
`aggregatedMetrics` |  `object (`[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics)`)` Output only. The aggregated metrics for this evaluation across all runs.  
`lastCompletedResult` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult)`)` Output only. The latest evaluation result for this evaluation.  
`invalid` |  `boolean` Output only. Whether the evaluation is invalid. This can happen if an evaluation is referencing a tool, toolset, or agent that has since been deleted.  
`lastTenResults[]` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult)`)` Output only. The last 10 evaluation results for this evaluation. This is only populated if include_last_ten_results is set to true in the ListEvaluationsRequest or GetEvaluationRequest.  
`evaluationMetricsThresholdOverride` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds)`)` Optional. Overrides metrics thresholds for this specific evaluation.  
`evaluationMetricsConfigOverride` |  `object (`[EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig)`)` Optional. Overrides metrics config for this specific evaluation.  
The inputs for the evaluation The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`golden` |  `object (`[Evaluation.Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Golden)`)` Optional. The golden steps to be evaluated.  
`scenario` |  `object (`[Evaluation.Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Scenario)`)` Optional. The config for a scenario.  
End of mutually exclusive fields.  
  
## Evaluation.Golden

The steps required to replay a golden conversation.

JSON representation  
---  
      
    
    {
      "turns": [
        {
          object ([Evaluation.GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.GoldenTurn))
        }
      ],
      "evaluationExpectations": [
        string
      ]
    }  
  
Fields  
---  
`turns[]` |  `object (`[Evaluation.GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.GoldenTurn)`)` Required. The golden turns required to replay a golden conversation. The maximum number of allowed turns is 100.  
`evaluationExpectations[]` |  `string` Optional. The evaluation expectations to evaluate the replayed conversation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
  
## Evaluation.GoldenTurn

A golden turn defines a single turn in a golden conversation.

JSON representation  
---  
      
    
    {
      "steps": [
        {
          object ([Evaluation.Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Step))
        }
      ],
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Span))
      },
      "turnLevelMetricsThresholdsOverride": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds))
      },
      "hallucinationMetricBehaviorOverride": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`steps[]` |  `object (`[Evaluation.Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Step)`)` Required. The steps required to replay a golden conversation.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Span)`)` Optional. The root span of the golden turn for processing and maintaining audio information. The uri for the audio must contain audio saved in 16Khz sample rate.  
`turnLevelMetricsThresholdsOverride` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)`)` Optional. Overrides for turn-level metric thresholds.  
`hallucinationMetricBehaviorOverride` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` Optional. Override for turn-level hallucination metric behavior.  
  
## Evaluation.Step

A step defines a singular action to happen during the evaluation.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userInput": {
        object ([SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#SessionInput))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentTransfer))
      },
      "expectation": {
        object ([Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The step to perform. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userInput` |  `object (`[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#SessionInput)`)` Optional. User input for the conversation.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentTransfer)`)` Optional. Transfer the conversation to a different agent.  
`expectation` |  `object (`[Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.GoldenExpectation)`)` Optional. Executes an expectation on the current turn.  
End of mutually exclusive fields.  
  
## SessionInput

Input for the session.

JSON representation  
---  
      
    
    {
      "willContinue": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "dtmf": string,
      "audio": string,
      "toolResponses": {
        object ([ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#ToolResponses))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Image))
      },
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Blob))
      },
      "variables": {
        object
      },
      "event": {
        object ([Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Event))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`willContinue` |  `boolean` Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session.When set to `true`, the agent defers processing until it receives a subsequent message where `willContinue` is `false`, or until the system detects an endpoint in the audio input.NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.  
The type of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Optional. Text data from the end user.  
`dtmf` |  `string` Optional. DTMF digits from the end user.  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Audio data from the end user.A base64-encoded string.  
`toolResponses` |  `object (`[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#ToolResponses)`)` Optional. Execution results for the tool calls from the client.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Image)`)` Optional. Image data from the end user.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Blob)`)` Optional. Blob data from the end user.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters.  
`event` |  `object (`[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Event)`)` Optional. Event input.  
End of mutually exclusive fields.  
  
## ToolResponses

Execution results for the requested tool calls from the client.

JSON representation  
---  
      
    
    {
      "toolResponses": [
        {
          object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
        }
      ]
    }  
  
Fields  
---  
`toolResponses[]` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Optional. The list of tool execution results.  
  
## Event

Event input.

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
  
## Evaluation.Scenario

The config for a scenario

JSON representation  
---  
      
    
    {
      "task": string,
      "userFacts": [
        {
          object ([Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.Scenario.UserFact))
        }
      ],
      "maxTurns": integer,
      "rubrics": [
        string
      ],
      "scenarioExpectations": [
        {
          object ([Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation))
        }
      ],
      "variableOverrides": {
        object
      },
      "taskCompletionBehavior": enum ([Evaluation.Scenario.TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Scenario.TaskCompletionBehavior)),
      "userGoalBehavior": enum ([Evaluation.Scenario.UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Scenario.UserGoalBehavior)),
      "evaluationExpectations": [
        string
      ],
      "scenarioExecutionMode": enum ([EvaluationSettings.ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationSettings.ScenarioExecutionMode))
    }  
  
Fields  
---  
`task` |  `string` Required. The task to be targeted by the scenario.  
`userFacts[]` |  `object (`[Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.Scenario.UserFact)`)` Optional. The user facts to be used by the scenario.  
`maxTurns` |  `integer` Optional. The maximum number of turns to simulate. The maximum allowed value is 100. The default value is 100.  
`rubrics[]` |  `string` Required. The rubrics to score the scenario against.  
`scenarioExpectations[]` |  `object (`[Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation)`)` Required. The ScenarioExpectations to evaluate the conversation produced by the user simulation.  
`variableOverrides` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Variables / Session Parameters as context for the session, keyed by variable names. Members of this struct will override any default values set by the system.Note, these are different from user facts, which are facts known to the user. Variables are parameters known to the agent: i.e. MDN (phone number) passed by the telephony system.  
`taskCompletionBehavior  
**(deprecated)**` |  `enum (`[Evaluation.Scenario.TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Scenario.TaskCompletionBehavior)`)` This item is deprecated!Optional. Deprecated. Use userGoalBehavior instead.  
`userGoalBehavior` |  `enum (`[Evaluation.Scenario.UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations#Evaluation.Scenario.UserGoalBehavior)`)` Optional. The expected behavior of the user goal.  
`evaluationExpectations[]` |  `string` Optional. The evaluation expectations to evaluate the conversation produced by the simulation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
`scenarioExecutionMode` |  `enum (`[EvaluationSettings.ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationSettings.ScenarioExecutionMode)`)` Optional. The execution mode for scenario evaluations.  
  
## Evaluation.Scenario.TaskCompletionBehavior

The expected behavior of the user task. This is used to determine whether the scenario is successful.

Enums  
---  
`TASK_COMPLETION_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to TASK_SATISFIED.  
`TASK_SATISFIED` | The user task should be completed successfully.  
`TASK_REJECTED` | The user task should be rejected.  
  
## Evaluation.Scenario.UserGoalBehavior

The expected behavior of the user goal. This is used to determine whether the scenario is successful.

Enums  
---  
`USER_GOAL_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to USER_GOAL_SATISFIED.  
`USER_GOAL_SATISFIED` | The user goal should be completed successfully.  
`USER_GOAL_REJECTED` | The user goal should be rejected.  
`USER_GOAL_IGNORED` | Ignore the user goal status.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/create)`

|  Creates an evaluation.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/delete)`

|  Deletes an evaluation.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/export)`

|  Exports evaluations.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/get)`

|  Gets details of the specified evaluation.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/list)`

|  Lists all evaluations in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/patch)`

|  Updates an evaluation.  
  
### `[uploadEvaluationAudio](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations/uploadEvaluationAudio)`

|  Uploads audio for use in Golden Evaluations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
