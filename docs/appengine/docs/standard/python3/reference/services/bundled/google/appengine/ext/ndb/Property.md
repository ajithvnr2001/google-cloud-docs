---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Property/
title: google.appengine.ext.ndb.Property \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:07.483102+00:00
---

# google.appengine.ext.ndb.Property  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Property/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Property Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L789-L1570) A class describing a typed, persisted attribute of a Cloud Datastore entity. Inherits From: [`ModelAttribute`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/ModelAttribute), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Property(
        name=None,
        indexed=None,
        repeated=None,
        required=None,
        default=None,
        choices=None,
        validator=None,
        verbose_name=None,
        write_empty_list=None
    )
    

Not to be confused with Python's 'property' built-in. This is just a base class; there are specific subclasses that describe Properties of various types (and GenericProperty which describes a dynamically typed Property). All special Property attributes, even those considered 'public', have names starting with an underscore, because StructuredProperty uses the non-underscore attribute namespace to refer to nested Property names; this is essential for specifying queries on subproperties (see the module docstring). The Property class and its predefined subclasses allow easy subclassing using composable (or stackable) validation and conversion APIs. These require some terminology definitions:

  * A 'user value' is a value such as would be set and accessed by the application code using standard attributes on the entity.
  * A 'base value' is a value such as would be serialized to and deserialized from Cloud Datastore.

The values stored in ent._values[name] and accessed by _store_value() and _retrieve_value() can be either user values or base values. To retrieve user values, use _get_user_value(). To retrieve base values, use _get_base_value(). In particular, _get_value() calls _get_user_value(), and _serialize() effectively calls _get_base_value(). To store a user value, just call _store_value(). To store a base value, wrap the value in a _BaseValue() and then call _store_value(). A Property subclass that wants to implement a specific transformation between user values and serialiazble values should implement two methods, _to_base_type() and _from_base_type(). These should _NOT_ call their super() method; super calls are taken care of by _call_to_base_type() and _call_from_base_type(). This is what is meant by composable (or stackable) APIs. The API supports 'stacking' classes with ever more sophisticated user<\-->base conversions: the user-->base conversion goes from more sophisticated to less sophisticated, while the base-->user conversion goes from less sophisticated to more sophisticated. For example, see the relationship between BlobProperty, TextProperty and StringProperty. In addition to _to_base_type() and _from_base_type(), the _validate() method is also a composable API. The validation API distinguishes between 'lax' and 'strict' user values. The set of lax values is a superset of the set of strict values. The _validate() method takes a lax value and if necessary converts it to a strict value. This means that when setting the property value, lax values are accepted, while when getting the property value, only strict values will be returned. If no conversion is needed, _validate() may return None. If the argument is outside the set of accepted lax values, _validate() should raise an exception, preferably TypeError or datastore_errors.BadValueError. Example/boilerplate: def _validate(self, value): 'Lax user value to strict user value.' if not isinstance(value, ): raise TypeError(...) # Or datastore_errors.BadValueError(...). def _to_base_type(self, value): '(Strict) user value to base value.' if isinstance(value, ): return (value) def _from_base_type(self, value): 'base value to (strict) user value.' if not isinstance(value, ): return (value) Things that _validate(), _to_base_type() and _from_base_type() do _not_ need to handle:

  * None: They will not be called with None (and if they return None, this means that the value does not need conversion).
  * Repeated values: The infrastructure (_get_user_value() and _get_base_value()) takes care of calling _from_base_type() or _to_base_type() for each list item in a repeated value.
  * Wrapping values in _BaseValue(): The wrapping and unwrapping is taken care of by the infrastructure that calls the composable APIs.
  * Comparisons: The comparison operations call _to_base_type() on their operand.
  * Distinguishing between user and base values: the infrastructure guarantees that _from_base_type() will be called with an (unwrapped) base value, and that _to_base_type() will be called with a user value.
  * Returning the original value: if any of these return None, the original value is kept. (Returning a differen value not equal to None will substitute the different value.)



## Methods

### `IN`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1045-L1071)
    
    
    IN(
        value
    )
    

Comparison operator for the `IN` comparison operator. The Python `IN` operator cannot be overloaded in the way we want to, so we define a method. For example:
    
    
    Employee.query(Employee.rank.IN([4, 5, 6]))
    

Note that the method is called `._IN()` but may normally be invoked as `.IN()`; `._IN()` is provided for the case you have a `StructuredProperty` with a model that has a Property named `IN`.

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1020-L1022)
    
    
    __eq__(
        value
    )
    

Return a `FilterNode` instance representing the `=` comparison.

### `__ge__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1040-L1042)
    
    
    __ge__(
        value
    )
    

Return a `FilterNode` instance representing the `>=` comparison.

### `__gt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1036-L1038)
    
    
    __gt__(
        value
    )
    

Return a `FilterNode` instance representing the `>` comparison.

### `__le__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1032-L1034)
    
    
    __le__(
        value
    )
    

Return a `FilterNode` instance representing the `<=` comparison.

### `__lt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1028-L1030)
    
    
    __lt__(
        value
    )
    

Return a `FilterNode` instance representing the `<` comparison.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1024-L1026)
    
    
    __ne__(
        value
    )
    

Return a `FilterNode` instance representing the `!=` comparison.

### `__neg__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1074-L1084)
    
    
    __neg__()
    

Return a descending sort order on this Property.

#### For example:
    
    
    Employee.query().order(-Employee.rank)
    

### `__pos__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1086-L1097)
    
    
    __pos__()
    

Returns an ascending sort order on this property. Note that this is redundant but provided for consistency with `__neg__`. For example, the following two are equivalent:
    
    
    Employee.query().order(+Employee.rank)
    Employee.query().order(Employee.rank)
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
