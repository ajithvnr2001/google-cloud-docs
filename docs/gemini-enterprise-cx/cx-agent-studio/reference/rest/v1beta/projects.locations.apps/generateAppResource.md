---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource/
title: Method: projects.locations.apps.generateAppResource \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:43.591711+00:00
---

# Method: projects.locations.apps.generateAppResource  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.generateAppResource Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * GenerateAppResourceRequest.AppVersionContext
    * JSON representation
  * GenerateAppResourceRequest.RefineInstructions
    * JSON representation
  * GenerateAppResourceRequest.ToolGenerationConfig
    * JSON representation
  * FileContext
    * JSON representation
  * FileContext.FileBytes
    * JSON representation
  * GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig
    * JSON representation
  * GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig
    * JSON representation
  * GenerateAppResourceRequest.AppGenerationConfig
    * JSON representation
  * GenerateAppResourceRequest.EvaluationGenerationConfig
    * JSON representation
  * GenerateAppResourceRequest.EvaluationPersonasGenerationConfig
  * GenerateAppResourceRequest.QualityReportGenerationConfig
    * JSON representation
  * GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm
  * GenerateAppResourceRequest.HillClimbingFixConfig
    * JSON representation
  * QualityReport
    * JSON representation
  * QualityReport.AgentIssues
    * JSON representation
  * QualityReport.Issue
    * JSON representation



Generates specific resources (e.g. agent) in the app using LLM assistant.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{parent=projects/*/locations/*/apps/*}:generateAppResource`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the app to generate the resource for.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "refineInstructions": [
        {
          object ([GenerateAppResourceRequest.RefineInstructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.RefineInstructions))
        }
      ],
      "toolGenerationConfig": {
        object ([GenerateAppResourceRequest.ToolGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.ToolGenerationConfig))
      },
      "appGenerationConfig": {
        object ([GenerateAppResourceRequest.AppGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.AppGenerationConfig))
      },
      "evaluationGenerationConfig": {
        object ([GenerateAppResourceRequest.EvaluationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.EvaluationGenerationConfig))
      },
      "evaluationPersonasGenerationConfig": {
        object ([GenerateAppResourceRequest.EvaluationPersonasGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.EvaluationPersonasGenerationConfig))
      },
      "qualityReportGenerationConfig": {
        object ([GenerateAppResourceRequest.QualityReportGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.QualityReportGenerationConfig))
      },
      "hillClimbingFixConfig": {
        object ([GenerateAppResourceRequest.HillClimbingFixConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.HillClimbingFixConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agent": {
        object ([Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent))
      },
      "tool": {
        object ([Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool))
      },
      "toolset": {
        object ([Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset))
      },
      "appVersionContext": {
        object ([GenerateAppResourceRequest.AppVersionContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.AppVersionContext))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`refineInstructions[]` |  `object (`[GenerateAppResourceRequest.RefineInstructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.RefineInstructions)`)` Optional. List of refine instructions to be used to refine the resource.  
`toolGenerationConfig` |  `object (`[GenerateAppResourceRequest.ToolGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.ToolGenerationConfig)`)` Optional. The configuration to be used to generate the tool.  
`appGenerationConfig` |  `object (`[GenerateAppResourceRequest.AppGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.AppGenerationConfig)`)` Optional. The configuration to be used to generate the agents and tools.  
`evaluationGenerationConfig` |  `object (`[GenerateAppResourceRequest.EvaluationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.EvaluationGenerationConfig)`)` Optional. The configuration to be used to generate the evaluations.  
`evaluationPersonasGenerationConfig` |  `object (`[GenerateAppResourceRequest.EvaluationPersonasGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.EvaluationPersonasGenerationConfig)`)` Optional. The configuration to be used to generate the evaluation personas.  
`qualityReportGenerationConfig` |  `object (`[GenerateAppResourceRequest.QualityReportGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.QualityReportGenerationConfig)`)` Optional. The configuration to be used for quality report generation.  
`hillClimbingFixConfig` |  `object (`[GenerateAppResourceRequest.HillClimbingFixConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.HillClimbingFixConfig)`)` Optional. The configuration to be used for hill climbing fixes.  
The resource to generate. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agent` |  `object (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent)`)` The agent resource to be used by the LLM assistant, can be empty for generating a new agent.  
`tool` |  `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool)`)` The tool resource to be used by the LLM assistant, can be empty for generating a new tool.  
`toolset` |  `object (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset)`)` The toolset resource to be used by the LLM assistant, can be empty for generating a new toolset.  
`appVersionContext` |  `object (`[GenerateAppResourceRequest.AppVersionContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.AppVersionContext)`)` The app version context specifying the base snapshot and target agent.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.apps.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GenerateAppResourceRequest.AppVersionContext

The app version context specifying the base snapshot and target agent.

JSON representation  
---  
      
    
    {
      "appVersion": string,
      "agentResourceName": string
    }  
  
Fields  
---  
`appVersion` |  `string` The resource name of the app version to be used by the LLM assistant. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`agentResourceName` |  `string` The resource name of the target agent to be used by the LLM assistant. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
  
## GenerateAppResourceRequest.RefineInstructions

The instructions to be used to refine a part of the resource. The part of the resource can be specified with a start index, end index and a field mask. For example, if you want to refine a part of the agent instructions you can specify the index of the first character of the instructions, the index of the last character of the instructions and the field mask as "instructions".

JSON representation  
---  
      
    
    {
      "startIndex": string,
      "endIndex": string,
      "fieldMask": string,
      "instructions": string
    }  
  
Fields  
---  
`startIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The first character (inclusive) of the text to refine.  
`endIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The last character (inclusive) of the text to refine.  
`fieldMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The field of the resource being refined. Only one field is allowed per RefineInstructions. If refining agent instructions, the field mask should be "instructions".This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`instructions` |  `string` Required. The instructions to refine the resource.  
  
## GenerateAppResourceRequest.ToolGenerationConfig

The configuration to be used to generate a tool.

JSON representation  
---  
      
    
    {
      "context": string,
      "fileContexts": [
        {
          object ([FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#FileContext))
        }
      ],
      "openApiToolsetGenerationConfig": {
        object ([GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig))
      }
    }  
  
Fields  
---  
`context` |  `string` Optional. The context which describes the tool to be generated. This can be empty if the tool request & response are provided.  
`fileContexts[]` |  `object (`[FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#FileContext)`)` Optional. The files to be used as context.  
`openApiToolsetGenerationConfig` |  `object (`[GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig)`)` Optional. The configuration to be used to generate an Open API schema.  
  
## FileContext

Files to be used as context. Files can be provided as raw bytes.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "fileBytes": {
        object ([FileContext.FileBytes](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#FileContext.FileBytes))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
File provided as context. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`fileBytes` |  `object (`[FileContext.FileBytes](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#FileContext.FileBytes)`)` Optional. File provided as raw bytes.  
End of mutually exclusive fields.  
  
## FileContext.FileBytes

File provided as raw bytes.

JSON representation  
---  
      
    
    {
      "fileName": string,
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`fileName` |  `string` Required. The name of the file provided as raw bytes.  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the file.A base64-encoded string.  
  
## GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig

The configuration to be used to generate an Open API schema.

JSON representation  
---  
      
    
    {
      "uri": string,
      "operationGenerationConfigs": [
        {
          object ([GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig))
        }
      ]
    }  
  
Fields  
---  
`uri` |  `string` Required. The base uri of the tool.  
`operationGenerationConfigs[]` |  `object (`[GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig)`)` Required. The list of operations to be added to the Open API schema.  
  
## GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig

The configuration to be used to generate an operation in the Open API schema.

JSON representation  
---  
      
    
    {
      "method": string,
      "path": string,
      "requestJson": string,
      "responseJson": string
    }  
  
Fields  
---  
`method` |  `string` Required. The uri of the tool. This should include query and path parameters if any.  
`path` |  `string` Required. The path of the tool to be appended to the base uri. This should include query and path parameters if any.  
`requestJson` |  `string` Required. A sample request to the tool in JSON format. Skip if the tool does not support request body.  
`responseJson` |  `string` Required. A sample response from the tool in JSON format.  
  
## GenerateAppResourceRequest.AppGenerationConfig

The configuration to be used to generate the app.

JSON representation  
---  
      
    
    {
      "context": string,
      "fileContexts": [
        {
          object ([FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#FileContext))
        }
      ],
      "datasetId": string,
      "generateEvaluations": boolean,
      "gcsLocation": string
    }  
  
Fields  
---  
`context` |  `string` Optional. The context which describes the requirements of the agents & tools to be generated.  
`fileContexts[]` |  `object (`[FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#FileContext)`)` Optional. The files to be used as context.  
`datasetId` |  `string` Optional. The insights dataset to be used to fetch conversation data for generating the agents & tools. Format: `projects/{project}/locations/{location}/datasets/{dataset}`.  
`generateEvaluations` |  `boolean` Optional. Whether to generate the evaluations for the app. If true, the provided context will be used to generate the evaluations data.  
`gcsLocation` |  `string` Optional. The Cloud Storage location to store the generated question answer data to be used by the Datastore tool. This data is generated only when using conversation data as an input source. The location must be in the same project as the app. Format: `gs://...`.  
  
## GenerateAppResourceRequest.EvaluationGenerationConfig

The configuration to be used to generate the evaluations.

JSON representation  
---  
      
    
    {
      "datasetId": string
    }  
  
Fields  
---  
`datasetId` |  `string` Optional. The insights dataset to be used to fetch conversation data for generating the evaluations. Format: `projects/{project}/locations/{location}/datasets/{dataset}`.  
  
## GenerateAppResourceRequest.EvaluationPersonasGenerationConfig

This type has no fields.

The configuration to be used to generate the evaluation personas.

## GenerateAppResourceRequest.QualityReportGenerationConfig

The configuration to be used for quality report generation.

JSON representation  
---  
      
    
    {
      "evaluationRun": string,
      "algorithm": enum ([GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm))
    }  
  
Fields  
---  
`evaluationRun` |  `string` Required. The evaluation run used to inform quality report analysis.  
`algorithm` |  `enum (`[GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm)`)` Optional. The loss attribution algorithm to use.  
  
## GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm

The algorithm to use for loss attribution.

Enums  
---  
`LOSS_ATTRIBUTION_ALGORITHM_UNSPECIFIED` | Unspecified.  
`APP_CENTRIC` | App-centric loss attribution. Treats the app as a single unit.  
`AGENT_CENTRIC` | Agent-centric loss attribution. Attributes loss to individual agents.  
  
## GenerateAppResourceRequest.HillClimbingFixConfig

The configuration to be used for hill climbing fixes.

JSON representation  
---  
      
    
    {
      "qualityReport": {
        object ([QualityReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport))
      }
    }  
  
Fields  
---  
`qualityReport` |  `object (`[QualityReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport)`)` Required. The quality report used to inform the instruction following fix.  
  
## QualityReport

The report describing any identified quality issues in the app.

JSON representation  
---  
      
    
    {
      "issues": [
        {
          object ([QualityReport.AgentIssues](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport.AgentIssues))
        }
      ],
      "evaluationRuns": [
        string
      ],
      "generalIssues": [
        {
          object ([QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport.Issue))
        }
      ]
    }  
  
Fields  
---  
`issues[]` |  `object (`[QualityReport.AgentIssues](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport.AgentIssues)`)` Optional. The issues grouped by agent.  
`evaluationRuns[]` |  `string` Optional. A list of evaluation runs used to generate the quality report. Format: `projects/{project}/locations/{location}/evaluationRuns/{evaluationRun}`.  
`generalIssues[]` |  `object (`[QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport.Issue)`)` Optional. General issues not specific to any agent.  
  
## QualityReport.AgentIssues

Issues identified for a single agent.

JSON representation  
---  
      
    
    {
      "agent": string,
      "issues": [
        {
          object ([QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport.Issue))
        }
      ]
    }  
  
Fields  
---  
`agent` |  `string` Optional. The name of the agent to which the issues are related. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`issues[]` |  `object (`[QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/generateAppResource#QualityReport.Issue)`)` Optional. List of issues found for this agent.  
  
## QualityReport.Issue

The issue identified.

JSON representation  
---  
      
    
    {
      "description": string,
      "occurrenceCount": integer,
      "proposedSolution": string
    }  
  
Fields  
---  
`description` |  `string` Optional. Description of the issue found.  
`occurrenceCount` |  `integer` Optional. How many times this issue occurred.  
`proposedSolution` |  `string` Optional. Proposed solution to fix the issue by modifying instructions or tools.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
