---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults/get/
title: Method: projects.locations.brands.evaluationCaseResults.get \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:00.799743+00:00
---

# Method: projects.locations.brands.evaluationCaseResults.get  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.evaluationCaseResults.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes



Gets an EvaluationCaseResult.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{name=projects/*/locations/*/brands/*/evaluationCaseResults/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the evaluation case result to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluationCaseResult}  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[EvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults#EvaluationCaseResult)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
