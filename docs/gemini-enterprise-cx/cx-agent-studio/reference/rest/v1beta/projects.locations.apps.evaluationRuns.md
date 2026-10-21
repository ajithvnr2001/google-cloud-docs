---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns
title: REST Resource: projects.locations.apps.evaluationRuns \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:08:16.798009+00:00
---

# REST Resource: projects.locations.apps.evaluationRuns  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.evaluationRuns Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationRun
    * JSON representation
  * EvaluationRun.EvaluationType
  * EvaluationRun.EvaluationRunState
  * EvaluationRun.Progress
    * JSON representation
  * EvaluationRun.EvaluationRunSummary
    * JSON representation
  * LatencyReport
    * JSON representation
  * LatencyReport.ToolLatency
    * JSON representation
  * LatencyReport.LatencyMetrics
    * JSON representation
  * LatencyReport.CallbackLatency
    * JSON representation
  * LatencyReport.GuardrailLatency
    * JSON representation
  * LatencyReport.LlmCallLatency
    * JSON representation
  * Methods



## Resource: EvaluationRun

An evaluation run represents an all the evaluation results from an evaluation execution.

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
      "evaluationType": enum ([EvaluationRun.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.EvaluationType)),
      "state": enum ([EvaluationRun.EvaluationRunState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.EvaluationRunState)),
      "progress": {
        object ([EvaluationRun.Progress](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.Progress))
      },
      "config": {
        object ([EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status))
      },
      "errorInfo": {
        object ([EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo))
      },
      "evaluationRunSummaries": {
        string: {
          object ([EvaluationRun.EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.EvaluationRunSummary))
        },
        ...
      },
      "latencyReport": {
        object ([LatencyReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport))
      },
      "runCount": integer,
      "personaRunConfigs": [
        {
          object ([PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/PersonaRunConfig))
        }
      ],
      "optimizationConfig": {
        object ([OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig))
      },
      "scheduledEvaluationRun": string,
      "goldenRunMethod": enum ([GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoldenRunMethod)),
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
`appVersionDisplayName` |  `string` Output only. The display name of the `appVersion` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelogCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`evaluations[]` |  `string` Output only. The evaluations that are part of this run. The list may contain evaluations of either type. This field is mutually exclusive with `evaluationDataset`. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`evaluationDataset` |  `string` Output only. The evaluation dataset that this run is associated with. This field is mutually exclusive with `evaluations`. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`evaluationType` |  `enum (`[EvaluationRun.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.EvaluationType)`)` Output only. The type of the evaluations in this run.  
`state` |  `enum (`[EvaluationRun.EvaluationRunState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.EvaluationRunState)`)` Output only. The state of the evaluation run.  
`progress` |  `object (`[EvaluationRun.Progress](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.Progress)`)` Output only. The progress of the evaluation run.  
`config` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig)`)` Output only. The configuration used in the run.  
`error  
**(deprecated)**` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Status)`)` This item is deprecated!Output only. Deprecated: Use errorInfo instead. Errors encountered during execution.  
`errorInfo` |  `object (`[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo)`)` Output only. Error information for the evaluation run.  
`evaluationRunSummaries` |  `map (key: string, value: object (`[EvaluationRun.EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#EvaluationRun.EvaluationRunSummary)`))` Output only. Map of evaluation name to EvaluationRunSummary.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`latencyReport` |  `object (`[LatencyReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport)`)` Output only. Latency report for the evaluation run.  
`runCount` |  `integer` Output only. The number of times the evaluations inside the run were run.  
`personaRunConfigs[]` |  `object (`[PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/PersonaRunConfig)`)` Output only. The configuration to use for the run per persona.  
`optimizationConfig` |  `object (`[OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig)`)` Optional. Configuration for running the optimization step after the evaluation run. If not set, the optimization step will not be run.  
`scheduledEvaluationRun` |  `string` Output only. The scheduled evaluation run resource name that created this evaluation run. This field is only set if the evaluation run was created by a scheduled evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduledEvaluationRun}`  
`goldenRunMethod` |  `enum (`[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoldenRunMethod)`)` Output only. The method used to run the evaluation.  
`operation` |  `string` Output only. The operation that created this evaluation run. Format: `projects/{project}/locations/{location}/operations/{operation}`  
  
## EvaluationRun.EvaluationType

The type of the evaluations in this run. Additional values may be added in the future.

Enums  
---  
`EVALUATION_TYPE_UNSPECIFIED` | Evaluation type is not specified.  
`GOLDEN` | Golden evaluation.  
`SCENARIO` | Scenario evaluation.  
`MIXED` | Indicates the run includes a mix of golden and scenario evaluations.  
  
## EvaluationRun.EvaluationRunState

The state of the evaluation run.

Enums  
---  
`EVALUATION_RUN_STATE_UNSPECIFIED` | Evaluation run state is not specified.  
`QUEUED` | Indicates the evaluation run is queued.  
`RUNNING` | Evaluation run is running.  
`COMPLETED` | Evaluation run has completed.  
`ERROR` | The evaluation run has an error.  
`CANCELLED` | Evaluation run was cancelled.  
  
## EvaluationRun.Progress

The progress of the evaluation run.

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
  
## EvaluationRun.EvaluationRunSummary

Contains the summary of passed and failed result counts for a specific evaluation in an evaluation run.

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
  
## LatencyReport

Latency report for the evaluation run.

JSON representation  
---  
      
    
    {
      "toolLatencies": [
        {
          object ([LatencyReport.ToolLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.ToolLatency))
        }
      ],
      "callbackLatencies": [
        {
          object ([LatencyReport.CallbackLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.CallbackLatency))
        }
      ],
      "guardrailLatencies": [
        {
          object ([LatencyReport.GuardrailLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.GuardrailLatency))
        }
      ],
      "llmCallLatencies": [
        {
          object ([LatencyReport.LlmCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LlmCallLatency))
        }
      ],
      "sessionCount": integer
    }  
  
Fields  
---  
`toolLatencies[]` |  `object (`[LatencyReport.ToolLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.ToolLatency)`)` Output only. Unordered list. Latency metrics for each tool.  
`callbackLatencies[]` |  `object (`[LatencyReport.CallbackLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.CallbackLatency)`)` Output only. Unordered list. Latency metrics for each callback.  
`guardrailLatencies[]` |  `object (`[LatencyReport.GuardrailLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.GuardrailLatency)`)` Output only. Unordered list. Latency metrics for each guardrail.  
`llmCallLatencies[]` |  `object (`[LatencyReport.LlmCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LlmCallLatency)`)` Output only. Unordered list. Latency metrics for each LLM call.  
`sessionCount` |  `integer` Output only. The total number of sessions considered in the latency report.  
  
## LatencyReport.ToolLatency

Latency metrics for a single tool.

JSON representation  
---  
      
    
    {
      "toolDisplayName": string,
      "latencyMetrics": {
        object ([LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`toolDisplayName` |  `string` Output only. The display name of the tool.  
`latencyMetrics` |  `object (`[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics)`)` Output only. The latency metrics for the tool.  
The identifier of the tool. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Output only. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`.  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool)`)` Output only. The toolset tool identifier.  
End of mutually exclusive fields.  
  
## LatencyReport.LatencyMetrics

Latency metrics for a component.

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
  
## LatencyReport.CallbackLatency

Latency metrics for a single callback.

JSON representation  
---  
      
    
    {
      "stage": string,
      "latencyMetrics": {
        object ([LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics))
      }
    }  
  
Fields  
---  
`stage` |  `string` Output only. The stage of the callback.  
`latencyMetrics` |  `object (`[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics)`)` Output only. The latency metrics for the callback.  
  
## LatencyReport.GuardrailLatency

Latency metrics for a single guardrail.

JSON representation  
---  
      
    
    {
      "guardrail": string,
      "guardrailDisplayName": string,
      "latencyMetrics": {
        object ([LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics))
      }
    }  
  
Fields  
---  
`guardrail` |  `string` Output only. The name of the guardrail. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`.  
`guardrailDisplayName` |  `string` Output only. The display name of the guardrail.  
`latencyMetrics` |  `object (`[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics)`)` Output only. The latency metrics for the guardrail.  
  
## LatencyReport.LlmCallLatency

Latency metrics for a single LLM call.

JSON representation  
---  
      
    
    {
      "model": string,
      "latencyMetrics": {
        object ([LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics))
      }
    }  
  
Fields  
---  
`model` |  `string` Output only. The name of the model.  
`latencyMetrics` |  `object (`[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns#LatencyReport.LatencyMetrics)`)` Output only. The latency metrics for the LLM call.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns/delete)`

|  Deletes an evaluation run.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns/export)`

|  Exports evaluations runs.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns/get)`

|  Gets details of the specified evaluation run.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationRuns/list)`

|  Lists all evaluation runs in the given app.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
