---
url: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.SqlCondition.Daily
title: Class Daily (2.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:58.421103+00:00
---

# Class Daily (2.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.SqlCondition.Daily

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Daily (2.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.32.0 (latest)  2.31.0  2.30.0  2.29.1  2.28.0  2.27.2  2.26.0  2.25.0  2.24.0  2.23.1  2.22.2  2.21.0  2.20.0  2.19.4  2.18.0  2.17.0  2.16.0  2.15.1  2.14.2  2.13.0  2.12.0  2.11.3  2.10.1  2.9.2  2.8.0  2.7.0  2.6.0  2.5.2  2.4.2  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.36.2  0.35.0  0.34.0  0.33.0  0.32.0 
    
    
    Daily(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Used to schedule the query to run every so many days.

## Attributes  
  
---  
**Name** | **Description**  
`periodicity` |  `int`   
Required. The number of days between runs. Must be greater than or equal to 1 day and less than or equal to 31 days.   
`execution_time` |  `google.type.timeofday_pb2.TimeOfDay`   
Optional. The time of day (in UTC) at which the query should run. If left unspecified, the server picks an arbitrary time of day and runs the query at the same time each day.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
