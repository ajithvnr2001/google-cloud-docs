---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations
title: REST Resource: projects.locations.repositories.workflowInvocations \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:23.174616+00:00
---

# REST Resource: projects.locations.repositories.workflowInvocations  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.repositories.workflowInvocations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkflowInvocation
    * JSON representation
  * State
  * Methods



## Resource: WorkflowInvocation

Represents a single invocation of a compilation result.

JSON representation  
---  
      
    
    {
      "name": string,
      "invocationConfig": {
        object ([InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/InvocationConfig))
      },
      "state": enum ([State](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations#State)),
      "invocationTiming": {
        object ([Interval](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/Interval))
      },
      "resolvedCompilationResult": string,
      "dataEncryptionState": {
        object ([DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DataEncryptionState))
      },
      "privateResourceMetadata": {
        object ([PrivateResourceMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PrivateResourceMetadata))
      },
      "pipelineConfig": {
        object ([PipelineConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig))
      },
    
      // Union field compilation_source can be only one of the following:
      "compilationResult": string,
      "workflowConfig": string
      // End of list of possible types for union field compilation_source.
      "internalMetadata": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The workflow invocation's name.  
`invocationConfig` |  `object (`[InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/InvocationConfig)`)` Immutable. If left unset, a default InvocationConfig will be used.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations#State)`)` Output only. This workflow invocation's current state.  
`invocationTiming` |  `object (`[Interval](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/Interval)`)` Output only. This workflow invocation's timing details.  
`resolvedCompilationResult` |  `string` Output only. The resolved compilation result that was used to create this invocation. Will be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.  
`dataEncryptionState` |  `object (`[DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DataEncryptionState)`)` Output only. Only set if the repository has a KMS Key.  
`privateResourceMetadata` |  `object (`[PrivateResourceMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PrivateResourceMetadata)`)` Output only. Metadata indicating whether this resource is user-scoped. `WorkflowInvocation` resource is `userScoped` only if it is sourced from a compilation result and the compilation result is user-scoped.  
`pipelineConfig` |  `object (`[PipelineConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig)`)` Output only. The pipeline options which define the pipeline type and path within the Git repository.  
Union field `compilation_source`. The source of the compilation result to use for this invocation. `compilation_source` can be only one of the following:  
`compilationResult` |  `string` Immutable. The name of the compilation result to use for this invocation. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.  
`workflowConfig` |  `string` Immutable. The name of the workflow config to invoke. Must be in the format `projects/*/locations/*/repositories/*/workflowConfigs/*`.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## State

Represents the current state of a workflow invocation.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`RUNNING` | The workflow invocation is currently running.  
`SUCCEEDED` | The workflow invocation succeeded. A terminal state.  
`CANCELLED` | The workflow invocation was cancelled. A terminal state.  
`FAILED` | The workflow invocation failed. A terminal state.  
`CANCELING` | The workflow invocation is being cancelled, but some actions are still running.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/cancel)`

|  Requests cancellation of a running WorkflowInvocation.  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/create)`

|  Creates a new WorkflowInvocation in a given Repository.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/delete)`

|  Deletes a single WorkflowInvocation.  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/get)`

|  Fetches a single WorkflowInvocation.  
  
### `[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/list)`

|  Lists WorkflowInvocations in a given Repository.  
  
### `[query](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/query)`

|  Returns WorkflowInvocationActions in a given WorkflowInvocation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
