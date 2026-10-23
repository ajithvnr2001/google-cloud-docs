---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/subclassprop/
title: Writing Property Subclasses \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:21.320330+00:00
---

# Writing Property Subclasses  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/subclassprop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Writing Property Subclasses Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The `Property` class is designed to be subclassed. However, it is normally easier to subclass an existing `Property` subclass. 

All special `Property` attributes, even those considered 'public', have names starting with an underscore. This is because `StructuredProperty` uses the non-underscore attribute namespace to refer to nested `Property` names; this is essential for specifying queries on subproperties. 

The `Property` class and its predefined subclasses allow subclassing using composable (or stackable) validation and conversion APIs. These require some terminology definitions: 

  * A _user value_ is a value such as would be set and accessed by the application code using standard attributes on the entity. 
  * A _base value_ is a value such as would be serialized to and deserialized from the Datastore. 



A `Property` subclass that implements a specific transformation between user values and serializable values should implement two methods, `_to_base_type()` and `_from_base_type()`. These should **not** call their `super()` method. This is what is meant by composable (or stackable) APIs. 

The API supports _stacking_ classes with ever more sophisticated user-base conversions: the user-to-base conversion goes from more sophisticated to less sophisticated, while the base-to-user conversion goes from less sophisticated to more sophisticated. For example, see the relationship between `BlobProperty`, `TextProperty`, and `StringProperty`. For example, `TextProperty` inherits from `BlobProperty`; its code is pretty simple because it inherits most of the behavior it needs. 

In addition to `_to_base_type()` and `_from_base_type()`, the `_validate()` method is also a composable API. 

The validation API distinguishes between _lax_ and _strict_ user values. The set of lax values is a superset of the set of strict values. The `_validate()` method takes a lax value and if necessary converts it to a strict value. This means that when setting the property value, lax values are accepted, while when getting the property value, only strict values will be returned. If no conversion is needed, `_validate()` may return None. If the argument is outside the set of accepted lax values, `_validate()` should raise an exception, preferably `TypeError` or `datastore_errors.BadValueError`. 

The `_validate()`, `_to_base_type()`, and `_from_base_type()` do _not_ need to handle: 

  * `None`: They will not be called with `None` (and if they return None, this means that the value does not need conversion). 
  * Repeated values: The infrastructure takes care of calling `_from_base_type()` or `_to_base_type()` for each list item in a repeated value. 
  * Distinguishing user values from base values: The infrastructure handles this by calling the composable APIs. 
  * Comparisons: The comparison operations call `_to_base_type()` on their operand. 
  * Distinguishing between user and base values: the infrastructure guarantees that `_from_base_type()` will be called with an (unwrapped) base value, and that `_to_base_type()` will be called with a user value. 



For example, suppose you need to store really long integers. The standard `IntegerProperty` only supports (signed) 64-bit integers. Your property might store a longer integer as a string; it would be good to have the property class handle the conversion. An application using your property class might look something like: 
    
    
    from datetime import date
    
    import my_models

`...`
    
    
    class MyModel(ndb.Model):
        name = ndb.StringProperty()
        abc = LongIntegerProperty(default=0)
        xyz = LongIntegerProperty(repeated=True)

`...`
    
    
    # Create an entity and write it to the Datastore.
    entity = my_models.MyModel(name='booh', xyz=[10**100, 6**666])
    assert entity.abc == 0
    key = entity.put()

`...`
    
    
    # Read an entity back from the Datastore and update it.
    entity = key.get()
    entity.abc += 1
    entity.xyz.append(entity.abc//3)
    entity.put()

`...`
    
    
    # Query for a MyModel entity whose xyz contains 6**666.
    # (NOTE: using ordering operations don't work, but == does.)
    results = my_models.MyModel.query(
        my_models.MyModel.xyz == 6**666).fetch(10)

This looks simple and straightforward. It also demonstrates the use of some standard property options (default, repeated); as the author of `LongIntegerProperty`, you will be glad to hear you don't have to write any "boilerplate" to get those working. It's easier to define a subclass of another property, for example: 
    
    
    class LongIntegerProperty(ndb.StringProperty):
        def _validate(self, value):
            if not isinstance(value, (int, long)):
                raise TypeError('expected an integer, got %s' % repr(value))
    
        def _to_base_type(self, value):
            return str(value)  # Doesn't matter if it's an int or a long
    
        def _from_base_type(self, value):
            return long(value)  # Always return a long

When you set a property value on an entity, e.g. `ent.abc = 42`, your `_validate()` method is called, and (if it doesn't raise an exception) the value is stored on the entity. When you write the entity to the Datastore, your `_to_base_type()` method is called, converting the value to the string. Then that value is serialized by the base class, `StringProperty`. The inverse chain of events happens when the entity is read back from the Datastore. The `StringProperty` and `Property` classes together take care of the other details, such as serializing the and deserializing the string, setting the default, and handling repeated property values. 

In this example, supporting inequalities (i.e. queries using <, <=, >, >=) requires more work. The following example implementation imposes a maximum size of integer and stores values as fixed-length strings: 
    
    
    class BoundedLongIntegerProperty(ndb.StringProperty):
        def __init__(self, bits, **kwds):
            assert isinstance(bits, int)
            assert bits > 0 and bits % 4 == 0  # Make it simple to use hex
            super(BoundedLongIntegerProperty, self).__init__(**kwds)
            self._bits = bits
    
        def _validate(self, value):
            assert -(2 ** (self._bits - 1)) <= value < 2 ** (self._bits - 1)
    
        def _to_base_type(self, value):
            # convert from signed -> unsigned
            if value < 0:
                value += 2 ** self._bits
            assert 0 <= value < 2 ** self._bits
            # Return number as a zero-padded hex string with correct number of
            # digits:
            return '%0*x' % (self._bits // 4, value)
    
        def _from_base_type(self, value):
            value = int(value, 16)
            if value >= 2 ** (self._bits - 1):
                value -= 2 ** self._bits
            return value

This can be used in the same way as `LongIntegerProperty` except that you must pass the number of bits to the property constructor, e.g. `BoundedLongIntegerProperty(1024)`. 

You can subclass other property types in similar ways. 

This approach also works for storing structured data. Suppose you have a `FuzzyDate` Python class that represents a date range; it uses fields `first` and `last` to store the date range's beginning and end: 
    
    
    from datetime import date
    
    

`...`
    
    
    class FuzzyDate(object):
        def __init__(self, first, last=None):
            assert isinstance(first, date)
            assert last is None or isinstance(last, date)
            self.first = first
            self.last = last or first

You can create a `FuzzyDateProperty` that derives from `StructuredProperty`. Unfortunately, the latter doesn't work with plain old Python classes; it needs a `Model` subclass. So define a Model subclass as an intermediate representation; 
    
    
    class FuzzyDateModel(ndb.Model):
        first = ndb.DateProperty()
        last = ndb.DateProperty()

Next, construct a subclass of `StructuredProperty` that hardcodes the modelclass argument to be `FuzzyDateModel`, and defines `_to_base_type()` and `_from_base_type()` methods to convert between `FuzzyDate` and `FuzzyDateModel`: 
    
    
    class FuzzyDateProperty(ndb.StructuredProperty):
        def __init__(self, **kwds):
            super(FuzzyDateProperty, self).__init__(FuzzyDateModel, **kwds)
    
        def _validate(self, value):
            assert isinstance(value, FuzzyDate)
    
        def _to_base_type(self, value):
            return FuzzyDateModel(first=value.first, last=value.last)
    
        def _from_base_type(self, value):
            return FuzzyDate(value.first, value.last)

An application might use this class like so: 
    
    
    class HistoricPerson(ndb.Model):
        name = ndb.StringProperty()
        birth = FuzzyDateProperty()
        death = FuzzyDateProperty()
        # Parallel lists:
        event_dates = FuzzyDateProperty(repeated=True)
        event_names = ndb.StringProperty(repeated=True)

`...`
    
    
    columbus = my_models.HistoricPerson(
        name='Christopher Columbus',
        birth=my_models.FuzzyDate(date(1451, 8, 22), date(1451, 10, 31)),
        death=my_models.FuzzyDate(date(1506, 5, 20)),
        event_dates=[my_models.FuzzyDate(
            date(1492, 1, 1), date(1492, 12, 31))],
        event_names=['Discovery of America'])
    columbus.put()
    
    # Query for historic people born no later than 1451.
    results = my_models.HistoricPerson.query(
        my_models.HistoricPerson.birth.last <= date(1451, 12, 31)).fetch()

Suppose you want to accept plain `date` objects in addition to `FuzzyDate` objects as the values for `FuzzyDateProperty`. To do this, modify the `_validate()` method as follows: 
    
    
    def _validate(self, value):
        if isinstance(value, date):
            return FuzzyDate(value)  # Must return the converted value!
        # Otherwise, return None and leave validation to the base class

You could instead subclass `FuzzyDateProperty` as follows (assuming `FuzzyDateProperty._validate()` is as shown above). 
    
    
    class MaybeFuzzyDateProperty(FuzzyDateProperty):
        def _validate(self, value):
            if isinstance(value, date):
                return FuzzyDate(value)  # Must return the converted value!
            # Otherwise, return None and leave validation to the base class

When you assign a value to a `MaybeFuzzyDateProperty` field, both `MaybeFuzzyDateProperty._validate()` and `FuzzyDateProperty._validate()` are invoked, in that order. The same applies to `_to_base_type()` and `_from_base_type()`: the methods in in superclass and subclass are implicitly combined. (Don't use `super` to control inherited behavior for this. For these three methods, the interaction is subtle and `super` doesn't do what you want.) 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
