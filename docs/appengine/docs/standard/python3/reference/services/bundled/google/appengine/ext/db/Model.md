---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model/
title: google.appengine.ext.db.Model \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:57:49.351340+00:00
---

# google.appengine.ext.db.Model  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.Model Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L787-L1477) `Model` is the superclass of all object entities in the datastore. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.Model(
        parent=None, key_name=None, _app=None, _from_entity=False, **kwds
    )
    

The programming model is to declare Python subclasses of the `Model` class, declaring datastore properties as class members of that class. So if you want to publish a story with title, body, and created date, you would do it like this: class Story(db.Model): title = db.StringProperty() body = db.TextProperty() created = db.DateTimeProperty(auto_now_add=True) A model instance can have a single parent. `Model` instances without any parent are root entities. It is possible to efficiently query for instances by their shared parent. All descendents of a single root instance also behave as a transaction group. This means that when you work one member of the group within a transaction all descendents of that root join the transaction. All operations within a transaction on this group are ACID. | 

## Args  
  
---  
  
`parent` |  Parent instance for this instance or `None`, indicating a top- level instance.   
`key_name` |  Name for new model instance.   
`_from_entity` |  Intentionally undocumented.   
`kwds` |  Keyword arguments mapping to properties of model. Also: key: `Key` instance for this instance, if provided makes `parent` and `key_name` redundant (they do not need to be set but if they are they must match the key).   
  
## Methods

### `all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1380-L1387)
    
    
    @classmethod
    all(
        **kwds
    )
    

Returns a query over all instances of this model from the datastore.

Returns  
---  
`Query` that will retrieve all instances from entity collection.   
  
### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1127-L1142)
    
    
    delete(
        **kwargs
    )
    

Deletes this entity from the datastore.

Args  
---  
  
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
Raises  
---  
`TransactionFailedError` if the data could not be committed.   
  
### `dynamic_properties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1170-L1172)
    
    
    dynamic_properties()
    

Returns a list of all dynamic properties defined for instance.

### `entity_type`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1464-L1467)
    
    
    @classmethod
    entity_type()
    

Soon to be removed alias for `kind`.

### `fields`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1474-L1477)
    
    
    @classmethod
    fields()
    

Soon to be removed alias for `properties`.

### `from_entity`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1435-L1454)
    
    
    @classmethod
    from_entity(
        entity
    )
    

Converts the entity representation of this model to an instance.

Converts [`datastore.Entity`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Entity) instance to an instance of `cls`.

Args  
---  
  
`entity` |  Entity loaded directly from datastore.   
  
Raises  
---  
`KindError` when `cls` is incorrect model for entity.   
  
### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1225-L1267)
    
    
    @classmethod
    get(
        keys, **kwargs
    )
    

Fetch instance from the datastore of a specific `Model` type using key.

We support `Key` objects and string keys (we convert them to `Key` objects automatically).

Useful for ensuring that specific instance types are retrieved from the datastore. It also helps that the source code clearly indicates what kind of object is being retrieved. Example:

story = Story.get(story_key)

Args  
---  
  
`keys` |  `Key` within datastore entity collection to find; or string key; or list of `Keys` or string keys.   
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
Returns  
---  
If a single key was given: a `Model` instance associated with key for the provided class if it exists in the datastore, otherwise `None`. If a list of keys was given: a list where `list[i]` is the `Model` instance for `keys[i]`, or `None` if no instance exists.   
  
Raises  
---  
`KindError` if any of the retrieved objects are not instances of the type associated with call to `get`.   
  
### `get_by_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1293-L1310)
    
    
    @classmethod
    get_by_id(
        ids, parent=None, **kwargs
    )
    

Returns instance of `Model` class by id.

Args  
---  
  
`key_names` |  A single id or a list of ids.   
`parent` |  Parent of instances to get. Can be a model or key.   
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
### `get_by_key_name`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1269-L1291)
    
    
    @classmethod
    get_by_key_name(
        key_names, parent=None, **kwargs
    )
    

Returns instance of `Model` class by its key's name.

Args  
---  
  
`key_names` |  A single `key-name` or a list of `key-names`.   
`parent` |  Parent of instances to get. Can be a model or key.   
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
### `get_or_insert`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1315-L1378)
    
    
    @classmethod
    get_or_insert(
        key_name, **kwds
    )
    

Transactionally retrieve or create an instance of `Model` class.

This acts much like the Python dictionary `setdefault()` method, where we first try to retrieve a `Model` instance with the given key name and `parent`. If it's not present, then we create a new instance (using the `*kwds` supplied) and insert that with the supplied key name.

Subsequent calls to this method with the same `key_name` and `parent` will always yield the same entity (though not the same actual object instance), regardless of the `*kwds` supplied. If the specified entity has somehow been deleted separately, then the next call will create a new entity and return it.

If the `parent` keyword argument is supplied, it must be a `Model` instance. It will be used as the `parent` of the new instance of this `Model` class if one is created.

This method is especially useful for having just one unique entity for a specific identifier. Insertion/retrieval is done transactionally, which guarantees uniqueness.

#### Example usage:

class WikiTopic(db.Model): creation_date = db.DatetimeProperty(auto_now_add=True) body = db.TextProperty(required=True)

# The first time through we'll create the new topic.

wiki_word = 'CommonIdioms' topic = `WikiTopic`.get_or_insert(wiki_word, body='This topic is totally new!') assert topic.key().name() == 'CommonIdioms' assert topic.body == 'This topic is totally new!'

# The second time through will just retrieve the entity.

overwrite_topic = `WikiTopic`.get_or_insert(wiki_word, body='A totally different message!') assert topic.key().name() == 'CommonIdioms' assert topic.body == 'This topic is totally new!'

Args  
---  
  
`key_name` |  Key name to retrieve or create.   
`**kwds` |  Keyword arguments to pass to the constructor of the model class if an instance for the specified key name does not already exist. If an instance with the supplied `key_name` and `parent` already exists, the rest of these arguments will be discarded.   
  
Returns  
---  
Existing instance of `Model` class with the specified `key_name` and `parent` or a new one that has just been created.   
  
Raises  
---  
`TransactionFailedError` if the specified `Model` instance could not be retrieved or created transactionally (due to high contention, etc).   
  
### `gql`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1389-L1405)
    
    
    @classmethod
    gql(
        query_string, *args, **kwds
    )
    

Returns a query using GQL query string.

See `appengine/ext/gql` for more information about GQL.

Args  
---  
  
`query_string` |  properly formatted GQL query string with the `SELECT * FROM <entity>` part omitted   
`*args` |  rest of the positional arguments used to bind numeric references in the query.   
`**kwds` |  dictionary-based arguments (for named parameters).   
  
### `has_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1157-L1168)
    
    
    has_key()
    

Determine if this model instance has a complete key.

When not using a fully self-assigned `Key`, ids are not assigned until the data is saved to the Datastore, but instances with a key name always have a full key.

Returns  
---  
`True` if the object has been persisted to the datastore or has a `key` or has a `key_name`, otherwise `False`.   
  
### `instance_properties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1175-L1177)
    
    
    instance_properties()
    

Alias for `dyanmic_properties`.

### `is_saved`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1146-L1155)
    
    
    is_saved()
    

Determine if entity is persisted in the datastore.

New instances of `Model` do not start out saved in the data. Objects which are saved to or loaded from the Datastore will have a `True` saved state.

Returns  
---  
`True` if object has been persisted to the datastore, otherwise `False`.   
  
### `key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L991-L1015)
    
    
    key()
    

Unique key for this entity.

This property is only available if this entity is already stored in the datastore or if it has a full key, so it is available if this entity was fetched returned from a query, or after `put()` is called the first time for new entities, or if a complete key was given when constructed.

Returns  
---  
Datastore key of persisted entity.   
  
Raises  
---  
`NotSavedError` when entity is not persistent.   
  
### `kind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1456-L1462)
    
    
    @classmethod
    kind()
    

Returns the datastore kind we use for this model.

We just use the name of the model for now, ignoring potential collisions.

### `parent`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1179-L1191)
    
    
    parent()
    

Get the parent of the model instance.

Returns  
---  
Parent of contained entity or parent provided in constructor, `None` if instance has no parent.   
  
### `parent_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1193-L1211)
    
    
    parent_key()
    

Get the parent's key.

This method is useful for avoiding a potential fetch from the datastore but still get information about the instance's parent.

Returns  
---  
Parent key of entity, `None` if there is no parent.   
  
### `properties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1469-L1472)
    
    
    @classmethod
    properties()
    

Returns a dictionary of all the properties defined for this model.

### `put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1068-L1085)
    
    
    put(
        **kwargs
    )
    

Writes this model instance to the datastore.

If this instance is new, we add an entity to the datastore. Otherwise, we update this instance, and the key will remain the same.

Args  
---  
  
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
Returns  
---  
The key of the instance (either the existing key or a new key).   
  
Raises  
---  
`TransactionFailedError` if the data could not be committed.   
  
### `save`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1068-L1085)
    
    
    save(
        **kwargs
    )
    

Writes this model instance to the datastore.

If this instance is new, we add an entity to the datastore. Otherwise, we update this instance, and the key will remain the same.

Args  
---  
  
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request.   
  
Returns  
---  
The key of the instance (either the existing key or a new key).   
  
Raises  
---  
`TransactionFailedError` if the data could not be committed.   
  
### `to_xml`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1213-L1223)
    
    
    to_xml(
        _entity_class=[google.appengine.api.datastore.Entity](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Entity)
    )
    

Generate an XML representation of this model instance.

`atom` and `gd:namespace` properties are converted to XML according to their respective schemas. For more information, see:

http://www.atomenabled.org/developers/syndication/ https://developers.google.com/gdata/docs/1.0/elements

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
