---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/stublib/Patchers/
title: google.appengine.api.stublib.Patchers \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:32:50.398703+00:00
---

# google.appengine.api.stublib.Patchers  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/stublib/Patchers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.stublib.Patchers Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/stublib.py#L39-L66) A list of patchers with helper functions to bulk start and stop them. Inherits From: [`data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/ListProperty/data_type), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.stublib.Patchers(
        *args, **kwargs
    )
    

## Methods

### `StartAll`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/stublib.py#L42-L57)
    
    
    StartAll()
    

Start all patchers and return a map of the created mocks.

### `StopAll`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/stublib.py#L59-L66)
    
    
    StopAll()
    

### `append`
    
    
    append(
        object, /
    )
    

Append object to the end of the list.

### `clear`
    
    
    clear()
    

Remove all items from list.

### `copy`
    
    
    copy()
    

Return a shallow copy of the list.

### `count`
    
    
    count(
        value, /
    )
    

Return number of occurrences of value.

### `extend`
    
    
    extend(
        iterable, /
    )
    

Extend list by appending elements from the iterable.

### `index`
    
    
    index(
        value, start, stop, /
    )
    

Return first index of value. Raises ValueError if the value is not present.

### `insert`
    
    
    insert(
        index, object, /
    )
    

Insert object before index.

### `pop`
    
    
    pop(
        index, /
    )
    

Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

### `remove`
    
    
    remove(
        value, /
    )
    

Remove first occurrence of value. Raises ValueError if the value is not present.

### `reverse`
    
    
    reverse()
    

Reverse _IN PLACE_.

### `sort`
    
    
    sort(
        *, key=None, reverse=False
    )
    

Sort the list in ascending order and return None. The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained). If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values. The reverse flag can be set to sort in descending order.

### `__add__`
    
    
    __add__(
        value, /
    )
    

Return self+value.

### `__contains__`
    
    
    __contains__(
        key, /
    )
    

Return key in self.

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

### `__mul__`
    
    
    __mul__(
        value, /
    )
    

Return self*value.

### `__ne__`
    
    
    __ne__(
        value, /
    )
    

Return self!=value.

### `__rmul__`
    
    
    __rmul__(
        value, /
    )
    

Return value*self. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
