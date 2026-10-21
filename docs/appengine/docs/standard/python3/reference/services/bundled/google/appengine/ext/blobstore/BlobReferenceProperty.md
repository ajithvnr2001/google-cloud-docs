---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReferenceProperty/
title: google.appengine.ext.blobstore.BlobReferenceProperty \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:20:19.264813+00:00
---

# google.appengine.ext.blobstore.BlobReferenceProperty  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReferenceProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.BlobReferenceProperty Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L717-L789) Property compatible with [`db.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model) classes. Inherits From: [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Property), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.blobstore.BlobReferenceProperty`
    
    
    google.appengine.ext.blobstore.BlobReferenceProperty(
        verbose_name=None,
        name=None,
        default=None,
        required=False,
        validator=None,
        choices=None,
        indexed=True
    )
    

Add references to blobs to domain models using BlobReferenceProperty::
    
    
    class Picture(db.Model):
      title = db.StringProperty()
      image = blobstore.BlobReferenceProperty()
      thumbnail = blobstore.BlobReferenceProperty()
    

To find the size of a picture using this model::
    
    
    picture = Picture.get(picture_key)
    print picture.image.size
    

`BlobInfo` objects are lazily loaded, so iterating over models for `BlobKeys` is efficient. The following sample code does not need to hit Datastore for each image key::
    
    
    list_of_untitled_blobs = []
    for picture in Picture.gql("WHERE title=''"):
      list_of_untitled_blobs.append(picture.image.key())
    

| 

## Args  
  
---  
  
`verbose_name` |  User friendly name of property.   
`name` |  Storage name for property. By default, uses attribute name as it is assigned in the `Model` sub-class.   
`default` |  Default value for property if none is assigned.   
`required` |  Whether property is required.   
`validator` |  User provided method used for validation.   
`choices` |  User provided set of valid property values.   
`indexed` |  Whether property is indexed.   
  
## Child Classes

[`class data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobInfo)

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L746-L759)
    
    
    get_value_for_datastore(
        model_instance
    )
    

Returns a model property translated to a datastore value.

Args  
---  
  
`model_instance` |  The model property that you want to translate.   
  
Returns  
---  
The model property that was translated from datastore.   
  
### `make_value_from_datastore`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L761-L772)
    
    
    make_value_from_datastore(
        value
    )
    

Returns a datastore value to `BlobInfo`.

Args  
---  
  
`value` |  The datastore value that you want to translate.   
  
Returns  
---  
A `BlobInfo` that was translated from datastore.   
  
### `make_value_from_datastore_index_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L716-L718)
    
    
    make_value_from_datastore_index_value(
        index_value
    )
    

### `validate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L774-L789)
    
    
    validate(
        value
    )
    

Validates that an assigned value is `BlobInfo`.

This method automatically converts from strings and `BlobKey` instances.

Args  
---  
  
`value` |  The value that you want to validate.   
  
Returns  
---  
Information about whether an assigned value is `BlobInfo`.   
  
## Class Variables  
  
---  
  
creation_counter |  `2`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
