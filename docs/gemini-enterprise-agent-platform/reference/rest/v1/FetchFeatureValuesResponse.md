---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FetchFeatureValuesResponse/
title: FetchFeatureValuesResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:47:53.241058+00:00
---

# FetchFeatureValuesResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FetchFeatureValuesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  FetchFeatureValuesResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[FeatureOnlineStoreService.FetchFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/fetchFeatureValues#google.cloud.aiplatform.v1.FeatureOnlineStoreService.FetchFeatureValues)`

Fields  
  
`dataKey` `object (`[FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey)`)` The data key associated with this response. Will only be populated for [FeatureOnlineStoreService.StreamingFetchFeatureValues][] RPCs. | `format` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`keyValues` `object (`[FeatureNameValuePairList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FetchFeatureValuesResponse#FeatureNameValuePairList)`)` feature values in keyvalue format. | `protoStruct` `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` feature values in proto Struct format. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "dataKey": {
        object ([FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey))
      },
    
      // format
      "keyValues": {
        object ([FeatureNameValuePairList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FetchFeatureValuesResponse#FeatureNameValuePairList))
      },
      "protoStruct": {
        object
      }
      // Union type
    }  
  
## FeatureNameValuePairList

Response structure in the format of key (feature name) and (feature) value pair.

Fields  
  
`features[]` `object (`[FeatureNameValuePair](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FetchFeatureValuesResponse#FeatureNameValuePair)`)` List of feature names and values. | JSON representation  
---  
      
    
    {
      "features": [
        {
          object ([FeatureNameValuePair](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FetchFeatureValuesResponse#FeatureNameValuePair))
        }
      ]
    }  
  
## FeatureNameValuePair

feature name & value pair.

Fields  
  
`name` `string` feature short name. | `data` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`value` `object (`[FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue)`)` feature value. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
    
      // data
      "value": {
        object ([FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue))
      }
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
