---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/DatastoreAdapter/
title: google.appengine.api.datastore.DatastoreAdapter \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:21.986776+00:00
---

# google.appengine.api.datastore.DatastoreAdapter  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/DatastoreAdapter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.DatastoreAdapter Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L322-L366) Adapter between datatypes defined here (Entity etc.) and protobufs. Inherits From: [`AbstractAdapter`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/AbstractAdapter), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.datastore.DatastoreAdapter(
        _id_resolver=None
    )
    

See the base class in datastore_rpc.py for more docs.

## Methods

### `entity_to_pb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L351-L352)
    
    
    entity_to_pb(
        entity
    )
    

Turn a user-level entity into an entity_pb2.EntityProto.

### `entity_to_pb_v1`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L199-L204)
    
    
    entity_to_pb_v1(
        entity
    )
    

Turn a user-level entity into an googledatastore.Key.

### `get_entity_converter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L140-L141)
    
    
    get_entity_converter()
    

### `get_query_converter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L143-L144)
    
    
    get_query_converter()
    

### `key_to_pb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L345-L346)
    
    
    key_to_pb(
        key
    )
    

Turn a user-level key into an entity_pb2.Reference.

### `key_to_pb_v1`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L188-L193)
    
    
    key_to_pb_v1(
        key
    )
    

Turn a user-level key into an googledatastore.Key.

### `new_entity_pb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L210-L212)
    
    
    new_entity_pb()
    

Create a new, empty entity_pb2.EntityProto.

### `new_key_pb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L206-L208)
    
    
    new_key_pb()
    

Create a new, empty entity_pb2.Reference.

### `pb_to_entity`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L354-L355)
    
    
    pb_to_entity(
        pb
    )
    

Turn an entity_pb2.EntityProto into a user-level entity.

### `pb_to_index`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L357-L366)
    
    
    pb_to_index(
        pb
    )
    

Turn an entity_pb2.CompositeIndex into a user-level Index representation.

### `pb_to_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L348-L349)
    
    
    pb_to_key(
        pb
    )
    

Turn an entity_pb2.Reference into a user-level key.

### `pb_to_query_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L177-L182)
    
    
    pb_to_query_result(
        pb, query_options
    )
    

Turn an entity_pb2.EntityProto into a user-level query result.

### `pb_v1_to_entity`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L160-L164)
    
    
    pb_v1_to_entity(
        pb, is_projection
    )
    

Turn an googledatastore.Entity into a user-level entity.

### `pb_v1_to_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L150-L154)
    
    
    pb_v1_to_key(
        pb
    )
    

Turn an googledatastore.Key into a user-level key.

### `pb_v1_to_query_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L166-L171)
    
    
    pb_v1_to_query_result(
        pb, query_options
    )
    

Turn an googledatastore.Entity into a user-level query result. | 

## Class Variables  
  
---  
  
index_direction_mappings | 
    
    
    {
     1: 1,
     2: 2
    }
      
  
index_state_mappings | 
    
    
    {
     1: 0,
     2: 1,
     3: 2,
     4: 3
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
