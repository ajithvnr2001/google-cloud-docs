---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Regex/
title: google.appengine.api.validation.Regex \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:02:41.640066+00:00
---

# google.appengine.api.validation.Regex  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Regex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.validation.Regex Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L1037-L1107) Regular expression validator. Inherits From: [`Validator`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.validation.Regex(
        regex, string_type=six.text_type, default=None
    )
    

Regular expression validator always converts value to string. Note that matches must be exact. Partial matches will not validate. For example: class ClassDescr(Validated): ATTRIBUTES = { 'name': Regex(r'[a-zA-Z_][a-zA-Z_0-9]*'), 'parent': Type(type)` } Alternatively, any attribute that is defined as a string is automatically interpreted to be of type Regex. It is possible to specify unicode regex strings as well. This approach is slightly less efficient, but usually is not significant unless parsing large amounts of data:
    
    
      class ClassDescr(Validated):
        ATTRIBUTES = { 'name': r'[a-zA-Z_][a-zA-Z_0-9]*',
                       'parent': Type(type),
                       }
    
      # This will raise a ValidationError exception.
      my_class(name='AName with space', parent=AnotherClass)
    

| 

## Args  
  
---  
  
`regex` |  Regular expression string to use for comparison.   
`string_type` |  Type to be considered a string.   
`default` |  Default value.   
  
## Raises  
  
---  
  
`AttributeDefinitionError` |  if `string_type` is not a kind of string.   
  
## Child Classes

[`class expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

## Methods

### `CheckFieldInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L689-L705)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L1088-L1107)
    
    
    Validate(
        value, key
    )
    

Does validation of a string against a regular expression.

Args  
---  
  
`value` |  String to match against regular expression.   
`key` |  Name of the field being validated.   
  
Raises  
---  
  
`ValidationError` |  When value does not match regular expression or when value does not match provided string type.   
  
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
