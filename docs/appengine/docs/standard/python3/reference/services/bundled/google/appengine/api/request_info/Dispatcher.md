---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/Dispatcher/
title: google.appengine.api.request_info.Dispatcher \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:05:48.840141+00:00
---

# google.appengine.api.request_info.Dispatcher  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/Dispatcher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.request_info.Dispatcher Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L73-L280) Provides information about and dispatches requests to modules. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

## Methods

### `add_async_request`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L241-L260)
    
    
    add_async_request(
        method,
        relative_url,
        headers,
        body,
        source_ip,
        module_name=None,
        version=None,
        instance_id=None
    )
    

Dispatch an HTTP request asynchronously. | Args  
---  
  
`method` |  A str containing the HTTP method of the request.   
`relative_url` |  A str containing path and query string of the request.   
`headers` |  A list of (key, value) tuples where key and value are both str.   
`body` |  A str containing the request body.   
`source_ip` |  The source ip address for the request.   
`module_name` |  An optional str containing the module name to service this request. If unset, the request will be dispatched to the default module.   
`version` |  An optional str containing the version to service this request. If unset, the request will be dispatched to the default version.   
`instance_id` |  An optional str containing the instance_id of the instance to service this request. If unset, the request will be dispatched to according to the load-balancing for the module and version.   
  
### `add_event`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L191-L203)
    
    
    add_event(
        runnable, eta, service=None, event_id=None
    )
    

Add a callable to be run at the specified time.

Args  
---  
  
`runnable` |  A callable object to call at the specified time.   
`eta` |  An int containing the time to run the event, in seconds since the epoch.   
`service` |  A str containing the name of the service that owns this event. This should be set if `event_id` is set.   
`event_id` |  A str containing the id of the event. If set, this can be passed to update_event to change the time at which the event should run.   
  
### `add_request`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L216-L239)
    
    
    add_request(
        method,
        relative_url,
        headers,
        body,
        source_ip,
        module_name=None,
        version=None,
        instance_id=None
    )
    

Process an HTTP request.

Args  
---  
  
`method` |  A str containing the HTTP method of the request.   
`relative_url` |  A str containing path and query string of the request.   
`headers` |  A list of (key, value) tuples where key and value are both str.   
`body` |  A str containing the request body.   
`source_ip` |  The source ip address for the request.   
`module_name` |  An optional str containing the module name to service this request. If unset, the request will be dispatched to the default module.   
`version` |  An optional str containing the version to service this request. If unset, the request will be dispatched to the default version.   
`instance_id` |  An optional str containing the `instance_id` of the instance to service this request. If unset, the request will be dispatched to according to the load-balancing for the module and version.   
  
Returns  
---  
A `ResponseTuple` containing the response information for the HTTP request.   
  
### `get_default_version`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L94-L106)
    
    
    get_default_version(
        module
    )
    

Returns the default version for a module.

Args  
---  
  
`module` |  A str containing the name of the module.   
  
Returns  
---  
A str containing the default version for the specified module.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
  
### `get_hostname`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L108-L128)
    
    
    get_hostname(
        module, version, instance=None
    )
    

Returns the hostname for a `(module, version, instance)` tuple.

If instance is set, this will return a hostname for that particular instances. Otherwise, it will return the hostname for load-balancing.

Args  
---  
  
`module` |  A str containing the name of the module.   
`version` |  A str containing the version.   
`instance` |  An optional str containing the instance `ID`.   
  
Returns  
---  
A str containing the hostname.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
`VersionDoesNotExistError` |  The version does not exist.   
`InvalidInstanceIdError` |  The instance `ID` is not valid for the module/version or the module/version uses automatic scaling.   
  
### `get_module_names`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L76-L78)
    
    
    get_module_names()
    

Returns a list of module names.

### `get_num_instances`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L146-L159)
    
    
    get_num_instances(
        module, version
    )
    

Gets the number of instances running for a version of a module.

Args  
---  
  
`module` |  A str containing the name of the module.   
`version` |  A str containing the version.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
`VersionDoesNotExistError` |  The version does not exist.   
`NotSupportedWithAutoScalingError` |  The provided module/version uses automatic scaling.   
  
### `get_versions`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L80-L92)
    
    
    get_versions(
        module
    )
    

Returns a list of versions for a module.

Args  
---  
  
`module` |  A str containing the name of the module.   
  
Returns  
---  
A list of str containing the versions for the specified module.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
  
### `send_background_request`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L262-L280)
    
    
    send_background_request(
        module_name, version, instance, background_request_id
    )
    

Dispatch a background thread request.

Args  
---  
  
`module_name` |  A str containing the module name to service this request.   
`version` |  A str containing the version to service this request.   
`instance` |  The instance to service this request.   
`background_request_id` |  A str containing the unique background thread request identifier.   
  
Raises  
---  
  
`NotSupportedWithAutoScalingError` |  The provided module/version uses automatic scaling.   
`BackgroundThreadLimitReachedError` |  The instance is at its background thread capacity.   
  
### `set_num_instances`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L130-L144)
    
    
    set_num_instances(
        module, version, instances
    )
    

Sets the number of instances to run for a version of a module.

Args  
---  
  
`module` |  A str containing the name of the module.   
`version` |  A str containing the version.   
`instances` |  An int containing the number of instances to run.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
`VersionDoesNotExistError` |  The version does not exist.   
`NotSupportedWithAutoScalingError` |  The provided module/version uses automatic scaling.   
  
### `start_version`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L161-L174)
    
    
    start_version(
        module, version
    )
    

Starts a version.

Args  
---  
  
`module` |  A str containing the name of the module.   
`version` |  A str containing the version.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
`VersionDoesNotExistError` |  The version does not exist.   
`NotSupportedWithAutoScalingError` |  The provided module/version uses automatic scaling.   
  
### `stop_version`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L176-L189)
    
    
    stop_version(
        module, version
    )
    

Stops a version.

Args  
---  
  
`module` |  A str containing the name of the module.   
`version` |  A str containing the version.   
  
Raises  
---  
  
`ModuleDoesNotExistError` |  The module does not exist.   
`VersionDoesNotExistError` |  The version does not exist.   
`NotSupportedWithAutoScalingError` |  The provided module/version uses automatic scaling.   
  
### `update_event`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py#L205-L214)
    
    
    update_event(
        eta, service, event_id
    )
    

Update the eta of a scheduled event.

Args  
---  
  
`eta` |  An int containing the time to run the event, in seconds since the epoch.   
`service` |  A str containing the name of the service that owns this event.   
`event_id` |  A str containing the id of the event to update.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
