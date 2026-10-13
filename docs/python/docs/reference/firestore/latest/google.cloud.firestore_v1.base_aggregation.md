---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation
title: Module base_aggregation (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:32.621249+00:00
---

# Module base_aggregation (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module base_aggregation (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

Classes for representing aggregation queries for the Google Cloud Firestore API.

A [AggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation.AggregationQuery) can be created directly from a Collection and that can be a more common way to create an aggregation query than direct usage of the constructor.

## Classes 

### [AggregationResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.AggregationResult)
    
    
    AggregationResult(alias: str, value: float, read_time=None)

A class representing result from Aggregation Query

**Parameters**  
---  
**Name** | **Description**  
`alias` |  `str`   
The alias for the aggregation.  
`value` |  `int`   
The resulting read_time  
  
### [AvgAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.AvgAggregation)
    
    
    AvgAggregation(
        field_ref: str | google.cloud.firestore_v1.field_path.FieldPath,
        alias: typing.Optional[str] = None,
    )

Helper class that provides a standard way to create an ABC using inheritance.

### [BaseAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregation)
    
    
    BaseAggregation(alias: typing.Optional[str] = None)

Helper class that provides a standard way to create an ABC using inheritance.

### [BaseAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery)
    
    
    BaseAggregationQuery(nested_query, alias: typing.Optional[str] = None)

Represents an aggregation query to the Firestore API.

### [CountAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.CountAggregation)
    
    
    CountAggregation(alias: typing.Optional[str] = None)

Helper class that provides a standard way to create an ABC using inheritance.

### [SumAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.SumAggregation)
    
    
    SumAggregation(
        field_ref: str | google.cloud.firestore_v1.field_path.FieldPath,
        alias: typing.Optional[str] = None,
    )

Helper class that provides a standard way to create an ABC using inheritance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
