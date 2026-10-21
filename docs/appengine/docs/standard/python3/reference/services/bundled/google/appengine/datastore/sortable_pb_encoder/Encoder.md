---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/Encoder/
title: google.appengine.datastore.sortable_pb_encoder.Encoder \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:17:43.186592+00:00
---

# google.appengine.datastore.sortable_pb_encoder.Encoder  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/Encoder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.sortable_pb_encoder.Encoder Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L101-L316) Encodes protocol buffers in a form that sorts nicely. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.sortable_pb_encoder.Encoder()
    

## Methods

### `Buffer`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L114-L115)
    
    
    Buffer()
    

### `EncodeMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L104-L108)
    
    
    @classmethod
    EncodeMessage(
        msg
    )
    

### `Put16`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L117-L123)
    
    
    Put16(
        value
    )
    

Encode a fixed size 16 bit value in the buffer.

### `Put32`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L125-L133)
    
    
    Put32(
        value
    )
    

Encode a fixed size 32 bit value in the buffer.

### `Put64`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L135-L147)
    
    
    Put64(
        value
    )
    

Encode a fixed size 64 bit value in the buffer.

### `PutBoolean`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L255-L261)
    
    
    PutBoolean(
        v
    )
    

Encode a boolean value in the buffer.

### `PutBytes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L247-L253)
    
    
    PutBytes(
        value
    )
    

Encode a byte array in the buffer.

### `PutDouble`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L220-L238)
    
    
    PutDouble(
        value
    )
    

Encode a double value in the buffer.

### `PutFloat`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L204-L218)
    
    
    PutFloat(
        value
    )
    

Encode a floating point value in the buffer.

### `PutMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L263-L269)
    
    
    PutMessage(
        msg
    )
    

Encode a protocol buffer message on the buffer.

### `PutPrefixedString`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L240-L245)
    
    
    PutPrefixedString(
        value
    )
    

### `PutVarInt32`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L186-L190)
    
    
    PutVarInt32(
        value
    )
    

Encode a 32 bit `varint` value in the buffer.

### `PutVarInt64`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L192-L196)
    
    
    PutVarInt64(
        value
    )
    

Encode a 64 bit `varint` value in the buffer.

### `PutVarUint64`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L198-L202)
    
    
    PutVarUint64(
        value
    )
    

Encode a 64 bit unsigned `varint` value in the buffer. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
