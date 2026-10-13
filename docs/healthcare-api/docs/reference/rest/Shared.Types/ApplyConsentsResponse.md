---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ApplyConsentsResponse/
title: ApplyConsentsResponse \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:42.407962+00:00
---

# ApplyConsentsResponse  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ApplyConsentsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  ApplyConsentsResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response when all Consent resources in scope were processed and all affected resources were reindexed successfully. This structure is included in the `[response](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.response)` when the operation finishes successfully.

JSON representation  
---  
      
    
    {
      "consentApplySuccess": string,
      "consentApplyFailure": string,
      "affectedResources": string,
      "failedResources": string
    }  
  
Fields  
---  
`consentApplySuccess` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` If `validateOnly = false` in `ApplyConsentsRequest`, this counter is the number of Consent resources that were successfully applied. Otherwise, it is the number of Consent resources that are supported.  
`consentApplyFailure` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` If `validateOnly = false` in `ApplyConsentsRequest`, this counter is the number of Consent resources that were failed to apply. Otherwise, it is the number of Consent resources that are not supported or invalid.  
`affectedResources` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of resources (including the Consent resources) that may have consensual access change.  
`failedResources` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of resources (including the Consent resources) that [ApplyConsents][] failed to re-index.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
