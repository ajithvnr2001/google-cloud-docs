---
url: https://docs.cloud.google.com/datastore/docs/reference/admin/rest/Shared.Types/Progress/
title: Progress \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:54.070217+00:00
---

# Progress  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/reference/admin/rest/Shared.Types/Progress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Reference ](https://docs.cloud.google.com/datastore/docs/apis)



Send feedback 

#  Progress Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Measures the progress of a particular metric.

JSON representation  
---  
      
    
    {
      "workCompleted": string,
      "workEstimated": string
    }  
  
Fields  
---  
`workCompleted` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The amount of work that has been completed. Note that this may be greater than workEstimated.  
`workEstimated` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An estimate of how much work needs to be performed. May be zero if the work estimate is unavailable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
