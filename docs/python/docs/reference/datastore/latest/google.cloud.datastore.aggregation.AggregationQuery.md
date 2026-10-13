---
url: https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.aggregation.AggregationQuery
title: Class AggregationQuery (2.27.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:54.210605+00:00
---

# Class AggregationQuery (2.27.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.aggregation.AggregationQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AggregationQuery (2.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.27.0 (latest)  2.26.1  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.2  2.14.0  2.13.2  2.12.0  2.11.1  2.10.0  2.9.0  2.8.3  2.7.2  2.6.2  2.5.1  2.4.0  2.3.0  2.2.0  2.1.6  2.0.1  1.15.5  1.14.0  1.13.2  1.12.0  1.11.0  1.10.0  1.9.0 
    
    
    AggregationQuery(client, query, explain_options=None)

An Aggregation query against the Cloud Datastore.

This class serves as an abstraction for creating aggregations over query in the Cloud Datastore.

## Parameters  
  
---  
**Name** | **Description**  
`client` |  `[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client)`   
The client used to connect to Datastore.  
`query` |  `[Query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.Query)`   
The query used for aggregations.  
`explain_options` |  `ExplainOptions`   
(Optional) Options to enable query profiling for this query. When set, explain_metrics will be available on the iterator returned by query.fetch(). If not passed, will use value from given query.  
  
## Properties 

### namespace

The nested query's namespace

**Returns**  
---  
**Type** | **Description**  
`str or None` | the namespace assigned to this query  
  
### project

Get the project for this AggregationQuery.

**Returns**  
---  
**Type** | **Description**  
`str` | The project for the query.  
  
## Methods 

### add_aggregation
    
    
    add_aggregation(aggregation)

Adds an aggregation operation to the nested query

**Parameter**  
---  
**Name** | **Description**  
`aggregation` |  `[BaseAggregation](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.aggregation.BaseAggregation)`   
An aggregation operation, e.g. a CountAggregation  
  
### add_aggregations
    
    
    add_aggregations(aggregations)

Adds a list of aggregations to the nested query

**Parameter**  
---  
**Name** | **Description**  
`aggregations` |  `list`   
a list of aggregation operations  
  
### avg
    
    
    avg(property_ref, alias=None)

Adds a avg over the nested query

**Parameter**  
---  
**Name** | **Description**  
`property_ref` |  `str`   
The property_ref for the sum  
  
### count
    
    
    count(alias=None)

Adds a count over the nested query

**Parameter**  
---  
**Name** | **Description**  
`alias` |  `str`   
(Optional) The alias for the count  
  
### fetch
    
    
    fetch(
        client=None, limit=None, eventual=False, retry=None, timeout=None, read_time=None
    )

Execute the Aggregation Query; return an iterator for the aggregation results.

For example:

.. testsetup:: aggregation-query-fetch
    
    
    import uuid
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    unique = str(uuid.uuid4())[0:8]
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)(namespace='ns{}'.format(unique))
    

.. doctest:: aggregation-query-fetch
    
    
    >>> andy = datastore.Entity(client.key('Person', 1234))
    >>> andy['name'] = 'Andy'
    >>> sally = datastore.Entity(client.key('Person', 2345))
    >>> sally['name'] = 'Sally'
    >>> bobby = datastore.Entity(client.key('Person', 3456))
    >>> bobby['name'] = 'Bobby'
    >>> client.put_multi([andy, sally, bobby])
    >>> query = client.query(kind='Andy')
    >>> aggregation_query = client.aggregation_query(query)
    >>> result = aggregation_query.count(alias="total").fetch(limit=5)
    >>> result
    <<xref uid="google.cloud.datastore.aggregation.AggregationResultIterator">google.cloud.datastore.aggregation.AggregationResultIterator</xref> object at ...>
    

.. testcleanup:: aggregation-query-fetch
    
    
    client.delete(andy.key)
    

**Parameters**  
---  
**Name** | **Description**  
`client` |  `[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client)`   
(Optional) client used to connect to datastore. If not supplied, uses the query's value.  
`eventual` |  `bool`   
(Optional) Defaults to strongly consistent (False). Setting True will use eventual consistency, but cannot be used inside a transaction or with read_time, otherwise will raise ValueError.  
`retry` |  ``google.api_core.retry.Retry``   
A retry object used to retry requests. If `None` is specified, requests will be retried using a default configuration.  
`timeout` |  `float`   
Time, in seconds, to wait for the request to complete. Note that if `retry` is specified, the timeout applies to each individual attempt.  
`read_time` |  `datetime`   
(Optional) use read_time read consistency, cannot be used inside a transaction or with eventual consistency, or will raise ValueError.  
**Returns**  
---  
**Type** | **Description**  
``AggregationIterator`` | The iterator for the aggregation query.  
  
### sum
    
    
    sum(property_ref, alias=None)

Adds a sum over the nested query

**Parameter**  
---  
**Name** | **Description**  
`property_ref` |  `str`   
The property_ref for the sum  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
