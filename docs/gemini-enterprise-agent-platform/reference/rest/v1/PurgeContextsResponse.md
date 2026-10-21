---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PurgeContextsResponse/
title: PurgeContextsResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:18:49.101811+00:00
---

# PurgeContextsResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PurgeContextsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PurgeContextsResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[MetadataService.PurgeContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/purge#google.cloud.aiplatform.v1.MetadataService.PurgeContexts)`.

Fields  
  
`purgeCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of Contexts that this request deleted (or, if `force` is false, the number of Contexts that will be deleted). This can be an estimate. | `purgeSample[]` `string` A sample of the Context names that will be deleted. Only populated if `force` is set to false. The maximum number of samples is 100 (it is possible to return fewer). | JSON representation  
---  
      
    
    {
      "purgeCount": string,
      "purgeSample": [
        string
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
