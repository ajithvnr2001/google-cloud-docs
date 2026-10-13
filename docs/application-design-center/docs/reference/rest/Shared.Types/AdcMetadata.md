---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AdcMetadata/
title: AdcMetadata \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:36.981788+00:00
---

# AdcMetadata  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AdcMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  AdcMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Application Design Center specific information and metadata.

JSON representation  
---  
      
    
    {
    
      // Union field app_uri can be only one of the following:
      "applicationUri": string,
      "applicationTemplateUri": string,
      "spaceUri": string
      // End of list of possible types for union field app_uri.
    }  
  
Fields  
---  
Union field `app_uri`. Application or ApplicationTemplate URI `app_uri` can be only one of the following:  
`applicationUri` |  `string` Output only. Application URI  
`applicationTemplateUri` |  `string` Output only. ApplicationTemplate URI  
`spaceUri` |  `string` Output only. Space URI  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
