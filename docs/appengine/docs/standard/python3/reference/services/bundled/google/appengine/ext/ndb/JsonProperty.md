---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/JsonProperty/
title: google.appengine.ext.ndb.JsonProperty \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:23.402471+00:00
---

# google.appengine.ext.ndb.JsonProperty  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/JsonProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.JsonProperty Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L1920-L1948) A property whose value is any Json-encodable Python object. Inherits From: [`BlobProperty`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/BlobProperty), [`Property`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Property), [`ModelAttribute`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/ModelAttribute), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.JsonProperty(
        name=None, compressed=False, json_type=None, **kwds
    )
    

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
