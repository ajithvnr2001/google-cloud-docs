---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/ListOfHooks/
title: google.appengine.api.apiproxy_stub_map.ListOfHooks \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:28:58.968546+00:00
---

# google.appengine.api.apiproxy_stub_map.ListOfHooks  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/ListOfHooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.apiproxy_stub_map.ListOfHooks Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L99-L210) An ordered collection of hooks for a particular API call. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.apiproxy_stub_map.ListOfHooks()
    

A hook is a function that has exactly the same signature as a service stub. It will be called before or after an API hook is executed, depending on whether this list is for precall of postcall hooks. Hooks can be used for debugging purposes (check certain pre- or postconditions on api calls) or to apply patches to protocol buffers before/after a call gets submitted.

## Methods

### `Append`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L148-L161)
    
    
    Append(
        key, function, service=None
    )
    

Appends a hook at the end of the list. | Args  
---  
  
`key` |  A unique key (within the module) for this particular function. If something from the same module with the same key is already registered, nothing will be added.   
`function` |  The hook to be added.   
`service` |  Optional argument that restricts the hook to a particular API.   
  
Returns  
---  
`True` if the collection was modified.   
  
### `Call`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L183-L210)
    
    
    Call(
        service, call, request, response, rpc=None, error=None
    )
    

Invokes all hooks in this collection.

NOTE: For backwards compatibility, if error is not `None`, hooks with 4 or 5 arguments are _not_ called. This situation (`error=None`) only occurs when the RPC request raised an exception; in the past no hooks would be called at all in that case.

Args  
---  
  
`service` |  `string`. Represents which service to call.   
`call` |  `string`. Representswhich function to call.   
`request` |  Protocol buffer for the request.   
`response` |  Protocol buffer for the response.   
`rpc` |  Optional RPC used to make this call.   
`error` |  Optional `Exception` instance to be passed as sixth argument.   
  
### `Clear`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L178-L181)
    
    
    Clear()
    

Removes all hooks from the list (useful for unit tests).

### `Push`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L163-L176)
    
    
    Push(
        key, function, service=None
    )
    

Inserts a hook at the beginning of the list.

Args  
---  
  
`key` |  A unique key (within the module) for this particular function. If something from the same module with the same key is already registered, nothing will be added.   
`function` |  The hook to be added.   
`service` |  Optional argument that restricts the hook to a particular API.   
  
Returns  
---  
`True` if the collection was modified.   
  
### `__len__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L119-L121)
    
    
    __len__()
    

Returns the amount of elements in the collection.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
