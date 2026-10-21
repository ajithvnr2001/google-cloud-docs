---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/streamingFetchFeatureValues/
title: Method: featureViews.streamingFetchFeatureValues \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:31:47.697215+00:00
---

# Method: featureViews.streamingFetchFeatureValues  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/streamingFetchFeatureValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featureViews.streamingFetchFeatureValues Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featureOnlineStores.featureViews.streamingFetchFeatureValues

Bidirectional streaming RPC to fetch feature values under a FeatureView. Requests may not have a one-to-one mapping to responses and responses may be returned out-of-order to reduce latency.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{featureView}:streamingFetchFeatureValues`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`featureView` `string` Required. FeatureView resource format `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}`

### Request body

The request body contains data with the following structure: | Fields  
  
`dataKeys[]` `object (`[FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataKey)`)` | `dataFormat` `enum (`[FeatureViewDataFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataFormat)`)` Specify response data format. If not set, keyvalue format will be used.

### Response body

Response message for `[FeatureOnlineStoreService.StreamingFetchFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/streamingFetchFeatureValues#google.cloud.aiplatform.v1beta1.FeatureOnlineStoreService.StreamingFetchFeatureValues)`. If successful, the response body contains data with the following structure: | Fields  
  
`status` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Response status. If OK, then `[StreamingFetchFeatureValuesResponse.data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/streamingFetchFeatureValues#body.StreamingFetchFeatureValuesResponse.FIELDS.data)` will be populated. Otherwise `[StreamingFetchFeatureValuesResponse.data_keys_with_error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/streamingFetchFeatureValues#body.StreamingFetchFeatureValuesResponse.FIELDS.data_keys_with_error)` will be populated with the appropriate data keys. The error only applies to the listed data keys - the stream will remain open for further [FeatureOnlineStoreService.StreamingFetchFeatureValuesRequest][] requests. | `data[]` `object (`[FetchFeatureValuesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FetchFeatureValuesResponse)`)` | `dataKeysWithError[]` `object (`[FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataKey)`)` | JSON representation  
---  
      
    
    {
      "status": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "data": [
        {
          object ([FetchFeatureValuesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FetchFeatureValuesResponse))
        }
      ],
      "dataKeysWithError": [
        {
          object ([FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataKey))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
