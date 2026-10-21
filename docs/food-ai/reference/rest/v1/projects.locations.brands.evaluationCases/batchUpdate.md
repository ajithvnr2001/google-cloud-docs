---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchUpdate/
title: Method: projects.locations.brands.evaluationCases.batchUpdate \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:01.946673+00:00
---

# Method: projects.locations.brands.evaluationCases.batchUpdate  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.evaluationCases.batchUpdate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * UpdateEvaluationCaseRequest
    * JSON representation



Batch updates EvaluationCases.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}/evaluationCases:batchUpdate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource shared by all evaluation cases being updated. Format: projects/{project}/locations/{location}/brands/{brand} If this is set, the parent of all of the evaluation cases specified in `requests` must match this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([UpdateEvaluationCaseRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchUpdate#UpdateEvaluationCaseRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[UpdateEvaluationCaseRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchUpdate#UpdateEvaluationCaseRequest)`)` Required. The request message specifying the resources to update. A maximum of 1000 evaluation cases can be modified in a batch.  
  
### Response body

Response message for `[MenuService.BatchUpdateEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchUpdate#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateEvaluationCases)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "evaluationCases": [
        {
          object ([EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases#EvaluationCase))
        }
      ]
    }  
  
Fields  
---  
`evaluationCases[]` |  `object (`[EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases#EvaluationCase)`)` EvaluationCases updated.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## UpdateEvaluationCaseRequest

Request message for `[MenuService.UpdateEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/patch#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationCase)`.

JSON representation  
---  
      
    
    {
      "evaluationCase": {
        object ([EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases#EvaluationCase))
      },
      "updateMask": string,
      "allowMissing": boolean
    }  
  
Fields  
---  
`evaluationCase` |  `object (`[EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases#EvaluationCase)`)` Required. The evaluation case to update.The evaluation case's `name` field is used to identify the evaluation case to update. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluationCase}  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to updateThis is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`allowMissing` |  `boolean` Optional. If set to true, and the evaluation case is not found, a new evaluation case will be created. In this situation, `updateMask` is ignored.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
