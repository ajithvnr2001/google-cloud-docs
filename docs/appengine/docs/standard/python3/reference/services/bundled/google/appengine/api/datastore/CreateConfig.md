---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/CreateConfig/
title: google.appengine.api.datastore.CreateConfig \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:19:37.605257+00:00
---

# google.appengine.api.datastore.CreateConfig  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/CreateConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.CreateConfig Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L508-L531) Create a Configuration object for use in configuring datastore calls.
    
    
    google.appengine.api.datastore.CreateConfig(
        **kwds
    )
    

This configuration can be passed to most datastore calls using the 'config=...' argument. | 

## Args  
  
---  
  
`deadline` |  Optional deadline; default None (which means the system default deadline will be used, typically 5 seconds).   
`on_completion` |  Optional callback function; default None. If specified, it will be called with a `UserRPC` object as argument when an RPC completes.   
`read_policy` |  Optional read policy; set to EVENTUAL_CONSISTENCY to enable eventually consistent reads (i.e. reads that may be satisfied from an older version of the datastore in some cases). The default read policy may have to wait until in-flight transactions are committed.   
`**kwds` |  Other keyword arguments as long as they are supported by datastore_rpc.Configuration().   
  
## Returns  
  
---  
A datastore_rpc.Configuration instance.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
