---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.DiversificationLevel
title: Class DiversificationLevel (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:58.467249+00:00
---

# Class DiversificationLevel (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.DiversificationLevel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DiversificationLevel (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 
    
    
    DiversificationLevel(value)

Controls whether highly similar jobs are returned next to each other in the search results. Jobs are identified as highly similar based on their titles, job categories, and locations. Highly similar results are clustered so that only one representative job of the cluster is displayed to the job seeker higher up in the results, with the other jobs being displayed lower down in the results.

If you are using pageToken to page through the result set, latency might be lower but we can't guarantee that all results are returned. If you are using page offset, latency might be higher but all results are returned.

## Enums  
  
---  
**Name** | **Description**  
`DIVERSIFICATION_LEVEL_UNSPECIFIED` | The diversification level isn't specified.  
`DISABLED` | Disables diversification. Jobs that would normally be pushed to the last page would not have their positions altered. This may result in highly similar jobs appearing in sequence in the search results.  
`SIMPLE` | Default diversifying behavior. The result list is ordered so that highly similar results are pushed to the end of the last page of search results.  
`ONE_PER_COMPANY` | Only one job from the same company will be shown at once, other jobs under same company are pushed to the end of the last page of search result.  
`TWO_PER_COMPANY` | Similar to ONE_PER_COMPANY, but it allows at most two jobs in the same company to be shown at once, the other jobs under same company are pushed to the end of the last page of search result.  
`MAX_THREE_PER_COMPANY` | Similar to ONE_PER_COMPANY, but it allows at most three jobs in the same company to be shown at once, the other jobs under same company are dropped.  
`DIVERSIFY_BY_LOOSER_SIMILARITY` | The result list is ordered such that somewhat similar results are pushed to the end of the last page of the search results. This option is recommended if SIMPLE diversification does not diversify enough.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
