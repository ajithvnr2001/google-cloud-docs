---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass/
title: NDB Key Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:52.667110+00:00
---

# NDB Key Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Key Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

An instance of the `Key` class represents an immutable Datastore key.

This page has API reference documentation. For an overview, see [NDB Entities and Keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entities). 

## Introduction

A Key is an immutable Datastore key. Applications normally use them to refer to entities. Any entity that has been stored has a key. To get an entity's key, use the model's [key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model_key) property. To retrieve an entity from its key, call the `Key` object's get() method.

Keys support comparisons, for example `key1 == key2` or `key1 < key2`. These operators compare application ID, namespace, and the full "ancestor path". They use the same ordering as the Datastore uses for queries when ordering by a key property or by key. 

`repr(key)` or `str(key)` returns a string representation resembling the shortest constructor form, omitting the app and namespace unless they differ from the default value.

`hash(key)` works. Thus, you can store keys in a hash table. 

## Constructors

For flexibility and convenience, multiple constructor signatures are supported.

class Key(kind1, id1, kind2, id2, ...)
class Key(pairs=[(kind1, id1), (kind2, id2), ...])
class Key(flat=[kind1, id1, kind2, id2, ...])
class Key(urlsafe=string)
    

The positional arguments kind1, id1, kind2, id2... are in "ancestor" order. (This is a shortcut for `flat=[kind1, id1, kind2, id2]`) Parents come before children. 

The positional-arguments, `pairs`, and `flat` constructor forms can additionally pass in another key using parent=key. The (kind, id) pairs of the parent key are inserted before the (kind, id) pairs passed explicitly. 

The `urlsafe` keyword parameter uses a websafe-base64-encoded serialized reference but it's best to think of it as just an opaque unique string. 

Additional constructor keyword arguments: 

app
    specify the application id (a string) 
namespace
    specify the namespace (a string) 

## Instance Methods that Don't Affect the Datastore

The following methods access the contents of a key. They do not engage in any Datastore I/O activity.

pairs()
    

Returns a tuple of (kind, id) pairs.

flat()
    

Returns a tuple of flattened kind and id values (kind1, id1, kind2, id2, ...).

app()
    

Returns the application id.

id()
    

Returns the string or integer id in the last (kind, id) pair, or `None` if the key is incomplete.

string_id()
    

Returns the string id in the last (kind, id) pair, or `None` if the key has an integer id or is incomplete.

integer_id()
    

Returns the integer id in the last (kind, id) pair, or `None` if the key has an string id or is incomplete.

namespace()
    

Returns the namespace.

kind()
    

Returns the kind in the last (kind, id) pair.

parent()
    

Returns a Key constructed from all but the last (kind, id) pair (or `None` if the key has just one (kind, id) pair).

urlsafe()
    

Returns a websafe-base64-encoded serialized version of the key.

**Note:** The URL-safe string looks cryptic, but it is not encrypted! It can easily be decoded to recover the original entity's kind and identifier. 

to_old_key()
    

Returns a `[Key](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/keyclass)` for the "old" Datastore API (`db`).

## Instance Methods that Affect the Datastore

These methods interact with the Datastore.

get(**ctx_options)
    

Returns the entity for the Key.

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)
get_async(**ctx_options)
    

Returns a `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` whose eventual result is the entity for the Key.

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)
delete(**ctx_options)
    

Delete the entity for the Key.

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)
delete_async(**ctx_options)
    

Asynchronously delete the entity for the Key.

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)

## Class Methods

from_old_key(k)
    

Returns an NDB key from the passed in "old" Datastore API (`db`) `[Key](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/keyclass)`.

**Arguments**

**ctx_options
    [Context options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
