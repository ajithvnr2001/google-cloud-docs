---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Query/
title: google.appengine.ext.db.Query \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:31:05.485708+00:00
---

# google.appengine.ext.db.Query  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.Query Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2397-L2691) A `Query` instance queries over instances of `Model`s. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.Query(
        model_class=None,
        keys_only=False,
        cursor=None,
        namespace=None,
        _app=None,
        distinct=False,
        projection=None
    )
    

You construct a query with a model class, like this: class Story(db.Model): title = db.StringProperty() date = db.DateTimeProperty() query = `Query(Story)` You modify a query with filters and orders like this: query.filter('title =', 'Foo') query.order('-date') query.ancestor(key_or_model_instance) Every query can return an iterator, so you access the results of a query by iterating over it: for story in query: print story.title For convenience, all of the filtering and ordering methods return "self", so the easiest way to use the query interface is to cascade all filters and orders in the iterator line like this: for story in `Query(story).filter('title =', 'Foo')`.order('-date'): print story.title | 

## Args  
  
---  
  
`model_class` |  `Model` class to build query for.   
`keys_only` |  Whether the query should return full entities or only keys.   
`projection` |  A tuple of strings representing the property names to include in the projection this query should produce or `None`. Setting a projection is similar to specifying `SELECT prop1, prop2, ...` in SQL. See `_BaseQuery.projection` for details on projection queries.   
`distinct` |  A boolean, true if the projection should be distinct. See `_BaseQuery.is_distinct` for details on distinct queries.   
`cursor` |  A compiled query from which to resume.   
`namespace` |  The namespace to use for this query.   
  
## Methods

### `ancestor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2661-L2691)
    
    
    ancestor(
        ancestor
    )
    

Sets an ancestor for this query.

This restricts the query to only return results that descend from a given model instance. In other words, all of the results will have the ancestor as their parent, or parent's parent, etc. The ancestor itself is also a possible result!

Args  
---  
  
`ancestor` |  `Model` or `Key` (that has already been saved)   
  
Returns  
---  
Self to support method chaining.   
  
Raises  
---  
`TypeError` if the argument isn't a `Key` or `Model`; `NotSavedError` if it is, but isn't saved yet.   
  
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
  
### `filter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2568-L2616)
    
    
    filter(
        property_operator, value
    )
    

Add filter to query.

Args  
---  
  
`property_operator` |  string with the property and operator to filter by.   
`value` |  the filter value.   
  
Returns  
---  
Self to support method chaining.   
  
Raises  
---  
`PropertyError` if invalid property is provided.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2475-L2476)
    
    
    is_distinct()
    

Returns true if the projection query should be distinct.

This is equivalent to the SQL syntax: `SELECT DISTINCT`. It is only available for projection queries, it is not valid to specify `distinct` without also specifying projection properties.

Distinct projection queries on entities with multi-valued properties will return the same entity multiple times, once for each unique combination of properties included in the projection.

Returns  
---  
`True` if this projection query is distinct.   
  
### `is_keys_only`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2469-L2470)
    
    
    is_keys_only()
    

Returns whether this query is keys only.

Returns  
---  
`True` if this query returns keys, `False` if it returns entities.   
  
### `order`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2618-L2659)
    
    
    order(
        property
    )
    

Set order of query result.

To use descending order, prepend `-` (minus) to the property name, e.g., `-date` rather than `date`.

Args  
---  
  
`property` |  Property to sort on.   
  
Returns  
---  
Self to support method chaining.   
  
Raises  
---  
`PropertyError` if invalid property is provided.   
  
### `projection`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2472-L2473)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L2079-L2104)
    
    
    run(
        **kwargs
    )
    

Iterator for this query.

If you know the number of results you need, use `run(limit=...)` instead, or use a GQL query with a `LIMIT` clause. It's more efficient. If you want all results use `run(batch_size=<large number>)`.

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
