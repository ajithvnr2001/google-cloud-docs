---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models/
title: Creating entity models \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:18.827857+00:00
---

# Creating entity models  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entity-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating entity models Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

You need to create a model class for your entity. You can do this in two ways:

  * Create a model class that defines entity properties.
  * Create an expando model class that does not define entities in advance.



This document describes how to create each of these types of model classes. It also describes how to create a model hook, so that your application can run some code before or after some type of operations, for example, before each `get()`.

## Creating a model class with properties

Before creating an entity, you must create a model class that defines one or more entity properties. For example:
    
    
    from google.appengine.ext import ndb

`...`
    
    
    class Account(ndb.Model):
        username = ndb.StringProperty()
        userid = ndb.IntegerProperty()
        email = ndb.StringProperty()

where you want each Account entity to have properties for user name, user ID, and email.

For a full list of property types, see the [Entity Property Reference](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference).

## Creating an Expando model class

You don't have to use a model class that defines properties in advance. A special model subclass called `Expando` changes the behavior of its entities so that any attribute assigned is saved to the data store. Note that such attributes can't start with an underscore.

Here is how to create an Expando model:
    
    
    class Mine(ndb.Expando):
        pass

`...`
    
    
    e = Mine()
    e.foo = 1
    e.bar = 'blah'
    e.tags = ['exp', 'and', 'oh']
    e.put()
    

This writes an entity to the data store with a `foo` property with integer value `1`, a `bar` property with string value `'blah'`, and a repeated `tag` property with string values `'exp'`, `'and'`, and `'oh'`. The properties are indexed, and you can inspect them using the entity's `_properties` attribute:
    
    
    return e._properties
    # {
    #     'foo': GenericProperty('foo'),
    #     'bar': GenericProperty('bar'),
    #     'tags': GenericProperty('tags', repeated=True)
    # }

An `Expando` created by getting a value from the data store has properties for all property values that were saved in the data store.

An application can add predefined properties to an `Expando` subclass:
    
    
    class FlexEmployee(ndb.Expando):
        name = ndb.StringProperty()
        age = ndb.IntegerProperty()

`...`
    
    
    employee = FlexEmployee(name='Sandy', location='SF')

This gives `employee` a `name` attribute with value `'Sandy'`, an `age` attribute with value `None`, and a dynamic attribute `location` with value `'SF'`.

To create an `Expando` subclass whose properties are unindexed, set `_default_indexed = False` in the subclass definition:
    
    
    class Specialized(ndb.Expando):
        _default_indexed = False

`...`
    
    
    e = Specialized(foo='a', bar=['b'])
    return e._properties
    # {
    #     'foo': GenericProperty('foo', indexed=False),
    #     'bar': GenericProperty('bar', indexed=False, repeated=True)
    # }

You can also set `_default_indexed` on an `Expando` entity. In this case it will affect all properties assigned _after_ it was set.

Another useful technique is querying an `Expando` kind for a dynamic property. A query like the following
    
    
    FlexEmployee.query(FlexEmployee.location == 'SF')

won't work, because the class doesn't have a property object for the location property. Instead, use `GenericProperty`, the class `Expando` uses for dynamic properties:
    
    
    FlexEmployee.query(ndb.GenericProperty('location') == 'SF')

## Using Model Hooks

NDB offers a lightweight hooking mechanism. By defining a hook, an application can run some code before or after some type of operations; for example, a `Model` might run some function before every `get()`.

A hook function runs when using the synchronous, asynchronous and multi versions of the appropriate method. For example, a "pre-get" hook would apply to all of `get()`, `get_async()`, and `get_multi()`. There are pre-RPC and post-RPC versions of each hook.

Hooks can be useful for the following:

  * query caching
  * auditing Cloud Datastore activity per-user
  * mimicking database triggers



The following example shows how to define hook functions:
    
    
    from google.appengine.ext import ndb

`...`
    
    
    class Friend(ndb.Model):
        name = ndb.StringProperty()
    
        def _pre_put_hook(self):
            _notify('Gee wiz I have a new friend!')
    
        @classmethod
        def _post_delete_hook(cls, key, future):
            _notify('I have found occasion to rethink our friendship.')

`...`
    
    
    f = Friend()
    f.name = 'Carole King'
    f.put()  # _pre_put_hook is called
    fut = f.key.delete_async()  # _post_delete_hook not yet called
    fut.get_result()  # _post_delete_hook is called

If you use post-hooks with asynchronous APIs, the hooks are triggered by calling `check_result()`, `get_result()` or yielding (inside a tasklet) an async method's future. Post hooks do not check whether the RPC was successful; the hook runs regardless of failure.

All post- hooks have a [`Future`](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/async) argument at the end of the call signature. This `Future` object holds the result of the action. You can call `get_result()` on this `Future` to retrieve the result; you can be sure that `get_result()` won't block, since the `Future` is complete by the time the hook is called.

Raising an exception during a pre-hook prevents the request from taking place. Although hooks are triggered inside `<var>*</var>_async` methods, you cannot pre-empt an RPC by raising `tasklets.Return` in a pre-RPC hook.

## What's next

  * [Learn more about the NDB Model class](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass).
  * [Explore the entity property reference documentation](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
