---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BuiltinHandler/
title: google.appengine.api.appinfo.BuiltinHandler \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:03:08.482631+00:00
---

# google.appengine.api.appinfo.BuiltinHandler  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BuiltinHandler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.BuiltinHandler Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1446-L1640) Class representing built-in handler directives in application info. Inherits From: [`Validated`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated), [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.BuiltinHandler(
        **attributes
    )
    

This class permits arbitrary keys, but their values must be described by the [`validation.Options`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Options) object that is returned by `ATTRIBUTES`. | 

## Args  
  
---  
  
`**attributes` |  The attributes that you want to use.   
  
## Child Classes

[`class DynamicAttributes`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BuiltinHandler/DynamicAttributes)

## Methods

### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L395-L398)
    
    
    CheckInitialized()
    

Checks for missing or conflicting attributes.

Subclasses should override this function and raise an exception for any errors. Always run this method when all assignments are complete.

Raises  
---  
  
`ValidationError` |  When there are missing or conflicting attributes.   
  
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
  
### `GetUnnormalized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1549-L1553)
    
    
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
  
### `IsDefined`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1563-L1580)
    
    
    @classmethod
    IsDefined(
        builtins_list, builtin_name
    )
    

Finds if a builtin is defined in a given list of builtin handler objects.

Args  
---  
  
`builtins_list` |  A list of `BuiltinHandler` objects, typically `yaml.builtins`.   
`builtin_name` |  The name of the built-in that you want to determine whether it is defined.   
  
Returns  
---  
`True` if `builtin_name` is defined by a member of `builtins_list`; all other results return `False`.   
  
### `ListToTuples`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1582-L1593)
    
    
    @classmethod
    ListToTuples(
        builtins_list
    )
    

Converts a list of `BuiltinHandler` objects.

Args  
---  
  
`builtins_list` |  A list of `BuildinHandler` objects to convert to tuples.   
  
Returns  
---  
A list of `(name, status)` that is derived from the `BuiltinHandler` objects.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1555-L1561)
    
    
    ToDict()
    

Converts a `BuiltinHander` object to a dictionary.

Returns  
---  
A dictionary in `{builtin_handler_name: on/off}` form   
  
### `ToYAML`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L251-L260)
    
    
    ToYAML()
    

Print validated object as simplified YAML.

Returns  
---  
Object as a simplified YAML string compatible with parsing using the `SafeLoader`.   
  
### `Validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1595-L1640)
    
    
    @classmethod
    Validate(
        builtins_list, runtime=None
    )
    

Verifies that all `BuiltinHandler` objects are valid and not repeated.

Args  
---  
  
`builtins_list` |  A list of `BuiltinHandler` objects to validate.   
`runtime` |  If you specify this argument, warnings are generated for built-ins that have been deprecated in the given runtime.   
  
Raises  
---  
  
`InvalidBuiltinFormat` |  If the name of a `BuiltinHandler` object cannot be determined.   
`DuplicateBuiltinsSpecified` |  If a `BuiltinHandler` name is used more than once in the list.   
  
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
    
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
