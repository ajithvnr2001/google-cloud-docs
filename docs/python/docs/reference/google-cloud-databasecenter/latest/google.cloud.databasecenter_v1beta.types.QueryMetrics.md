---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-databasecenter/latest/google.cloud.databasecenter_v1beta.types.QueryMetrics
title: Class QueryMetrics (0.9.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:27.670343+00:00
---

# Class QueryMetrics (0.9.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-databasecenter/latest/google.cloud.databasecenter_v1beta.types.QueryMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class QueryMetrics (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    QueryMetrics(mapping=None, *, ignore_unknown_fields=False, **kwargs)

QueryMetrics contains the metrics related to the query execution.

## Attributes  
  
---  
**Name** | **Description**  
`execution_count` |  `int`   
The number of times the query was executed.   
`avg_cpu_time` |  `google.protobuf.duration_pb2.Duration`   
The average execution period of the query across all runs.   
`total_cpu_time` |  `google.protobuf.duration_pb2.Duration`   
The total CPU time consumed by the query across all runs.   
`rows_processed` |  `int`   
The average number of rows processed by the query across all runs.   
`metrics_window` |  `[google.cloud.databasecenter_v1beta.types.QueryMetrics.MetricsWindow](https://docs.cloud.google.com/python/docs/reference/google-cloud-databasecenter/latest/google.cloud.databasecenter_v1beta.types.QueryMetrics.MetricsWindow)`   
The window over which the metrics are aggregated.   
  
## Classes 

### MetricsWindow
    
    
    MetricsWindow(value)

Enum to represent the window over which the metrics are aggregated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
