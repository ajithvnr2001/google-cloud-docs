---
url: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/list/
title: Method: projects.occurrences.list \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:43.321536+00:00
---

# Method: projects.occurrences.list  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-analysis/docs/apis)



Send feedback 

#  Method: projects.occurrences.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists occurrences for the specified project.

### HTTP request

Choose a location:

global asia-east1 asia-east2 asia-northeast1 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 africa-south1 asia-northeast2 australia-southeast2 europe-west10 us eu

  
`GET https://containeranalysis.googleapis.com/v1beta1/{parent=projects/*}/occurrences`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project to list occurrences for in the form of `projects/[PROJECT_ID]`.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` The filter expression.  
`pageSize` |  `integer` Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20.  
`pageToken` |  `string` Token to provide to skip to a particular spot in the list.  
`returnPartialSuccess` |  `boolean` If set, the request will return all reachable Occurrences and report all unreachable regions in the `unreachable` field in the response.Only applicable for requests in the global region.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListOccurrencesResponse](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/ListOccurrencesResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-09 UTC."],[],[]] 
