---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query/
title: Method: projects.locations.repositories.workflowInvocations.query \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:08.664111+00:00
---

# Method: projects.locations.repositories.workflowInvocations.query  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Method: projects.locations.repositories.workflowInvocations.query Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * WorkflowInvocationAction
    * JSON representation
  * BigQueryAction
    * JSON representation
  * NotebookAction
    * JSON representation
  * DataPreparationAction
    * JSON representation
  * ActionSqlDefinition
    * JSON representation
  * ActionErrorTable
    * JSON representation
  * ActionLoadConfig
    * JSON representation
  * ActionSimpleLoadMode
  * ActionIncrementalLoadMode
    * JSON representation
  * State
  * Try it!



Returns WorkflowInvocationActions in a given WorkflowInvocation.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://dataform.googleapis.com/v1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}:query`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The workflow invocation's name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dataform.workflowInvocations.query`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of workflow invocations to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.  
`pageToken` |  `string` Optional. Page token received from a previous `workflowInvocations.query` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `workflowInvocations.query`, with the exception of `pageSize`, must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

`workflowInvocations.query` response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workflowInvocationActions": [
        {
          object ([WorkflowInvocationAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#WorkflowInvocationAction))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workflowInvocationActions[]` |  `object (`[WorkflowInvocationAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#WorkflowInvocationAction)`)` List of workflow invocation actions.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/bigquery`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `dataform.workflowInvocations.query`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## WorkflowInvocationAction

Represents a single action in a workflow invocation.

JSON representation  
---  
      
    
    {
      "target": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target))
      },
      "canonicalTarget": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target))
      },
      "state": enum ([State](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#State)),
      "failureReason": string,
      "invocationTiming": {
        object ([Interval](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/Interval))
      },
    
      // Union field action can be only one of the following:
      "bigqueryAction": {
        object ([BigQueryAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#BigQueryAction))
      },
      "notebookAction": {
        object ([NotebookAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#NotebookAction))
      },
      "dataPreparationAction": {
        object ([DataPreparationAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#DataPreparationAction))
      }
      // End of list of possible types for union field action.
      "internalMetadata": string
    }  
  
Fields  
---  
`target` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target)`)` Output only. This action's identifier. Unique within the workflow invocation.  
`canonicalTarget` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target)`)` Output only. The action's identifier if the project had been compiled without any overrides configured. Unique within the compilation result.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#State)`)` Output only. This action's current state.  
`failureReason` |  `string` Output only. If and only if action's state is FAILED a failure reason is set.  
`invocationTiming` |  `object (`[Interval](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/Interval)`)` Output only. This action's timing details. `startTime` will be set if the action is in [RUNNING, SUCCEEDED, CANCELLED, FAILED] state. `endTime` will be set if the action is in [SUCCEEDED, CANCELLED, FAILED] state.  
Union field `action`. The action's details. `action` can be only one of the following:  
`bigqueryAction` |  `object (`[BigQueryAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#BigQueryAction)`)` Output only. The workflow action's bigquery action details.  
`notebookAction` |  `object (`[NotebookAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#NotebookAction)`)` Output only. The workflow action's notebook action details.  
`dataPreparationAction` |  `object (`[DataPreparationAction](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#DataPreparationAction)`)` Output only. The workflow action's data preparation action details.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## BigQueryAction

Represents a workflow action that will run against BigQuery.

JSON representation  
---  
      
    
    {
      "sqlScript": string,
      "jobId": string
    }  
  
Fields  
---  
`sqlScript` |  `string` Output only. The generated BigQuery SQL script that will be executed.  
`jobId` |  `string` Output only. The ID of the BigQuery job that executed the SQL in sqlScript. Only set once the job has started to run.  
  
## NotebookAction

Represents a workflow action that will run against a Notebook runtime.

JSON representation  
---  
      
    
    {
      "contents": string,
      "jobId": string,
      "filePath": string
    }  
  
Fields  
---  
`contents` |  `string` Output only. The code contents of a Notebook to be run.  
`jobId` |  `string` Output only. The ID of the Gemini Enterprise Agent Platform job that executed the notebook in contents and also the ID used for the outputs created in Google Cloud Storage buckets. Only set once the job has started to run.  
`filePath` |  `string` Output only. The path to the notebook file in the repository.  
  
## DataPreparationAction

Represents a workflow action that will run a Data Preparation.

JSON representation  
---  
      
    
    {
      "generatedSql": string,
      "jobId": string,
    
      // Union field definition can be only one of the following:
      "contentsYaml": string,
      "contentsSql": {
        object ([ActionSqlDefinition](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionSqlDefinition))
      }
      // End of list of possible types for union field definition.
    }  
  
Fields  
---  
`generatedSql` |  `string` Output only. The generated BigQuery SQL script that will be executed. For reference only.  
`jobId` |  `string` Output only. The ID of the BigQuery job that executed the SQL in sqlScript. Only set once the job has started to run.  
Union field `definition`. The definition for the data preparation. `definition` can be only one of the following:  
`contentsYaml` |  `string` Output only. YAML representing the contents of the data preparation. Can be used to show the customer what the input was to their workflow.  
`contentsSql` |  `object (`[ActionSqlDefinition](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionSqlDefinition)`)` SQL definition for a Data Preparation. Contains a SQL query and additional context information.  
  
## ActionSqlDefinition

Definition of a SQL Data Preparation

JSON representation  
---  
      
    
    {
      "query": string,
      "errorTable": {
        object ([ActionErrorTable](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionErrorTable))
      },
      "loadConfig": {
        object ([ActionLoadConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionLoadConfig))
      }
    }  
  
Fields  
---  
`query` |  `string` The SQL query representing the data preparation steps. Formatted as a Pipe SQL query statement.  
`errorTable` |  `object (`[ActionErrorTable](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionErrorTable)`)` Error table configuration,  
`loadConfig` |  `object (`[ActionLoadConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionLoadConfig)`)` Load configuration.  
  
## ActionErrorTable

Error table information, used to write error data into a BigQuery table.

JSON representation  
---  
      
    
    {
      "target": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target))
      },
      "retentionDays": integer
    }  
  
Fields  
---  
`target` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target)`)` Error Table target.  
`retentionDays` |  `integer` Error table partition expiration in days. Only positive values are allowed.  
  
## ActionLoadConfig

Simplified load configuration for actions

JSON representation  
---  
      
    
    {
    
      // Union field mode can be only one of the following:
      "replace": {
        object ([ActionSimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionSimpleLoadMode))
      },
      "append": {
        object ([ActionSimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionSimpleLoadMode))
      },
      "maximum": {
        object ([ActionIncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionIncrementalLoadMode))
      },
      "unique": {
        object ([ActionIncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionIncrementalLoadMode))
      }
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
Union field `mode`. Load mode `mode` can be only one of the following:  
`replace` |  `object (`[ActionSimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionSimpleLoadMode)`)` Replace destination table  
`append` |  `object (`[ActionSimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionSimpleLoadMode)`)` Append into destination table  
`maximum` |  `object (`[ActionIncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionIncrementalLoadMode)`)` Insert records where the value exceeds the previous maximum value for a column in the destination table  
`unique` |  `object (`[ActionIncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query#ActionIncrementalLoadMode)`)` Insert records where the value of a column is not already present in the destination table  
  
## ActionSimpleLoadMode

This type has no fields.

Simple load definition

## ActionIncrementalLoadMode

Load definition for incremental load modes

JSON representation  
---  
      
    
    {
      "column": string
    }  
  
Fields  
---  
`column` |  `string` Column name for incremental load modes  
  
## State

Represents the current state of a workflow invocation action.

Enums  
---  
`PENDING` | The action has not yet been considered for invocation.  
`RUNNING` | The action is currently running.  
`SKIPPED` | Execution of the action was skipped because upstream dependencies did not all complete successfully. A terminal state.  
`DISABLED` | Execution of the action was disabled as per the configuration of the corresponding compilation result action. A terminal state.  
`SUCCEEDED` | The action succeeded. A terminal state.  
`CANCELLED` | The action was cancelled. A terminal state.  
`FAILED` | The action failed. A terminal state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
