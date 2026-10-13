---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora.collections/viewCollectionItems/
title: Method: projects.locations.corpora.collections.viewCollectionItems \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:29.015636+00:00
---

# Method: projects.locations.corpora.collections.viewCollectionItems  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora.collections/viewCollectionItems/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  Method: projects.locations.corpora.collections.viewCollectionItems Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



View items inside a collection.

### HTTP request

`GET https://visionai.googleapis.com/v1alpha1/{collection=projects/*/locations/*/corpora/*/collections/*}:viewCollectionItems`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`collection` |  `string` Required. The collection to view. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of collections to return. The service may return fewer than this value. If unspecified, at most 50 collections will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous `ViewCollectionItemsRequest` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ViewCollectionItemsRequest` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for collections.viewCollectionItems.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([CollectionItem](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/CollectionItem))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`items[]` |  `object (`[CollectionItem](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/CollectionItem)`)` The items from the specified collection.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
