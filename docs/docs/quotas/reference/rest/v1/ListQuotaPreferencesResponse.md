---
url: https://docs.cloud.google.com/docs/quotas/reference/rest/v1/ListQuotaPreferencesResponse/
title: ListQuotaPreferencesResponse \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:10.912514+00:00
---

# ListQuotaPreferencesResponse  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/rest/v1/ListQuotaPreferencesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  ListQuotaPreferencesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Message for response to listing QuotaPreferences

JSON representation  
---  
      
    
    {
      "quotaPreferences": [
        {
          object ([QuotaPreference](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences#QuotaPreference))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`quotaPreferences[]` |  `object (`[QuotaPreference](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences#QuotaPreference)`)` The list of QuotaPreference  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
