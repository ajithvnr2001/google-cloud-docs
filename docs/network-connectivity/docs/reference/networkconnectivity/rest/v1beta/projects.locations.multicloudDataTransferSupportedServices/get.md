---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.multicloudDataTransferSupportedServices/get/
title: Method: projects.locations.multicloudDataTransferSupportedServices.get \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:22.120479+00:00
---

# Method: projects.locations.multicloudDataTransferSupportedServices.get  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.multicloudDataTransferSupportedServices/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  Method: projects.locations.multicloudDataTransferSupportedServices.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets the details of a service that is supported for Data Transfer Essentials.

### HTTP request

`GET https://networkconnectivity.googleapis.com/v1beta/{name=projects/*/locations/*/multicloudDataTransferSupportedServices/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the service.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.multicloudDataTransferSupportedServices#MulticloudDataTransferSupportedService)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
