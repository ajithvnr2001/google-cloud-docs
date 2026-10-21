---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/StubQueryConverter/
title: google.appengine.datastore.datastore_stub_util.StubQueryConverter \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:13:11.472161+00:00
---

# google.appengine.datastore.datastore_stub_util.StubQueryConverter  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/StubQueryConverter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.StubQueryConverter Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3602-L4032) Converter for v3, v4 and v1 queries suitable for use in stubs. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.StubQueryConverter(
        entity_converter
    )
    

## Methods

### `get_entity_converter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py#L1594-L1595)
    
    
    get_entity_converter()
    

### `v1_to_v3_compiled_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3815-L3826)
    
    
    v1_to_v3_compiled_cursor(
        v1_cursor, v3_compiled_cursor
    )
    

Converts a v1 cursor string to a v3 CompiledCursor. | Args  
---  
  
`v1_cursor` |  a string representing a v1 query cursor   
`v3_compiled_cursor` |  a datastore_pb.CompiledCursor to populate   
  
### `v1_to_v3_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3839-L3901)
    
    
    v1_to_v3_query(
        v1_partition_id, v1_query, v3_query
    )
    

Converts a v1 Query to a v3 Query.

Args  
---  
  
`v1_partition_id` |  a googledatastore.PartitionId   
`v1_query` |  a googledatastore.Query   
`v3_query` |  a datastore_pb.Query to populate   
  
Raises  
---  
InvalidConversionError if the query cannot be converted   
  
### `v3_order_to_v1_order`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py#L1637-L1646)
    
    
    v3_order_to_v1_order(
        v3_order, v1_order
    )
    

Converts a v3 Query order to a v1 `PropertyOrder`.

Args  
---  
  
`v3_order` |  A `datastore_pb.Query.Order`.   
`v1_order` |  A `googledatastore.PropertyOrder` to populate.   
  
### `v3_order_to_v4_order`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py#L1680-L1689)
    
    
    v3_order_to_v4_order(
        v3_order, v4_order
    )
    

Converts a v3 Query order to a v4 `PropertyOrder`.

Args  
---  
  
`v3_order` |  A `datastore_pb.Query.Order`.   
`v4_order` |  A `datastore_v4_pb2.PropertyOrder` to populate.   
  
### `v3_to_v1_compiled_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3828-L3837)
    
    
    v3_to_v1_compiled_cursor(
        v3_compiled_cursor
    )
    

Converts a v3 CompiledCursor to a v1 cursor string.

Args  
---  
  
`v3_compiled_cursor` |  a datastore_pb.CompiledCursor   
  
Returns  
---  
a string representing a v1 query cursor   
  
### `v3_to_v1_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3903-L3968)
    
    
    v3_to_v1_query(
        v3_query, v1_query
    )
    

Converts a v3 Query to a v1 Query.

Args  
---  
  
`v3_query` |  a datastore_pb.Query   
`v1_query` |  a googledatastore.Query to populate   
  
Raises  
---  
InvalidConversionError if the query cannot be converted   
  
### `v3_to_v4_compiled_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3621-L3630)
    
    
    v3_to_v4_compiled_cursor(
        v3_compiled_cursor
    )
    

Converts a v3 CompiledCursor to a v4 cursor string.

Args  
---  
  
`v3_compiled_cursor` |  a datastore_pb.CompiledCursor   
  
Returns  
---  
a string representing a v4 query cursor   
  
### `v3_to_v4_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3696-L3762)
    
    
    v3_to_v4_query(
        v3_query, v4_query
    )
    

Converts a v3 Query to a v4 Query.

Args  
---  
  
`v3_query` |  a datastore_pb.Query   
`v4_query` |  a datastore_v4_pb2.Query to populate   
  
Raises  
---  
InvalidConversionError if the query cannot be converted   
  
### `v4_to_v3_compiled_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3608-L3619)
    
    
    v4_to_v3_compiled_cursor(
        v4_cursor, v3_compiled_cursor
    )
    

Converts a v4 cursor string to a v3 CompiledCursor.

Args  
---  
  
`v4_cursor` |  a string representing a v4 query cursor   
`v3_compiled_cursor` |  a datastore_pb.CompiledCursor to populate   
  
### `v4_to_v3_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3632-L3694)
    
    
    v4_to_v3_query(
        v4_partition_id, v4_query, v3_query
    )
    

Converts a v4 Query to a v3 Query.

Args  
---  
  
`v4_partition_id` |  a datastore_v4_pb2.PartitionId   
`v4_query` |  a datastore_v4_pb2.Query   
`v3_query` |  a datastore_pb.Query to populate   
  
Raises  
---  
InvalidConversionError if the query cannot be converted   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
