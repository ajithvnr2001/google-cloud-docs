---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/APIProxyStubMap/
title: google.appengine.api.apiproxy_stub_map.APIProxyStubMap \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:32.784235+00:00
---

# google.appengine.api.apiproxy_stub_map.APIProxyStubMap  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/APIProxyStubMap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.apiproxy_stub_map.APIProxyStubMap Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L235-L375) Container of APIProxy stubs for more convenient unittesting. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.apiproxy_stub_map.APIProxyStubMap(
        default_stub=None
    )
    

Stubs may be either trivial implementations of APIProxy services (e.g. DatastoreFileStub, UserServiceStub) or "real" implementations. For unittests, we may want to mix and match real and trivial implementations of services in order to better focus testing on individual service implementations. To achieve this, we allow the client to attach stubs to service names, as well as define a default stub to be used if no specific matching stub is identified. | 

## Args  
  
---  
  
`default_stub` |  optional stub. `default_stub` will be used whenever no specific matching stub is found.   
  
## Methods

### `CancelApiCalls`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L373-L375)
    
    
    CancelApiCalls()
    

### `GetPostCallHooks`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L270-L272)
    
    
    GetPostCallHooks()
    

Gets a collection for all precall hooks.

### `GetPreCallHooks`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L266-L268)
    
    
    GetPreCallHooks()
    

Gets a collection for all precall hooks.

### `GetStub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L305-L317)
    
    
    GetStub(
        service
    )
    

Retrieve the stub registered for the specified service.

Args  
---  
  
`service` |  string   
  
Returns  
---  
stub   
  
Returns the stub registered for 'service', and returns the default stub if no such stub is found.

### `MakeSyncCall`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L327-L371)
    
    
    MakeSyncCall(
        service, call, request, response
    )
    

The APIProxy entry point.

Args  
---  
  
`service` |  string representing which service to call   
`call` |  string representing which function to call   
`request` |  protocol buffer for the request   
`response` |  protocol buffer for the response   
  
Returns  
---  
Response protocol buffer or `None`. Some implementations may return a response protocol buffer instead of modifying `response`. Caller must use returned value in such cases. If `response` is modified then returns `None`.   
  
Raises  
---  
[`apiproxy_errors.Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/apiproxy_errors/Error) or a subclass.   
  
### `RegisterStub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L295-L303)
    
    
    RegisterStub(
        service, stub
    )
    

Register the provided stub for the specified service.

Args  
---  
  
`service` |  string   
`stub` |  stub   
  
### `ReplaceStub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L274-L293)
    
    
    ReplaceStub(
        service, stub
    )
    

Replace the existing stub for the specified service with a new one.

NOTE: This is a risky operation; external callers should use this with caution.

Args  
---  
  
`service` |  string   
`stub` |  stub   
  
### `SetDefaultStub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L263-L264)
    
    
    SetDefaultStub(
        stub
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
