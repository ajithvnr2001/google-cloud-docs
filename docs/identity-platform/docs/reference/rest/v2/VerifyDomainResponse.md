---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/VerifyDomainResponse/
title: VerifyDomainResponse \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:18.417590+00:00
---

# VerifyDomainResponse  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/VerifyDomainResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  VerifyDomainResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response for VerifyDomain request.

JSON representation  
---  
      
    
    {
      "verificationState": enum ([VerificationState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/VerificationState)),
      "verificationError": string
    }  
  
Fields  
---  
`verificationState` |  `enum (`[VerificationState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/VerificationState)`)` The resulting state for the given domain after this request is processed.  
`verificationError` |  `string` When applicable, a textual explanation for why the domain wasn't enable to be verified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
