---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/apply_query/
title: google.appengine.datastore.datastore_query.apply_query \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:57:36.453527+00:00
---

# google.appengine.datastore.datastore_query.apply_query  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/apply_query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.apply_query Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L2251-L2320) Performs the given query on a set of in-memory results.
    
    
    google.appengine.datastore.datastore_query.apply_query(
        query, entities, _key=None
    )
    

This function can perform queries impossible in the datastore (e.g a query with multiple inequality filters on different properties) because all operations are done in memory. For queries that can also be executed on the the datastore, the results produced by this function may not use the same implicit ordering as the datastore. To ensure compatibility, explicit ordering must be used (e.g. 'ORDER BY ineq_prop, ..., **key** '). Order by **key** should always be used when a consistent result is desired (unless there is a sort order on another globally unique property). | 

## Args  
  
---  
  
`query` |  a datastore_query.Query to apply   
`entities` |  a list of results, of arbitrary type, on which to apply the query.   
`_key` |  a function that takes an element of the result array as an argument and must return an entity_pb2.EntityProto. If not specified, the identity function is used (and entities must be a list of entity_pb2.EntityProto).   
  
## Returns  
  
---  
A subset of entities, filtered and ordered according to the query.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
