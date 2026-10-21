---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Query/
title: google.appengine.ext.ndb.Query \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:05:26.267566+00:00
---

# google.appengine.ext.ndb.Query  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Query Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L819-L1552) Query object. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Query(
        kind=None,
        ancestor=None,
        filters=None,
        orders=None,
        app=None,
        namespace=None,
        default_options=None,
        projection=None,
        group_by=None
    )
    

Usually constructed by calling Model.query(). See module docstring for examples. Note that not all operations on Queries are supported by _MultiQuery instances; the latter are generated as necessary when any of the operators !=, IN or OR is used. | 

## Args  
  
---  
  
`kind` |  Optional kind string.   
`ancestor` |  Optional ancestor Key.   
`filters` |  Optional Node representing a filter expression tree.   
`orders` |  Optional datastore_query.Order object.   
`app` |  Optional app id.   
`namespace` |  Optional namespace.   
`default_options` |  Optional QueryOptions object.   
`projection` |  Optional list or tuple of properties to project.   
`group_by` |  Optional list or tuple of properties to group by.   
  
## Attributes  
  
---  
  
`ancestor` |  Accessor for the ancestor (a Key or None).   
`app` |  Accessor for the app (a string or None).   
`default_options` |  Accessor for the default_options (a QueryOptions instance or None).   
`filters` |  Accessor for the filters (a Node or None).   
`group_by` |  Accessor for the group by properties (a tuple instance or None).   
`is_distinct` |  True if results are guaranteed to contain a unique set of property values. This happens when every property in the group_by is also in the projection.   
`kind` |  Accessor for the kind (a string or None).   
`namespace` |  Accessor for the namespace (a string or None).   
`orders` |  Accessor for the filters (a datastore_query.Order or None).   
`projection` |  Accessor for the projected properties (a tuple instance or None).   
  
## Methods

### `analyze`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1501-L1522)
    
    
    analyze()
    

Return a list giving the parameters required by a query.

### `bind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1524-L1526)
    
    
    bind(
        *args, **kwds
    )
    

Bind parameter values. Returns a new Query object.

### `count`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1319-L1335)
    
    
    count(
        limit=None, **q_options
    )
    

Count the number of query results, up to a limit.

This returns the same result as len(q.fetch(limit)) but more efficiently.

Note that you must pass a maximum value to limit the amount of work done by the query.

Args  
---  
  
`limit` |  How many results to count at most.   
`**q_options` |  All query options keyword arguments are supported.   
  
Returns:

### `count_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1337-L1344)
    
    
    count_async(
        limit=None, **q_options
    )
    

Count the number of query results, up to a limit.

This is the asynchronous version of Query.count().

### `fetch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1255-L1266)
    
    
    fetch(
        limit=None, **q_options
    )
    

Fetch a list of query results, up to a limit.

Args  
---  
  
`limit` |  How many results to retrieve at most.   
`**q_options` |  All query options keyword arguments are supported.   
  
Returns  
---  
A list of results.   
  
### `fetch_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1268-L1287)
    
    
    fetch_async(
        limit=None, **q_options
    )
    

Fetch a list of query results, up to a limit.

This is the asynchronous version of Query.fetch().

### `fetch_page`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1385-L1410)
    
    
    fetch_page(
        page_size, **q_options
    )
    

Fetch a page of results.

This is a specialized method for use by paging user interfaces.

Args  
---  
  
`page_size` |  The requested page size. At most this many results will be returned.   
  
In addition, any keyword argument supported by the QueryOptions class is supported. In particular, to fetch the next page, you pass the cursor returned by one call to the next call using start_cursor=. A common idiom is to pass the cursor to the client using .to_websafe_string() and to reconstruct that cursor on a subsequent request using Cursor.from_websafe_string().

Returns  
---  
A tuple (results, cursor, more) where results is a list of query results, cursor is a cursor pointing just after the last result returned, and more is a bool indicating whether there are (likely) more results after that.   
  
### `fetch_page_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1412-L1419)
    
    
    fetch_page_async(
        page_size, **q_options
    )
    

Fetch a page of results.

This is the asynchronous version of Query.fetch_page().

### `filter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1132-L1154)
    
    
    filter(
        *args
    )
    

Return a new Query with additional filter(s) applied.

### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1289-L1301)
    
    
    get(
        **q_options
    )
    

Get the first query result, if any.

This is similar to calling q.fetch(1) and returning the first item of the list of results, if any, otherwise None.

Args  
---  
  
`**q_options` |  All query options keyword arguments are supported.   
  
Returns  
---  
A single result, or None if there are no results.   
  
### `get_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1303-L1309)
    
    
    get_async(
        **q_options
    )
    

Get the first query result, if any.

This is the asynchronous version of Query.get().

### `iter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1187-L1197)
    
    
    iter(
        **q_options
    )
    

Construct an iterator over the query.

Args  
---  
  
`**q_options` |  All query options keyword arguments are supported.   
  
Returns  
---  
A QueryIterator object.   
  
### `map`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1201-L1238)
    
    
    map(
        callback, pass_batch_into_callback=None, merge_future=None, **q_options
    )
    

Map a callback function or tasklet over the query results.

Args  
---  
  
`callback` |  A function or tasklet to be applied to each result; see below.   
`merge_future` |  Optional Future subclass; see below.   
`**q_options` |  All query options keyword arguments are supported.   
  
Callback signature: The callback is normally called with an entity as argument. However if keys_only=True is given, it is called with a Key. Also, when pass_batch_into_callback is True, it is called with three arguments: the current batch, the index within the batch, and the entity or Key at that index. The callback can return whatever it wants. If the callback is None, a trivial callback is assumed that just returns the entity or key passed in (ignoring produce_cursors).

Optional merge future: The merge_future is an advanced argument that can be used to override how the callback results are combined into the overall map() return value. By default a list of callback return values is produced. By substituting one of a small number of specialized alternatives you can arrange otherwise. See tasklets.MultiFuture for the default implementation and a description of the protocol the merge_future object must implement the default. Alternatives from the same module include QueueFuture, SerialQueueFuture and ReducingFuture.

Returns  
---  
When the query has run to completion and all callbacks have returned, map() returns a list of the results of all callbacks. (But see 'optional merge future' above.)   
  
### `map_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1240-L1253)
    
    
    map_async(
        callback, pass_batch_into_callback=None, merge_future=None, **q_options
    )
    

Map a callback function or tasklet over the query results.

This is the asynchronous version of Query.map().

### `order`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1156-L1183)
    
    
    order(
        *args
    )
    

Return a new Query with additional sort order(s) applied.

### `run_to_queue`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1004-L1033)
    
    
    run_to_queue(
        queue, conn, options=None, dsquery=None
    )
    

Run this query, putting entities into the given queue.

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1187-L1197)
    
    
    __iter__(
        **q_options
    )
    

Construct an iterator over the query.

Args  
---  
  
`**q_options` |  All query options keyword arguments are supported.   
  
Returns  
---  
A QueryIterator object.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
