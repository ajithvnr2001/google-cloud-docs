---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services/list/
title: Method: projects.locations.services.list \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:15.058420+00:00
---

# Method: projects.locations.services.list  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Method: projects.locations.services.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists Services in a given project and location.

### HTTP request

`GET https://commerceproducer.googleapis.com/v1beta/{parent=projects/*/locations/*}/services`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListServicesRequest  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum results to return. The service may return fewer than this value. The maximum value is 500; values above 500 will be coerced to 500. If unspecified, the server will default to the maximum.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing Services

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "services": [
        {
          object ([Service](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#Service))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`services[]` |  `object (`[Service](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#Service)`)` The list of Service  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `commerceproducer.services.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
