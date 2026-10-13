---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery
title: Class BaseAggregationQuery (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:40.114908+00:00
---

# Class BaseAggregationQuery (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BaseAggregationQuery (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    BaseAggregationQuery(nested_query, alias: typing.Optional[str] = None)

Represents an aggregation query to the Firestore API.

## Methods 

### add_aggregation
    
    
    add_aggregation(
        aggregation: google.cloud.firestore_v1.base_aggregation.BaseAggregation,
    ) -> None

Adds an aggregation operation to the nested query

**Parameter**  
---  
**Name** | **Description**  
`aggregation` |  `BaseAggregation`   
An aggregation operation, e.g. a CountAggregation  
  
### add_aggregations
    
    
    add_aggregations(
        aggregations: typing.List[
            google.cloud.firestore_v1.base_aggregation.BaseAggregation
        ],
    ) -> None

Adds a list of aggregations to the nested query

**Parameter**  
---  
**Name** | **Description**  
`aggregations` |  `list`   
a list of aggregation operations  
  
### avg
    
    
    avg(
        field_ref: str | google.cloud.firestore_v1.field_path.FieldPath,
        alias: typing.Optional[str] = None,
    )

Adds an avg over the nested query

### count
    
    
    count(alias: typing.Optional[str] = None)

Adds a count over the nested query

### get
    
    
    get(
        transaction=None,
        retry: Union[
            retries.Retry, retries.AsyncRetry, None, object
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> (
        QueryResultsList[AggregationResult]
        | Coroutine[Any, Any, List[List[AggregationResult]]]
    )

Runs the aggregation query.

This sends a `RunAggregationQuery` RPC and returns a list of aggregation results in the stream of `RunAggregationQueryResponse` messages.

**Parameters**  
---  
**Name** | **Description**  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
`(QueryResultsList[List[AggregationResult]] Coroutine[Any, Any, List[List[AggregationResult]]])` | The aggregation query results.  
  
### stream
    
    
    stream(
        transaction: Optional[transaction.Transaction] = None,
        retry: (
            retries.Retry | retries.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> (
        StreamGenerator[List[AggregationResult]]
        | AsyncStreamGenerator[List[AggregationResult]]
    )

Runs the aggregation query.

This sends a`RunAggregationQuery` RPC and returns a generator in the stream of `RunAggregationQueryResponse` messages.

**Parameters**  
---  
**Name** | **Description**  
`retry` |  `Optional[google.api_core.retry.Retry]`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `Optinal[float]`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
`StreamGenerator[List[AggregationResult]] AsyncStreamGenerator[List[AggregationResult]]` | A generator of the query results.  
  
### sum
    
    
    sum(
        field_ref: str | google.cloud.firestore_v1.field_path.FieldPath,
        alias: typing.Optional[str] = None,
    )

Adds a sum over the nested query

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
