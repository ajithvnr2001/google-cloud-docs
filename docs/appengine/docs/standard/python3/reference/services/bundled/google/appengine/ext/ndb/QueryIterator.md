---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/QueryIterator/
title: google.appengine.ext.ndb.QueryIterator \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:17:18.687476+00:00
---

# google.appengine.ext.ndb.QueryIterator  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/QueryIterator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.QueryIterator Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1656-L1875) This iterator works both for synchronous and async callers! Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.QueryIterator(
        query, **q_options
    )
    

For synchronous callers, just use: for entity in Account.query():  Async callers use this idiom: it = iter(Account.query()) while (yield it.has_next_async()): entity = it.next()  You can also use q.iter([options]) instead of iter(q); this allows passing query options such as keys_only or produce_cursors. When keys_only is set, it.next() returns a key instead of an entity. When produce_cursors is set, the methods it.cursor_before() and it.cursor_after() return Cursor objects corresponding to the query position just before and after the item returned by it.next(). Before it.next() is called for the first time, both raise an exception. Once the loop is exhausted, both return the cursor after the last item returned. Calling it.has_next() does not affect the cursors; you must call it.next() before the cursors move. Note that sometimes requesting a cursor requires a Cloud Datastore roundtrip (but not if you happen to request a cursor corresponding to a batch boundary). If produce_cursors is not set, both methods always raise an exception. Note that queries requiring in-memory merging of multiple queries (i.e. queries using the IN, != or OR operators) do not support query options.

## Methods

### `cursor_after`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1766-L1778)
    
    
    cursor_after()
    

Return the cursor after the current item. You must pass a QueryOptions object with produce_cursors=True for this to work. If there is no cursor or no current item, raise BadArgumentError. Before next() has returned there is no cursor. Once the loop is exhausted, this returns the cursor after the last item.

### `cursor_before`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1750-L1764)
    
    
    cursor_before()
    

Return the cursor before the current item. You must pass a QueryOptions object with produce_cursors=True for this to work. If there is no cursor or no current item, raise BadArgumentError. Before next() has returned there is no cursor. Once the loop is exhausted, this returns the cursor after the last item.

### `has_next`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1835-L1840)
    
    
    has_next()
    

Return whether a next item is available. See the module docstring for the usage pattern.

### `has_next_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1842-L1855)
    
    
    has_next_async()
    

Return a Future whose result will say whether a next item is available. See the module docstring for the usage pattern.

### `index_list`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1780-L1811)
    
    
    index_list()
    

Return the list of indexes used for this query. This returns a list of index representations, where an index representation is the same as what is returned by get_indexes(). Before the first result, the information is unavailable, and then None is returned. This is not the same as an empty list -- the empty list means that no index was used to execute the query. (In the dev_appserver, an empty list may also mean that only built-in indexes were used; metadata queries also return an empty list here.) Proper use is as follows: q = .query() i = q.iter() try: i.next() except Stopiteration: pass indexes = i.index_list() assert isinstance(indexes, list)

#### Notes:

  * Forcing produce_cursors=False makes this always return None.
  * This always returns None for a multi-query.



### `probably_has_next`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1819-L1833)
    
    
    probably_has_next()
    

Return whether a next item is (probably) available. This is not quite the same as has_next(), because when produce_cursors is set, some shortcuts are possible. However, in some cases (e.g. when the query has a post_filter) we can get a false positive (returns True but next() will raise StopIteration). There are no false negatives.

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L1814-L1816)
    
    
    __iter__()
    

Iterator protocol: get the iterator for this iterator, i.e. self. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
