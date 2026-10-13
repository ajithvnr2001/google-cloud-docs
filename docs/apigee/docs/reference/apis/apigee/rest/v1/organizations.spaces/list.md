---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/list/
title: Method: organizations.spaces.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:56.248095+00:00
---

# Method: organizations.spaces.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.spaces.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists spaces under an organization.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/spaces`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Use the following structure in your request: `organizations`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of spaces to return. The service may return fewer than this value. If unspecified, at most 50 spaces will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `spaces.list` call. Provide this to retrieve the subsequent page. When paginating, all parameters must match the original call.  
  
### Request body

The request body must be empty.

### Response body

A response to a spaces.list request containing the list of organization spaces and a page token for the next page.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "spaces": [
        {
          object ([Space](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces#Space))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`spaces[]` |  `object (`[Space](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces#Space)`)` List of Apigee organization spaces.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
