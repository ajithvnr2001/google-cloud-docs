---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/Decoder/
title: google.appengine.datastore.sortable_pb_encoder.Decoder \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:31:18.723869+00:00
---

# google.appengine.datastore.sortable_pb_encoder.Decoder  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/Decoder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.sortable_pb_encoder.Decoder Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L319-L545) Decoder that decodes a bytes buffer into a protocol buffer message. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.sortable_pb_encoder.Decoder(
        buf, idx=0, limit=None
    )
    

## Methods

### `DecodeMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L327-L329)
    
    
    @classmethod
    DecodeMessage(
        prototype, buf, idx=0, limit=None
    )
    

### `Get16`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L354-L361)
    
    
    Get16()
    

Get the next 16 bits from the buffer.

### `Get32`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L363-L372)
    
    
    Get32()
    

Get the next 32 bits from the buffer.

### `Get64`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L374-L388)
    
    
    Get64()
    

Get the next 64 bits from the buffer.

### `Get8`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L346-L352)
    
    
    Get8()
    

Get the next 8 bits from the buffer.

### `GetBoolean`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L470-L475)
    
    
    GetBoolean()
    

Decode the next bits as a boolean value.

### `GetDouble`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L445-L457)
    
    
    GetDouble()
    

Decode the next bits as a double value.

### `GetFloat`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L431-L443)
    
    
    GetFloat()
    

Decode the next bits as a floating point value.

### `GetMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L518-L545)
    
    
    GetMessage(
        prototype
    )
    

Decode a message. | Args  
---  
  
`prototype` |  The prototype of the protocol buffer message.   
  
Returns  
---  
The decoded message.   
  
### `GetPrefixedString`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L459-L468)
    
    
    GetPrefixedString()
    

### `GetVarInt32`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L417-L422)
    
    
    GetVarInt32()
    

Decode the next bits as a `varint` and check it's a 32 bit value.

### `GetVarInt64`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L390-L415)
    
    
    GetVarInt64()
    

Decode the next bits as a `varint`.

### `GetVarUint64`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py#L424-L429)
    
    
    GetVarUint64()
    

Decode the next bits as a `varint` and check it's non-negative value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
