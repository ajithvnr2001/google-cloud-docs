---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery
title: Class AsyncQuery (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:32.195804+00:00
---

# Class AsyncQuery (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncQuery (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    AsyncQuery(
        parent,
        projection=None,
        field_filters=(),
        orders=(),
        limit=None,
        limit_to_last=False,
        offset=None,
        start_at=None,
        end_at=None,
        all_descendants=False,
        recursive=False,
    )

Represents a query to the Firestore API.

Instances of this class are considered immutable: all methods that would modify an instance instead return a new instance.

## Parameters  
  
---  
**Name** | **Description**  
`parent` |  `[CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)`   
The collection that this query applies to.  
`projection` |  `Optional[Projection]`   
A projection of document fields to limit the query results to.  
`field_filters` |  `Optional[Tuple[FieldFilter, ...]]`   
The filters to be applied in the query.  
`orders` |  `Optional[Tuple[Order, ...]]`   
The "order by" entries to use in the query.  
`limit` |  `Optional[int]`   
The maximum number of documents the query is allowed to return.  
`offset` |  `Optional[int]`   
The number of results to skip.  
`start_at` |  `Optional[Tuple[dict, bool]]`   
Two-tuple of : * a mapping of fields. Any field that is present in this mapping must also be present in `orders` * an `after` flag The fields and the flag combine to form a cursor used as a starting point in a query result set. If the `after` flag is :data:`True`, the results will start just after any documents which have fields matching the cursor, otherwise any matching documents will be included in the result set. When the query is formed, the document values will be used in the order given by `orders`.  
`end_at` |  `Optional[Tuple[dict, bool]]`   
Two-tuple of: * a mapping of fields. Any field that is present in this mapping must also be present in `orders` * a `before` flag The fields and the flag combine to form a cursor used as an ending point in a query result set. If the `before` flag is :data:`True`, the results will end just before any documents which have fields matching the cursor, otherwise any matching documents will be included in the result set. When the query is formed, the document values will be used in the order given by `orders`.  
`all_descendants` |  `Optional[bool]`   
When false, selects only collections that are immediate children of the `parent` specified in the containing `RunQueryRequest`. When true, selects all descendant collections.  
`recursive` |  `Optional[bool]`   
When true, returns all documents and all documents in any subcollections below them. Defaults to false.  
  
## Methods 

### avg
    
    
    avg(
        field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]

Adds an avg over the nested query.

**Parameters**  
---  
**Name** | **Description**  
`field_ref` |  `Union[str, [google.cloud.firestore_v1.field_path.FieldPath](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath)]`   
The field to aggregate across.  
`alias` |  `Optional[str]`   
Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format field_<incremental_id++>.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery)` | An instance of an AsyncAggregationQuery object  
  
### count
    
    
    count(
        alias: typing.Optional[str] = None,
    ) -> typing.Type[google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery]

Adds a count over the nested query.

**Parameter**  
---  
**Name** | **Description**  
`alias` |  `Optional[str]`   
Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format field_<incremental_id++>.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery)` | An instance of an AsyncAggregationQuery object  
  
### find_nearest
    
    
    find_nearest(
        vector_field: str,
        query_vector: Union[Vector, Sequence[float]],
        limit: int,
        distance_measure: DistanceMeasure,
        *,
        distance_result_field: Optional[str] = None,
        distance_threshold: Optional[float] = None
    ) -> AsyncVectorQuery

Finds the closest vector embeddings to the given query vector.

**Parameters**  
---  
**Name** | **Description**  
`vector_field` |  `str`   
An indexed vector field to search upon. Only documents which contain vectors whose dimensionality match the query_vector can be returned.  
`query_vector` |  `Vector Sequence[float]`   
The query vector that we are searching on. Must be a vector of no more than 2048 dimensions.  
`limit` |  `int`   
The number of nearest neighbors to return. Must be a positive integer of no more than 1000.  
`distance_measure` |  ``DistanceMeasure``   
The Distance Measure to use.  
`distance_result_field` |  `Optional[str]`   
Name of the field to output the result of the vector distance calculation. If unset then the distance will not be returned.  
`distance_threshold` |  `Optional[float]`   
A threshold for which no less similar documents will be returned.  
  
### get
    
    
    get(
        transaction: Optional[AsyncTransaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[DocumentSnapshot]

Read the documents in the collection that match this query.

This sends a `RunQuery` RPC and returns a list of documents returned in the stream of `RunQueryResponse` messages.

**Parameters**  
---  
**Name** | **Description**  
`retry` |  `Optional[google.api_core.retry.Retry]`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `Otional[float]`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime] If a `transaction` is used and it already has write operations added, this method cannot be used (i.e. read-after-write is not allowed).`   
If set, reads documents as they were at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. For the most accurate results, use UTC timezone.  
**Returns**  
---  
**Type** | **Description**  
`QueryResultsList[DocumentSnapshot]` | The documents in the collection that match this query.  
  
### stream
    
    
    stream(
        transaction: Optional[AsyncTransaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncStreamGenerator[DocumentSnapshot]

Read the documents in the collection that match this query.

This sends a `RunQuery` RPC and then returns a generator which consumes each document returned in the stream of `RunQueryResponse` messages.

**Note:** The underlying stream of responses will time out after the `max_rpc_timeout_millis` value set in the GAPIC client configuration for the `RunQuery` API. Snapshots not consumed from the iterator before that point will be lost. 

**Parameters**  
---  
**Name** | **Description**  
`transaction` |  `Optional[ Transaction]`   
An existing transaction that the query will run in.  
`retry` |  `Optional[google.api_core.retry.Retry]`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `Optional[float]`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. For the most accurate results, use UTC timezone.  
**Returns**  
---  
**Type** | **Description**  
``AsyncStreamGenerator[DocumentSnapshot]`` | An asynchronous generator of the queryresults.  
  
### sum
    
    
    sum(
        field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]

Adds a sum over the nested query.

**Parameters**  
---  
**Name** | **Description**  
`field_ref` |  `Union[str, [google.cloud.firestore_v1.field_path.FieldPath](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath)]`   
The field to aggregate across.  
`alias` |  `Optional[str]`   
Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format field_<incremental_id++>.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery)` | An instance of an AsyncAggregationQuery object  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
