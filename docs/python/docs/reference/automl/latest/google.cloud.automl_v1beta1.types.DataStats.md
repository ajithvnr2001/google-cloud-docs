---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DataStats
title: Class DataStats (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:46.312480+00:00
---

# Class DataStats (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DataStats

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataStats (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    DataStats(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The data statistics of a series of values that share the same DataType.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`float64_stats` |  `[google.cloud.automl_v1beta1.types.Float64Stats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Float64Stats)`   
The statistics for FLOAT64 DataType. This field is a member of `oneof`_ `stats`.   
`string_stats` |  `[google.cloud.automl_v1beta1.types.StringStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StringStats)`   
The statistics for STRING DataType. This field is a member of `oneof`_ `stats`.   
`timestamp_stats` |  `[google.cloud.automl_v1beta1.types.TimestampStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TimestampStats)`   
The statistics for TIMESTAMP DataType. This field is a member of `oneof`_ `stats`.   
`array_stats` |  `[google.cloud.automl_v1beta1.types.ArrayStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ArrayStats)`   
The statistics for ARRAY DataType. This field is a member of `oneof`_ `stats`.   
`struct_stats` |  `[google.cloud.automl_v1beta1.types.StructStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StructStats)`   
The statistics for STRUCT DataType. This field is a member of `oneof`_ `stats`.   
`category_stats` |  `[google.cloud.automl_v1beta1.types.CategoryStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CategoryStats)`   
The statistics for CATEGORY DataType. This field is a member of `oneof`_ `stats`.   
`distinct_value_count` |  `int`   
The number of distinct values.   
`null_value_count` |  `int`   
The number of values that are null.   
`valid_value_count` |  `int`   
The number of values that are valid.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
