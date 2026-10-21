---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BuiltinHandler/DynamicAttributes/
title: google.appengine.api.appinfo.BuiltinHandler.DynamicAttributes \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:25:21.459741+00:00
---

# google.appengine.api.appinfo.BuiltinHandler.DynamicAttributes  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BuiltinHandler/DynamicAttributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.BuiltinHandler.DynamicAttributes Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1481-L1497) Provides a dictionary object that will always claim to have a key. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.BuiltinHandler.DynamicAttributes(
        return_value, **parameters
    )
    

This dictionary returns a fixed value for any `get` operation. The fixed value that you pass in as a constructor parameter should be a [`validation.Validated`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated) object.

## Methods

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
    

D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If the key is not found, return the default if given; otherwise, raise a KeyError.

### `popitem`
    
    
    popitem()
    

Remove and return a (key, value) pair as a 2-tuple. Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

### `setdefault`
    
    
    setdefault(
        key, default, /
    )
    

Insert key with a value of default if key is not in the dictionary. Return the value for key if key is in the dictionary, else default.

### `update`
    
    
    update()
    

D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

### `values`
    
    
    values()
    

D.values() -> an object providing a view on D's values

### `__contains__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1493-L1494)
    
    
    __contains__(
        _
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1496-L1497)
    
    
    __getitem__(
        _
    )
    

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
    

Return value|self. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
