---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns
title: REST Resource: projects.locations.apps.scheduledEvaluationRuns \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:18:39.303760+00:00
---

# REST Resource: projects.locations.apps.scheduledEvaluationRuns  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.scheduledEvaluationRuns Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ScheduledEvaluationRun
    * JSON representation
  * RunEvaluationRequest
    * JSON representation
  * ScheduledEvaluationRun.SchedulingConfig
    * JSON representation
  * ScheduledEvaluationRun.SchedulingConfig.Frequency
  * Methods



## Resource: ScheduledEvaluationRun

Represents a scheduled evaluation run configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "request": {
        object ([RunEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#RunEvaluationRequest))
      },
      "description": string,
      "schedulingConfig": {
        object ([ScheduledEvaluationRun.SchedulingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#ScheduledEvaluationRun.SchedulingConfig))
      },
      "active": boolean,
      "lastCompletedRun": string,
      "totalExecutions": integer,
      "nextScheduledExecutionTime": string,
      "createTime": string,
      "createdBy": string,
      "updateTime": string,
      "lastUpdatedBy": string,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the scheduled evaluation run config. Format: projects/{projectId}/locations/{locationId}/apps/{appId}/scheduledEvaluationRuns/{scheduledEvaluationRunId}  
`displayName` |  `string` Required. User-defined display name of the scheduled evaluation run config.  
`request` |  `object (`[RunEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#RunEvaluationRequest)`)` Required. The RunEvaluationRequest to schedule  
`description` |  `string` Optional. User-defined description of the scheduled evaluation run.  
`schedulingConfig` |  `object (`[ScheduledEvaluationRun.SchedulingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#ScheduledEvaluationRun.SchedulingConfig)`)` Required. Configuration for the timing and frequency with which to execute the evaluations.  
`active` |  `boolean` Optional. Whether this config is active  
`lastCompletedRun` |  `string` Output only. The last successful EvaluationRun of this scheduled execution. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`totalExecutions` |  `integer` Output only. The total number of times this run has been executed  
`nextScheduledExecutionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The next time this is scheduled to executeUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the scheduled evaluation run was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createdBy` |  `string` Output only. The user who created the scheduled evaluation run.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdatedBy` |  `string` Output only. The user who last updated the evaluation.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
## RunEvaluationRequest

Request message for `[EvaluationService.RunEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runEvaluation#google.cloud.ces.v1beta.EvaluationService.RunEvaluation)`.

JSON representation  
---  
      
    
    {
      "app": string,
      "evaluations": [
        string
      ],
      "evaluationDataset": string,
      "displayName": string,
      "appVersion": string,
      "config": {
        object ([EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig))
      },
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
      "generateLatencyReport": boolean,
      "evaluationRunCachingSettings": {
        object ([EvaluationRunCachingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationRunCachingSettings))
      },
      "runCount": integer
    }  
  
Fields  
---  
`app` |  `string` Required. The app to evaluate. Format: `projects/{project}/locations/{location}/apps/{app}`  
`evaluations[]` |  `string` Optional. List of evaluations to run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`evaluationDataset` |  `string` Optional. An evaluation dataset to run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`displayName` |  `string` Optional. The display name of the evaluation run.  
`appVersion` |  `string` Optional. The app version to evaluate. At most one of `appVersion` or `deployment` can be set. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`config` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig)`)` Optional. The configuration to use for the run.  
`personaRunConfigs[]` |  `object (`[PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/PersonaRunConfig)`)` Optional. The configuration to use for the run per persona.  
`optimizationConfig` |  `object (`[OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig)`)` Optional. Configuration for running the optimization step after the evaluation run. If not set, the optimization step will not be run.  
`scheduledEvaluationRun` |  `string` Optional. The resource name of the `ScheduledEvaluationRun` that is triggering this evaluation run.If this field is set, the `scheduledEvaluationRun` field on the created `EvaluationRun` resource will be populated from this value. Format: `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduledEvaluationRun}`  
`goldenRunMethod` |  `enum (`[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoldenRunMethod)`)` Optional. The method to run the evaluation if it is a golden evaluation. If not set, default to STABLE.  
`generateLatencyReport` |  `boolean` Optional. Whether to generate a latency report for the evaluation run.  
`evaluationRunCachingSettings` |  `object (`[EvaluationRunCachingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationRunCachingSettings)`)` Optional. The caching settings to use for the evaluation run.  
`runCount` |  `integer` Optional. The number of times to run the evaluation. If not set, the default value is 1 per golden, and 5 per scenario.  
  
## ScheduledEvaluationRun.SchedulingConfig

Eval scheduling configuration details

JSON representation  
---  
      
    
    {
      "frequency": enum ([ScheduledEvaluationRun.SchedulingConfig.Frequency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#ScheduledEvaluationRun.SchedulingConfig.Frequency)),
      "startTime": string,
      "daysOfWeek": [
        integer
      ]
    }  
  
Fields  
---  
`frequency` |  `enum (`[ScheduledEvaluationRun.SchedulingConfig.Frequency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#ScheduledEvaluationRun.SchedulingConfig.Frequency)`)` Required. The frequency with which to run the eval  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Timestamp when the eval should start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`daysOfWeek[]` |  `integer` Optional. The days of the week to run the eval. Applicable only for Weekly and Biweekly frequencies. 1 is Monday, 2 is Tuesday, ..., 7 is Sunday.  
  
## ScheduledEvaluationRun.SchedulingConfig.Frequency

The frequencies evals can be run at

Enums  
---  
`FREQUENCY_UNSPECIFIED` | The frequency is unspecified.  
`NONE` | Indicates a one-time scheduled run that should not repeat  
`DAILY` | Run the evaluation daily.  
`WEEKLY` | Run the evaluation weekly.  
`BIWEEKLY` | Run the evaluation biweekly.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/create)`

|  Creates a scheduled evaluation run.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/delete)`

|  Deletes a scheduled evaluation run.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/get)`

|  Gets details of the specified scheduled evaluation run.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list)`

|  Lists all scheduled evaluation runs in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/patch)`

|  Updates a scheduled evaluation run.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
