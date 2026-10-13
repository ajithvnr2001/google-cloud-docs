---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/
title: google.appengine.ext.db.DateProperty \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:37.675074+00:00
---

# google.appengine.ext.db.DateProperty  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.DateProperty Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3105-L3179) A date property, which stores a date without a time. Inherits From: [`DateTimeProperty`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty), [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Property), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.DateProperty(
        verbose_name=None, auto_now=False, auto_now_add=False, **kwds
    )
    

| 

## Args  
  
---  
  
`verbose_name` |  Verbose name is always first parameter.   
`auto_now` |  Date/time property is updated with the current time every time it is saved to the datastore. Useful for properties that want to track the modification time of an instance.   
`auto_now_add` |  Date/time is set to the when its instance is created. Useful for properties that record the creation time of an entity.   
  
## Child Classes

[`class data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/data_type)

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L662-L676)
    
    
    empty(
        value
    )
    

Determine if value is empty in the context of this property.

For most kinds, this is equivalent to "not value", but for kinds like `bool`, the test is more subtle, so subclasses can override this method if necessary.

Args  
---  
  
`value` |  Value to validate against this `Property`.   
  
Returns  
---  
`True` if this value is considered empty in the context of this `Property` type, otherwise `False`.   
  
### `get_updated_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3141-L3150)
    
    
    get_updated_value_for_datastore(
        model_instance
    )
    

Get new value for property to send to datastore.

Returns  
---  
`now()` as appropriate to the `date` instance in the odd case where `auto_now` is set to `True`, else `AUTO_UPDATE_UNCHANGED`.   
  
### `get_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3152-L3164)
    
    
    get_value_for_datastore(
        model_instance
    )
    

Get value from property to send to datastore.

We retrieve a `datetime.date` from the model instance and return a `datetime.datetime` instance with the time set to zero.

See base class method documentation for details.

### `make_value_from_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3166-L3177)
    
    
    make_value_from_datastore(
        value
    )
    

Native representation of this property.

We receive a `datetime.datetime` retrieved from the entity and return a `datetime.date` instance representing its `date` portion.

See base class method documentation for details.

### `make_value_from_datastore_index_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L716-L718)
    
    
    make_value_from_datastore_index_value(
        index_value
    )
    

### `now`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3115-L3122)
    
    
    @staticmethod
    now()
    

Get `now` as a `date` `datetime` value.

Returns  
---  
'date' part of 'now' only.   
  
### `validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3124-L3139)
    
    
    validate(
        value
    )
    

Validate `date`.

Returns  
---  
A valid value.   
  
Raises  
---  
`BadValueError` if property is not instance of 'date', or if it is an instance of 'datetime' (which is a subclass of 'date', but for all practical purposes a different type).   
  
## Class Variables  
  
---  
  
creation_counter |  `2`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
