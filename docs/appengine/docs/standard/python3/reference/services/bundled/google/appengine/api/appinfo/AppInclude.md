---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInclude/
title: google.appengine.api.appinfo.AppInclude \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:20:51.900415+00:00
---

# google.appengine.api.appinfo.AppInclude  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInclude/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.AppInclude Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2085-L2286) Class representing the contents of an included `app.yaml` file. Inherits From: [`Validated`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated), [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.AppInclude(
        **attributes
    )
    

This class is used for both `builtins` and `includes` directives. | 

## Raises  
  
---  
  
`AttributeDefinitionError` |  When class instance is missing `ATTRIBUTE` definition or when `ATTRIBUTE` is of the wrong type.   
  
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
  
### `MergeAppIncludes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2235-L2268)
    
    
    @classmethod
    MergeAppIncludes(
        appinclude_one, appinclude_two
    )
    

Merges the non-referential state of the provided `AppInclude`.

That is, `builtins` and `includes` directives are not preserved, but any static objects are copied into an aggregate `AppInclude` object that preserves the directives of both provided `AppInclude` objects.

`appinclude_one` is updated to be the merged result in this process.

Args  
---  
  
`appinclude_one` |  First `AppInclude` to merge.   
`appinclude_two` |  Second `AppInclude` to merge.   
  
Returns  
---  
`AppInclude` object that is the result of merging the static directives of `appinclude_one` and `appinclude_two`. An updated version of `appinclude_one` is returned.   
  
### `MergeAppYamlAppInclude`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2195-L2233)
    
    
    @classmethod
    MergeAppYamlAppInclude(
        appyaml, appinclude
    )
    

Merges an `app.yaml` file with referenced builtins/includes.

Args  
---  
  
`appyaml` |  The `app.yaml` file that you want to update with `appinclude`.   
`appinclude` |  The includes that you want to merge into `appyaml`.   
  
Returns  
---  
An updated `app.yaml` file that includes the directives you specified in `appinclude`.   
  
### `MergeManualScaling`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2110-L2153)
    
    
    @classmethod
    MergeManualScaling(
        appinclude_one, appinclude_two
    )
    

Takes the greater of `<manual_scaling.instances>` from the arguments.

`appinclude_one` is mutated to be the merged result in this process.

Also, this function must be updated if `ManualScaling` gets additional fields.

Args  
---  
  
`appinclude_one` |  The first object to merge. The object must have a `manual_scaling` field that contains a `ManualScaling()`.   
`appinclude_two` |  The second object to merge. The object must have a `manual_scaling` field that contains a `ManualScaling()`.   
  
Returns  
---  
An object that is the result of merging `appinclude_one.manual_scaling.instances` and `appinclude_two.manual_scaling.instances`; this is returned as a revised `appinclude_one` object after the mutations are complete.   
  
### `MergeSkipFiles`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2270-L2286)
    
    
    @staticmethod
    MergeSkipFiles(
        skip_files_one, skip_files_two
    )
    

Merges two `skip_files` directives.

Args  
---  
  
`skip_files_one` |  The first `skip_files` element that you want to merge.   
`skip_files_two` |  The second `skip_files` element that you want to merge.   
  
Returns  
---  
A list of regular expressions that are merged.   
  
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
     'beta_settings': <google.appengine.api.validation.Optional object>,
     'build_env_variables': <google.appengine.api.validation.Optional object>,
     'builtins': <google.appengine.api.validation.Optional object>,
     'env_variables': <google.appengine.api.validation.Optional object>,
     'handlers': <google.appengine.api.validation.Optional object>,
     'includes': <google.appengine.api.validation.Optional object>,
     'manual_scaling': <google.appengine.api.validation.Optional object>,
     'skip_files': <google.appengine.api.validation.RegexStr object>,
     'vm': <google.appengine.api.validation.Optional object>,
     'vm_settings': <google.appengine.api.validation.Optional object>
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
