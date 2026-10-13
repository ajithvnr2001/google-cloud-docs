---
url: https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.adaptiveMtDatasets.adaptiveMtFiles/get/
title: Method: projects.locations.adaptiveMtDatasets.adaptiveMtFiles.get \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:59.012557+00:00
---

# Method: projects.locations.adaptiveMtDatasets.adaptiveMtFiles.get  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.adaptiveMtDatasets.adaptiveMtFiles/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ API and references ](https://docs.cloud.google.com/translate/docs/reference/api-overview)



Send feedback 

#  Method: projects.locations.adaptiveMtDatasets.adaptiveMtFiles.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets and AdaptiveMtFile

### HTTP request

`GET https://translate.googleapis.com/v3/{name=projects/*/locations/*/adaptiveMtDatasets/*/adaptiveMtFiles/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the file, in form of `projects/{project-number-or-id}/locations/{locationId}/adaptiveMtDatasets/{dataset}/adaptiveMtFiles/{file}`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[AdaptiveMtFile](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.adaptiveMtDatasets.adaptiveMtFiles#AdaptiveMtFile)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-translation`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
