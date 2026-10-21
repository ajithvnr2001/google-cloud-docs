---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Expando/
title: google.appengine.ext.ndb.Expando \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:43:07.366346+00:00
---

# google.appengine.ext.ndb.Expando  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Expando/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Expando Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3783-L3846) Model subclass to support dynamic Property names and types. Inherits From: [`Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Model), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Expando(
        *args, **kwds
    )
    

See the module docstring for details. | 

## Attributes  
  
---  
  
`key` |  Special property to store the Model key.   
  
## Methods

### `allocate_ids`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3634-L3650)
    
    
    @classmethod
    allocate_ids(
        size=None, max=None, parent=None, **ctx_options
    )
    

Allocates a range of key IDs for this model class.

Args  
---  
  
`size` |  Number of IDs to allocate. Either size or max can be specified, not both.   
`max` |  Maximum ID to allocate. Either size or max can be specified, not both.   
`parent` |  Parent key for which the IDs will be allocated.   
`**ctx_options` |  Context options.   
  
Returns  
---  
A tuple with (start, end) for the allocated range, inclusive.   
  
### `allocate_ids_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3653-L3669)
    
    
    @classmethod
    allocate_ids_async(
        size=None, max=None, parent=None, **ctx_options
    )
    

Allocates a range of key IDs for this model class.

This is the asynchronous version of Model._allocate_ids().

### `get_by_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3672-L3689)
    
    
    @classmethod
    get_by_id(
        id, parent=None, **ctx_options
    )
    

Returns an instance of Model class by ID.

This is really just a shorthand for Key(cls, id, ...).get().

Args  
---  
  
`id` |  A string or integer key ID.   
`parent` |  Optional parent key of the model to get.   
`namespace` |  Optional namespace.   
`app` |  Optional app ID.   
`**ctx_options` |  Context options.   
  
Returns  
---  
A model instance or None if not found.   
  
### `get_by_id_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3692-L3701)
    
    
    @classmethod
    get_by_id_async(
        id, parent=None, app=None, namespace=None, **ctx_options
    )
    

Returns an instance of Model class by ID (and app, namespace).

This is the asynchronous version of Model._get_by_id().

### `get_or_insert`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3561-L3583)
    
    
    @classmethod
    get_or_insert(
        *args, **kwds
    )
    

Transactionally retrieves an existing entity or creates a new one.

#### Positional Args:

  * **`name`** : Key name to retrieve or create.



#### Keyword Args:

  * **`namespace`** : Optional namespace.
  * **`app`** : Optional app ID.
  * **`parent`** : Parent entity key, if any.
  * **`context_options`** : ContextOptions object (not keyword args!) or None.
  * **`**kwds`** : Keyword arguments to pass to the constructor of the model class if an instance for the specified key name does not already exist. If an instance with the supplied key_name and parent already exists, these arguments will be discarded.



Returns  
---  
Existing instance of Model class with the specified key name and parent or a new one that has just been created.   
  
### `get_or_insert_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3586-L3630)
    
    
    @classmethod
    get_or_insert_async(
        *args, **kwds
    )
    

Transactionally retrieves an existing entity or creates a new one.

This is the asynchronous version of Model._get_or_insert().

### `gql`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3521-L3526)
    
    
    @classmethod
    gql(
        query_string, *args, **kwds
    )
    

Run a GQL query.

### `has_complete_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3182-L3184)
    
    
    has_complete_key()
    

Return whether this entity has a complete key.

### `populate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3051-L3059)
    
    
    populate(
        **kwds
    )
    

Populate an instance from keyword arguments.

Each keyword argument will be used to set a corresponding property. Keywords must refer to valid property name. This is similar to passing keyword arguments to the Model constructor, except that no provisions for key, id or parent are made.

### `put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3529-L3538)
    
    
    put(
        **ctx_options
    )
    

Write this entity to Cloud Datastore.

If the operation creates or completes a key, the entity's key attribute is set to the new, complete key.

Returns  
---  
The key for the entity. This is always a complete key.   
  
### `put_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3541-L3558)
    
    
    put_async(
        **ctx_options
    )
    

Write this entity to Cloud Datastore.

This is the asynchronous version of Model._put().

### `query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3489-L3518)
    
    
    @classmethod
    query(
        *args, **kwds
    )
    

Create a Query object for this class.

Args  
---  
  
`distinct` |  Optional bool, short hand for group_by = projection.   
`*args` |  Used to apply an initial filter   
`**kwds` |  are passed to the Query() constructor.   
  
Returns  
---  
A Query object.   
  
### `to_dict`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3355-L3381)
    
    
    to_dict(
        include=None, exclude=None
    )
    

Return a dict containing the entity's property values.

Args  
---  
  
`include` |  Optional set of property names to include, default all.   
`exclude` |  Optional set of property names to skip, default none. A name contained in both include and exclude is excluded.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3197-L3205)
    
    
    __eq__(
        other
    )
    

Compare two entities of the same class for equality.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L417-L422)
    
    
    __ne__(
        other
    )
    

Implement self != other as not(self == other).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
