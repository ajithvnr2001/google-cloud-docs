---
url: https://docs.cloud.google.com/vision/docs/reference/rest/v1p4beta1/projects.locations.products.referenceImages/list/
title: Method: projects.locations.products.referenceImages.list \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:27.096762+00:00
---

# Method: projects.locations.products.referenceImages.list  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/reference/rest/v1p4beta1/projects.locations.products.referenceImages/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Method: projects.locations.products.referenceImages.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist.
  * Returns INVALID_ARGUMENT if the pageSize is greater than 100, or less than 1.



### HTTP request

`GET https://vision.googleapis.com/v1p4beta1/{parent=projects/*/locations/*/products/*}/referenceImages`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the product containing the reference images.Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `number` The maximum number of items to return. Default 10, maximum 100.   
`pageToken` |  `string` A token identifying a page of results to be returned. This is the value of `nextPageToken` returned in a previous reference image list request.Defaults to the first page if not specified.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for the `referenceImages.list` method.

JSON representation  
---  
      
    
    {
      "referenceImages": [
        {
          object ([ReferenceImage](https://docs.cloud.google.com/vision/docs/reference/rest/v1p4beta1/projects.locations.products.referenceImages#ReferenceImage))
        }
      ],
      "pageSize": number,
      "nextPageToken": string
    }  
  
Fields  
---  
`referenceImages[]` |  `object (`[ReferenceImage](https://docs.cloud.google.com/vision/docs/reference/rest/v1p4beta1/projects.locations.products.referenceImages#ReferenceImage)`)` The list of reference images.   
`pageSize` |  `number` The maximum number of items to return. Default 10, maximum 100.   
`nextPageToken` |  `string` The nextPageToken returned from a previous List request, if any.   
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
