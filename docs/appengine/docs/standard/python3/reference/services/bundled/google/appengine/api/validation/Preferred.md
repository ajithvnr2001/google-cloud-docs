---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Preferred/
title: google.appengine.api.validation.Preferred \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:22:57.663722+00:00
---

# google.appengine.api.validation.Preferred  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Preferred/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.validation.Preferred Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L1469-L1510) A non-deprecated field when there's a deprecated one. Inherits From: [`Normalized`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Normalized), [`Validator`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.validation.Preferred(
        deprecated, validator, default=None
    )
    

For use with Deprecated. Only works as a field on `Validated`. Both fields will work for value access. It's an error to set both the deprecated and the corresponding preferred field. | 

## Args  
  
---  
  
`deprecated` |  The name of the corresponding deprecated field   
`validator` |  The validator for the actual value of this field.   
`default` |  The default value for this field.   
  
## Child Classes

[`class expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

## Methods

### `CheckFieldInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L1493-L1502)
    
    
    CheckFieldInitialized(
        value, key, obj
    )
    

Check for missing fields or conflicts between fields.

Default behavior performs a simple `None`-check, but this can be overridden. If the intent is to allow optional fields, then use the `Optional` validator instead.

Args  
---  
  
`value` |  Value to validate.   
`key` |  Name of the field being validated.   
`obj` |  The object to validate against.   
  
Raises  
---  
  
`ValidationError` |  When there are missing or conflicting fields.   
  
### `Get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L1504-L1510)
    
    
    Get(
        value, key, obj
    )
    

Returns the normalized value. Subclasses must override.

### `GetWarnings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L722-L738)
    
    
    GetWarnings(
        value, key, obj
    )
    

Return any warnings on this attribute.

Validates the value with an eye towards things that aren't fatal problems.

Args  
---  
  
`value` |  Value to validate.   
`key` |  Name of the field being validated.   
`obj` |  The object to validate against.   
  
Returns  
---  
A list of tuples (context, warning) where 

  * Context is the field (or dotted field path, if a sub-field)
  * Warning is the string warning text 

  
  
### `ToValue`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L707-L720)
    
    
    ToValue(
        value
    )
    

Convert `value` to a simplified collection or basic type.

Subclasses of `Validator` should override this method when the dumped representation of `value` is not a simple `<type>(value)` (e.g., a regex).

Args  
---  
  
`value` |  An object of the same type that was returned from `Validate()`.   
  
Returns  
---  
An instance of a builtin type (e.g., int, str, dict, etc). By default it returns `value` unmodified.   
  
### `Validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L1461-L1462)
    
    
    Validate(
        value, key
    )
    

Validate this field. Override to customize subclass behavior.

Args  
---  
  
`value` |  Value to validate.   
`key` |  Name of the field being validated.   
  
Returns  
---  
Value if value is valid, or a valid representation of value.   
  
### `__call__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L673-L675)
    
    
    __call__(
        value, key='???'
    )
    

Main interface to validator is call mechanism.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
