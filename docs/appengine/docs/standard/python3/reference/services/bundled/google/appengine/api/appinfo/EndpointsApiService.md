---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/EndpointsApiService/
title: google.appengine.api.appinfo.EndpointsApiService \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:02.979287+00:00
---

# google.appengine.api.appinfo.EndpointsApiService  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/EndpointsApiService/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.EndpointsApiService Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1733-L1766) Class representing EndpointsApiService in AppInfoExternal. Inherits From: [`Validated`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated), [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.EndpointsApiService(
        **attributes
    )
    

| 

## Raises  
  
---  
  
`AttributeDefinitionError` |  When class instance is missing `ATTRIBUTE` definition or when `ATTRIBUTE` is of the wrong type.   
  
## Methods

### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1748-L1766)
    
    
    CheckInitialized()
    

Determines if the Endpoints API Service is not valid.

Raises  
---  
  
`appinfo_errors.MissingEndpointsConfigId` |  If the config id is missing when the rollout strategy is unspecified or set to "fixed".   
`appinfo_errors.UnexpectedEndpointsConfigId` |  If the config id is set when the rollout strategy is "managed".   
  
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
     'config_id': <google.appengine.api.validation.Optional object>,
     'name': <google.appengine.api.validation.Regex object>,
     'rollout_strategy': <google.appengine.api.validation.Optional object>,
     'trace_sampling': <google.appengine.api.validation.Optional object>
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
