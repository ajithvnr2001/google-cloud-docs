---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.SessionOutput
title: Class SessionOutput (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:21.736508+00:00
---

# Class SessionOutput (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.SessionOutput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SessionOutput (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    SessionOutput(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Output for the session.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`text` |  `str`   
Output text from the CES agent. This field is a member of `oneof`_ `output_type`.   
`audio` |  `bytes`   
Output audio from the CES agent. This field is a member of `oneof`_ `output_type`.   
`tool_calls` |  `[google.cloud.ces_v1.types.ToolCalls](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.ToolCalls)`   
Request for the client to execute the tools. This field is a member of `oneof`_ `output_type`.   
`citations` |  `[google.cloud.ces_v1.types.Citations](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.Citations)`   
Citations that provide the source information for the agent's generated text. This field is a member of `oneof`_ `output_type`.   
`google_search_suggestions` |  `[google.cloud.ces_v1.types.GoogleSearchSuggestions](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.GoogleSearchSuggestions)`   
The suggestions returned from Google Search as a result of invoking the GoogleSearchTool. This field is a member of `oneof`_ `output_type`.   
`end_session` |  `[google.cloud.ces_v1.types.EndSession](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.EndSession)`   
Indicates the session has ended. This field is a member of `oneof`_ `output_type`.   
`payload` |  `google.protobuf.struct_pb2.Struct`   
Custom payload with structured output from the CES agent. This field is a member of `oneof`_ `output_type`.   
`turn_index` |  `int`   
Indicates the sequential order of conversation turn to which this output belongs to, starting from 1.   
`turn_completed` |  `bool`   
If true, the CES agent has detected the end of the current conversation turn and will provide no further output for this turn.   
`diagnostic_info` |  `[google.cloud.ces_v1.types.SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.SessionOutput.DiagnosticInfo)`   
Optional. Diagnostic information contains execution details during the processing of the input. Only populated in the last SessionOutput (with `turn_completed=true`) for each turn.   
`context` |  `MutableSequence[google.protobuf.any_pb2.Any]`   
Context messages for external supervision guardrails.   
  
## Classes 

### DiagnosticInfo
    
    
    DiagnosticInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains execution details during the processing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
