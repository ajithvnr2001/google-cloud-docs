---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/MinimalCompositeIndexForQuery/
title: google.appengine.datastore.datastore_index.MinimalCompositeIndexForQuery \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:30:51.018101+00:00
---

# google.appengine.datastore.datastore_index.MinimalCompositeIndexForQuery  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/MinimalCompositeIndexForQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_index.MinimalCompositeIndexForQuery Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_index.py#L850-L944) Computes the minimal composite index for this query.
    
    
    google.appengine.datastore.datastore_index.MinimalCompositeIndexForQuery(
        query, index_defs
    )
    

Unlike [`datastore_index.CompositeIndexForQuery`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/CompositeIndexForQuery), this function takes into account indexes that already exist in the system. | 

## Args  
  
---  
  
`query` |  The `datastore_pb.Query` to compute suggestions for.   
`index_defs` |  A list of [`datastore_index.Index`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/Index) objects that already exist.   
  
## Returns  
  
---  
`None` if no index is needed, otherwise the minimal index in the form `(is_most_efficient, kind, ancestor, properties)`. Where `is_most_efficient` is a boolean denoting if the suggested index is the most efficient (i.e., the one returned by [`datastore_index.CompositeIndexForQuery`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/CompositeIndexForQuery)). kind and ancestor are the same variables returned by [`datastore_index.CompositeIndexForQuery`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/CompositeIndexForQuery). properties is a tuple consisting of the prefix and postfix properties returend by [`datastore_index.CompositeIndexForQuery`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/CompositeIndexForQuery).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
