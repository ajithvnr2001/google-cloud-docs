---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/TimeGranularity/
title: TimeGranularity \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:43:03.016834+00:00
---

# TimeGranularity  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/TimeGranularity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  TimeGranularity Stay organized with collections  Save and categorize content based on your preferences. 

A time granularity divides the time line into discrete time periods. This is useful for defining buckets over which filtering and aggregation should be performed.

Enums  
---  
`TIME_GRANULARITY_UNSPECIFIED` | The time granularity is unspecified and will default to NONE.  
`NONE` | No time granularity. The response won't contain a time series. This is the default value if no time granularity is specified.  
`DAILY` | Data points in the time series will aggregate at a daily granularity. 1 day means [midnight to midnight).  
`HOURLY` | Data points in the time series will aggregate at a daily granularity. 1 HOUR means [01:00 to 02:00).  
`PER_MINUTE` | Data points in the time series will aggregate at a daily granularity. PER_MINUTE means [01:00 to 01:01).  
`PER_5_MINUTES` | Data points in the time series will aggregate at a 1 minute granularity. PER_5_MINUTES means [01:00 to 01:05).  
`MONTHLY` | Data points in the time series will aggregate at a monthly granularity. 1 MONTH means [01st of the month to 1st of the next month).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
