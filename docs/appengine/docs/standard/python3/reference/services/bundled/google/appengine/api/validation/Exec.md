---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Exec/
title: google.appengine.api.validation.Exec \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:56:13.888092+00:00
---

# google.appengine.api.validation.Exec  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Exec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.validation.Exec Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L858-L886) Coerces the value to accommodate Docker `CMD/ENTRYPOINT` requirements. Inherits From: [`Type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Type), [`Validator`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.validation.Exec(
        default=None
    )
    

Validates the value is a string, then tries to modify the string (if necessary) so that the command represented will become `PID` 1 inside the Docker container. See Docker documentation on `docker kill` for more information: https://docs.docker.com/engine/reference/commandline/kill/. If the command already starts with `exec` or appears to be in "exec form" (starts with `[`), no further action is needed. Otherwise, prepend the command with `exec` so that it will become `PID 1` on execution.

## Child Classes

[`class expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

## Methods

### `CheckFieldInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L689-L705)
    
    
    CheckFieldInitialized(
        value, key, obj
    )
    

Check for missing fields or conflicts between fields. Default behavior performs a simple `None`-check, but this can be overridden. If the intent is to allow optional fields, then use the `Optional` validator instead. | Args  
---  
  
`value` |  Value to validate.   
`key` |  Name of the field being validated.   
`obj` |  The object to validate against.   
  
Raises  
---  
  
`ValidationError` |  When there are missing or conflicting fields.   
  
### `GetWarnings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L838-L843)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L875-L886)
    
    
    Validate(
        value, key
    )
    

Validate according to parent behavior and coerce to start with `exec`.

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
