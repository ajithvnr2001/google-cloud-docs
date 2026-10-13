---
url: https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/OverrideInlineSource/
title: OverrideInlineSource \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:00.825668+00:00
---

# OverrideInlineSource  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/OverrideInlineSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage)
  * [ Reference ](https://docs.cloud.google.com/service-usage/docs/apis)



Send feedback 

#  OverrideInlineSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Import data embedded in the request message

JSON representation  
---  
      
    
    {
      "overrides": [
        {
          object ([QuotaOverride](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides#QuotaOverride))
        }
      ]
    }  
  
Fields  
---  
`overrides[]` |  `object (`[QuotaOverride](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides#QuotaOverride)`)` The overrides to create. Each override must have a value for 'metric' and 'unit', to specify which metric and which limit the override should be applied to. The 'name' field of the override does not need to be set; it is ignored.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-11 UTC."],[],[]] 
