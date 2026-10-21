---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/CheckQuery/
title: google.appengine.datastore.datastore_stub_util.CheckQuery \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:50:30.110805+00:00
---

# google.appengine.datastore.datastore_stub_util.CheckQuery  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/CheckQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.CheckQuery Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L615-L754) Check a datastore query with normalized filters, orders.
    
    
    google.appengine.datastore.datastore_stub_util.CheckQuery(
        query, filters, orders, max_query_components
    )
    

Raises an ApplicationError when any of the following conditions are violated:

  * transactional queries have an ancestor
  * queries that are not too large (sum of filters, orders, ancestor <= max_query_components)
  * ancestor (if any) app and namespace match query app and namespace
  * kindless queries only filter on **key** and only sort on **key** ascending
  * multiple inequality (<, <=, >, >=) filters all applied to the same property
  * filters on **key** compare to a reference in the same app and namespace as the query
  * if an inequality filter on prop X is used, the first order (if any) must be on X

| 

## Args  
  
---  
  
`query` |  query to validate   
`filters` |  normalized (by datastore_index.Normalize) filters from query   
`orders` |  normalized (by datastore_index.Normalize) orders from query   
`max_query_components` |  limit on query complexity   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
