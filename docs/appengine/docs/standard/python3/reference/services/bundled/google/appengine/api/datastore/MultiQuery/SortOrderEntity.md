---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/MultiQuery/SortOrderEntity/
title: google.appengine.api.datastore.MultiQuery.SortOrderEntity \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:11.875550+00:00
---

# google.appengine.api.datastore.MultiQuery.SortOrderEntity  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/MultiQuery/SortOrderEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.MultiQuery.SortOrderEntity Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2097-L2210) Allow entity comparisons using provided orderings. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.datastore.MultiQuery.SortOrderEntity(
        entity_iterator, orderings
    )
    

The iterator passed to the constructor is eventually consumed via calls to `GetNext()`, which generate new `SortOrderEntity` s with the same orderings. | 

## Args  
  
---  
  
`entity_iterator` |  an iterator of entities which will be wrapped.   
`orderings` |  an iterable of `(identifier, order)` pairs. order should be either [`Query.ASCENDING`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Query#ASCENDING) or [`Query.DESCENDING`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Query#DESCENDING).   
  
## Methods

### `CmpProperties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2139-L2172)
    
    
    CmpProperties(
        that
    )
    

Compare two entities and return their relative order.

Compares self to that based on the current sort orderings and the key orders between them. Returns negative, 0, or positive depending on whether self is less, equal to, or greater than that. This comparison returns as if all values were to be placed in ascending order (highest value last). Only uses the sort orderings to compare (ignores keys).

Args  
---  
  
`that` |  `SortOrderEntity`  
  
Returns  
---  
Negative if self < that Zero if self == that Positive if self > that   
  
### `GetEntity`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2127-L2129)
    
    
    GetEntity()
    

Gets the wrapped entity.

### `GetNext`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2131-L2137)
    
    
    GetNext()
    

Wrap and return the next entity.

The entity is retrieved from the iterator given at construction time.

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
