---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/capabilities/capability_stub/CapabilityServiceStub/
title: google.appengine.api.capabilities.capability_stub.CapabilityServiceStub \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:11.770066+00:00
---

# google.appengine.api.capabilities.capability_stub.CapabilityServiceStub  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/capabilities/capability_stub/CapabilityServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.capabilities.capability_stub.CapabilityServiceStub Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/capabilities/capability_stub.py#L63-L164) Capability service stub. Inherits From: [`APIProxyStub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub/APIProxyStub), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.capabilities.capability_stub.CapabilityServiceStub(
        service_name='capability_service'
    )
    

| 

## Args  
  
---  
  
`service_name` |  Service name expected for all calls.   
  
## Methods

### `Clear`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/capabilities/capability_stub.py#L163-L164)
    
    
    Clear()
    

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
  
### `SetCapabilityStatus`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/capabilities/capability_stub.py#L100-L126)
    
    
    SetCapabilityStatus(
        package, capability, status
    )
    

Set the status of an individual capability.

This method is thread-unsafe, so should only be called during set-up, before multiple API server threads start.

Args  
---  
  
`package` |  String name of package containing the capability.   
`capability` |  String capability name.   
`status` |  The CapabilityConfig status enum to set.   
  
Raises  
---  
  
`KeyError` |  When an unsupported package or capability is requested.   
  
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
  
### `SetPackageEnabled`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/capabilities/capability_stub.py#L77-L98)
    
    
    SetPackageEnabled(
        package, enabled
    )
    

Set all features of a given package to enabled.

This method is thread-unsafe, so should only be called during set-up, before multiple API server threads start.

Args  
---  
  
`package` |  Name of package.   
`enabled` |  True to enable, False to disable.   
  
Raises  
---  
  
`KeyError` |  When an unsupported package is requested.   
  
## Class Variables  
  
---  
  
THREADSAFE |  `True`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
