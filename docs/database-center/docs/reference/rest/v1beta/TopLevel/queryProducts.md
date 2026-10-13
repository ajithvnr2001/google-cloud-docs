---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryProducts/
title: Method: queryProducts \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.531635+00:00
---

# Method: queryProducts  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryProducts/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Method: queryProducts Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



v1beta.queryProducts provides a list of all possible products which can be used to filter database resources.

### HTTP request

`GET https://databasecenter.googleapis.com/v1beta:queryProducts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization.The allowed values are:

  * projects/{PROJECT_ID}/locations/{LOCATION} (e.g.,"projects/foo-bar/locations/us-central1")
  * projects/{PROJECT_NUMBER}/locations/{LOCATION} (e.g.,"projects/12345678/locations/us-central1")
  * folders/{FOLDER_NUMBER}/locations/{LOCATION} (e.g.,"folders/1234567/locations/us-central1")
  * organizations/{ORGANIZATION_NUMBER}/locations/{LOCATION} (e.g.,"organizations/123456/locations/us-central1")
  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`pageSize` |  `integer` Optional. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListLocations` call. Provide this to retrieve the subsequent page. All other parameters except page size should match the call that provided the page page token.  
  
### Request body

The request body must be empty.

### Response body

QueryProductsResponse represents the response containing a list of products.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product)`)` List of database products returned.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.products.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
