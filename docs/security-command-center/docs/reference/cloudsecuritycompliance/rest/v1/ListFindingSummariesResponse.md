---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/ListFindingSummariesResponse/
title: ListFindingSummariesResponse \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:50.658618+00:00
---

# ListFindingSummariesResponse  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/ListFindingSummariesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  ListFindingSummariesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for [ListFindingSummaries][].

JSON representation  
---  
      
    
    {
      "findingSummaries": [
        {
          object ([FindingSummary](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.findingSummaries#FindingSummary))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`findingSummaries[]` |  `object (`[FindingSummary](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.findingSummaries#FindingSummary)`)` List of finding summary by category.  
`nextPageToken` |  `string` Output only. The token to retrieve the next page of results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-07 UTC."],[],[]] 
