---
url: https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.TimeSeries
title: Class TimeSeries (0.15.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:59.894491+00:00
---

# Class TimeSeries (0.15.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.TimeSeries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TimeSeries (0.15.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.2 (latest)  0.15.1  0.14.0  0.13.0  0.12.0  0.11.15  0.10.0  0.9.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.3  0.3.1  0.2.1  0.1.0 
    
    
    TimeSeries(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The metrics object for a SubTask.

## Attributes  
  
---  
**Name** | **Description**  
`metric` |  `str`   
Required. The name of the metric. If the metric is not known by the service yet, it will be auto-created.   
`value_type` |  `google.api.metric_pb2.ValueType`   
Required. The value type of the time series.   
`metric_kind` |  `google.api.metric_pb2.MetricKind`   
Optional. The metric kind of the time series. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`.   
`points` |  `MutableSequence[[google.cloud.bigquery_migration_v2.types.Point](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2.types.Point)]`   
Required. The data points of this time series. When listing time series, points are returned in reverse time order. When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
