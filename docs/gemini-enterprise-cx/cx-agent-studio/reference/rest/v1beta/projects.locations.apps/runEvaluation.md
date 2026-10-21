---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runEvaluation/
title: Method: projects.locations.apps.runEvaluation \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:43.764952+00:00
---

# Method: projects.locations.apps.runEvaluation  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/runEvaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.runEvaluation Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Runs an evaluation of the app.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{app=projects/*/locations/*/apps/*}:runEvaluation`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`app` |  `string` Required. The app to evaluate. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
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
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `app` resource:

  * `ces.apps.runEvaluation`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
