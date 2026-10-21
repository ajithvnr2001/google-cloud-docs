---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInfoExternal/
title: google.appengine.api.appinfo.AppInfoExternal \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:00:17.471239+00:00
---

# google.appengine.api.appinfo.AppInfoExternal  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInfoExternal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.AppInfoExternal Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2291-L2665) Class representing users application info. Inherits From: [`Validated`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated), [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.AppInfoExternal(
        **attributes
    )
    

This class is passed to a `yaml_object` builder to provide the validation for the application information file format parser. | 

## Raises  
  
---  
  
`AttributeDefinitionError` |  When class instance is missing `ATTRIBUTE` definition or when `ATTRIBUTE` is of the wrong type.   
  
## Attributes  
  
---  
  
`application` |  Unique identifier for application.   
`version` |  Application's major version.   
`runtime` |  Runtime used by application.   
`api_version` |  Which version of APIs to use.   
`source_language` |  Optional specification of the source language. For example, you could specify `php-quercus` if this is a Java app that was generated from PHP source using Quercus.   
`handlers` |  List of URL handlers.   
`default_expiration` |  Default time delta to use for cache expiration for all static files, unless they have their own specific `expiration` set. See the documentation for the `URLMap.expiration` field for more information.   
`skip_files` |  A regular expression object. Files that match this regular expression will not be uploaded by `appcfg.py`. For example:: skip_files: | .svn._| #._ #   
`nobuild_files` |  A regular expression object. Files that match this regular expression will not be built into the app. This directive is valid for Go only.   
`api_config` |  URL root and script or servlet path for enhanced API serving.   
`service_account` |  Service account that the deployed app will run as.   
  
## Methods

### `ApplyBackendSettings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2550-L2591)
    
    
    ApplyBackendSettings(
        backend_name
    )
    

Applies settings from the indicated backend to the `AppInfoExternal`.

Backend entries can contain directives that modify other parts of the `app.yaml` file, such as the `start` directive, which adds a handler for the start request. This method performs those modifications.

Args  
---  
  
`backend_name` |  The name of a backend that is defined in the `backends` directive.   
  
Raises  
---  
  
`BackendNotFound` |  If the indicated backend was not listed in the `backends` directive.   
`DuplicateBackend` |  If the backend is found more than once in the `backends` directive.   
  
### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2394-L2507)
    
    
    CheckInitialized()
    

Performs non-regular expression-based validation.

The following are verified:
    
    
    - At least one URL mapping is provided in the URL mappers.
    - The number of URL mappers doesn't exceed `MAX_URL_MAPS`.
    - The major version does not contain the string `-dot-`.
    - If `api_endpoints` are defined, an `api_config` stanza must be
      defined.
    - If the `runtime` is `python27` and `threadsafe` is set, then no CGI
      handlers can be used.
    - The version name doesn't start with `BUILTIN_NAME_PREFIX`.
    - If `redirect_http_response_code` exists, it is in the list of valid
      300s.
    - Module and service aren't both set. Services were formerly known as
      modules.
    

Raises  
---  
  
`DuplicateLibrary` |  If `library_name` is specified more than once.   
`MissingURLMapping` |  If no `URLMap` object is present in the object.   
`TooManyURLMappings` |  If there are too many `URLMap` entries.   
`MissingApiConfig` |  If `api_endpoints` exists without an `api_config`.   
`ThreadsafeWithCgiHandler` |  If the `runtime` is `python27`, `max_concurrent_requests` under `automatic_scaling` is not 1 and CGI handlers are specified.   
`TooManyScalingSettingsError` |  If more than one scaling settings block is present.   
`RuntimeDoesNotSupportLibraries` |  If the libraries clause is used for a runtime that does not support it, such as `python25`.   
  
### `Get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L366-L378)
    
    
    Get(
        key
    )
    

Get a single value on Validated instance.

This method can only be used to retrieve validated attributes.

Args  
---  
  
`key` |  The name of the attributes   
  
Raises  
---  
`ValidationError` when no validated attribute exists on class.   
  
### `GetAllLibraries`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2509-L2531)
    
    
    GetAllLibraries()
    

Returns a list of all `Library` instances active for this configuration.

Returns  
---  
The list of active `Library` instances for this configuration. This includes directly-specified libraries as well as any required dependencies.   
  
### `GetEffectiveRuntime`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2593-L2606)
    
    
    GetEffectiveRuntime()
    

Returns the app's runtime, resolving VMs to the underlying `vm_runtime`.

Returns  
---  
The effective runtime: The value of `beta/vm_settings.vm_runtime` if `runtime` is `vm`, or `runtime` otherwise.   
  
### `GetNormalizedLibraries`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2533-L2548)
    
    
    GetNormalizedLibraries()
    

Returns a list of normalized `Library` instances for this configuration.

Returns  
---  
The list of active `Library` instances for this configuration. This includes directly-specified libraries, their required dependencies, and any libraries enabled by default. Any libraries with `latest` as their version will be replaced with the latest available version.   
  
### `GetUnnormalized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L358-L364)
    
    
    GetUnnormalized(
        key
    )
    

Get a single value on the `Validated` instance, without normalizing.

### `GetValidator`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L317-L335)
    
    
    @classmethod
    GetValidator(
        key
    )
    

Safely get the underlying attribute definition as a `Validator`.

Args  
---  
  
`key` |  Name of attribute to get.   
  
Returns  
---  
Validator associated with key or attribute value wrapped in a validator.   
  
Raises  
---  
  
`ValidationError` |  if no such attribute exists.   
  
### `GetWarnings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L337-L342)
    
    
    GetWarnings()
    

Return all the warnings we've got, along with their associated fields.

Returns  
---  
A list of tuples of (dotted_field, warning), both strings.   
  
### `IsThreadsafe`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2659-L2665)
    
    
    IsThreadsafe()
    

### `IsVm`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2655-L2657)
    
    
    IsVm()
    

### `NormalizeVmSettings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2625-L2652)
    
    
    NormalizeVmSettings()
    

Normalizes VM settings.

### `Set`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L344-L356)
    
    
    Set(
        key, value
    )
    

Set a single value on `Validated` instance.

This method can only be used to assign validated attributes.

Args  
---  
  
`key` |  The name of the attributes   
`value` |  The value to set   
  
Raises  
---  
`ValidationError` when no validated attribute exists on class.   
  
### `SetEffectiveRuntime`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2608-L2623)
    
    
    SetEffectiveRuntime(
        runtime
    )
    

Sets the runtime while respecting vm runtimes rules for runtime settings.

Args  
---  
  
`runtime` |  The runtime to use.   
  
### `SetMultiple`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L197-L209)
    
    
    SetMultiple(
        attributes
    )
    

Set multiple values on Validated instance.

All attributes will be validated before being set.

Args  
---  
  
`attributes` |  A dict of attributes/items to set.   
  
Raises  
---  
  
`ValidationError` |  When no validated attribute exists on class.   
  
### `ToDict`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L476-L494)
    
    
    ToDict()
    

Convert Validated object to a dictionary.

Recursively traverses all of its elements and converts everything to simplified collections.

Returns  
---  
A dict of all attributes defined in this classes `ATTRIBUTES` mapped to its value. This structure is recursive in that Validated objects that are referenced by this object and in lists are also converted to dicts.   
  
### `ToYAML`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L251-L260)
    
    
    ToYAML()
    

Print validated object as simplified YAML.

Returns  
---  
Object as a simplified YAML string compatible with parsing using the `SafeLoader`.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L437-L454)
    
    
    __eq__(
        other
    )
    

Equality operator.

Comparison is done by comparing all attribute values to those in the other instance. Objects which are not of the same type are not equal.

Args  
---  
  
`other` |  Other object to compare against.   
  
Returns  
---  
`True` if validated objects are equal, else `False`.   
  
### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L456-L458)
    
    
    __ne__(
        other
    )
    

Inequality operator.

## Class Variables  
  
---  
  
ATTRIBUTES | 
    
    
    {
     'admin_console': <google.appengine.api.validation.Optional object>,
     'api_config': <google.appengine.api.validation.Optional object>,
     'api_version': <google.appengine.api.validation.Optional object>,
     'app_engine_apis': <google.appengine.api.validation.Optional object>,
     'application': <google.appengine.api.validation.Optional object>,
     'auto_id_policy': <google.appengine.api.validation.Optional object>,
     'automatic_scaling': <google.appengine.api.validation.Optional object>,
     'backends': <google.appengine.api.validation.Optional object>,
     'basic_scaling': <google.appengine.api.validation.Optional object>,
     'beta_settings': <google.appengine.api.validation.Optional object>,
     'build_env_variables': <google.appengine.api.validation.Optional object>,
     'builtins': <google.appengine.api.validation.Optional object>,
     'code_lock': <google.appengine.api.validation.Optional object>,
     'default_expiration': <google.appengine.api.validation.Optional object>,
     'derived_file_type': <google.appengine.api.validation.Optional object>,
     'endpoints_api_service': <google.appengine.api.validation.Optional object>,
     'entrypoint': <google.appengine.api.validation.Optional object>,
     'env': <google.appengine.api.validation.Optional object>,
     'env_variables': <google.appengine.api.validation.Optional object>,
     'error_handlers': <google.appengine.api.validation.Optional object>,
     'handlers': <google.appengine.api.validation.Optional object>,
     'health_check': <google.appengine.api.validation.Optional object>,
     'inbound_services': <google.appengine.api.validation.Optional object>,
     'includes': <google.appengine.api.validation.Optional object>,
     'instance_class': <google.appengine.api.validation.Optional object>,
     'libraries': <google.appengine.api.validation.Optional object>,
     'liveness_check': <google.appengine.api.validation.Optional object>,
     'main': <google.appengine.api.validation.Optional object>,
     'manual_scaling': <google.appengine.api.validation.Optional object>,
     'module': <google.appengine.api.validation.Deprecated object>,
     'network': <google.appengine.api.validation.Optional object>,
     'nobuild_files': <google.appengine.api.validation.RegexStr object>,
     'project': <google.appengine.api.validation.Optional object>,
     'readiness_check': <google.appengine.api.validation.Optional object>,
     'resources': <google.appengine.api.validation.Optional object>,
     'runtime': <google.appengine.api.validation.Optional object>,
     'runtime_channel': <google.appengine.api.validation.Optional object>,
     'runtime_config': <google.appengine.api.validation.Optional object>,
     'service': <google.appengine.api.validation.Preferred object>,
     'service_account': <google.appengine.api.validation.Optional object>,
     'skip_files': <google.appengine.api.validation.RegexStr object>,
     'source_language': <google.appengine.api.validation.Optional object>,
     'standard_websocket': <google.appengine.api.validation.Optional object>,
     'threadsafe': <google.appengine.api.validation.Optional object>,
     'version': <google.appengine.api.validation.Optional object>,
     'vm': <google.appengine.api.validation.Optional object>,
     'vm_health_check': <google.appengine.api.validation.Optional object>,
     'vm_settings': <google.appengine.api.validation.Optional object>,
     'vpc_access_connector': <google.appengine.api.validation.Optional object>,
     'zones': <google.appengine.api.validation.Optional object>
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
