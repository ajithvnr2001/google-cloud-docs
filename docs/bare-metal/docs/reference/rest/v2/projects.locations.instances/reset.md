---
url: https://docs.cloud.google.com/bare-metal/docs/reference/rest/v2/projects.locations.instances/reset/
title: Method: projects.locations.instances.reset \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:52.207942+00:00
---

# Method: projects.locations.instances.reset  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/reference/rest/v2/projects.locations.instances/reset/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Reference ](https://docs.cloud.google.com/bare-metal/docs/reference)



Send feedback 

#  Method: projects.locations.instances.reset Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Perform an ungraceful, hard reset on a server. Equivalent to shutting the power off and then turning it back on.

### HTTP request

`POST https://baremetalsolution.googleapis.com/v2/{name=projects/*/locations/*/instances/*}:reset`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the resource.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/bare-metal/docs/reference/rest/v2/projects.locations.operations#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
