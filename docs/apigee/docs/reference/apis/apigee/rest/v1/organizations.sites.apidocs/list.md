---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/list/
title: Method: organizations.sites.apidocs.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:38.902348+00:00
---

# Method: organizations.sites.apidocs.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.sites.apidocs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Returns the catalog items associated with a portal.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/sites/*}/apidocs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the portal. Use the following structure in your request: `organizations/{org}/sites/{site}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 25 books will be returned. The maximum value is 100; values above 100 will be coerced to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous `apidocs.list` call. Provide this to retrieve the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "status": string,
      "message": string,
      "requestId": string,
      "errorCode": string,
      "data": [
        {
          object ([ApiDoc](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs#ApiDoc))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`status` |  `string` Status of the operation.  
`message` |  `string` Description of the operation.  
`requestId` |  `string` Unique ID of the request.  
`errorCode` |  `string` Unique error code for the request, if any.  
`data[]` |  `object (`[ApiDoc](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs#ApiDoc)`)` The catalog item resources.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
