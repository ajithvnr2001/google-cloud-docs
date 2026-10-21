---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Query/
title: google.appengine.datastore.datastore_query.Query \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:04:12.649413+00:00
---

# google.appengine.datastore.datastore_query.Query  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.Query Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1891-L2249) An immutable class that represents a query signature. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_query.Query(
        app=None,
        namespace=None,
        kind=None,
        ancestor=None,
        filter_predicate=None,
        group_by=None,
        order=None,
        read_time_us=None
    )
    

A query signature consists of a source of entities (specified as app, namespace and optionally kind and ancestor) as well as a FilterPredicate, grouping and a desired ordering. | 

## Args  
  
---  
  
`app` |  Optional app to query, derived from the environment if not specified.   
`namespace` |  Optional namespace to query, derived from the environment if not specified.   
`kind` |  Optional kind to query.   
`ancestor` |  Optional ancestor to query, an entity_pb2.Reference.   
`filter_predicate` |  Optional FilterPredicate by which to restrict the query.   
`group_by` |  Optional list of properties to group the results by.   
`order` |  Optional Order in which to return results.   
`read_time_us` |  Optional timestamp to read the storage from. Internal use only.   
  
## Raises  
  
---  
datastore_errors.BadArgumentError if any argument is invalid.   
  
## Attributes  
  
---  
  
`ancestor` |   
`app` |   
`filter_predicate` |   
`group_by` |   
`kind` |   
`namespace` |   
`order` |   
`read_time_us` |   
  
## Methods

### `run`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1855-L1868)
    
    
    run(
        conn, query_options=None
    )
    

Runs the query using provided datastore_rpc.Connection.

Args  
---  
  
`conn` |  The datastore_rpc.Connection to use   
`query_options` |  Optional query options to use   
  
Returns  
---  
A Batcher that implicitly fetches query results asynchronously.   
  
Raises  
---  
datastore_errors.BadArgumentError if any of the arguments are invalid.   
  
### `run_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2020-L2040)
    
    
    run_async(
        conn, query_options=None
    )
    

Runs the query using the provided datastore_rpc.Connection.

Args  
---  
  
`conn` |  the datastore_rpc.Connection on which to run the query.   
`query_options` |  Optional QueryOptions with which to run the query.   
  
Returns  
---  
An async object that can be used to grab the first Batch. Additional batches can be retrieved by calling Batch.next_batch/next_batch_async.   
  
Raises  
---  
datastore_errors.BadArgumentError if any of the arguments are invalid.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L81-L84)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L86-L90)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
