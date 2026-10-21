---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/
title: Module: google.appengine.datastore.sortable_pb_encoder \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:02:56.043358+00:00
---

# Module: google.appengine.datastore.sortable_pb_encoder  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.datastore.sortable_pb_encoder Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/sortable_pb_encoder.py) An Encoder class for protocol buffers (PB) that preserves sorting characteristics. This is used by `datastore_sqlite_stub` and `datastore_types` to match the ordering semantics of the production datastore. Broadly, there are four changes from regular PB encoding:

  * Strings are escaped and null terminated instead of length-prefixed. The escaping replaces `\x00` with `\x01\x01` and `\x01` with `\x01\x02`, thus preserving the ordering of the original string.
  * Variable length integers are encoded using a variable length encoding that preserves order. The first byte stores the absolute value if it's between -119 to 119, otherwise it stores the number of bytes that follow.
  * Numbers are stored big endian instead of little endian.
  * Negative doubles are entirely negated, while positive doubles have their sign bit flipped.



#### Warning:

Due to the way nested Protocol Buffers are encoded, this encoder will NOT preserve sorting characteristics for embedded protocol buffers!

## Classes

[`class Decoder`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/Decoder): Decoder that decodes a bytes buffer into a protocol buffer message. [`class Encoder`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/Encoder): Encodes protocol buffers in a form that sorts nicely.

## Functions

[`EncodeDouble(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/EncodeDouble): Encode a double into a sortable byte buffer. [`FromBytes(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/FromBytes) [`GetFieldNumber(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/GetFieldNumber): Get the field number from the tuple returned by `Message.ListFields`. [`IsFloatNegative(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/IsFloatNegative) [`ToBytes(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/sortable_pb_encoder/ToBytes) Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
