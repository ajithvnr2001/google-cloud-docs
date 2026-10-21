---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseCursor/
title: google.appengine.datastore.datastore_stub_util.BaseCursor \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:39:35.189764+00:00
---

# google.appengine.datastore.datastore_stub_util.BaseCursor  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseCursor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.BaseCursor Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1079-L1270) A base query cursor over a list of entities. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.BaseCursor(
        query, dsquery, orders, index_list
    )
    

#### Public properties:

  * **`cursor`** : the integer cursor.
  * **`app`** : the app for which this cursor was created.
  * **`keys_only`** : whether the query is keys_only.



#### Class attributes:

  * **`_next_cursor`** : the next cursor to allocate.
  * **`_next_cursor_lock`** : protects _next_cursor.

| 

## Args  
  
---  
  
`query` |  the query request proto.   
`dsquery` |  a datastore_query.Query over query.   
`orders` |  the orders of query as returned by _GuessOrders.   
`index_list` |  the list of indexes used by the query.   
  
## Methods

### `PopulateQueryResult`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1242-L1266)
    
    
    PopulateQueryResult(
        result, count, deprecated_offset, compile=False, first_result=False
    )
    

Populates a QueryResult with this cursor and the given number of results.

Args  
---  
  
`result` |  datastore_pb.QueryResult   
`count` |  integer of how many results to return, or None if not specified   
`deprecated_offset` |  integer of how many results to skip, deprecated.   
`compile` |  boolean, whether we are compiling this query   
`first_result` |  whether the query result is the first for this query   
  
Raises  
---  
  
`datastore_errors.BadArgumentError` |  if the offset doesn't match the original offset from the RunQuery call.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
