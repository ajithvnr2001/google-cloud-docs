---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation
title: Class Aggregation (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:50.960406+00:00
---

# Class Aggregation (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Aggregation (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    Aggregation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines an aggregation that produces a single result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`count` |  `[google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Count](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Count)`   
Count aggregator. This field is a member of `oneof`_ `operator`.   
`sum` |  `[google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Sum](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Sum)`   
Sum aggregator. This field is a member of `oneof`_ `operator`.   
`avg` |  `[google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Avg](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Avg)`   
Average aggregator. This field is a member of `oneof`_ `operator`.   
`alias` |  `str`   
Optional. Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format `field_`. For example: :: AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); becomes: :: AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS field_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS field_2 OVER ( ... ); Requires: \- Must be unique across all aggregation aliases. \- Conform to [document field name][google.firestore.v1.Document.fields] limitations.   
  
## Classes 

### Avg
    
    
    Avg(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Average of the values of the requested field.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns `NULL`.

  * Always returns the result as a double.




### Count
    
    
    Count(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Count of documents that match the query.

The `COUNT(*)` aggregation function operates on the entire document so it does not require a field reference.

### Sum
    
    
    Sum(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Sum of the values of the requested field.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns 0.

  * Returns a 64-bit integer if all aggregated numbers are integers and the sum result does not overflow. Otherwise, the result is returned as a double. Note that even if all the aggregated values are integers, the result is returned as a double if it cannot fit within a 64-bit signed integer. When this occurs, the returned value will lose precision.

  * When underflow occurs, floating-point aggregation is non-deterministic. This means that running the same query repeatedly without any changes to the underlying values could produce slightly different results each time. In those cases, values should be stored as integers over floating-point numbers.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
