---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/QueryMode/
title: QueryMode \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:20.411486+00:00
---

# QueryMode  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/QueryMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  QueryMode Stay organized with collections  Save and categorize content based on your preferences. 

Mode in which the statement must be processed.

Enums  
---  
`NORMAL` | The default mode. Only the statement results are returned.  
`PLAN` | This mode returns only the query plan, without any results or execution statistics information.  
`PROFILE` | This mode returns the query plan, overall execution statistics, operator level execution statistics along with the results. This has a performance overhead compared to the other modes. It isn't recommended to use this mode for production traffic.  
`WITH_STATS` | This mode returns the overall (but not operator-level) execution statistics along with the results.  
`WITH_PLAN_AND_STATS` | This mode returns the query plan, overall (but not operator-level) execution statistics along with the results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
