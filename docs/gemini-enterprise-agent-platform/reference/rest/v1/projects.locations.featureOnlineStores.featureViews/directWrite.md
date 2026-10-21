---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite/
title: Method: featureViews.directWrite \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:31.620009+00:00
---

# Method: featureViews.directWrite  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featureViews.directWrite Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featureOnlineStores.featureViews.directWrite

Bidirectional streaming RPC to directly write to feature values in a feature view. Requests may not have a one-to-one mapping to responses and responses may be returned out-of-order to reduce latency.

### Endpoint

post  `https://{service-endpoint}/v1/{featureView}:directWrite`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`featureView` `string` FeatureView resource format `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}`

### Request body

The request body contains data with the following structure: | Fields  
  
`dataKeyAndFeatureValues[]` `object (`[DataKeyAndFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#DataKeyAndFeatureValues)`)` Required. The data keys and associated feature values.

### Response body

Response message for `[FeatureOnlineStoreService.FeatureViewDirectWrite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#google.cloud.aiplatform.v1.FeatureOnlineStoreService.FeatureViewDirectWrite)`. If successful, the response body contains data with the following structure: | Fields  
  
`status` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Response status for the keys listed in `[FeatureViewDirectWriteResponse.write_responses](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#body.FeatureViewDirectWriteResponse.FIELDS.write_responses)`.The error only applies to the listed data keys - the stream will remain open for further [FeatureOnlineStoreService.FeatureViewDirectWriteRequest][] requests.Partial failures (e.g. if the first 10 keys of a request fail, but the rest succeed) from a single request may result in multiple responses - there will be one response for the successful request keys and one response for the failing request keys. | `writeResponses[]` `object (`[WriteResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#WriteResponse)`)` Details about write for each key. If status is not OK, `[WriteResponse.data_key](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#WriteResponse.FIELDS.data_key)` will have the key with error, but `[WriteResponse.online_store_write_time](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#WriteResponse.FIELDS.online_store_write_time)` will not be present. | JSON representation  
---  
      
    
    {
      "status": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "writeResponses": [
        {
          object ([WriteResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#WriteResponse))
        }
      ]
    }  
  
## DataKeyAndFeatureValues

A data key and associated feature values to write to the feature view.

Fields  
  
`dataKey` `object (`[FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey)`)` The data key. | `features[]` `object (`[Feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#Feature)`)` List of features to write. | JSON representation  
---  
      
    
    {
      "dataKey": {
        object ([FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey))
      },
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#Feature))
        }
      ]
    }  
  
## Feature

feature name & value pair.

Fields  
  
`name` `string` feature short name. | `data_oneof` `Union type`  
  
Feature value data to write. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`value` `object (`[FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue)`)` feature value. A user provided timestamp may be set in the `FeatureValue.metadata.generate_time` field. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
    
      // data_oneof
      "value": {
        object ([FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue))
      }
      // Union type
    }  
  
## WriteResponse

Details about the write for each key.

Fields  
  
`dataKey` `object (`[FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey)`)` What key is this write response associated with. | `onlineStoreWriteTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the feature values were written to the online store. If `[FeatureViewDirectWriteResponse.status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/directWrite#body.FeatureViewDirectWriteResponse.FIELDS.status)` is not OK, this field is not populated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | JSON representation  
---  
      
    
    {
      "dataKey": {
        object ([FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey))
      },
      "onlineStoreWriteTime": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
