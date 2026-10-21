---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/ListProperty/
title: google.appengine.ext.db.ListProperty \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:41:38.578864+00:00
---

# google.appengine.ext.db.ListProperty  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/ListProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.ListProperty Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3437-L3617) A property that stores a list of things. Inherits From: [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Property), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.ListProperty(
        item_type, verbose_name=None, default=None, write_empty_list=None, **kwds
    )
    

This is a parameterized property; the parameter must be a valid non-list data type, and all items must conform to this type. | 

## Args  
  
---  
  
`item_type` |  Type for the list items; must be one of the allowed property types.   
`verbose_name` |  Optional verbose name.   
`write_empty_list` |  Optional whether to write empty list properties or no property   
`default` |  Optional default value; if omitted, an empty list is used.   
`**kwds` |  Optional additional keyword arguments, passed to base class. Note that the only permissible value for `required` is `True`.   
  
## Child Classes

[`class data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/ListProperty/data_type)

## Methods

### `datastore_type`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L772-L775)
    
    
    datastore_type()
    

Deprecated backwards-compatible accessor method for `self.data_type`.

### `default_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3554-L3564)
    
    
    default_value()
    

Default value for list.

Because the property supplied to `default` is a static value, that value must be shallow copied to prevent all fields with default values from sharing the same instance.

Returns  
---  
Copy of the default value.   
  
### `empty`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3542-L3550)
    
    
    empty(
        value
    )
    

Is `list` property empty.

`[]` is not an empty value.

Returns  
---  
`True` if value is `None`, else `False`.   
  
### `get_updated_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L699-L714)
    
    
    get_updated_value_for_datastore(
        model_instance
    )
    

Determine new value for auto-updated property.

Some properies (e.g. `DateTimeProperty`, `UserProperty`) optionally update their value on every `put()`. This call must return the new desired value for such properties. For all other properties, this call must return `AUTO_UPDATE_UNCHANGED`.

Args  
---  
  
`model_instance` |  Instance to get new value for.   
  
Returns  
---  
Datastore representation of the new model value in a form that is appropriate for storing in the datastore, or `AUTO_UPDATE_UNCHANGED`.   
  
### `get_value_for_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3566-L3592)
    
    
    get_value_for_datastore(
        model_instance
    )
    

Get value from property to send to datastore.

Returns  
---  
validated list appropriate to save in the datastore.   
  
### `make_value_from_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3594-L3613)
    
    
    make_value_from_datastore(
        value
    )
    

Native representation of this property.

If this list is a list of `datetime.date` or `datetime.time`, we convert the list of `datetime.datetime` retrieved from the entity into `datetime.date` or `datetime.time`.

See base class method documentation for details.

### `make_value_from_datastore_index_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3615-L3617)
    
    
    make_value_from_datastore_index_value(
        index_value
    )
    

### `validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3486-L3502)
    
    
    validate(
        value
    )
    

Validate list.

Returns  
---  
A valid value.   
  
Raises  
---  
`BadValueError` if property is not a list whose items are instances of the `item_type` given to the constructor.   
  
### `validate_list_contents`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3510-L3540)
    
    
    validate_list_contents(
        value
    )
    

Validates that all items in the list are of the correct type.

Returns  
---  
The validated list.   
  
Raises  
---  
`BadValueError` if the list has items are not instances of the `item_type` given to the constructor.   
  
## Class Variables  
  
---  
  
creation_counter |  `2`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
