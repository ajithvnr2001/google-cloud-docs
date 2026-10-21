---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/EnterpriseWebSearch/
title: EnterpriseWebSearch \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:10.743008+00:00
---

# EnterpriseWebSearch  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/EnterpriseWebSearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  EnterpriseWebSearch Stay organized with collections  Save and categorize content based on your preferences. 

Tool to search public web data, powered by Agent Platform Search and Sec4 compliance.

Fields  
  
`excludeDomains[]` `string` Optional. List of domains to be excluded from the search results. The default limit is 2000 domains. | `blockingConfidence` `enum (`[PhishBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PhishBlockThreshold)`)` Optional. Sites with confidence level chosen & above this value will be blocked from the search results. | JSON representation  
---  
      
    
    {
      "excludeDomains": [
        string
      ],
      "blockingConfidence": enum ([PhishBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PhishBlockThreshold))
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
