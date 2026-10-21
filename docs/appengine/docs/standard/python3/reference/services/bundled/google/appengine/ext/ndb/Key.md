---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Key/
title: google.appengine.ext.ndb.Key \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:07:31.508821+00:00
---

# google.appengine.ext.ndb.Key  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Key Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L125-L660) An immutable datastore key. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Key(
        *_args, **kwargs
    )
    

For flexibility and convenience, multiple constructor signatures are supported. The primary way to construct a key is using positional arguments:

  * Key(kind1, id1, kind2, id2, ...).

This is shorthand for either of the following two longer forms:

  * Key(pairs=[(kind1, id1), (kind2, id2), ...])
  * Key(flat=[kind1, id1, kind2, id2, ...])

Either of the above constructor forms can additionally pass in another key using parent=. The (kind, id) pairs of the parent key are inserted before the (kind, id) pairs passed explicitly. You can also construct a Key from a 'url-safe' encoded string:

  * Key(urlsafe=)

For esoteric purposes the following constructors exist:

  * Key(reference=) -- passing in a low-level Reference object
  * Key(serialized=) -- passing in a serialized low-level Reference
  * Key() -- for unpickling, the same as Key(**)

The 'url-safe' string is really a websafe-base64-encoded serialized Reference, but it's best to think of it as just an opaque unique string. Additional constructor keyword arguments:

  * app= \-- specify the application id
  * namespace= \-- specify the namespace

If a Reference is passed (using one of reference, serialized or urlsafe), the args and namespace keywords must match what is already present in the Reference (after decoding if necessary). The parent keyword cannot be combined with a Reference in any form. Keys are immutable, which means that a Key object cannot be modified once it has been created. This is enforced by the implementation as well as Python allows. For access to the contents of a key, the following methods and operations are supported:

  * repr(key), str(key) -- return a string representation resembling the shortest constructor form, omitting the app and namespace unless they differ from the default value.
  * key1 == key2, key1 != key2 -- comparison for equality between Keys.
  * hash(key) -- a hash value sufficient for storing Keys in a dict.
  * key.pairs() -- a tuple of (kind, id) pairs.
  * key.flat() -- a tuple of flattened kind and id values, i.e. (kind1, id1, kind2, id2, ...).
  * key.app() -- the application id.
  * key.id() -- the string or integer id in the last (kind, id) pair, or None if the key is incomplete.
  * key.string_id() -- the string id in the last (kind, id) pair, or None if the key has an integer id or is incomplete.
  * key.integer_id() -- the integer id in the last (kind, id) pair, or None if the key has a string id or is incomplete.
  * key.namespace() -- the namespace.
  * key.kind() -- a shortcut for key.pairs()[-1][0].
  * key.parent() -- a Key constructed from all but the last (kind, id) pairs.
  * key.urlsafe() -- a websafe-base64-encoded serialized Reference.
  * key.serialized() -- a serialized Reference.
  * key.reference() -- a Reference object. The caller promises not to mutate it.

Keys also support interaction with the datastore; these methods are the only ones that engage in any kind of I/O activity. For Future objects, see the document for ndb/tasklets.py.

  * key.get() -- return the entity for the Key.
  * key.get_async() -- return a Future whose eventual result is the entity for the Key.
  * key.delete() -- delete the entity for the Key.
  * key.delete_async() -- asynchronously delete the entity for the Key.

Keys may be pickled. Subclassing Key is best avoided; it would be hard to get right.

## Methods

### `app`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L514-L516)
    
    
    app()
    

Return the application id.

### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L627-L632)
    
    
    delete(
        **ctx_options
    )
    

Synchronously delete the entity for this Key. This is a no-op if no such entity exists.

### `delete_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L634-L653)
    
    
    delete_async(
        **ctx_options
    )
    

Schedule deletion of the entity for this Key. This returns a Future, whose result becomes available once the deletion is complete. If no such entity exists, a Future is still returned. In all cases the Future's result is None (i.e. there is no way to tell whether the entity existed or not).

### `flat`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L553-L559)
    
    
    flat()
    

Return a tuple of alternating kind and id values.

### `from_old_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L655-L657)
    
    
    @classmethod
    from_old_key(
        old_key
    )
    

### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L601-L606)
    
    
    get(
        **ctx_options
    )
    

Synchronously get the entity for this Key. Return None if there is no such entity.

### `get_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L608-L625)
    
    
    get_async(
        **ctx_options
    )
    

Return a Future whose result is the entity for this Key. If no such entity exists, a Future is still returned, and the Future's eventual return result be None.

### `id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L518-L524)
    
    
    id()
    

Return the string or integer id in the last (kind, id) pair, if any. | Returns  
---  
A string or integer id, or None if the key is incomplete.   
  
### `integer_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L537-L546)
    
    
    integer_id()
    

Return the integer id in the last (kind, id) pair, if any.

Returns  
---  
An integer id, or None if the key has a string id or is incomplete.   
  
### `kind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L561-L566)
    
    
    kind()
    

Return the kind of the entity referenced.

This is the kind from the last (kind, id) pair.

### `namespace`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L510-L512)
    
    
    namespace()
    

Return the namespace.

### `pairs`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L548-L551)
    
    
    pairs()
    

Return a tuple of (kind, id) pairs.

### `parent`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L493-L501)
    
    
    parent()
    

Return a Key constructed from all but the last (kind, id) pairs.

If there is only one (kind, id) pair, return None.

### `reference`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L568-L581)
    
    
    reference()
    

Return the Reference object for this Key.

This is a entity_pb2.Reference instance -- a protocol buffer class used by the lower-level API to the datastore.

NOTE: The caller should not mutate the return value.

### `root`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L503-L508)
    
    
    root()
    

Return the root key. This is either self or the highest parent.

### `serialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L583-L585)
    
    
    serialized()
    

Return a serialized Reference object for this Key.

### `string_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L526-L535)
    
    
    string_id()
    

Return the string id in the last (kind, id) pair, if any.

Returns  
---  
A string id, or None if the key has an integer id or is incomplete.   
  
### `to_old_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L659-L660)
    
    
    to_old_key()
    

### `urlsafe`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/key.py#L587-L596)
    
    
    urlsafe()
    

Return a url-safe string encoding this Key's Reference.

This string is compatible with other APIs and languages and with the strings used to represent Keys in GQL and in the App Engine Admin Console.

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L55-L55)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ge__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L57-L57)
    
    
    __ge__(
        other
    )
    

Return self>=value.

### `__gt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L52-L57)
    
    
    __gt__(
        other
    )
    

Return self>value.

### `__le__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L54-L54)
    
    
    __le__(
        other
    )
    

Return self<=value.

### `__lt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L53-L53)
    
    
    __lt__(
        other
    )
    

Return self<value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L56-L56)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
