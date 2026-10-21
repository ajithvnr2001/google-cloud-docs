---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/query/
title: Method: projects.locations.collections.dataObjects.query \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:17:27.084505+00:00
---

# Method: projects.locations.collections.dataObjects.query  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.query Stay organized with collections  Save and categorize content based on your preferences. 

Queries data objects.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{parent}/dataObjects:query`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Collection for which to query. Format: `projects/{project}/locations/{location}/collections/{collection}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": {
        object
      },
      "outputFields": {
        object ([OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/OutputFields))
      },
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`filter` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A JSON filter expression, e.g. {"genre": {"$eq": "sci-fi"}}, represented as a google.protobuf.Struct.  
`outputFields` |  `object (`[OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/OutputFields)`)` Optional. Mask specifying which fields to return.  
`pageSize` |  `integer` Optional. The standard list page size. Default is 100. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. The standard list page token. Typically obtained via `[QueryDataObjectsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/query#body.QueryDataObjectsResponse.FIELDS.next_page_token)` of the previous `[DataObjectSearchService.QueryDataObjects](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/query#google.cloud.vectorsearch.v1beta.DataObjectSearchService.QueryDataObjects)` call.  
  
### Response body

Response message for `[DataObjectSearchService.QueryDataObjects](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/query#google.cloud.vectorsearch.v1beta.DataObjectSearchService.QueryDataObjects)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataObjects": [
        {
          object ([DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects#DataObject))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dataObjects[]` |  `object (`[DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects#DataObject)`)` Output only. The list of dataObjects that match the query.  
`nextPageToken` |  `string` Output only. A token to retrieve next page of results. Pass to [DataObjectSearchService.QueryDataObjectsRequest.page_token][] to obtain that page.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `vectorsearch.dataObjects.query`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
