---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass/
title: NDB Model Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:53.050574+00:00
---

# NDB Model Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Model Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

A class that inherits from the `Model` class represents the structure of entities stored in the Datastore. Applications define model classes to indicate the structure of their entities, then instantiate those model classes to create entities. All model classes must inherit (directly or indirectly) from Model. 

This page has API reference documentation. For an overview, please see [NDB Entities and Keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entities). 

## Introduction

A class that inherits from `Model` describes Datastore entities. 

All model classes must inherit (directly or indirectly) from `Model`. Straightforward assignments in the model class definition can be used to declare the model's structure:
    
    
    from google.appengine.ext import ndb
    
    class Person(ndb.Model):
      name = ndb.StringProperty()
      age = ndb.IntegerProperty()

We can now create a Person entity and write it to the Datastore:
    
    
    p = Person(name='Arthur Dent', age=42)
    k = p.put()

The return value from `put()` is a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass), which can be used to retrieve the same entity later: 
    
    
    p2 = k.get()
    p2 == p  # Returns True

To update an entity, simply change its attributes and write it back (note that this doesn't change the key):
    
    
    p2.name = 'Arthur Philip Dent'
    p2.put()

We can also delete an entity (by using the key):
    
    
    k.delete()

The property definitions in the class body tell the system the names and the types of the fields to be stored in the Datastore, whether they must be indexed, their default value, and more. Many different [Property types](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference) exist. 

The _kind_ is normally equal to the class name (exclusive of the module name or any other parent scope). To override the kind (useful for schema changes), define a class method named `_get_kind()`, as follows: 
    
    
      class MyModel(ndb.Model):
        @classmethod
        def _get_kind(cls):
          return 'AnotherKind'

An application should not define two model classes with the same kind, even if they live in different modules. An application's kinds are considered a global "namespace". 

`Model` subclasses may define pre-call and post-call [hooks](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models#using_model_hooks) for most operations (get, put, delete, allocate_ids).

## Constructor

An application won't normally call `Model()`, but is likely to call the constructor of a class that inherits from `Model`. This creates a new instance of this model, also known as an entity. 

The newly-created entity isn't automatically written to the Datastore. To make that happen, it must be written to the Datastore using an explicit call to `put()`. 

**Arguments:**

`Model` subclasses support these keyword arguments: 

key
    [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance for this model. If the `key` parameter is used, `id` and `parent` must be `None` (the default). 
id
    Key id for this model. If `id` is used, key must be `None` (the default). 
parent
    [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance for the parent model or `None` for a top-level one. If `parent` is used, `key` must be `None`. 
namespace
    [Namespace](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy) to use for this entity, or `None` (default) to use the current namespace. If `namespace` is used, `key` must be `None`. 

An application can also use keyword arguments mapping to the model's properties. For example, the following works:
    
    
    class Person(ndb.Model):
      name = StringProperty()
      age = IntegerProperty()
    
    p = Person(name='Arthur Dent', age=42)

You cannot easily define a property named "key", "id", "parent", or "namespace". If you pass, for example, `key="foo"` in a constructor or `populate()` call, it sets the entity's key, not a property attribute named "key".

**Note:** If you override the constructor in a Model subclass, beware that the constructor is also called implicitly in some cases, and be sure that you support those calls. When an entity is read from the Datastore, an empty entity is first created by calling the constructor without arguments, after which the key and property values are set one by one. When `get_or_insert()` or `get_or_insert_async()` creates a new instance, it passes **constructor_args to the constructor, and sets the key afterwards.

## Class Methods

allocate_ids(size=None, max=None, parent=None, **ctx_options)
    

Allocates a range of key IDs for this model class. 

Arguments

size
    Number of IDs to allocate. Either `size` or `max` can be specified, not both. 
max
    Maximum ID to allocate. Either `size` or `max` can be specified, not both. 
parent
    Parent key for which the IDs will be allocated. 
**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)

Returns a tuple with (start, end) for the allocated range, inclusive. 

An application cannot call `allocate_ids()` in a transaction. 

allocate_ids_async(size=None, max=None, parent=None, **ctx_options)
    

Asynchronous version of allocate_ids. 

Returns a `Future` object whose result is a tuple with (start, end) for the allocated range, inclusive. 

get_by_id(id, parent=None, app=None, namespace=None, **ctx_options)
    Returns an entity by ID. This is really just a shorthand for `Key(cls, id).get()`. 

Arguments

id
    A string or integer key ID.
parent
    Parent key of the model to get.
app (keyword arg)
    ID of app. If not specified, gets data for current app.
namespace (keyword arg)
    Namespace. If not specified, gets data for default namespace.
**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)

Returns a model instance or `None` if not found.

get_by_id_async(id, parent=None, app=None, namespace=None, **ctx_options)
    Asynchronous version of get_by_id. 

Returns a `Future` object whose result is a model instance or `None` if not found.

get_or_insert(key_name, parent=None, app=None, namespace=None, context_options=None, **constructor_args)
    Transactionally retrieves an existing entity or creates a new one. 

Arguments

key_name
    A Key name (i.e., a string key ID) to retrieve or create.
parent
    Parent entity key, if any.
app
    ID of app. If not specified, gets data for current app.
namespace
    Namespace. If not specified, gets data for default namespace.
context_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)

This function also takes keyword arguments to pass to the constructor of the model class if an instance for the specified key name does not already exist. If an instance with the supplied `key_name` and parent already exists, these arguments will be discarded. 

Returns existing instance of `Model` class with the specified key name and parent or a new one that has just been created. 

This function uses a transaction. If the code that calls this function is already in a transaction, this function attempts to re-use the existing transaction. If this function's entity group is incompatible with the existing transaction, this can cause an error. 

get_or_insert_async(key_name, parent=None, app=None, namespace=None, context_options=None, **constructor_args)
    

This is the asynchronous version of get_or_insert. 

It returns a `Future` object whose result is an existing instance of `Model` class with the specified key name and parent or a new one that has just been created. 

query([filter1, filter2, ...,] ancestor=None, app=None, namespace=None, filters=None, orders=None, default_options=None, projection=None distinct=False group_by=None) 
    

Creates a `[Query](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queryclass)` object for this class as described in [Queries](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries).

The keyword argument `distinct` is shorthand for group_by = projection. All other keyword arguments are passed to the [Query constructor](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queryclass#constructor).

If positional arguments are given, they are used to set up initial filters.

Returns a `Query` object.

## Instance Methods

populate(**constructor_options)
    

Sets values of the entity's properties. Its keyword arguments automatically recognize property names in the same way that the constructor does.

put(**ctx_options)
    

Writes the entity's data to the Datastore. Returns the entity's [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass).

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)
put_async(**ctx_options)
    

Asynchronously writes the entity's data to the Datastore. Returns a `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` object. The `Future` object's result will be the entity's [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass).

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)
to_dict(include=all, exclude=None)
    

Returns a `dict` containing the model's property values. Property values for `StructuredProperty` and `LocalStructuredProperty` are recursively converted into dictionaries.

**Arguments:**

include
    Optional list of properties to include. Default: all.
exclude
    Optional list of properties to exclude. If there is overlap between include and exclude, then exclude "wins."

Note: If a property value is a mutable object (e.g. a list representing a repeated property, or a dict or list stored in a `JsonProperty`), _unless_ the value is explicitly converted (e.g. in the case of a `StructuredProperty`), the same object is returned in the dict that is stored in the entity. In such cases, mutating the dictionary will mutate the entity, and vice versa.

## Instance Data

key
    Special property to store the Model key.

## Hook Methods

An application's subclass of `Model` can define one or more of these methods as pre- or post- operation "hook" methods. E.g., to run some code before each "get", define the model subclass' `_pre_get_hook()` method. For advice on writing hook functions, see [Model Hooks](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models#using_model_hooks). 

@classmethod  
_pre_allocate_ids_hook(cls, size, max, parent) 
    Hook that runs before `allocate_ids()`
@classmethod  
_post_allocate_ids_hook(cls, size, max, parent, future) 
    Hook that runs after `allocate_ids()`
@classmethod  
_pre_delete_hook(cls, key) 
    Hook that runs before `delete()`
@classmethod  
_post_delete_hook(cls, key, future) 
    Hook that runs after `delete()`
@classmethod  
_pre_get_hook(cls, key) 
    Hook that runs before `[Key.get()](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass#Key_get)` when getting an entity of this model. 
@classmethod  
_post_get_hook(cls, key, future) 
    Hook that runs after `[Key.get()](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass#Key_get)` when getting an entity of this model. 
_pre_put_hook(self) 
    Hook that runs before `put()`
_post_put_hook(self, future) 
    Hook that runs after `put()`

## Introspection

You can use these methods to inspect the properties and configuration of a given model. This is useful if you're writing a library or function that accepts multiple types of models. 

### Lookup by kind

Every model has a _kind_ that is usually the same as the class name unless overridden. You can use the kind to find the associated model class by using `_lookup_model`. 
    
    
    class Animal(ndb.Model):
        type = ndb.StringProperty()
    
    print Animal._get_kind()  # 'Animal'
    print ndb.Model._lookup_model('Animal')  # class Animal

Note that `_lookup_model` only works for model classes that have already been imported by the application. 

### Properties

You can get a list of all properties associated with a model using `_properties`. 
    
    
    class User(ndb.Model):
        name = ndb.StringProperty()
        email = ndb.StringProperty()
    
    print User._properties
    # {'email': StringProperty('email'), 'name': StringProperty('name')}

`_properties` also works for [Expando instances](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models#expando). 
    
    
    class Example(ndb.Expando):
      pass
    
    e = Example()
    e.foo = 1
    e.bar = 'blah'
    e.tags = ['exp', 'and', 'oh']
    print e._properties
    # {'foo': GenericProperty('foo'), 'bar': GenericProperty('bar'),
    # 'tags': GenericProperty('tags', repeated=True)}

Property instances can be introspected. The [options provided to the constructor](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference#options) are available as `_`-prefixed properties. 
    
    
    print User._properties['email']._name  # 'email'
    print User._properties['email']._required  # False
    print User._properties['email']._default  # None
    print User._properties['email']._choices  # None
    print User._properties['email']._compressed  # False
    print User._properties['email']._indexed  # True
    print User._properties['email']._compressed  # False
    print User._properties['email']._repeated  # False
    print User._properties['email']._verbose_name  # None
    print isinstance(User._properties['email'], ndb.StringProperty)  # True

### Method Aliases

Every method in the `Model` class has a `_`-prefixed alias. For example, `_put()` is equivalent to `put()`. This means that you can have properties with names that conflict with method names provided you always use the `_`-prefixed methods. However, note that you can not specify any properties named `key`, `parent`, or `id` in the constructor. 
    
    
    class MyModel(ndb.Model):
        put = ndb.StringProperty()
        query = ndb.StringProperty()
        key = ndb.StringProperty()
    
    entity = MyModel()
    entity.put = '1'
    entity.query = '2'
    entity.key = '3'
    
    entity._put()
    print entity
    # MyModel(key=Key('MyModel', ...), put=u'1', query=u'2', key=u'3')
    
    print MyModel._query().fetch()
    # same as above.

If you are creating third-party libraries that interact with arbitrary models, using the `_`-prefixed methods is recommended. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
