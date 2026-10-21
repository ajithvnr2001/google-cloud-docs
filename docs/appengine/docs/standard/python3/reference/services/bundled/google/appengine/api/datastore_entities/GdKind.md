---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_entities/GdKind/
title: google.appengine.api.datastore_entities.GdKind \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:39:29.703405+00:00
---

# google.appengine.api.datastore_entities.GdKind  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_entities/GdKind/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_entities.GdKind Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_entities.py#L46-L180) A base class for gd namespace kinds. Inherits From: [`Entity`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Entity), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.datastore_entities.GdKind(
        kind, title, kind_properties, contact_properties=[]
    )
    

This class contains common logic for all gd namespace kinds. For example, this class translates datastore `(app id, kind, key)` tuples to tag: URIs appropriate for use in  tags. | 

## Args  
  
---  
  
`kind` |  String   
`title` |  String   
`kind_properties` |  List of strings   
`contact_properties` |  List of string   
  
## Methods

### `FromPb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1103-L1123)
    
    
    @staticmethod
    FromPb(
        pb,
        validate_reserved_properties=True,
        default_kind='<not specified>'
    )
    

Static factory method. Returns the Entity representation of the given protocol buffer (datastore_pb.Entity).

Args  
---  
  
`pb` |  datastore_pb.Entity or str encoding of a datastore_pb.Entity   
`validate_reserved_properties` |  deprecated   
`default_kind` |  str, the kind to use if the pb has no key.   
  
Returns  
---  
  
`Entity` |  the Entity representation of pb   
  
### `ToPb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L1041-L1047)
    
    
    ToPb()
    

Converts this Entity to its protocol buffer representation.

Returns  
---  
entity_pb2.Entity   
  
### `ToXml`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_entities.py#L172-L180)
    
    
    ToXml()
    

Returns an XML representation of this entity, as a string.

### `app`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L841-L845)
    
    
    app()
    

Returns the name of the application that created this entity, a string or None if not set.

### `clear`
    
    
    clear()
    

D.clear() -> None. Remove all items from D.

### `copy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L937-L940)
    
    
    copy()
    

The copy method is not supported.

### `entity_group`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L881-L887)
    
    
    entity_group()
    

Returns this entity's entity group as a Key.

Note that the returned Key will be incomplete if this is a a root entity and its key is incomplete.

### `fromkeys`
    
    
    fromkeys(
        value, /
    )
    

Create a new dictionary with keys from iterable and values set to value.

### `get`
    
    
    get(
        key, default, /
    )
    

Return the value for key if key is in the dictionary, else default.

### `is_projection`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L861-L869)
    
    
    is_projection()
    

Returns if this entity is a projection from full entity.

#### Projected entities:

  * may not contain all properties from the original entity;
  * only contain single values for lists;
  * may not contain values with the same type as the original entity.



### `is_saved`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L855-L859)
    
    
    is_saved()
    

Returns if this entity has been saved to the datastore.

### `items`
    
    
    items()
    

D.items() -> a set-like object providing a view on D's items

### `key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L871-L873)
    
    
    key()
    

Returns this entity's primary key, a Key instance.

### `keys`
    
    
    keys()
    

D.keys() -> a set-like object providing a view on D's keys

### `kind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L851-L853)
    
    
    kind()
    

Returns this entity's kind, a string.

### `namespace`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L847-L849)
    
    
    namespace()
    

Returns the namespace of this entity, a string or None.

### `parent`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L875-L879)
    
    
    parent()
    

Returns this entity's parent, as a Key. If this entity has no parent, returns None.

### `pop`
    
    
    pop()
    

D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

### `popitem`
    
    
    popitem()
    

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

### `set_unindexed_properties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L894-L903)
    
    
    set_unindexed_properties(
        unindexed_properties
    )
    

### `setdefault`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L916-L925)
    
    
    setdefault(
        name, value
    )
    

If the property exists, returns its value. Otherwise sets it to value.

If the property name is the empty string or not a string, raises `BadPropertyError`. If the value is not a supported type, raises `BadValueError`.

### `unindexed_properties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L889-L892)
    
    
    unindexed_properties()
    

Returns this entity's unindexed properties, as a frozenset of strings.

### `update`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L927-L935)
    
    
    update(
        other
    )
    

Updates this entity's properties from the values in other.

If any property name is the empty string or not a string, raises `BadPropertyError`. If any value is not a supported type, raises `BadValueError`.

### `values`
    
    
    values()
    

D.values() -> an object providing a view on D's values

### `__contains__`
    
    
    __contains__(
        key, /
    )
    

True if the dictionary has the specified key, else False.

### `__eq__`
    
    
    __eq__(
        value, /
    )
    

Return self==value.

### `__ge__`
    
    
    __ge__(
        value, /
    )
    

Return self>=value.

### `__getitem__`
    
    
    __getitem__()
    

x.**getitem**(y) <==> x[y]

### `__gt__`
    
    
    __gt__(
        value, /
    )
    

Return self>value.

### `__iter__`
    
    
    __iter__()
    

Implement iter(self).

### `__le__`
    
    
    __le__(
        value, /
    )
    

Return self<=value.

### `__len__`
    
    
    __len__()
    

Return len(self).

### `__lt__`
    
    
    __lt__(
        value, /
    )
    

Return self<value.

### `__ne__`
    
    
    __ne__(
        value, /
    )
    

Return self!=value.

### `__or__`
    
    
    __or__(
        value, /
    )
    

Return self|value.

### `__ror__`
    
    
    __ror__(
        value, /
    )
    

Return value|self.

## Class Variables  
  
---  
  
FOOTER |  `'\n</entry>'`  
HEADER |  `("<entry xmlns:gd='http://schemas.google.com/g/2005'>\n" " <category scheme='http://schemas.google.com/g/2005#kind'\n" " term='http://schemas.google.com/g/2005#%s' />")`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
