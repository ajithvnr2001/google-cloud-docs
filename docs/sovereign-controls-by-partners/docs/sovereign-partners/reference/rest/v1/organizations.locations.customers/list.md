---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers/list/
title: Method: organizations.locations.customers.list \u00a0|\u00a0 Sovereign Controls by Partners guides for partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:57.135258+00:00
---

# Method: organizations.locations.customers.list  |  Sovereign Controls by Partners guides for partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners)
  * [ Sovereign Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/guides)
  * [ Reference ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest)



Send feedback 

#  Method: organizations.locations.customers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists customers of a partner identified by its Google Cloud organization ID

### HTTP request

`GET https://cloudcontrolspartner.googleapis.com/v1/{parent=organizations/*/locations/*}/customers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent resource Format: organizations/{organization}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of Customers to return. The service may return fewer than this value. If unspecified, at most 500 Customers will be returned.  
`pageToken` |  `string` A page token, received from a previous `customers.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filtering results  
`orderBy` |  `string` Optional. Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

Response message for list customer Customers requests

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "customers": [
        {
          object ([Customer](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers#Customer))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`customers[]` |  `object (`[Customer](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers#Customer)`)` List of customers  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `cloudcontrolspartner.customers.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
