---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/list/
title: Method: services.list \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:37:25.256695+00:00
---

# Method: services.list  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes



Lists managed services.

Returns all public services. For authenticated users, also returns all services the calling user has "servicemanagement.services.get" permission for.

### HTTP request

`GET https://servicemanagement.googleapis.com/v1/services`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`producerProjectId` |  `string` Include services produced by the specified project.  
`pageSize` |  `integer` The max number of items to include in the response list. Page size is 50 if not specified. Maximum value is 500.  
`pageToken` |  `string` token identifying which result to start with; returned by a previous list call.  
`consumerId  
**(deprecated)**` |  `string` Include services consumed by the specified consumer.The Google Service Management implementation accepts the following forms: - project:  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for `services.list` method.

JSON representation  
---  
      
    
    {
      "services": [
        {
          object ([ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services#ManagedService))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`services[]` |  `object (`[ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services#ManagedService)`)` The returned services will only have the name field set.  
`nextPageToken` |  `string` token that can be passed to `services.list` to resume a paginated query.  
  
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
