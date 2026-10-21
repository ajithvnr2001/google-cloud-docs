---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations/
title: Method: projects.locations.apps.importEvaluations \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:43.456407+00:00
---

# Method: projects.locations.apps.importEvaluations  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.importEvaluations Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * ImportEvaluationsRequest.ConversationList
    * JSON representation
  * ImportEvaluationsRequest.ImportOptions
    * JSON representation
  * ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy



Imports evaluations into the app.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{parent=projects/*/locations/*/apps/*}:importEvaluations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The app to import the evaluations into. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "importOptions": {
        object ([ImportEvaluationsRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations#ImportEvaluationsRequest.ImportOptions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "conversationList": {
        object ([ImportEvaluationsRequest.ConversationList](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations#ImportEvaluationsRequest.ConversationList))
      },
      "gcsUri": string,
      "csvContent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`importOptions` |  `object (`[ImportEvaluationsRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations#ImportEvaluationsRequest.ImportOptions)`)` Optional. Options governing the import process for the evaluations.  
The source of the evaluations to import from. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`conversationList` |  `object (`[ImportEvaluationsRequest.ConversationList](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations#ImportEvaluationsRequest.ConversationList)`)` The conversations to import the evaluations from.  
`gcsUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import evaluations. The format of this URI must be `gs://<bucket-name>/<object-name>`.  
`csvContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Raw bytes representing the csv file with the evaluations structure.A base64-encoded string.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `ces.evaluations.create`
  * `ces.evaluations.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ImportEvaluationsRequest.ConversationList

A list of conversation resource names.

JSON representation  
---  
      
    
    {
      "conversations": [
        string
      ]
    }  
  
Fields  
---  
`conversations[]` |  `string` Optional. Conversation resource names.  
  
## ImportEvaluationsRequest.ImportOptions

Configuration options for the evaluation import process. These options control how the import behaves, particularly when conflicts arise with existing evaluations data.

JSON representation  
---  
      
    
    {
      "conflictResolutionStrategy": enum ([ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations#ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy))
    }  
  
Fields  
---  
`conflictResolutionStrategy` |  `enum (`[ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/importEvaluations#ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy)`)` Optional. The strategy to use when resolving conflicts during import.  
  
## ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy

Defines the strategy for handling conflicts when an evaluation with the same evaluation ID already exists in the app.

Enums  
---  
`CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED` | The conflict resolution strategy is unspecified.  
`OVERWRITE` | Overwrite the existing evaluation with the new one.  
`SKIP` | Keep the existing evaluation and skip the new one.  
`DUPLICATE` | Keep the existing evaluation and duplicate the new one as a new evaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
