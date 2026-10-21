---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/runtime/set_shutdown_hook/
title: google.appengine.api.runtime.set_shutdown_hook \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:50:17.243795+00:00
---

# google.appengine.api.runtime.set_shutdown_hook  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/runtime/set_shutdown_hook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.runtime.set_shutdown_hook Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/runtime/runtime.py#L86-L111) Registers a function to be called when the server is shutting down.

#### View aliases

**Main aliases** `google.appengine.api.runtime.runtime.set_shutdown_hook`
    
    
    google.appengine.api.runtime.set_shutdown_hook(
        hook
    )
    

The shutdown hook will be called when the server shuts down. Your code will have a short amount of time to save state and exit. The shutdown hook should interrupt any long running code you have, e.g. by calling apiproxy_stub_map.apiproxy.CancelApiCalls and/or raising an exception. | 

## Args  
  
---  
  
`hook` |  A no-argument callable which will be called when the server is shutting down.   
  
## Returns  
  
---  
The previously registered shutdown hook, or None if no hook was registered before.   
  
In some cases it may not be possible to run the shutdown hook before the server exits.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
