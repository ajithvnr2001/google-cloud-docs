---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/AbstractAdapter/
title: google.appengine.datastore.datastore_rpc.AbstractAdapter \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:14:46.536428+00:00
---

# google.appengine.datastore.datastore_rpc.AbstractAdapter  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/AbstractAdapter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_rpc.AbstractAdapter Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L111-L212) Abstract interface between protobufs and user-level classes. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_rpc.AbstractAdapter(
        id_resolver=None
    )
    

This class defines conversions between the protobuf classes defined in entity_pb.py on the one hand, and the corresponding user-level classes (which are defined by higher-level API libraries such as datastore.py or db.py) on the other hand. The premise is that the code in this module is agnostic about the user-level classes used to represent keys and entities, while at the same time provinging APIs that accept or return such user-level classes. Higher-level libraries must subclass this abstract class and pass an instance of the subclass to the Connection they want to use. These methods may raise datastore_errors.Error for bad inputs.

## Methods

### `entity_to_pb`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L195-L197)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L184-L186)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L156-L158)
    
    
    pb_to_entity(
        pb
    )
    

Turn an entity_pb2.EntityProto into a user-level entity.

### `pb_to_index`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L173-L175)
    
    
    pb_to_index(
        pb
    )
    

Turn an entity_pb2.CompositeIndex into a user-level Index representation.

### `pb_to_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L146-L148)
    
    
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
    

Turn an googledatastore.Entity into a user-level query result. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
