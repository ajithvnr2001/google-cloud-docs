---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/create/
title: Method: projects.locations.instances.dnsPeerings.create \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:10.623847+00:00
---

# Method: projects.locations.instances.dnsPeerings.create  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  Method: projects.locations.instances.dnsPeerings.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates DNS peering on the given resource.

### HTTP request

`POST https://datafusion.googleapis.com/v1beta1/{parent=projects/*/locations/*/instances/*}/dnsPeerings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource on which DNS peering will be created.  
  
### Query parameters

Parameters  
---  
`dnsPeeringId` |  `string` Required. The name of the peering to create.  
  
### Request body

The request body contains an instance of `[DnsPeering](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings#DnsPeering)`.

### Response body

If successful, the response body contains a newly created instance of `[DnsPeering](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings#DnsPeering)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-20 UTC."],[],[]] 
