---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub/APIProxyStub/
title: google.appengine.api.apiproxy_stub.APIProxyStub \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:27.555880+00:00
---

# google.appengine.api.apiproxy_stub.APIProxyStub  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub/APIProxyStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.apiproxy_stub.APIProxyStub Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L46-L163) Base class for implementing API proxy stub classes. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.apiproxy_stub.APIProxyStub(
        service_name, max_request_size=MAX_REQUEST_SIZE, request_data=None
    )
    

To implement an API proxy stub:

  * Extend this class.
  * Override `__init__` to pass in appropriate default service name.
  * Implement service methods as `_Dynamic_<method>(request, response)`.

| 

## Args  
  
---  
  
`service_name` |  Service name expected for all calls.   
`max_request_size` |  `int`. Maximum allowable size of the incoming request. An `apiproxy_errors.RequestTooLargeError` will be raised if the inbound request exceeds this size. Default is 1 MB. Subclasses can override it.   
`request_data` |  A `request_info.RequestInfo` instance used to look up state associated with the request that generated an API call.   
  
## Methods

### `CreateRPC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L87-L93)
    
    
    CreateRPC()
    

Creates RPC object instance.

Returns  
---  
An instance of RPC.   
  
### `MakeSyncCall`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L112-L143)
    
    
    MakeSyncCall(
        service, call, request, response, request_id=None
    )
    

The main RPC entry point.

Args  
---  
  
`service` |  Must be name as provided to `service_name` of constructor.   
`call` |  A string representing the rpc to make. Must be part of the underlying services methods and impemented by `_Dynamic_<call>`.   
`request` |  A protocol buffer of the type corresponding to `call`.   
`response` |  A protocol buffer of the type corresponding to `call`.   
`request_id` |  A unique string identifying the request associated with the API call.   
  
### `SetError`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L145-L163)
    
    
    SetError(
        error, method=None, error_rate=1
    )
    

Set an error condition that may be raised when calls made to stub.

If a method is specified, the error will only apply to that call. The error rate is applied to the method specified or all calls if method is not set.

Args  
---  
  
`error` |  An instance of [`apiproxy_errors.Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/apiproxy_errors/Error) or `None` for no error.   
`method` |  A string representing the method that the error will affect.   
`error_rate` |  a number from `[0, 1]` that sets the chance of the error, defaults to `1`.   
  
## Class Variables  
  
---  
  
THREADSAFE |  `False`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
