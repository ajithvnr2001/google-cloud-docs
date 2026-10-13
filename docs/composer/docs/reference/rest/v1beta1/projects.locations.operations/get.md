---
url: https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.operations/get/
title: Method: projects.locations.operations.get \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:28.482906+00:00
---

# Method: projects.locations.operations.get  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.operations/get/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Reference ](https://docs.cloud.google.com/composer/docs/apis)



Send feedback 

#  Method: projects.locations.operations.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

### HTTP request

`GET https://composer.googleapis.com/v1beta1/{name=projects/*/locations/*/operations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The name of the operation resource.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/composer/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudcomposer.readonly`
  * ` https://www.googleapis.com/auth/cloudcomposer`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-29 UTC."],[],[]] 
