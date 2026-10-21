---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_rpc/RPC/
title: google.appengine.api.apiproxy_rpc.RPC \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:42:20.393726+00:00
---

# google.appengine.api.apiproxy_rpc.RPC  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_rpc/RPC/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.apiproxy_rpc.RPC Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_rpc.py#L44-L239) Base class for implementing RPC of API proxy stubs. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.apiproxy_rpc.RPC(
        package=None,
        call=None,
        request=None,
        response=None,
        callback=None,
        deadline=None,
        stub=None
    )
    

Constructor for the RPC object. All arguments are optional, and simply set members on the class. These data members will be overriden by values passed to `MakeCall`. | 

## Args  
  
---  
  
`package` |  `string`. The package for the call.   
`call` |  `string`. The call within the package.   
`request` |  `ProtocolMessage` instance. Appropriate for the arguments.   
`response` |  `ProtocolMessage` instance. Appropriate for the response.   
`callback` |  `callable`. Called when call is complete.   
`deadline` |  `double`. Specifies the deadline for this call as the number of seconds from the current time. Ignored if non-positive.   
`stub` |  `APIProxyStub` instance. Used in default `_WaitImpl` to do real call.   
  
## Attributes  
  
---  
  
`exception` |   
`state` |   
  
## Methods

### `CheckSuccess`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_rpc.py#L142-L149)
    
    
    CheckSuccess()
    

If there was an exception, raise it now.

Raises  
---  
Exception of the API call or the `callback`, if any.   
  
### `Clone`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_rpc.py#L85-L101)
    
    
    Clone()
    

Make a shallow copy of this instances attributes, excluding methods.

This is usually used when an RPC has been specified with some configuration options and is being used as a template for multiple RPCs outside of a developer's easy control.

Returns  
---  
A clone of this RPC.   
  
### `MakeCall`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_rpc.py#L103-L133)
    
    
    MakeCall(
        package=None,
        call=None,
        request=None,
        response=None,
        callback=None,
        deadline=None
    )
    

Makes an asynchronous (i.e., non-blocking) API call within the specified package for the specified call method.

It will call the `_MakeRealCall` to do the real job.

Args  
---  
  
`package` |  `string`. The package for the call.   
`call` |  `string`. The call within the package.   
`request` |  `ProtocolMessage` instance. Appropriate for the arguments.   
`response` |  `ProtocolMessage` instance. Appropriate for the response.   
`callback` |  `callable`. Called when call is complete.   
`deadline` |  `double`. Specifies the deadline for this call as the number of seconds from the current time. Ignored if non-positive.   
  
Raises  
---  
`TypeError` or `AssertionError` if an argument is of an invalid type. `AssertionError` or `RuntimeError` is an RPC is already in use.   
  
### `Wait`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_rpc.py#L135-L140)
    
    
    Wait()
    

Waits on the API call associated with this RPC.

## Class Variables  
  
---  
  
FINISHING |  `2`  
IDLE |  `0`  
RUNNING |  `1`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
