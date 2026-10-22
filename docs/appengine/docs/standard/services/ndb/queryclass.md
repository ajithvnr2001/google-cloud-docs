---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queryclass/
title: NDB Query Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:44.729643+00:00
---

# NDB Query Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queryclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Query Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

A `Query` object represents an NDB query, a request for a filtered, sorted list of entities. 

This page contains reference documentation. For a general discussion of NDB queries, see [Queries](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries). 

## Query Options

Many query methods take a standard set of additional options, either in the form of keyword arguments such as `keys_only=True`, or as `QueryOptions` object passed with `options=QueryOptions(...)`. 

Queries support a variety of configuration options. These are specified by keyword arguments to the `Query` methods: 

Argument | Type | Default | Description   
---|---|---|---  
keys_only | `bool` | `False` | All operations return keys instead of entities.   
projection | tuple (or list) of properties (or strings) | `None` | Operations return entities with only the specified properties set. `projection=[Article.title, Article.date]` or `projection=['title', 'date']` fetches entities with just those two fields set. (See [Projection Queries](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#projection).)   
offset | `int` | `0` | Number of query results to skip.   
limit | `int` | No limit | Maximum number of query results to return.   
batch_size | `int` | `20` | Batch size.  
  
Affects efficiency of queries only; larger batch sizes use more memory but make fewer RPC calls.   
prefetch_size | `int` | `None` | Overrides batch size for first batch returned.   
produce_cursors | `bool` | `False` | Generate cursors from query (see [Query Iterators](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#iterators). [Query Cursors](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#cursors)).   
start_cursor | `Cursor` | `None` | Starting point for search (see [Query Cursors](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#cursors)).   
end_cursor | `Cursor` | `None` | Ending point for search (see [Query Cursors](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#cursors)).   
deadline | `int` | Depends on `Context` | Overrides RPC deadline (which defaults to 5 seconds if not overridden when `[Context](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/contextclass)` created)   
read_policy | `ndb.EVENTUAL_CONSISTENCY` |  | The read policy. Set to `ndb.EVENTUAL_CONSISTENCY` to get perhaps-quicker results without waiting for the Datastore to apply pending changes to all returned records.   
  
To run a query with a specific set of options, pass the keyword arguments to the applicable method: 
    
    
    qry = Employee.query().filter(...).order(...) # Create a query
    for acct in qry.fetch(10, offset=20): # Skip the first 20
      print acct

Occasionally, you might want to keep a set of query options around and use them in various places. While you could just keep them in a dictionary and pass this dictionary to the methods using `**kwds`, you can also create a `QueryOptions` object and pass it using the options keyword argument. The following two examples are equivalent: 
    
    
    qo = ndb.QueryOptions(keys_only=True, offset=20)
    results = qry.fetch(10, options=qo)
    results = qry.fetch(10, keys_only=True, offset=20)

## Constructor

Typically, an application creates a `Query` by calling `Model.query()`. But it's also possible to call `ndb.Query()`. 

**Arguments**

kind
    Optional kind string. Normally, the name of a entity class. 
ancestor
    Optional ancestor Key. 
filters
    Optional Node representing a filter expression tree. 
orders
    Optional `datastore_query.Order` object. 
app
    Optional app id. 
namespace
    Optional namespace. If not specified, the default namespace at the time the query is executed will be used. 
projection
    Optional list or tuple of properties to project. 
group_by
    Optional list or tuple of properties to group by. 
default_options
    Optional `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queryclass#kwdargs_options)` object giving default query options to be used when the query is executed. 

## Instance Methods

filter(filter1, filter2, ...)
    Returns a new `Query` with additional filter(s) applied. Takes filter arguments as described in [Queries](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries). `qry.filter(filter1).filter(filter2)` is equivalent to `qry.filter(filter1, filter2)`
get(**q_options)
    Returns the first query result, if any (otherwise `None`). This is similar to calling `q.fetch(1)` and returning the first item of the list of results. 

**Arguments**

**q_options
    All query options keyword arguments are supported. 
order(order1, order2, ...)
    Returns a new `Query` with additional sort order(s) applied. Takes one or more arguments which are properties or "negated" properties. For example, to sort users by age and "break ties" by name, you might use something like `qry.order(-Account.birthday, Account.name)`
bind(...values...)
    This function is for use with GQL queries that use parameter bindings (`:1`, `:2`, etc.) or named bindings (`:foo`, `:bar`, etc.). It binds the passed values to the parameters. 

To bind parameters, you might call something like `qry.bind("USA", 49)`. To bind named parameters, you might call something like `qry.bind(region = "USA", threshold = 49)`. 

Returns a new `Query` object with the parameter values bound. 

count(limit=None, **q_options)
    Returns the number of query results, up to a limit. This returns the same result as `len(q.fetch(limit))` but more efficiently. 

**Arguments**

limit
    How many results to count at most 
**q_options
    All query options keyword arguments and [context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options) are supported. 
count_async(limit, **q_options)
    Asynchronously counts the number of query results, up to a limit; it returns a `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` whose result is a number. This is the asynchronous version of count(). 
fetch(limit, **q_options)
    Fetch a list of query results, up to a limit. 

**Arguments**

limit
    How many results to count at most 
**q_options
    All query options keyword arguments are supported. 
fetch_async(limit, **q_options)
    Asynchronously fetch a list of query results, up to a limit. Returns a `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` whose result is a list of results. This is the asynchronous version of fetch(). 
fetch_page(page_size, **q_options)
    Fetch a "page" of results. This is a specialized method for use by paging user interfaces. 

**Arguments**

page_size
    At most this many results will be returned. 
**q_options
    All query options keyword arguments are supported. 
Returns a tuple `(results, cursor, more)`: 

  * results list of query results 
  * cursor a [query cursor](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#cursors) pointing to the "next" batch of results. If there are no more results, this might be `None`. 
  * more `bool` indicating whether there are (likely) more results after this batch. If `False`, there are no more results; if `True`, there are _probably_ more results. 



To fetch the next page, pass the cursor returned by one call to the next call using `start_cursor=cursor`. A common idiom is to pass the cursor to the client using `cursor.urlsafe()` and to reconstruct that cursor on a subsequent request using `Cursor(urlsafe=string)`. 

fetch_page_async(page_size, **q_options)
    Asynchronously fetch a "page" of results. This is the asynchronous version of fetch_page(). 
get_async(**q_options)
    Asynchronously returns the first query result, if any (otherwise `None`). This is the asynchronous version of get(). 
iter(**q_options)
    Constructs and returns an iterator over the query. 

**Arguments**

**q_options
    All query options keyword arguments are supported. 

Returns a [QueryIterator](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#iterators) object. 

map(callback, pass_batch_into_callback=None, merge_future=None, **q_options)
    Map a callback function or tasklet over the query results. That is, apply the function (or tasklet) to each entity in the query results. 

**Arguments**

callback
    A function or tasklet to be applied to each result. 
pass_batch_into_callback
    If `True`, calls the callback with batch information arguments as described below. 
merge_future
    Optional `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` subclass; see below. 
**q_options
    All query options keyword arguments are supported. 

_Callback signature_ The callback is normally called with an entity as argument. However, if `keys_only=True` is given, it is called with a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass). If `pass_batch_into_callback=True` is given, the callback is called with three arguments: the current batch, the index within the batch, and the entity or `Key` at that index. The callback can return whatever it wants. If the callback is `None`, a trivial callback is assumed that just returns the entity or key passed in. 

_Optional`merge_future`_ The `merge_future` is an advanced argument that can be used to override how the callback results are combined into the overall `map()` return value. By default, a list of callback return values is produced. By substituting one of a small number of specialized alternatives you can arrange otherwise. See the source code for `tasklets.MultiFuture` for the default implementation and a description of the protocol the `merge_future` object must implement. Alternatives from the same module include `QueueFuture`, `SerialQueueFuture` and `ReducingFuture`. 

Returns a list of the results of all the callbacks. (But see 'optional `merge_future`' above.) It returns when the query has run to completion and all callbacks have returned. 

map_async(callback, pass_batch_into_callback=None, merge_future=None, **q_options)
    Asynchronously map a callback function or tasklet over the query results. This is the asynchronous version of map(). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
