---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/allocate_id_range/
title: google.appengine.ext.db.allocate_id_range \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:34:47.913522+00:00
---

# google.appengine.ext.db.allocate_id_range  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/allocate_id_range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.allocate_id_range Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1660-L1725) Allocates a range of IDs with specific endpoints.
    
    
    google.appengine.ext.db.allocate_id_range(
        model, start, end, **kwargs
    )
    

Once these IDs have been allocated they may be provided manually to newly created entities. Since the datastore's automatic `ID` allocator will never assign a key to a new entity that will cause an existing entity to be overwritten, entities written to the given key range will never be overwritten. However, writing entities with manually assigned keys in this range may overwrite existing entities (or new entities written by a separate request) depending on the key range state returned. This method should only be used if you have an existing numeric id range that you want to reserve, e.g. bulk loading entities that already have IDs. If you don't care about which IDs you receive, use allocate_ids instead. | 

## Args  
  
---  
  
`model` |  `Model` instance, Key or string to serve as a template specifying the `ID` sequence in which to allocate IDs. Allocated ids should only be used in entities with the same parent (if any) and kind as this key.   
`start` |  first id of the range to allocate, inclusive.   
`end` |  last id of the range to allocate, inclusive.   
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
## Returns  
  
---  
One of `(KEY_RANGE_EMPTY, KEY_RANGE_CONTENTION, KEY_RANGE_COLLISION)`. If not `KEY_RANGE_EMPTY`, this represents a potential issue with using the allocated key range.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
