---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate/
title: Method: projects.locations.brands.evaluationCases.batchCreate \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:27:35.740720+00:00
---

# Method: projects.locations.brands.evaluationCases.batchCreate  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.brands.evaluationCases.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * CreateEvaluationCaseRequest
    * JSON representation



Batch creates EvaluationCases.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCases:batchCreate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource shared by all evaluation cases being created. Format: projects/{project}/locations/{location}/brands/{brand} If this is set, the parent of all of the evaluation cases specified in `requests` must match this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([CreateEvaluationCaseRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate#CreateEvaluationCaseRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[CreateEvaluationCaseRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate#CreateEvaluationCaseRequest)`)` Required. The request message specifying the resources to create. A maximum of 1000 evaluation cases can be created in a batch.  
  
### Response body

Response message for `[MenuService.BatchCreateEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchCreateEvaluationCases)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "evaluationCases": [
        {
          object ([EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase))
        }
      ]
    }  
  
Fields  
---  
`evaluationCases[]` |  `object (`[EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase)`)` EvaluationCases created.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## CreateEvaluationCaseRequest

Request message for `[MenuService.CreateEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/create#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateEvaluationCase)`.

JSON representation  
---  
      
    
    {
      "parent": string,
      "evaluationCase": {
        object ([EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase))
      },
      "evaluationCaseId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation cases. Format: projects/{project}/locations/{location}/brands/{brand}  
`evaluationCase` |  `object (`[EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase)`)` Required. The evaluation case to create.  
`evaluationCaseId` |  `string` Optional. The ID to use for the evaluation case, which will become the final component of the evaluation case's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
