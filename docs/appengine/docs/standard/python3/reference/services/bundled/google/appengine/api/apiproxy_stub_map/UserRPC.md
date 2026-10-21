---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/UserRPC/
title: google.appengine.api.apiproxy_stub_map.UserRPC \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:18:05.346779+00:00
---

# google.appengine.api.apiproxy_stub_map.UserRPC  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/UserRPC/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.apiproxy_stub_map.UserRPC Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L378-L768) Wrapper class for asynchronous RPC. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.apiproxy_stub_map.UserRPC(
        service, deadline=None, callback=None, stubmap=None
    )
    

Simplest low-level usage pattern:
    
    
      rpc = UserRPC('service', [deadline], [callback])
      rpc.make_call('method', request, response)
      .
      .
      .
      rpc.wait()
      rpc.check_success()
    

However, a service module normally provides a wrapper so that the typical usage pattern becomes more like this:
    
    
      from google.appengine.api import service
      rpc = service.create_rpc([deadline], [callback])
      service.make_method_call(rpc, [service-specific-args])
      .
      .
      .
      rpc.wait()
      result = rpc.get_result()
    

The `service.make_method_call()` function sets a service- and method- specific hook function that is called by `rpc.get_result()` with the rpc object as its first argument, and service-specific value as its second argument. The hook function should call `rpc.check_success()` and then extract the user-level result from the `rpc.result` protobuffer. Additional arguments may be passed from `make_method_call()` to the `get_result` hook via the second argument. Also note `wait_any()` and `wait_all()`, which wait for multiple RPCs. | 

## Args  
  
---  
  
`service` |  The service name.   
`deadline` |  Optional deadline. Default depends on the implementation.   
`callback` |  Optional argument-less callback function.   
`stubmap` |  optional APIProxyStubMap instance, for dependency injection.   
  
## Attributes  
  
---  
  
`deadline` |  Return the deadline, if set explicitly (otherwise `None`).   
`future` |  Return the underlying RPC's future, if present.   
`get_result_hook` |  Return the get-result hook function.   
`method` |  Return the method name.   
`request` |  Return the request protocol buffer object.   
`response` |  Return the response protocol buffer object.   
`service` |  Return the service name.   
`state` |  Return the RPC state. Possible values are attributes of apiproxy_rpc.RPC: IDLE, RUNNING, FINISHING.   
`user_data` |  Return the user data for the hook function.   
  
## Child Classes

[`class MyLocal`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/UserRPC/MyLocal)

## Methods

### `check_success`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L601-L629)
    
    
    check_success()
    

Check for success of the RPC, possibly raising an exception.

This function should be called at least once per RPC. If `wait()` hasn't been called yet, it is called first. If the RPC caused an exceptional condition, an exception will be raised here. The first time `check_success()` is called, the postcall hooks are called.

### `get_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L631-L648)
    
    
    get_result()
    

Get the result of the RPC, or possibly raise an exception.

This implies a call to `check_success()`. If a get-result hook was passed to `make_call()`, that hook is responsible for calling `check_success()`, and the return value of the hook is returned. Otherwise, `check_success()` is called directly and `None` is returned.

### `make_call`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L532-L565)
    
    
    make_call(
        method, request, response, get_result_hook=None, user_data=None
    )
    

Initiate a call.

Args  
---  
  
`method` |  The method name.   
`request` |  The request protocol buffer.   
`response` |  The response protocol buffer.   
`get_result_hook` |  Optional get-result hook function. If not `None`, this must be a function with exactly one argument, the RPC object (`self`). Its return value is returned from `get_result()`.   
`user_data` |  Optional additional arbitrary data for the get-result hook function. This can be accessed as `rpc.user_data`. The type of this value is up to the service module.   
  
This function may only be called once per RPC object. It sends the request to the remote server, but does not wait for a response. This allows concurrent execution of the remote call and further local processing (e.g., making additional remote calls).

Before the call is initiated, the precall hooks are called.

### `wait`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L567-L592)
    
    
    wait()
    

Wait for the call to complete, and call callback if needed.

This and `wait_any()`/`wait_all()` are the only time callback functions may be called. (However, note that `check_success()` and `get_result()` call `wait()`.) Waiting for one RPC will not cause callbacks for other RPCs to be called. Callback functions may call `check_success()` and `get_result()`.

Callbacks are called without arguments; if a callback needs access to the RPC object a Python nested function (a.k.a. closure) or a bound may be used. To facilitate this, the callback may be assigned after the RPC object is created (but before `make_call()` is called).

**Note:** Don't confuse callbacks with get-result hooks or precall and postcall hooks.

### `wait_all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L751-L768)
    
    
    @classmethod
    wait_all(
        rpcs
    )
    

Wait until all given RPCs are finished.

This is a thin wrapper around `wait_any()` that loops until all given RPCs have finished.

Args  
---  
  
`rpcs` |  Iterable collection of `UserRPC` instances.   
  
Returns  
---  
None.   
  
### `wait_any`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub_map.py#L693-L749)
    
    
    @classmethod
    wait_any(
        rpcs
    )
    

Wait until an RPC is finished.

A `WaitCanceller` can also be included in the list of RPCs as a mechanism to cancel the wait.

Args  
---  
  
`rpcs` |  Iterable collection of `UserRPC` or `WaitCanceller` instances.   
  
Returns  
---  
A `UserRPC` instance, indicating the first RPC among the given RPCs that finished; or `None`, indicating that either an RPC not among the given RPCs finished in the mean time, or the iterable is empty.   
  
#### NOTES:

  * Repeatedly calling `wait_any()` with the same arguments will not wait; it will immediately return, meaning it will return the same RPC until one earlier in the collection finishes. The callback, however, will only be called the first time the RPC finishes (which may be here or in the `wait()` method).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
