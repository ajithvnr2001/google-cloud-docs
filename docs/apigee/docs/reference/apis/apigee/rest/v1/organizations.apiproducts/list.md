---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/list/
title: Method: organizations.apiproducts.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:18.744512+00:00
---

# Method: organizations.apiproducts.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apiproducts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all API product names for an organization. Filter the list by passing an `attributename` and `attibutevalue`.

The maximum number of API products returned is 1000. You can paginate the list of API products returned using the `startKey` and `count` query parameters.

If the resource has the `space` attribute set, the response may not return all resources. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/apiproducts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the organization. Use the following structure in your request: `organizations/{org}`If the resource has the `space` attribute set, IAM permissions are checked against the Space resource path. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.apiproducts.list`

  
  
### Query parameters

Parameters  
---  
`attributename` |  `string` Name of the attribute used to filter the search.  
`attributevalue` |  `string` Value of the attribute used to filter the search.  
`expand` |  `boolean` Flag that specifies whether to expand the results. Set to `true` to get expanded details about each API.  
`startKey` |  `string` Gets a list of API products starting with a specific API product in the list. For example, if you're returning 50 API products at a time (using the `count` query parameter), you can view products 50-99 by entering the name of the 50th API product in the first API (without using `startKey`). Product name is case sensitive.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Enter the number of API products you want returned in the API call. The limit is 1000.  
`space` |  `string` Optional. The Space to list API products for. When none provided, all the spaces the user has list access, will be used implicitly, and the same following rules will apply. Can be used in conjunction with startKey, expand and count for paginated response. Composite queries with attributename and attributevalue are not supported yet.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "apiProduct": [
        {
          object ([ApiProduct](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#ApiProduct))
        }
      ]
    }  
  
Fields  
---  
`apiProduct[]` |  `object (`[ApiProduct](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#ApiProduct)`)` Lists all API product names defined for an organization.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
