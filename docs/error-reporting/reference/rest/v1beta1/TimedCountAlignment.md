---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/TimedCountAlignment/
title: TimedCountAlignment \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:42.093220+00:00
---

# TimedCountAlignment  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/TimedCountAlignment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  TimedCountAlignment Stay organized with collections  Save and categorize content based on your preferences. 

Specifies how the time periods of error group counts are aligned.

Enums  
---  
`ERROR_COUNT_ALIGNMENT_UNSPECIFIED` | No alignment specified.  
`ALIGNMENT_EQUAL_ROUNDED` | The time periods shall be consecutive, have width equal to the requested duration, and be aligned at the `[alignmentTime](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list#body.QUERY_PARAMETERS.alignment_time)` provided in the request.The `[alignmentTime](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list#body.QUERY_PARAMETERS.alignment_time)` does not have to be inside the query period but even if it is outside, only time periods are returned which overlap with the query period.A rounded alignment will typically result in a different size of the first or the last time period.  
`ALIGNMENT_EQUAL_AT_END` | The time periods shall be consecutive, have width equal to the requested duration, and be aligned at the end of the requested time period. This can result in a different size of the first time period.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
