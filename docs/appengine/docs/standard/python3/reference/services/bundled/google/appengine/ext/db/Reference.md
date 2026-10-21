---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Reference/
title: google.appengine.ext.db.Reference \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:14:16.575372+00:00
---

# google.appengine.ext.db.Reference  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.Reference Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3647-L3842) A property that represents a many-to-one reference to another model. Inherits From: [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Property), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.db.ReferenceProperty`
    
    
    google.appengine.ext.db.Reference(
        reference_class=None, verbose_name=None, collection_name=None, **attrs
    )
    

For example, a reference property in model A that refers to model B forms a many-to-one relationship from A to B: every instance of A refers to a single B instance, and every B instance can have many A instances refer to it. | 

## Args  
  
---  
  
`reference_class` |  Which model class this property references.   
`verbose_name` |  User friendly name of property.   
`collection_name` |  If provided, alternate name of collection on `reference_class` to store back references. Use this to allow a `Model` to have multiple fields which refer to the same class.   
  
## Methods

### `datastore_type`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L772-L775)
    
    
    datastore_type()
    

Deprecated backwards-compatible accessor method for `self.data_type`.

### `default_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L628-L634)
    
    
    default_value()
    

Default value for unassigned values.

Returns  
---  
Default value as provided by `__init__(default)`.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3793-L3796)
    
    
    get_value_for_datastore(
        model_instance
    )
    

Get key of reference rather than reference itself.

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3683-L3685)
    
    
    make_value_from_datastore_index_value(
        index_value
    )
    

### `validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L3798-L3823)
    
    
    validate(
        value
    )
    

Validate reference.

Returns  
---  
A valid value.   
  
Raises  
---  
`BadValueError` for the following reasons: 

  * Value is not saved.
  * Object not of correct model type for reference. 

  
  
## Class Variables  
  
---  
  
creation_counter |  `2`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
