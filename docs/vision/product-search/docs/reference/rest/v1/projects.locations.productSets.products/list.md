---
url: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets.products/list/
title: Method: projects.locations.productSets.products.list \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:11.238674+00:00
---

# Method: projects.locations.productSets.products.list  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets.products/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



#  Method: projects.locations.productSets.products.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes



Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if pageSize is greater than 100 or less than 1.



### HTTP request

`GET https://vision.googleapis.com/v1/{name=projects/*/locations/*/productSets/*}/products`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The ProductSet resource for which to retrieve Products.Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `number` The maximum number of items to return. Default 10, maximum 100.   
`pageToken` |  `string` The nextPageToken returned from a previous List request, if any.   
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for the `products.list` method.

JSON representation  
---  
      
    
    {
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products#Product))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products#Product)`)` The list of Products.   
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.   
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
