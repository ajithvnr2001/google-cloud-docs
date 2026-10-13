---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/QuotaMode/
title: QuotaMode \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:58.118090+00:00
---

# QuotaMode  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/QuotaMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  QuotaMode Stay organized with collections  Save and categorize content based on your preferences. 

Supported quota enforcement modes.

Enums  
---  
`ACQUIRE` | Decreases available quota by the cost specified for the operation. If cost is higher than available quota, operation fails and returns error.  
`ACQUIRE_BEST_EFFORT` | Decreases available quota by the cost specified for the operation. If cost is higher than available quota, operation does not fail and available quota goes down to zero but it returns error.  
`CHECK` | Does not change any available quota. Only checks if there is enough quota. No lock is placed on the checked tokens neither.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
