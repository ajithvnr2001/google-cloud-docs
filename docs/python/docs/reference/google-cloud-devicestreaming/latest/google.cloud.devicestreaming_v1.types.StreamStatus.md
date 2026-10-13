---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-devicestreaming/latest/google.cloud.devicestreaming_v1.types.StreamStatus
title: Class StreamStatus (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:09.501480+00:00
---

# Class StreamStatus (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-devicestreaming/latest/google.cloud.devicestreaming_v1.types.StreamStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamStatus (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    StreamStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The result of a stream.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`stream_id` |  `int`   
The unique ID of this stream, assigned by the client.   
`okay` |  `[google.cloud.devicestreaming_v1.types.Okay](https://docs.cloud.google.com/python/docs/reference/google-cloud-devicestreaming/latest/google.cloud.devicestreaming_v1.types.Okay)`   
Okay for success. This field is a member of `oneof`_ `status`.   
`fail` |  `[google.cloud.devicestreaming_v1.types.Fail](https://docs.cloud.google.com/python/docs/reference/google-cloud-devicestreaming/latest/google.cloud.devicestreaming_v1.types.Fail)`   
Fail for failure. This field is a member of `oneof`_ `status`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
