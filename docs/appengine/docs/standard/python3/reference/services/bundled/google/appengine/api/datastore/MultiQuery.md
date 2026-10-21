---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/MultiQuery/
title: google.appengine.api.datastore.MultiQuery \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:33:22.482402+00:00
---

# google.appengine.api.datastore.MultiQuery  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/MultiQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.MultiQuery Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2040-L2509) Class representing a query which requires multiple datastore queries. Inherits From: [`Query`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Query), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.datastore.MultiQuery(
        bound_queries, orderings
    )
    

This class is actually a subclass of datastore.Query as it is intended to act like a normal Query object (supporting the same interface). Does not support keys only queries, since it needs whole entities in order to merge sort them. (That's not true if there are no sort orders, or if the sort order is on **key** , but allowing keys only queries in those cases, but not in others, would be confusing.) | 

## Args  
  
---  
  
`namespace` |  string, the namespace to query.   
`kind` |  string, the kind of entities to query, or None.   
`filters` |  dict, initial set of filters.   
`keys_only` |  boolean, if keys should be returned instead of entities.   
`projection` |  iterable of property names to project.   
`distinct` |  boolean, if projection should be distinct.   
`compile` |  boolean, if the query should generate cursors.   
`cursor` |  datastore_query.Cursor, the start cursor to use.   
`end_cursor` |  datastore_query.Cursor, the end cursor to use.   
`_namespace` |  deprecated, use namespace instead.   
  
## Child Classes

[`class SortOrderEntity`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/MultiQuery/SortOrderEntity)

## Methods

### `Ancestor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1530-L1549)
    
    
    Ancestor(
        ancestor
    )
    

Sets an ancestor for this query.

This restricts the query to only return result entities that are descended from a given entity. In other words, all of the results will have the ancestor as their parent, or parent's parent, or etc.

Raises `BadArgumentError` or `BadKeyError` if parent is not an existing Entity or Key in the datastore.

Args  
---  
  
# the key must be complete  
  
`ancestor` |  Entity or Key   
  
Returns  
---  
  
# this query

Query   
  
### `Count`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2391-L2433)
    
    
    Count(
        limit=1000, **kwargs
    )
    

Return the number of matched entities for this query.

Will return the de-duplicated count of results. Will call the more efficient `Get()` function if a limit is given.

Args  
---  
  
`limit` |  maximum number of entries to count (for any result > limit, return limit).   
`config` |  Optional Configuration to use for this request.   
  
Returns  
---  
count of the number of entries returned.   
  
### `Get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2081-L2095)
    
    
    Get(
        limit, offset=0, **kwargs
    )
    

Deprecated, use `list(Run(...))` instead.

Args  
---  
  
`limit` |  int or long representing the maximum number of entities to return.   
`offset` |  int or long representing the number of entities to skip   
`kwargs` |  Any keyword arguments accepted by datastore_query.QueryOptions().   
  
Returns  
---  
A list of entities with at most "limit" entries (less if the query completes before reading limit values).   
  
### `GetBatcher`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1670-L1694)
    
    
    GetBatcher(
        config=None
    )
    

Runs this query and returns a datastore_query.Batcher.

This is not intended to be used by application developers. Use `Get()` instead!

Args  
---  
  
`config` |  Optional Configuration to use for this request.   
  
Returns  
---  
  
# an iterator that provides access to the query results

Iterator   
  
### `GetCompiledCursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2440-L2442)
    
    
    GetCompiledCursor()
    

Get the cursor from the last run of this query.

The source of this cursor varies depending on what the last call was:

  * Run: A cursor that points immediately after the last result pulled off the returned iterator.
  * Get: A cursor that points immediately after the last result in the returned list.
  * Count: A cursor that points immediately after the last result counted.



Returns  
---  
A datastore_query.Cursor object that can be used in subsequent query requests.   
  
Raises  
---  
  
`AssertionError` |  The query has not yet been run or cannot be compiled.   
  
### `GetCompiledQuery`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2444-L2447)
    
    
    GetCompiledQuery()
    

Internal only, do not use.

### `GetCursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2440-L2442)
    
    
    GetCursor()
    

Get the cursor from the last run of this query.

The source of this cursor varies depending on what the last call was:

  * Run: A cursor that points immediately after the last result pulled off the returned iterator.
  * Get: A cursor that points immediately after the last result in the returned list.
  * Count: A cursor that points immediately after the last result counted.



Returns  
---  
A datastore_query.Cursor object that can be used in subsequent query requests.   
  
Raises  
---  
  
`AssertionError` |  The query has not yet been run or cannot be compiled.   
  
### `GetDistinct`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1619-L1625)
    
    
    GetDistinct()
    

Returns `True` if the current instance is distinct.

Returns  
---  
A boolean indicating if the distinct flag is set.   
  
### `GetFilterPredicate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1585-L1617)
    
    
    GetFilterPredicate()
    

Returns a datastore_query.FilterPredicate for the current instance.

Returns  
---  
datastore_query.FilterPredicate or None if no filters are set on the current Query.   
  
### `GetIndexList`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2435-L2438)
    
    
    GetIndexList()
    

Get the index list from the last run of this query.

Returns  
---  
A list of indexes used by the last run of this query.   
  
Raises  
---  
  
`AssertionError` |  The query has not yet been run.   
  
### `GetOrder`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1570-L1583)
    
    
    GetOrder()
    

Gets a datastore_query.Order for the current instance.

Returns  
---  
datastore_query.Order or None if there are no sort orders set on the current Query.   
  
### `GetQuery`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1559-L1568)
    
    
    GetQuery()
    

Returns a datastore_query.Query for the current instance.

### `GetQueryOptions`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1555-L1557)
    
    
    GetQueryOptions()
    

Returns a datastore_query.QueryOptions for the current instance.

### `Hint`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1495-L1528)
    
    
    Hint(
        hint
    )
    

Sets a hint for how this query should run.

The query hint gives us information about how best to execute your query. Currently, we can only do one index scan, so the query hint should be used to indicates which index we should scan against.

Use FILTER_FIRST if your first filter will only match a few results. In this case, it will be most efficient to scan against the index for this property, load the results into memory, and apply the remaining filters and sort orders there.

Similarly, use ANCESTOR_FIRST if the query's ancestor only has a few descendants. In this case, it will be most efficient to scan all entities below the ancestor and load them into memory first.

Use ORDER_FIRST if the query has a sort order and the result set is large or you only plan to fetch the first few results. In that case, we shouldn't try to load all of the results into memory; instead, we should scan the index for this property, which is in sorted order.

Note that hints are currently ignored in the v3 datastore!

Arg  
---  
one of datastore.Query.[ORDER_FIRST, ANCESTOR_FIRST, FILTER_FIRST]   
  
Returns  
---  
  
# this query

Query   
  
### `IsKeysOnly`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1551-L1553)
    
    
    IsKeysOnly()
    

Returns `True` if this query is keys only, `False` otherwise.

### `Order`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1402-L1493)
    
    
    Order(
        *orderings
    )
    

Specify how the query results should be sorted.

Result entities will be sorted by the first property argument, then by the second, and so on. For example, this:

`> query = Query('Person')` `> query.Order('bday', ('age', Query.DESCENDING))`

sorts everyone in order of their birthday, starting with January 1. People with the same birthday are sorted by age, oldest to youngest.

The direction for each sort property may be provided; if omitted, it defaults to ascending.

`Order()` may be called multiple times. Each call resets the sort order from scratch.

If an inequality filter exists in this Query it must be the first property passed to Order. Any number of sort orders may be used after the inequality filter property. Without inequality filters, any number of filters with different orders may be specified.

Entities with multiple values for an order property are sorted by their lowest value.

Note that a sort order implies an existence filter! In other words, Entities without the sort order property are filtered out, and _not_ included in the query results.

If the sort order property has different types in different entities - ie, if bob['id'] is an int and fred['id'] is a string - the entities will be grouped first by the property type, then sorted within type. No attempt is made to compare property values across types.

Raises `BadArgumentError` if any argument is of the wrong format.

Args  
---  
  
# the properties to sort by, in sort order. each argument may be either a

# string or `(string, direction)` 2-tuple.  
  
Returns  
---  
  
# this query

Query   
  
### `Run`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2268-L2389)
    
    
    Run(
        **kwargs
    )
    

Return an iterable output with all results in order.

Merge sort the results. First create a list of iterators, then walk though them and yield results in order.

Args  
---  
  
`kwargs` |  Any keyword arguments accepted by datastore_query.QueryOptions().   
  
Returns  
---  
An iterator for the result set.   
  
### `clear`
    
    
    clear()
    

D.clear() -> None. Remove all items from D.

### `copy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1859-L1862)
    
    
    copy()
    

The copy method is not supported.

### `fromkeys`
    
    
    fromkeys(
        value, /
    )
    

Create a new dictionary with keys from iterable and values set to value.

### `get`
    
    
    get(
        key, default, /
    )
    

Return the value for key if key is in the dictionary, else default.

### `items`
    
    
    items()
    

D.items() -> a set-like object providing a view on D's items

### `keys`
    
    
    keys()
    

D.keys() -> a set-like object providing a view on D's keys

### `pop`
    
    
    pop()
    

D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

### `popitem`
    
    
    popitem()
    

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

### `setdefault`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1821-L1830)
    
    
    setdefault(
        filter, value
    )
    

If the filter exists, returns its value. Otherwise sets it to value.

If the property name is the empty string or not a string, raises `BadPropertyError`. If the value is not a supported type, raises `BadValueError`.

### `update`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1850-L1857)
    
    
    update(
        other
    )
    

Updates this query's filters from the ones in other.

If any filter string is invalid, raises `BadFilterError`. If any value is not a supported type, raises `BadValueError`.

### `values`
    
    
    values()
    

D.values() -> an object providing a view on D's values

### `__contains__`
    
    
    __contains__(
        key, /
    )
    

True if the dictionary has the specified key, else False.

### `__eq__`
    
    
    __eq__(
        value, /
    )
    

Return self==value.

### `__ge__`
    
    
    __ge__(
        value, /
    )
    

Return self>=value.

### `__getitem__`
    
    
    __getitem__()
    

x.**getitem**(y) <==> x[y]

### `__gt__`
    
    
    __gt__(
        value, /
    )
    

Return self>value.

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2504-L2505)
    
    
    __iter__()
    

Implement iter(self).

### `__le__`
    
    
    __le__(
        value, /
    )
    

Return self<=value.

### `__len__`
    
    
    __len__()
    

Return len(self).

### `__lt__`
    
    
    __lt__(
        value, /
    )
    

Return self<value.

### `__ne__`
    
    
    __ne__(
        value, /
    )
    

Return self!=value.

### `__or__`
    
    
    __or__(
        value, /
    )
    

Return self|value.

### `__ror__`
    
    
    __ror__(
        value, /
    )
    

Return value|self.

## Class Variables  
  
---  
  
ANCESTOR_FIRST |  `2`  
ASCENDING |  `1`  
DESCENDING |  `2`  
FILTER_FIRST |  `3`  
FILTER_REGEX |  Instance of `re.Pattern`  
INEQUALITY_OPERATORS | 
    
    
    {
     '<',
     '<=',
     '>',
     '>='
    }
      
  
OPERATORS | 
    
    
    {
     '<': 1,
     '<=': 2,
     '=': 5,
     '==': 5,
     '>': 3,
     '>=': 4
    }
      
  
ORDER_FIRST |  `1`  
UPPERBOUND_INEQUALITY_OPERATORS | 
    
    
    {
     '<',
     '<='
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
