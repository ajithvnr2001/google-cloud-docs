---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/list/
title: Method: projects.locations.brands.evaluationCaseResults.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:27:35.300379+00:00
---

# Method: projects.locations.brands.evaluationCaseResults.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.brands.evaluationCaseResults.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists EvaluationCaseResults.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCaseResults`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation case results. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of evaluation case results to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `evaluationCaseResults.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Only retrieve evaluation case results matching the filter. Currently only supports filtering by `evaluationCase`, e.g. `evaluationCase="projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{case_id}"`.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListEvaluationCaseResults](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/list#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationCaseResults)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "evaluationCaseResults": [
        {
          object ([EvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#EvaluationCaseResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`evaluationCaseResults[]` |  `object (`[EvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#EvaluationCaseResult)`)` The evaluation case results from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
