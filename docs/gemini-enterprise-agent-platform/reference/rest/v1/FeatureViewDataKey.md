---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey/
title: FeatureViewDataKey \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:04:04.224057+00:00
---

# FeatureViewDataKey  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  FeatureViewDataKey Stay organized with collections  Save and categorize content based on your preferences. 

Lookup key for a feature view.

Fields  
  
`key_oneof` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`key` `string` String key to use for lookup. | `compositeKey` `object (`[CompositeKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey#CompositeKey)`)` The actual Entity id will be composed from this struct. This should match with the way id is defined in the FeatureView spec. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // key_oneof
      "key": string,
      "compositeKey": {
        object ([CompositeKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureViewDataKey#CompositeKey))
      }
      // Union type
    }  
  
## CompositeKey

id that is comprised from several parts (columns).

Fields  
  
`parts[]` `string` Parts to construct Entity id. Should match with the same id columns as defined in FeatureView in the same order. | JSON representation  
---  
      
    
    {
      "parts": [
        string
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
