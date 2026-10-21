---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/get_indexes/
title: google.appengine.api.search.get_indexes \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:05:49.258467+00:00
---

# google.appengine.api.search.get_indexes  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/get_indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.get_indexes Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L882-L914) Returns a list of available indexes.

#### View aliases

**Main aliases** `google.appengine.api.search.search.get_indexes`
    
    
    google.appengine.api.search.get_indexes(
        namespace='',
        offset=None,
        limit=20,
        start_index_name=None,
        include_start_index=True,
        index_name_prefix=None,
        fetch_schema=False,
        deadline=None,
        **kwargs
    )
    

| 

## Args  
  
---  
  
`namespace` |  The namespace of indexes to be returned. If not set then the current namespace is used.   
`offset` |  The offset of the first returned index.   
`limit` |  The number of indexes to return.   
`start_index_name` |  The name of the first index to be returned.   
`include_start_index` |  Whether or not to return the start index.   
`index_name_prefix` |  The prefix used to select returned indexes.   
`fetch_schema` |  Whether to retrieve Schema for each Index or not.   
  
#### Kwargs:

  * **`deadline`** : Deadline for RPC call in seconds; if None use the default.



## Returns  
  
---  
The GetResponse containing a list of available indexes.   
  
## Raises  
  
---  
  
`InternalError` |  If the request fails on internal servers.   
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values (e.g., a negative deadline).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
