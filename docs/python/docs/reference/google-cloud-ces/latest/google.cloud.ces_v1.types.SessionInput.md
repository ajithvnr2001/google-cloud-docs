---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.SessionInput
title: Class SessionInput (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:28.343909+00:00
---

# Class SessionInput (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.SessionInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SessionInput (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    SessionInput(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Input for the session.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`text` |  `str`   
Optional. Text data from the end user. This field is a member of `oneof`_ `input_type`.   
`dtmf` |  `str`   
Optional. DTMF digits from the end user. This field is a member of `oneof`_ `input_type`.   
`audio` |  `bytes`   
Optional. Audio data from the end user. This field is a member of `oneof`_ `input_type`.   
`tool_responses` |  `[google.cloud.ces_v1.types.ToolResponses](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.ToolResponses)`   
Optional. Execution results for the tool calls from the client. This field is a member of `oneof`_ `input_type`.   
`image` |  `[google.cloud.ces_v1.types.Image](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Image)`   
Optional. Image data from the end user. This field is a member of `oneof`_ `input_type`.   
`blob` |  `[google.cloud.ces_v1.types.Blob](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Blob)`   
Optional. Blob data from the end user. This field is a member of `oneof`_ `input_type`.   
`variables` |  `google.protobuf.struct_pb2.Struct`   
Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent. Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters. This field is a member of `oneof`_ `input_type`.   
`event` |  `[google.cloud.ces_v1.types.Event](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Event)`   
Optional. Event input. This field is a member of `oneof`_ `input_type`.   
`will_continue` |  `bool`   
Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session. When set to `true`, the agent defers processing until it receives a subsequent message where `will_continue` is `false`, or until the system detects an endpoint in the audio input. NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
