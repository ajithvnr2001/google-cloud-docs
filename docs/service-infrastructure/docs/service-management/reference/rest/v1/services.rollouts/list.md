---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/list/
title: Method: services.rollouts.list \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:29.257207+00:00
---

# Method: services.rollouts.list  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.rollouts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes



Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest.

### HTTP request

`GET https://servicemanagement.googleapis.com/v1/services/{serviceName}/rollouts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.get`

  
  
### Query parameters

Parameters  
---  
`pageToken` |  `string` The token of the page to retrieve.  
`pageSize` |  `integer` The max number of items to include in the response list. Page size is 50 if not specified. Maximum value is 100.  
`filter` |  `string` Required. Use `filter` to return subset of rollouts. The following filters are supported:\-- By `[status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#RolloutStatus)`. For example, `filter='status=SUCCESS'`\-- By [strategy] [google.api.servicemanagement.v1.Rollout.strategy]. For example, `filter='strategy=TrafficPercentStrategy'`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for rollouts.list method.

JSON representation  
---  
      
    
    {
      "rollouts": [
        {
          object ([Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#Rollout))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`rollouts[]` |  `object (`[Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#Rollout)`)` The list of rollout resources.  
`nextPageToken` |  `string` The token of the next page of results.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
