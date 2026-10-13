---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/list/
title: Method: organizations.endpointAttachments.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:42.238905+00:00
---

# Method: organizations.endpointAttachments.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.endpointAttachments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the endpoint attachments in an organization.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/endpointAttachments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the organization for which to list endpoint attachments. Use the following structure in your request: `organizations/{org}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.endpointattachments.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of endpoint attachments to return. If unspecified, at most 25 attachments will be returned.  
`pageToken` |  `string` Optional. Page token, returned from a previous `endpointAttachments.list` call, that you can use to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

Response for endpointAttachments.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "endpointAttachments": [
        {
          object ([EndpointAttachment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments#EndpointAttachment))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`endpointAttachments[]` |  `object (`[EndpointAttachment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments#EndpointAttachment)`)` Endpoint attachments in the specified organization.  
`nextPageToken` |  `string` Page token that you can include in an `endpointAttachments.list` request to retrieve the next page. If omitted, no subsequent pages exist.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
