---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3/SearchTargetPolicyBindingsResponse/
title: SearchTargetPolicyBindingsResponse \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:28.191100+00:00
---

# SearchTargetPolicyBindingsResponse  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3/SearchTargetPolicyBindingsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  SearchTargetPolicyBindingsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for SearchTargetPolicyBindings method.

JSON representation  
---  
      
    
    {
      "policyBindings": [
        {
          object ([PolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`policyBindings[]` |  `object (`[PolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding)`)` The policy bindings bound to the specified target.  
`nextPageToken` |  `string` Optional. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
