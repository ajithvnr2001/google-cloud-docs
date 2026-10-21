---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/QueryTimeRange/
title: QueryTimeRange \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:41.470691+00:00
---

# QueryTimeRange  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/QueryTimeRange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  QueryTimeRange Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Period



A time range for which error group data shall be displayed. Query time ranges end at 'now'. When longer time ranges are selected, the resolution of the data decreases. The description of each time range below indicates the suggested minimum timed count duration for that range.

Requests might be rejected or the resulting timed count durations might be adjusted for lower durations.

JSON representation  
---  
      
    
    {
      "period": enum ([Period](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/QueryTimeRange#Period))
    }  
  
Fields  
---  
`period` |  `enum (`[Period](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/QueryTimeRange#Period)`)` Restricts the query to the specified time range.  
  
## Period

The supported time ranges.

Enums  
---  
`PERIOD_UNSPECIFIED` | Do not use.  
`PERIOD_1_HOUR` | Retrieve data for the last hour. Recommended minimum timed count duration: 1 min.  
`PERIOD_6_HOURS` | Retrieve data for the last 6 hours. Recommended minimum timed count duration: 10 min.  
`PERIOD_1_DAY` | Retrieve data for the last day. Recommended minimum timed count duration: 1 hour.  
`PERIOD_1_WEEK` | Retrieve data for the last week. Recommended minimum timed count duration: 6 hours.  
`PERIOD_30_DAYS` | Retrieve data for the last 30 days. Recommended minimum timed count duration: 1 day.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
