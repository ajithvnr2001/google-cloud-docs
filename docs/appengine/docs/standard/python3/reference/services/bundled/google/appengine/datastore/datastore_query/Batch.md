---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Batch/
title: google.appengine.datastore.datastore_query.Batch \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:54.938010+00:00
---

# google.appengine.datastore.datastore_query.Batch  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.Batch Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2601-L3042) A batch of results returned by a query. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_query.Batch(
        batch_shared,
        start_cursor=[Cursor()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Cursor)
    )
    

This class contains a batch of results returned from the datastore and relevant metadata. This metadata includes: query: The query that produced this batch query_options: The QueryOptions used to run the query. This does not contained any options passed to the .next_batch() call that created the current batch. start_cursor, end_cursor: These are the cursors that can be used with a query to re-fetch this batch. They can also be used to find all entities before or after the given batch (by use start_cursor as an end cursor or vice versa). start_cursor can also be advanced to point to a position within the batch using Cursor.advance(). skipped_results: the number of result skipped because of the offset given to the request that generated it. This can be set either on the original Query.run() request or in subsequent .next_batch() calls. more_results: If this is true there are more results that can be retrieved either by .next_batch() or Batcher.next(). This class is also able to fetch the next batch of the query using .next_batch(). As batches of results must be fetched serially, .next_batch() can only be called once. Additional calls to .next_batch() will return None. When there are no more batches .next_batch() will return None as well. Note that batches returned by iterating over Batcher will always return None for .next_batch() as the Bather handles fetching the next batch automatically. A Batch typically represents the result of a single RPC request. The datastore operates on a "best effort" basis so the batch returned by .next_batch() or Query.run_async().get_result() may not have satisfied the requested offset or number of results (specified through FetchOptions.offset and FetchOptions.batch_size respectively). To satisfy these restrictions additional batches may be needed (with FetchOptions that specify the remaining offset or results needed). The Batcher class hides these limitations. | 

## Args  
  
---  
  
`batch_shared` |  Data shared between batches for a a single query run.   
`start_cursor` |  Optional cursor pointing before this batch.   
  
## Attributes  
  
---  
  
`end_cursor` |  A cursor that points to the position just after the current batch.   
`index_list` |  Returns the list of indexes used to peform this batch's query. Possibly None when the adapter does not implement pb_to_index.   
`keys_only` |  Whether the entities in this batch only contain keys.   
`more_results` |  Whether more results can be retrieved from the query.   
`query` |  The query the current batch came from.   
`query_options` |  The QueryOptions used to retrieve the first batch.   
`results` |  A list of entities in this batch.   
`skipped_results` |  The number of results skipped because of an offset in the request. An offset is satisfied before any results are returned. The start_cursor points to the position in the query before the skipped results.   
`start_cursor` |  A cursor that points to the position just before the current batch.   
  
## Methods

### `create_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2640-L2646)
    
    
    @classmethod
    create_async(
        query, query_options, conn, req, start_cursor
    )
    

### `cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2739-L2789)
    
    
    cursor(
        index
    )
    

Gets the cursor that points just after the result at index - 1.

The index is relative to first result in .results. Since start_cursor points to the position before the first skipped result, the range of indexes this function supports is limited to [-skipped_results, len(results)].

For example, using start_cursor=batch.cursor(i) and end_cursor=batch.cursor(j) will return the results found in batch.results[i:j]. Note that any result added in the range (i-1, j] will appear in the new query's results.

**Warning:** Any index in the range (-skipped_results, 0) may cause continuation to miss or duplicate results if outside a transaction.

Args  
---  
  
`index` |  An int, the index relative to the first result before which the cursor should point.   
  
Returns  
---  
A Cursor that points to a position just after the result index - 1, which if used as a start_cursor will cause the first result to be batch.result[index].   
  
### `next_batch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2719-L2734)
    
    
    next_batch(
        fetch_options=None
    )
    

Synchronously get the next batch or None if there are no more batches.

Args  
---  
  
`fetch_options` |  Optional fetch options to use when fetching the next batch. Merged with both the fetch options on the original call and the connection.   
  
Returns  
---  
A new Batch of results or None if either the next batch has already been fetched or there are no more results.   
  
### `next_batch_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2791-L2839)
    
    
    next_batch_async(
        fetch_options=None
    )
    

Asynchronously get the next batch or None if there are no more batches.

Args  
---  
  
`fetch_options` |  Optional fetch options to use when fetching the next batch. Merged with both the fetch options on the original call and the connection.   
  
Returns  
---  
An async object that can be used to get the next Batch or None if either the next batch has already been fetched or there are no more results.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
