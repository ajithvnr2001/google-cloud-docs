---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/CompositeOrder/
title: google.appengine.datastore.datastore_query.CompositeOrder \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:27:31.769699+00:00
---

# google.appengine.datastore.datastore_query.CompositeOrder  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/CompositeOrder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.CompositeOrder Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1253-L1343) An immutable class that represents a sequence of Orders. Inherits From: [`Order`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Order), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_query.CompositeOrder(
        orders
    )
    

This class proactively flattens sub-orders that are of type CompositeOrder. For example: CompositeOrder([O1, CompositeOrder([02, 03]), O4]) is equivalent to: CompositeOrder([O1, 02, 03, O4]) | 

## Args  
  
---  
  
`orders` |  A list of Orders which are applied in order.   
  
## Attributes  
  
---  
  
`orders` |   
  
## Methods

### `cmp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1069-L1111)
    
    
    cmp(
        lhs, rhs, filter_predicate=None
    )
    

Compares the given values taking into account any filters.

This function can be used as the cmp argument for list.sort() and sorted().

This function is slightly more efficient that Order.key when comparing two entities, however it is much less efficient when sorting a list of entities.

Args  
---  
  
`lhs` |  An entity_pb2.EntityProto   
`rhs` |  An entity_pb2.EntityProto   
`filter_predicate` |  A FilterPredicate used to prune values before comparing entities or None.   
  
Returns  
---  
An integer <, = or > 0 representing the operator that goes in between lhs and rhs that to create a true statement.   
  
### `cmp_for_filter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1039-L1042)
    
    
    cmp_for_filter(
        filter_predicate
    )
    

### `key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1044-L1067)
    
    
    key(
        entity, filter_predicate=None
    )
    

Constructs a "key" value for the given entity based on the current order.

This function can be used as the key argument for list.sort() and sorted().

Args  
---  
  
`entity` |  The entity_pb2.EntityProto to convert   
`filter_predicate` |  A FilterPredicate used to prune values before comparing entities or None.   
  
Returns  
---  
A key value that identifies the position of the entity when sorted by the current order.   
  
### `key_for_filter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1034-L1037)
    
    
    key_for_filter(
        filter_predicate
    )
    

### `reversed`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1292-L1295)
    
    
    reversed(
        group_by=None
    )
    

Constructs an order representing the reverse of the current order.

This function takes into account the effects of orders on properties not in the group_by clause of a query. For example, consider: SELECT A, First(B) ... GROUP BY A ORDER BY A, B Changing the order of B would effect which value is listed in the 'First(B)' column which would actually change the results instead of just reversing them.

Args  
---  
  
`group_by` |  If specified, only orders on properties in group_by will be reversed.   
  
Returns  
---  
A new order representing the reverse direction.   
  
### `size`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1316-L1318)
    
    
    size()
    

Returns the number of sub-orders the instance contains.

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1332-L1343)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L86-L90)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
