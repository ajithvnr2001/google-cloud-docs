---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Chunk
title: Class Chunk (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:30.373494+00:00
---

# Class Chunk (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Chunk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Chunk (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    Chunk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A chunk of content within a message.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`text` |  `str`   
Optional. Text data. This field is a member of `oneof`_ `data`.   
`transcript` |  `str`   
Optional. Transcript associated with the audio. This field is a member of `oneof`_ `data`.   
`blob` |  `[google.cloud.ces_v1.types.Blob](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Blob)`   
Optional. Blob data. This field is a member of `oneof`_ `data`.   
`payload` |  `google.protobuf.struct_pb2.Struct`   
Optional. Custom payload data. This field is a member of `oneof`_ `data`.   
`image` |  `[google.cloud.ces_v1.types.Image](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Image)`   
Optional. Image data. This field is a member of `oneof`_ `data`.   
`tool_call` |  `[google.cloud.ces_v1.types.ToolCall](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.ToolCall)`   
Optional. Tool execution request. This field is a member of `oneof`_ `data`.   
`tool_response` |  `[google.cloud.ces_v1.types.ToolResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.ToolResponse)`   
Optional. Tool execution response. This field is a member of `oneof`_ `data`.   
`agent_transfer` |  `[google.cloud.ces_v1.types.AgentTransfer](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.AgentTransfer)`   
Optional. Agent transfer event. This field is a member of `oneof`_ `data`.   
`updated_variables` |  `google.protobuf.struct_pb2.Struct`   
A struct represents variables that were updated in the conversation, keyed by variable names. This field is a member of `oneof`_ `data`.   
`default_variables` |  `google.protobuf.struct_pb2.Struct`   
A struct represents default variables at the start of the conversation, keyed by variable names. This field is a member of `oneof`_ `data`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
