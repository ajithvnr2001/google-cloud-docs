---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/
title: google.appengine.ext.db.TimeProperty \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:42:27.560398+00:00
---

# google.appengine.ext.db.TimeProperty  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.TimeProperty Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3182-L3249) A `time` property, which stores a `time` without a `date`. Inherits From: [`DateTimeProperty`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty), [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Property), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.TimeProperty(
        verbose_name=None, auto_now=False, auto_now_add=False, **kwds
    )
    

| 

## Args  
  
---  
  
`verbose_name` |  Verbose name is always first parameter.   
`auto_now` |  Date/time property is updated with the current time every time it is saved to the datastore. Useful for properties that want to track the modification time of an instance.   
`auto_now_add` |  Date/time is set to the when its instance is created. Useful for properties that record the creation time of an entity.   
  
## Child Classes

[`class data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/data_type)

## Methods

### `datastore_type`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L772-L775)
    
    
    datastore_type()
    

Deprecated backwards-compatible accessor method for `self.data_type`.

### `default_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3042-L3052)
    
    
    default_value()
    

Default value for datetime.

Returns  
---  
value of `now()` as appropriate to the date-time instance if `auto_now` or `auto_now_add` is set, else user configured default value implementation.   
  
### `empty`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3201-L3209)
    
    
    empty(
        value
    )
    

Is `time` property empty.

`0:0` (midnight) is not an empty value.

Returns  
---  
`True` if value is `None`, else `False`.   
  
### `get_updated_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3211-L3220)
    
    
    get_updated_value_for_datastore(
        model_instance
    )
    

Get new value for property to send to datastore.

Returns  
---  
`now()` as appropriate to the `time` instance in the odd case where `auto_now` is set to `True`, else `AUTO_UPDATE_UNCHANGED`.   
  
### `get_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3222-L3234)
    
    
    get_value_for_datastore(
        model_instance
    )
    

Get value from property to send to datastore.

We retrieve a `datetime.time` from the model instance and return a `datetime.datetime` instance with the `date` set to `1/1/1970`.

See base class method documentation for details.

### `make_value_from_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3236-L3247)
    
    
    make_value_from_datastore(
        value
    )
    

Native representation of this property.

We receive a `datetime.datetime` retrieved from the entity and return a `datetime.date` instance representing its `time` portion.

See base class method documentation for details.

### `make_value_from_datastore_index_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L716-L718)
    
    
    make_value_from_datastore_index_value(
        index_value
    )
    

### `now`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3192-L3199)
    
    
    @staticmethod
    now()
    

Get `now` as a `time` `datetime` value.

Returns  
---  
'time' part of 'now' only.   
  
### `validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3027-L3040)
    
    
    validate(
        value
    )
    

Validate datetime.

Returns  
---  
A valid value.   
  
Raises  
---  
`BadValueError` if property is not instance of 'datetime'.   
  
## Class Variables  
  
---  
  
creation_counter |  `2`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
