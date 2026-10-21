---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/GqlQuery/
title: google.appengine.ext.db.GqlQuery \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:42:28.313726+00:00
---

# google.appengine.ext.db.GqlQuery  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/GqlQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.GqlQuery Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2694-L2789) A `Query` class that uses GQL query syntax instead of `.filter()` etc. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.GqlQuery(
        query_string, *args, **kwds
    )
    

| 

## Args  
  
---  
  
`query_string` |  Properly formatted GQL query string.   
`*args` |  Positional arguments used to bind numeric references in the query.   
`**kwds` |  Dictionary-based arguments for named references.   
  
## Raises  
  
---  
  
`PropertyError` |  if the query filters or sorts on a property that's not indexed.   
  
## Methods

### `bind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2747-L2766)
    
    
    bind(
        *args, **kwds
    )
    

Bind arguments (positional or keyword) to the query.

Note that you can also pass arguments directly to the query constructor. Each time you call `bind()` the previous set of arguments is replaced with the new set. This is useful because the hard work in in parsing the query; so if you expect to be using the same query with different sets of arguments, you should hold on to the `GqlQuery()` object and call `bind()` on it each time.

Args  
---  
  
`*args` |  Positional arguments used to bind numeric references in the query.   
`**kwds` |  Dictionary-based arguments for named references.   
  
### `count`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2137-L2156)
    
    
    count(
        limit=1000, **kwargs
    )
    

Number of entities this query fetches.

Beware: `count()` ignores the `LIMIT` clause on GQL queries.

Args  
---  
  
`limit` |  A number. If there are more results than this, stop short and just return this number. Providing this argument makes the count operation more efficient.   
`kwargs` |  Any keyword arguments accepted by [`datastore_query.QueryOptions()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/QueryOptions).   
  
Returns  
---  
Number of entities this query fetches.   
  
### `cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2198-L2214)
    
    
    cursor()
    

Get a serialized cursor for an already executed query.

The returned cursor effectively lets a future invocation of a similar query to begin fetching results immediately after the last returned result from this query invocation.

Returns  
---  
A base64-encoded serialized cursor.   
  
Raises  
---  
  
`AssertionError` |  If the query has not been executed.   
  
### `fetch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2158-L2179)
    
    
    fetch(
        limit, offset=0, **kwargs
    )
    

Return a list of items selected using SQL-like limit and offset.

Always use `run(limit=...)` instead of `fetch()` when iterating over a query.

Beware: offset must read and discard all skipped entities. Use `cursor()`/`with_cursor()` instead.

Args  
---  
  
`limit` |  Maximum number of results to return.   
`offset` |  Optional number of results to skip first; default zero.   
`kwargs` |  Any keyword arguments accepted by [`datastore_query.QueryOptions()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/QueryOptions).   
  
Returns  
---  
A list of [`db.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model) instances. There may be fewer than 'limit' results if there aren't enough results to satisfy the request.   
  
### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2119-L2135)
    
    
    get(
        **kwargs
    )
    

Get first result from this.

Beware: `get()` ignores the `LIMIT` clause on GQL queries.

Args  
---  
  
`kwargs` |  Any keyword arguments accepted by [`datastore_query.QueryOptions()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/QueryOptions).   
  
Returns  
---  
First result from running the query if there are any, else `None`.   
  
### `index_list`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2181-L2196)
    
    
    index_list()
    

Get the index list for an already executed query.

Returns  
---  
A list of indexes used by the query.   
  
Raises  
---  
  
`AssertionError` |  If the query has not been executed.   
  
### `is_distinct`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2744-L2745)
    
    
    is_distinct()
    

Returns true if the projection query should be distinct.

This is equivalent to the SQL syntax: `SELECT DISTINCT`. It is only available for projection queries, it is not valid to specify `distinct` without also specifying projection properties.

Distinct projection queries on entities with multi-valued properties will return the same entity multiple times, once for each unique combination of properties included in the projection.

Returns  
---  
`True` if this projection query is distinct.   
  
### `is_keys_only`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2738-L2739)
    
    
    is_keys_only()
    

Returns whether this query is keys only.

Returns  
---  
`True` if this query returns keys, `False` if it returns entities.   
  
### `projection`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2741-L2742)
    
    
    projection()
    

Returns the tuple of properties in the projection or `None`.

Projected results differ from normal results in multiple ways:

  * they only contain a portion of the original entity and cannot be put;
  * properties defined on the model, but not included in the projections will have a value of `None`, even if the property is required or has a default value;
  * multi-valued properties (such as a `ListProperty`) will only contain a single value.
  * dynamic properties not included in the projection will not appear on the model instance.
  * dynamic properties included in the projection are deserialized into their indexed type. Specifically one of `str`, `bool`, `long`, `float`, `GeoPt`, `Key` or `User`. If the original type is known, it can be restored using [`datastore_types.RestoreFromIndexValue`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/RestoreFromIndexValue).



However, projection queries are significantly faster than normal queries.

Projection queries on entities with multi-valued properties will return the same entity multiple times, once for each unique combination of values for properties included in the order, an inequality property, or the projected properties.

Returns  
---  
The list of properties in the projection, or `None` if no projection is set on this query.   
  
### `run`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2768-L2785)
    
    
    run(
        **kwargs
    )
    

Iterator for this query that handles the `LIMIT` clause property.

If the GQL query string contains a `LIMIT` clause, this function fetches all results before returning an iterator. Otherwise results are retrieved in batches by the iterator.

Args  
---  
  
`kwargs` |  Any keyword arguments accepted by [`datastore_query.QueryOptions()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/QueryOptions).   
  
Returns  
---  
Iterator for this query.   
  
### `with_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2216-L2269)
    
    
    with_cursor(
        start_cursor=None, end_cursor=None
    )
    

Set the start and end of this query using serialized cursors.

Conceptually cursors point to the position between the last result returned and the next result so running a query with each of the following cursors combinations will return all results in four chunks with no duplicate results:

query.with_cursor(end_cursor=cursor1) query.with_cursors(cursor1, cursor2) query.with_cursors(cursor2, cursor3) query.with_cursors(start_cursor=cursor3)

For example if the cursors pointed to: cursor: 1 2 3 result: a b c d e f g h

The results returned by these queries would be `[a, b]`, `[c, d]`, `[e, f]`, `[g, h]` respectively.

Cursors are pinned to the position just after the previous result (last result, exclusive), so if results are inserted or deleted between the time the cursor was made and these queries are executed, the cursors stay pinned to these positions. For example:

`delete(b, f, g, h)` `put(a1, b1, c1, d1)` cursor: `1(b) 2(d) 3(f)` result: a a1 b1 c c1 d d1 e

The results returned by these queries would now be: `[a, a1]`, `[b1, c, c1, d]`, `[d1, e]`, `[]` respectively.

Args  
---  
  
`start_cursor` |  The cursor position at which to start or `None`  
`end_cursor` |  The cursor position at which to end or `None`  
  
Returns  
---  
This `Query` instance, for chaining.   
  
Raises  
---  
`BadValueError` when cursor is not valid.   
  
### `__getitem__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2271-L2310)
    
    
    __getitem__(
        arg
    )
    

Support for `query[index]` and `query[start:stop]`.

Beware: this ignores the `LIMIT` clause on GQL queries.

Args  
---  
  
`arg` |  Either a single integer, corresponding to the `query[index]` syntax, or a Python `slice` object, corresponding to the `query[start:stop]` or `query[start:stop:step]` syntax.   
  
Returns  
---  
A single `Model` instance when the argument is a single integer. A list of `Model` instances when the argument is a slice.   
  
### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2106-L2112)
    
    
    __iter__()
    

Iterator for this query.

If you know the number of results you need, consider `fetch()` instead, or use a GQL query with a `LIMIT` clause. It's more efficient.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
