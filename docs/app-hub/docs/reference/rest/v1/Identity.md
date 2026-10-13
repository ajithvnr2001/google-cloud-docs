---
url: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Identity/
title: Identity \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:01.538200+00:00
---

# Identity  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Reference ](https://docs.cloud.google.com/app-hub/docs/apis)



Send feedback 

#  Identity Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The identity associated with a service or workload.

JSON representation  
---  
      
    
    {
      "principal": string
    }  
  
Fields  
---  
`principal` |  `string` Output only. The principal of the identity.Supported formats:

  * `sa://my-sa@PROJECT_ID.iam.gserviceaccount.com` for GCP Service Account
  * `principal://POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID` for Managed Workload Identity

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-19 UTC."],[],[]] 
