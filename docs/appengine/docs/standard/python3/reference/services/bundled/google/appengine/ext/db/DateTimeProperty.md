---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/
title: google.appengine.ext.db.DateTimeProperty \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:21:39.934424+00:00
---

# google.appengine.ext.db.DateTimeProperty  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.DateTimeProperty Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3004-L3074) The base class of all of our date/time properties. Inherits From: [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Property), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.DateTimeProperty(
        verbose_name=None, auto_now=False, auto_now_add=False, **kwds
    )
    

We handle common operations, like converting between time tuples and `datetime` instances. | 

## Args  
  
---  
  
`verbose_name` |  Verbose name is always first parameter.   
`auto_now` |  Date/time property is updated with the current time every time it is saved to the datastore. Useful for properties that want to track the modification time of an instance.   
`auto_now_add` |  Date/time is set to the when its instance is created. Useful for properties that record the creation time of an entity.   
  
## Child Classes

[`class data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/data_type)

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3054-L3063)
    
    
    get_updated_value_for_datastore(
        model_instance
    )
    

Get new value for property to send to datastore.

Returns  
---  
`now()` as appropriate to the date-time instance in the odd case where `auto_now` is set to `True`, else `AUTO_UPDATE_UNCHANGED`.   
  
### `get_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L678-L697)
    
    
    get_value_for_datastore(
        model_instance
    )
    

Datastore representation of this property.

Looks for this property in the given model instance, and returns the proper datastore representation of the value that can be stored in a datastore entity. Most critically, it will fetch the datastore key value for reference properties.

Some properies (e.g. `DateTimeProperty`, `UserProperty`) optionally update their value on every `put()`. This call must return the current value for such properties (`get_updated_value_for_datastore` returns the new value).

Args  
---  
  
`model_instance` |  Instance to fetch datastore value from.   
  
Returns  
---  
Datastore representation of the model value in a form that is appropriate for storing in the datastore.   
  
### `make_value_from_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L720-L740)
    
    
    make_value_from_datastore(
        value
    )
    

Native representation of this property.

Given a value retrieved from a datastore entity, return a value, possibly converted, to be stored on the model instance. Usually this returns the value unchanged, but a property class may override this when it uses a different datatype on the model instance than on the entity.

This API is not quite symmetric with `get_value_for_datastore()`, because the model instance on which to store the converted value may not exist yet -- we may be collecting values to be passed to a model constructor.

Args  
---  
  
`value` |  Value retrieved from the datastore entity.   
  
Returns  
---  
The value converted for use as a model instance attribute.   
  
### `make_value_from_datastore_index_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L716-L718)
    
    
    make_value_from_datastore_index_value(
        index_value
    )
    

### `now`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3067-L3074)
    
    
    @staticmethod
    now()
    

Get `now` as a full `datetime` value.

Returns  
---  
'now' as a whole timestamp, including both time and date.   
  
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
