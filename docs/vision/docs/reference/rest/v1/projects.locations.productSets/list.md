---
url: https://docs.cloud.google.com/vision/docs/reference/rest/v1/projects.locations.productSets/list/
title: Method: projects.locations.productSets.list \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:06.879273+00:00
---

# Method: projects.locations.productSets.list  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/reference/rest/v1/projects.locations.productSets/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Method: projects.locations.productSets.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if pageSize is greater than 100, or less than 1.



### HTTP request

`GET https://vision.googleapis.com/v1/{parent=projects/*/locations/*}/productSets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project from which ProductSets should be listed.Format is `projects/PROJECT_ID/locations/LOC_ID`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return. Default 10, maximum 100.  
`pageToken` |  `string` The nextPageToken returned from a previous List request, if any.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for the `productSets.list` method.

JSON representation  
---  
      
    
    {
      "productSets": [
        {
          object ([ProductSet](https://docs.cloud.google.com/vision/docs/reference/rest/v1/projects.locations.productSets#ProductSet))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`productSets[]` |  `object (`[ProductSet](https://docs.cloud.google.com/vision/docs/reference/rest/v1/projects.locations.productSets#ProductSet)`)` List of ProductSets.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
