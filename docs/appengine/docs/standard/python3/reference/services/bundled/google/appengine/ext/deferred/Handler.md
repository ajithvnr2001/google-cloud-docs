---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/Handler/
title: google.appengine.ext.deferred.Handler \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:32:28.075532+00:00
---

# google.appengine.ext.deferred.Handler  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/Handler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.deferred.Handler Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/deferred/deferred.py#L313-L428) A handler class for processesing deferred invocations. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.deferred.deferred.Handler`

## Methods

### `post`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/deferred/deferred.py#L370-L405)
    
    
    post(
        environ
    )
    

Default behavior for POST requests to the deferred endpoint. If the Deferred API has been enabled, this function is automatically called after 'deferred.defer()' is used to defer a task. Behind the scenes, the TaskQueue service calls the default Deferred endpoint '/_ah/queue/deferred', which is routed to this function. If deferred.defer() is passed a custom '_url' parameter, POST requests to the custom endpoint needs to be handled by the app. To replicate the default behavior of executing a deferred task, this function can be called by the custom endpoint handler, and passed the WSGI 'environ' dictionary of the POST request. | Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333)   
  
Returns  
---  
  
`response` |  a string containing body of the response   
`status` |  HTTP status code of enum type http.HTTPStatus   
`headers` |  a dict containing response headers   
  
### `run_from_request`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/deferred/deferred.py#L316-L368)
    
    
    run_from_request(
        environ
    )
    

Executes deferred tasks after verifying the caller.

This function assumes that the WSGI environ dict originated from a POST request by the GAE TaskQueue service. It checks the caller IP and request headers to verify the caller. Args: environ: a WSGI dict describing the HTTP request (See PEP 333). Returns: response: a string containing body of the response status: HTTP status code of enum type http.HTTPStatus headers: a dict containing response headers Raises: PermanentTaskFailure if an error occurred during unpickling the task.

### `__call__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/deferred/deferred.py#L407-L428)
    
    
    __call__(
        environ, start_response
    )
    

WSGI app callable to handle POST requests to the deferred endpoint.

This function allows the 'Handler' class to behave like a WSGI app for handling Deferred task execution.

If the parent WSGI app is required to handle multiple kinds of requests, a dispatcher (compliant with the app's Web Framework) can be used to route an endpoint/URL to be handled by this callable.

Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333)   
`start_response` |  callable (See PEP 3333)   
  
Returns  
---  
list of bytes response   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
