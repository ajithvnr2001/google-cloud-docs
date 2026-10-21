---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/create_rpc/
title: google.appengine.api.taskqueue.create_rpc \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:02:33.264882+00:00
---

# google.appengine.api.taskqueue.create_rpc  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/create_rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.taskqueue.create_rpc Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L555-L575) Creates an RPC object for use with the Task Queue API.
    
    
    google.appengine.api.taskqueue.create_rpc(
        deadline=None, callback=None
    )
    

| 

## Args  
  
---  
  
`deadline` |  Optional deadline in seconds for the operation; the default value is a system-specific deadline, which is typically 5 seconds. After the deadline, a `DeadlineExceededError` error will be returned.   
`callback` |  Optional function to be called with the Task Queue service returns results successfully when `get_result()`, `check_success()`, or `wait()` is invoked on the RPC object. The function is called without arguments. The function is not called in a background process or thread; the function is only called when one of the above methods is called by the application. The function is called even if the request fails or the RPC deadline elapses.   
  
## Returns  
  
---  
An [`apiproxy_stub_map.UserRPC`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/UserRPC) object specialized for this service.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
