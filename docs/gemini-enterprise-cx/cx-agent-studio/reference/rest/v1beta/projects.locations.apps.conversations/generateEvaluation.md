---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.conversations/generateEvaluation/
title: Method: projects.locations.apps.conversations.generateEvaluation \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:45.492163+00:00
---

# Method: projects.locations.apps.conversations.generateEvaluation  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.conversations/generateEvaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.conversations.generateEvaluation Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * GenerateEvaluationRequest.EvaluationType



Creates a golden evaluation from a conversation.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{conversation=projects/*/locations/*/apps/*/conversations/*}:generateEvaluation`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversation` |  `string` Required. The conversation to create the golden evaluation for. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "source": enum ([Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.conversations#Conversation.Source)),
      "evaluationType": enum ([GenerateEvaluationRequest.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.conversations/generateEvaluation#GenerateEvaluationRequest.EvaluationType))
    }  
  
Fields  
---  
`source  
**(deprecated)**` |  `enum (`[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.conversations#Conversation.Source)`)` Optional. Indicate the source of the conversation. If not set, all sources will be searched.  
`evaluationType` |  `enum (`[GenerateEvaluationRequest.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.conversations/generateEvaluation#GenerateEvaluationRequest.EvaluationType)`)` Optional. The type of evaluation to generate. Defaults to GOLDEN if unspecified.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `conversation` resource:

  * `ces.conversations.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GenerateEvaluationRequest.EvaluationType

The type of evaluation to generate.

Enums  
---  
`EVALUATION_TYPE_UNSPECIFIED` | Unspecified type. Defaults to GOLDEN.  
`GOLDEN` | Golden evaluation.  
`SCENARIO` | Scenario evaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
