---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Batcher/
title: google.appengine.datastore.datastore_query.Batcher \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:01:13.316357+00:00
---

# google.appengine.datastore.datastore_query.Batcher  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Batcher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.Batcher Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L3174-L3297) A class that implements the Iterator interface for Batches. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_query.Batcher(
        query_options, first_async_batch
    )
    

Typically constructed by a call to Query.run(). The class hides the "best effort" nature of the datastore by potentially making multiple requests to the datastore and merging the resulting batches. This is accomplished efficiently by prefetching results and mixing both non-blocking and blocking calls to the datastore as needed. Iterating through batches is almost always more efficient than pulling all results at once as RPC latency is hidden by asynchronously prefetching results. The batches produce by this class cannot be used to fetch the next batch (through Batch.next_batch()) as before the current batch is returned the request for the next batch has already been sent. | 

## Args  
  
---  
  
`query_options` |  The QueryOptions used to create the first batch.   
`first_async_batch` |  The first batch produced by Query.run_async(query_options).   
  
## Methods

### `next`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L3213-L3215)
    
    
    next()
    

Get the next batch. See .next_batch().

### `next_batch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L3220-L3290)
    
    
    next_batch(
        min_batch_size
    )
    

Get the next batch.

The batch returned by this function cannot be used to fetch the next batch (through Batch.next_batch()). Instead this function will always return None. To retrieve the next batch use .next() or .next_batch(N).

This function may return a batch larger than min_to_fetch, but will never return smaller unless there are no more results.

Special values can be used for min_batch_size: ASYNC_ONLY - Do not perform any synchrounous fetches from the datastore even if the this produces a batch with no results. AT_LEAST_OFFSET - Only pull enough results to satifiy the offset. AT_LEAST_ONE - Pull batches until at least one result is returned.

Args  
---  
  
`min_batch_size` |  The minimum number of results to retrieve or one of (ASYNC_ONLY, AT_LEAST_OFFSET, AT_LEAST_ONE)   
  
Returns  
---  
The next Batch of results.   
  
### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L3296-L3297)
    
    
    __iter__()
    

## Class Variables  
  
---  
  
ASYNC_ONLY |  `None`  
AT_LEAST_OFFSET |  `0`  
AT_LEAST_ONE |  Instance of [`google.appengine.api.validation.Validator.expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
