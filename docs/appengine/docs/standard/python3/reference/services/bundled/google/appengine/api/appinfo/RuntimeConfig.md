---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/RuntimeConfig/
title: google.appengine.api.appinfo.RuntimeConfig \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:02:17.923517+00:00
---

# google.appengine.api.appinfo.RuntimeConfig  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/RuntimeConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.RuntimeConfig Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1838-L1848) Class for "vanilla" runtime configuration. Inherits From: [`ValidatedDict`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedDict), [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.RuntimeConfig(
        **kwds
    )
    

Fields used vary by runtime, so validation is delegated to the per-runtime build processes. These are intended to be used during Dockerfile generation, not after VM boot. | 

## Args  
  
---  
  
`**kwds` |  keyword arguments will be validated and put into the dict.   
  
## Methods

### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L227-L235)
    
    
    CheckInitialized()
    

Checks for missing or conflicting attributes.

Subclasses should override this function and raise an exception for any errors. Always run this method when all assignments are complete.

Raises  
---  
  
`ValidationError` |  When there are missing or conflicting attributes.   
  
### `GetValidator`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L547-L555)
    
    
    @classmethod
    GetValidator(
        key
    )
    

Check the key for validity and return a corresponding value validator.

Args  
---  
  
`key` |  The key that will correspond to the validator we are returning.   
  
### `GetWarnings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L621-L625)
    
    
    GetWarnings()
    

Return all the warnings we've got, along with their associated fields.

Returns  
---  
A list of tuples of (dotted_field, warning), both strings.   
  
### `KEY_VALIDATOR`
    
    
    KEY_VALIDATOR(
        key='???'
    )
    

Regular expression validator.

Regular expression validator always converts value to string. Note that matches must be exact. Partial matches will not validate. For example:

class ClassDescr(Validated): ATTRIBUTES = { 'name': Regex(r'[a-zA-Z_][a-zA-Z_0-9]*'), 'parent': Type(type)` }

Alternatively, any attribute that is defined as a string is automatically interpreted to be of type Regex. It is possible to specify unicode regex strings as well. This approach is slightly less efficient, but usually is not significant unless parsing large amounts of data:
    
    
      class ClassDescr(Validated):
        ATTRIBUTES = { 'name': r'[a-zA-Z_][a-zA-Z_0-9]*',
                       'parent': Type(type),
                       }
    
      # This will raise a ValidationError exception.
      my_class(name='AName with space', parent=AnotherClass)
    

### `Set`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L606-L619)
    
    
    Set(
        key, value
    )
    

Set a single value on `Validated` instance.

This method checks that a given key and value are valid and if so puts the item into this dictionary.

Args  
---  
  
`key` |  The name of the attributes.   
`value` |  The value to set.   
  
Raises  
---  
  
`ValidationError` |  When no validated attribute exists on class.   
  
### `SetMultiple`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L197-L209)
    
    
    SetMultiple(
        attributes
    )
    

Set multiple values on Validated instance.

All attributes will be validated before being set.

Args  
---  
  
`attributes` |  A dict of attributes/items to set.   
  
Raises  
---  
  
`ValidationError` |  When no validated attribute exists on class.   
  
### `ToDict`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L627-L642)
    
    
    ToDict()
    

Convert `ValidatedBase` object to a dictionary.

Recursively traverses all of its elements and converts everything to simplified collections.

Subclasses should override this method.

Returns  
---  
A dictionary mapping all attributes to simple values or collections.   
  
### `ToYAML`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L251-L260)
    
    
    ToYAML()
    

Print validated object as simplified YAML.

Returns  
---  
Object as a simplified YAML string compatible with parsing using the `SafeLoader`.   
  
### `clear`
    
    
    clear()
    

D.clear() -> None. Remove all items from D.

### `copy`
    
    
    copy()
    

D.copy() -> a shallow copy of D

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

### `items`
    
    
    items()
    

D.items() -> a set-like object providing a view on D's items

### `keys`
    
    
    keys()
    

D.keys() -> a set-like object providing a view on D's keys

### `pop`
    
    
    pop()
    

D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

### `popitem`
    
    
    popitem()
    

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

### `setdefault`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L573-L582)
    
    
    setdefault(
        key, value=None
    )
    

Trap setdefaultss to ensure all key/value pairs are valid.

See the documentation for setdefault on dict for usage details.

Raises  
---  
  
`ValidationError` |  if the specified key is illegal or the value invalid.   
  
### `update`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L584-L604)
    
    
    update(
        other, **kwds
    )
    

Trap updates to ensure all key/value pairs are valid.

See the documentation for update on dict for usage details.

Raises  
---  
  
`ValidationError` |  if any of the specified keys are illegal or values invalid.   
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
