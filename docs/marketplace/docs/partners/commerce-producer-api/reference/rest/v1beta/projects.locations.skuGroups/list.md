---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups/list/
title: Method: projects.locations.skuGroups.list \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:01.321003+00:00
---

# Method: projects.locations.skuGroups.list  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Method: projects.locations.skuGroups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists SkuGroups for the given parent.

### HTTP request

`GET https://commerceproducer.googleapis.com/v1beta/{parent=projects/*/locations/*}/skuGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListSkuGroupsRequest  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum results to return. The service may return fewer than this value. The maximum value is 500; values above 500 will be coerced to 500. If unspecified, the server will default to the maximum.  
`pageToken` |  `string` Optional. A page token, received from a previous list response message. Provide this to retrieve the subsequent page.When paginating, all other parameters of the list request must match the request that returned the page token.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing SkuGroups

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "skuGroups": [
        {
          object ([SkuGroup](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups#SkuGroup))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`skuGroups[]` |  `object (`[SkuGroup](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups#SkuGroup)`)` The list of SkuGroup  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `commerceproducer.skuGroups.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
