---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/defer/
title: google.appengine.ext.deferred.defer \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:41.382597+00:00
---

# google.appengine.ext.deferred.defer  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/defer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.deferred.defer Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/deferred/deferred.py#L274-L310) Defers a callable for execution later.

#### View aliases

**Main aliases** `google.appengine.ext.deferred.deferred.defer`
    
    
    google.appengine.ext.deferred.defer(
        obj, *args, **kwargs
    )
    

The default deferred URL of /_ah/queue/deferred will be used unless an alternate URL is explicitly specified. If you want to use the default URL for a queue, specify _url=None. If you specify a different URL, you will need to install the handler on that URL (see the module docstring for details). | 

## Args  
  
---  
  
`obj` |  The callable to execute. See module docstring for restrictions. _countdown, _eta, _headers, _name, _target, _transactional, _url, _retry_options, _queue: Passed through to the task queue - see the task queue documentation for details.   
`*args` |  Positional arguments to call the callable with.   
`**kwargs` |  Any other keyword arguments are passed through to the callable.   
  
## Returns  
  
---  
A taskqueue.Task object which represents an enqueued callable.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
