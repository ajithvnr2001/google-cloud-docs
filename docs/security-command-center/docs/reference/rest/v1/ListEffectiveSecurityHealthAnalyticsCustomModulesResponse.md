---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListEffectiveSecurityHealthAnalyticsCustomModulesResponse/
title: ListEffectiveSecurityHealthAnalyticsCustomModulesResponse \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:11.365624+00:00
---

# ListEffectiveSecurityHealthAnalyticsCustomModulesResponse  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListEffectiveSecurityHealthAnalyticsCustomModulesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  ListEffectiveSecurityHealthAnalyticsCustomModulesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for listing effective Security Health Analytics custom modules.

JSON representation  
---  
      
    
    {
      "effectiveSecurityHealthAnalyticsCustomModules": [
        {
          object ([EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/folders.securityHealthAnalyticsSettings.effectiveCustomModules#EffectiveSecurityHealthAnalyticsCustomModule))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`effectiveSecurityHealthAnalyticsCustomModules[]` |  `object (`[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/folders.securityHealthAnalyticsSettings.effectiveCustomModules#EffectiveSecurityHealthAnalyticsCustomModule)`)` Effective custom modules belonging to the requested parent.  
`nextPageToken` |  `string` If not empty, indicates that there may be more effective custom modules to be returned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
