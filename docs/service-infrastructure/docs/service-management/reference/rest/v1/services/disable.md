---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/disable/
title: Method: services.disable \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:26.296499+00:00
---

# Method: services.disable  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.disable Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes



Enable and Disable methods in Service Management are deprecated in favor of the [Service Usage methods](https://cloud.google.com/service-usage/docs/reference/rest/v1/services/disable).

Disables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services#ManagedService)` for a project, so it can no longer be be used for the project. It prevents accidental usage that may cause unexpected billing charges or security leaks.

Operation<response: DisableServiceResponse>

### HTTP request

`POST https://servicemanagement.googleapis.com/v1/services/{serviceName}:disable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` Required. name of the service to disable. Specifying an unknown service name will cause the request to fail. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.bind`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consumerId": string
    }  
  
Fields  
---  
`consumerId` |  `string` Required. The identity of consumer resource which service disablement will be applied to.The Google Service Management implementation accepts the following forms: - "project:"Note: this is made compatible with google.api.servicecontrol.v1.Operation.consumer_id. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `consumerId`:

  * `servicemanagement.services.bind`

  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations#Operation)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
