---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/search/
title: Method: projects.locations.authorizedViewSets.authorizedViews.search \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:01.218898+00:00
---

# Method: projects.locations.authorizedViewSets.authorizedViews.search  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.authorizedViewSets.authorizedViews.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



SearchAuthorizedViewSets

### HTTP request

`GET https://{endpoint}/v1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews:search`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the AuthorizedViews. If the parent is set to `-`, all AuthorizedViews under the location will be returned.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of view to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `nextPageToken` in the response indicates that more data is available.  
`pageToken` |  `string` Optional. The value returned by the last `ListAuthorizedViewsResponse`. This value indicates that this is a continuation of a prior `authorizedViews.list` call and that the system should return the next page of data.  
`query` |  `string` Optional. The query expression to search authorized views.  
`orderBy` |  `string` Optional. The order by expression to order authorized views listed in the response.  
  
### Request body

The request body must be empty.

### Response body

The response from a authorizedViews.list request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "authorizedViews": [
        {
          object ([AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews#AuthorizedView))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`authorizedViews[]` |  `object (`[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews#AuthorizedView)`)` The AuthorizedViews under the parent.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
