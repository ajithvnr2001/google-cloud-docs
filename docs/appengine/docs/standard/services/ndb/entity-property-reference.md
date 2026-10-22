---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference/
title: Entity Property Reference \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:03.253896+00:00
---

# Entity Property Reference  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/entity-property-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Entity Property Reference Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Firestore in Datastore mode (Datastore) supports a variety of data types for property values. These include, among others:

  * Integers
  * Floating-point numbers
  * Strings
  * Dates
  * Binary data



For a full list of types, see properties and value types. 

## Properties and value types

The data values associated with an entity consist of one or more _properties._ Each property has a name and one or more values. A property can have values of more than one type, and two entities can have values of different types for the same property. Properties can be indexed or unindexed (queries that order or filter on a property _P_ will ignore entities where _P_ is unindexed). An entity can have at most 20,000 indexed properties.

**Note:** Properties with multiple values can be useful, for instance, when performing queries with equality filters: an entity satisfies the query if any of its values for a property matches the value specified in the filter. For more details on multiple-valued properties, including issues you should be aware of, see the [Datastore Queries](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/queries) page.

The following value types are supported:

When a query involves a property with values of mixed types, Datastore uses a deterministic ordering based on the internal representations:

  1. Null values
  2. Fixed-point numbers 
     * Integers
     * Dates and times 
  3. Boolean values
  4. Byte sequences 
     * Unicode string
     * Blobstore keys
     *      * Datastore keys



Because long text strings and long byte strings are not indexed, they have no ordering defined.

**Note:** Integers and floating-point numbers are considered separate types in Datastore. If an entity uses a mix of integers and floats for the same property, all integers will be sorted before all floats: for example,  
  
`7` < `3.2`

## Property Types

NDB supports the following property types:

Property type | Description  
---|---  
`IntegerProperty` | 64-bit signed integer  
`FloatProperty` | Double-precision floating-point number  
`BooleanProperty` | Boolean  
`StringProperty` | Unicode string; up to 1500 bytes, indexed  
`TextProperty` | Unicode string; unlimited length, not indexed  
`BlobProperty` | Uninterpreted byte string:  
if you set `indexed=True`, up to 1500 bytes, indexed;  
if `indexed` is `False` (the default), unlimited length, not indexed.  
Optional keyword argument: `compressed`.  
`DateTimeProperty` | Date and time (see Date and Time Properties)  
`DateProperty` | Date (see Date and Time Properties)  
`TimeProperty` | Time (see Date and Time Properties)  
`GeoPtProperty` | Geographical location. This is a `ndb.GeoPt` object. The object has attributes `lat` and `lon`, both floats. You can construct one with two floats like `ndb.GeoPt(52.37, 4.88)` or with a string `ndb.GeoPt("52.37, 4.88")`. (This is actually the same class as [`db.GeoPt`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/GeoPtProperty))  
`KeyProperty` | Datastore key  
Optional keyword argument: kind=kind, to require that keys assigned to this property always have the indicated kind. May be a string or a Model subclass.  
`BlobKeyProperty` | Blobstore key  
Corresponds to `BlobReferenceProperty` in the old db API, but the property value is a `BlobKey` instead of a `BlobInfo`; you can construct a `BlobInfo` from it using `BlobInfo(blobkey)`  
`UserProperty` | User object.  
`StructuredProperty` | Includes one kind of model inside another, by value (see Structured Properties)  
`LocalStructuredProperty` | Like `StructuredProperty`, but on-disk representation is an opaque blob and is not indexed (see Structured Properties).  
Optional keyword argument: `compressed`.  
`JsonProperty` | Value is a Python object (such as a list or a dict or a string) that is serializable using Python's `json` module; Datastore stores the JSON serialization as a blob. Unindexed by default.  
Optional keyword argument: `compressed`.  
`PickleProperty` | Value is a Python object (such as a list or a dict or a string) that is serializable using Python's pickle protocol; Datastore stores the pickle serialization as a blob. Unindexed by default.  
Optional keyword argument: `compressed`.  
`GenericProperty` | Generic value  
Used mostly by the [`Expando`](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entities#expando) class, but also usable explicitly. Its type may be any of `int`, `long`, `float`, `bool`, `str`, `unicode`, `datetime`, `Key`, `BlobKey`, `GeoPt`, `User`, `None`.  
`ComputedProperty` | Value computed from other properties by a user-defined function. (See Computed Properties.)  
  
Some of these properties have an optional keyword argument, `compressed`. If the property has `compressed=True`, then its data is compressed with gzip on disk. It takes up less space but needs CPU to encode/decode on write and read operations.

Both compression and decompression are "lazy"; a compressed property value will only be decompressed the first time you access it. If you read an entity containing a compressed property value and write it back without accessing the compressed property, it won't be decompressed and compressed at all. The [in-context cache](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/cache#incontext) participates in this lazy scheme as well, but [memcache](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/cache#memcache) always stores the compressed value for compressed properties.

Because of the extra CPU time needed for compression, it is usually best to use compressed properties only if the data would be too big to fit without it. Remember that gzip-based compression is typically not effective for images and other media data, since those formats already are compressed using a media-specific compression algorithm (e.g. JPEG for images).

## Property Options

Most property types support some standard arguments. The first is an optional positional argument specifying the property's Datastore name. You can use this to give the property a different name in Datastore than from the application's viewpoint. A common use for this is to reduce space in Datastore, letting Datastore use abbreviated property names while your code uses longer, more meaningful ones. For example,
    
    
    class Employee(ndb.Model):
        full_name = ndb.StringProperty('n')
        retirement_age = ndb.IntegerProperty('r')

This is particularly useful for repeated properties for which you expect many values per entity.

In addition, most property types support the following keyword arguments:

Argument | Type | Default | Description  
---|---|---|---  
`indexed` | `bool` | Usually `True` | Include property in Datastore's indexes; if `False`, values cannot be queried but writes are faster. Not all property types support indexing; setting `indexed` to `True` fails for these.  
Unindexed properties cost fewer write ops than indexed properties.  
`repeated` | `bool` | `False` | Property value is a Python list containing values of the underlying type (see Repeated Properties).  
Cannot be combined with `required=True` or `default=True`.  
`required` | `bool` | `False` | Property must have a value specified.  
`default` | Property's underlying type | None | Default value of property if none explicitly specified.  
`choices` | List of values of underlying type | `None` | Optional list of allowable values.  
`validator` | Function | `None` | Optional function to validate and possibly coerce the value. Will be called with arguments `(prop, value)` and should either return the (possibly coerced) value or raise an exception. Calling the function again on a coerced value should not modify the value further. (For example, returning `value.strip()` or `value.lower()` is fine, but not `value&nbsp;+&nbsp;'$'`.) May also return `None`, which means "no change". See also Writing Property Subclasses  
`verbose_name` | string | `None` | Optional HTML label to use in web form frameworks like jinja2.  
  
## Repeated Properties

Any property with `repeated=True` becomes a _repeated property_. The property takes a list of values of the underlying type, rather than a single value. For example, the value of a property defined with `IntegerProperty(repeated=True)` is a list of integers.

Datastore may see multiple values for such a property. A separate index record is created for each value. This affects query semantics; see [Querying for Repeated Properties](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#repeated_properties) for an example.

This example uses a repeated property:
    
    
    class Article(ndb.Model):
        title = ndb.StringProperty()
        stars = ndb.IntegerProperty()
        tags = ndb.StringProperty(repeated=True)

`...`
    
    
    article = Article(
        title='Python versus Ruby',
        stars=3,
        tags=['python', 'ruby'])
    article.put()

This creates a Datastore entity with the following contents:
    
    
    assert article.title == 'Python versus Ruby'
    assert article.stars == 3
    assert sorted(article.tags) == sorted(['python', 'ruby'])

When querying for the `tags` property, this entity will satisfy a query for either `'python'` or `'ruby'`.

When updating a repeated property, you can either assign it a new list or mutate the existing list in place. When you assign a new list, the types of the list items are validated immediately. Invalid item types (for example, assigning `[1,&nbsp;2]` to `art.tags` above) raise an exception. When you mutate the list, the change is not validated immediately. Instead, the value will be validated when you write the entity to Datastore.

Datastore preserves the order of the list items in a repeated property, so you can assign some meaning to their ordering.

## Date and Time Properties

Three property types are available for storing date- and time-related values:

  * `DateProperty`
  * `TimeProperty`
  * `DateTimeProperty`



These take values belonging to the corresponding classes (`date`, `time`, `datetime`) of the standard Python `datetime` module. The most general of the three is `DateTimeProperty`, which denotes both a calendar date and a time of day; the others are occasionally useful for special purposes requiring just a date (such as a date of birth) or just a time (such as a meeting time). For technical reasons, `DateProperty` and `TimeProperty` are subclasses of `DateTimeProperty`, but you shouldn't depend on this inheritance relationship (and note that it differs from the inheritance relationships between the underlying classes defined by the `datetime` module itself).

**Note:** App Engine clock times are always expressed in coordinated universal time (UTC). This becomes relevant if you use the current date or time (`datetime.datetime.now()`) as a value or convert between datetime objects and POSIX timestamps or time tuples. However, no explicit time zone information is stored in Datastore, so if you are careful you can use these to represent local times in any timezone—if you use the current time or the conversions.

Each of these properties has two extra Boolean keyword options:

Option | Description  
---|---  
`auto_now_add` | Set property to current date/time when entity is created. You can manually override this property. When the entity is updated, the property doesn't change. For that behavior, use `auto_now`.  
`auto_now` | Set property to current date/time when entity is created and whenever it is updated.  
  
These options cannot be combined with `repeated=True`. Both of them default to `False`; if both are set to `True`, `auto_now` takes precedence. It is possible to override the value for a property with `auto_now_add=True`, but not for one with `auto_now=True`. The automatic value is not generated until the entity is written; that is, these options don't provide dynamic defaults. (These details differ from the old db API.)

**Note:** When a transaction writing a property with `auto_now_add=True` fails and is later retried, it will reuse the same time value as on the original try rather than update it to the time of the retry. If the transaction fails permanently, the property's value will still be set in the in-memory copy of the entity.

## Structured Properties

You can structure a model's properties. For example, you can define a model class Contact containing a list of addresses, each with internal structure. _Structured properties_ (type `StructuredProperty```) let you do this; for example:
    
    
    class Address(ndb.Model):
        type = ndb.StringProperty()  # E.g., 'home', 'work'
        street = ndb.StringProperty()
        city = ndb.StringProperty()

`...`
    
    
    class Contact(ndb.Model):
        name = ndb.StringProperty()
        addresses = ndb.StructuredProperty(Address, repeated=True)

`...`
    
    
    guido = Contact(
        name='Guido',
        addresses=[
            Address(
                type='home',
                city='Amsterdam'),
            Address(
                type='work',
                street='Spear St',
                city='SF')])
    
    guido.put()

This creates a single Datastore entity with the following properties:
    
    
    assert guido.name == 'Guido'
    addresses = guido.addresses
    assert addresses[0].type == 'home'
    assert addresses[1].type == 'work'
    assert addresses[0].street is None
    assert addresses[1].street == 'Spear St'
    assert addresses[0].city == 'Amsterdam'
    assert addresses[1].city == 'SF'

Reading back such an entity reconstructs the original `Contact` entity exactly. Although the `Address` instances are defined using the same syntax as for model classes, they are not full-fledged entities. They don't have their own keys in Datastore. They cannot be retrieved independently of the `Contact` entity to which they belong. An application can, however, query for the values of their individual fields; see [Filtering for Structured Property Values](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/queries#filtering_structured_properties). Note that `address.type`, `address.street`, and `address.city` are viewed as parallel arrays from Datastore's viewpoint, but the NDB library hides this aspect and constructs the corresponding list of `Address` instances.

You can specify the usual property options for structured properties (except `indexed`). The Datastore name is the _second_ positional argument in this case (the first being the model class used to define the substructure).

When you don't need to query for a substructure's internal properties, you can use a local structured property (`LocalStructuredProperty`) instead. If you replace `StructuredProperty` with `LocalStructuredProperty` in the example above, the behavior of the Python code is the same, but Datastore sees just an opaque blob for each address. The `guido` entity created in the example would be stored as follows:
    
    
    name = 'Guido'
    address = &lt;opaque blob for {'type': 'home', 'city': 'Amsterdam'}&gt;
    address = &lt;opaque blob for {'type': 'work', 'city': 'SF',
                                  'street': 'Spear St'}&gt;
    

The entity will be read back correctly. Since properties of this type are always unindexed, you cannot query for address values.

**Note:** A `StructuredProperty` with a nested property (whether or not it is structured) supports only a single layer of repeated properties. The `StructuredProperty` can be repeated, or the nested property can be repeated, but not both. A work-around is to use `LocalStructuredProperty`, which does not have this constraint (but does not allow queries on its property values).

## Computed Properties

_Computed properties_ (`ComputedProperty`) are read-only properties whose value is computed from other property values by an application-supplied function. Note that a computed property only supports the types that are supported by generic properties! The computed value is written to Datastore so that it can be queried and displayed in the Datastore viewer, but the stored value is ignored when the entity is read back from Datastore; rather, the value is recomputed by calling the function whenever the value is requested. For example:
    
    
    class SomeEntity(ndb.Model):
        name = ndb.StringProperty()
        name_lower = ndb.ComputedProperty(lambda self: self.name.lower())

`...`
    
    
    entity = SomeEntity(name='Nick')
    entity.put()

This stores an entity with the following property values:
    
    
    assert entity.name == 'Nick'
    assert entity.name_lower == 'nick'

If we change name to 'Nickie' and ask for the value of `name_lower`, it returns 'nickie':
    
    
    entity.name = 'Nick'
    assert entity.name_lower == 'nick'
    entity.name = 'Nickie'
    assert entity.name_lower == 'nickie'

**Note:** Use `ComputedProperty` if the application **queries** for the computed value. If you just want to use the derived version in Python code, define a regular method or use Python's `@property` built-in.**Note:** If you create a model without a key manually specified, and instead rely on Datastore to auto-generate the entity's id, then on your first `put()` a `ComputedProperty` will not be able to read the id field since the field is computed before the id is generated. If you need a `ComputedProperty` that uses the entity's id, you can use the [`allocate_ids`](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model_allocate_ids) method to generate an id and key to create the entity with, so that your `ComputedProperty` will be able to reference that id on the entity's first `put()`.**Caution:** `ComputedProperties` are not calculated on `query`, but rather on `put()`. If you update a model's schema to include a `ComputedProperty`, you should remember to update existing entities by loading and writing them to Datastore.

## Google Protocol RPC Message Properties

The [Google Protocol RPC](https://docs.cloud.google.com/appengine/docs/standard/python/tools/protorpc) library uses [`Message`](https://docs.cloud.google.com/appengine/docs/standard/python/tools/protorpc/messages/messageclass) objects for structured data; they can represent RPC requests, responses, or other things. NDB provides an API for storing Google Protocol RPC `Message` objects as entity properties. Suppose you define a `Message` subclass:
    
    
    from protorpc import messages

`...`
    
    
    class Note(messages.Message):
        text = messages.StringField(1, required=True)
        when = messages.IntegerField(2)

You can store `Note` objects in Datastore as entity property values by using NDB's `msgprop` API.
    
    
    from google.appengine.ext import ndb
    from google.appengine.ext.ndb import msgprop

`...`
    
    
    class NoteStore(ndb.Model):
        note = msgprop.MessageProperty(Note, indexed_fields=['when'])
        name = ndb.StringProperty()

`...`
    
    
    my_note = Note(text='Excellent note', when=50)
    
    ns = NoteStore(note=my_note, name='excellent')
    key = ns.put()
    
    new_notes = NoteStore.query(NoteStore.note.when >= 10).fetch()

If you want to query for field names, they must be indexed. You can specify a list of field names that will be indexed with the `indexed_fields` parameter to `MessageProperty`.

`MessageProperty` supports many, but not all, Property options. It supports:

  * `name`
  * `repeated`
  * `required`
  * `default`
  * `choices`
  * `validator`
  * `verbose_name`



Message properties do not support the `indexed` property option; you can't index `Message` values. (You can index fields of a message as described above.)

Nested messages (using `MessageField`) also work:
    
    
    class Notebook(messages.Message):
        notes = messages.MessageField(Note, 1, repeated=True)

`...`
    
    
    class SignedStorableNotebook(ndb.Model):
        author = ndb.StringProperty()
        nb = msgprop.MessageProperty(
            Notebook, indexed_fields=['notes.text', 'notes.when'])

`MessageProperty` has a special property option, `protocol`, which specifies how the message object is serialized to Datastore. The values are protocol names as used by `protorpc.remote.Protocols` class. Supported protocol names are `protobuf` and `protojson`; the default is `protobuf`.

`msgprop` also defines `EnumProperty`, a property type which can be used to store a `protorpc.messages.Enum` value in an entity. Example:
    
    
    class Color(messages.Enum):
        RED = 620
        GREEN = 495
        BLUE = 450

`...`
    
    
    class Part(ndb.Model):
        name = ndb.StringProperty()
        color = msgprop.EnumProperty(Color, required=True)

`...`
    
    
    p1 = Part(name='foo', color=Color.RED)
    print p1.color  # prints "RED"

`EnumProperty` stores the value as an integer; in fact, `EnumProperty` is a subclass of `IntegerProperty`. This implies that you can rename your enum values without having to modify already-stored entities, but you cannot renumber them.

The EnumProperty supports the following property options:

  * `name`
  * `indexed`
  * `repeated`
  * `required`
  * `default`
  * `choices`
  * `validator`
  * `verbose_name`



## About NDB entity models

An NDB entity model can define _properties_. Entity properties are a bit like data members of Python classes, a structured way to hold data; they are also a bit like fields in a database schema.

A typical application defines a data model by defining a class that inherits from `Model` with some property class attributes. For example:
    
    
    from google.appengine.ext import ndb

`...`
    
    
    class Account(ndb.Model):
        username = ndb.StringProperty()
        userid = ndb.IntegerProperty()
        email = ndb.StringProperty()

Here, `username`, `userid`, and `email` are properties of `Account`.

Don't name a property "key." This name is reserved for a special property used to store the Model key. Though it may work locally, a property named "key" will prevent deployment to App Engine.

There are several other property types. Some are handy for representing dates and times and have convenient auto-update features.

An application can adjust a property's behavior by specifying options on the property; these can ease validation, set defaults, or change query indexing.

A model can have more complex properties. Repeated properties are list-like. Structured properties are object-like. Read-only computed properties are defined via functions; this makes it easy to define a property in terms of one or more other properties. [Expando](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/creating-entities#expando) models can define properties dynamically.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
