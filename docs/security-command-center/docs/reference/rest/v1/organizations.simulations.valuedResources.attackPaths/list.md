---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.simulations.valuedResources.attackPaths/list/
title: Method: organizations.simulations.valuedResources.attackPaths.list \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:04.156336+00:00
---

# Method: organizations.simulations.valuedResources.attackPaths.list  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.simulations.valuedResources.attackPaths/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.simulations.valuedResources.attackPaths.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists the attack paths for a set of simulation results or valued resources and filter.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`GET https://securitycenter.googleapis.com/v1/{parent=organizations/*/simulations/*/valuedResources/*}/attackPaths`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of parent to list attack paths.Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}` `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}`  
  
### Query parameters

Parameters  
---  
`filter` |  `string` The filter expression that filters the attack path in the response. Supported fields:

  * `valuedResources` supports =

  
`pageToken` |  `string` The value returned by the last `ListAttackPathsResponse`; indicates that this is a continuation of a prior `attackPaths.list` call, and that the system should return the next page of data.  
`pageSize` |  `integer` The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListAttackPathsResponse](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
