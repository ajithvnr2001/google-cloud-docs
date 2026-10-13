---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency
title: Class SpanLatency (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:31.182285+00:00
---

# Class SpanLatency (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SpanLatency (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    SpanLatency(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The latency of a span execution.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`resource` |  `str`   
Output only. The resource name of the guardrail or tool spans. This field is a member of `oneof`_ `identifier`.   
`toolset` |  `[google.cloud.ces_v1beta.types.ToolsetTool](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.ToolsetTool)`   
Output only. The toolset tool identifier. This field is a member of `oneof`_ `identifier`.   
`model` |  `str`   
Output only. The name of the LLM span. This field is a member of `oneof`_ `identifier`.   
`callback` |  `str`   
Output only. The name of the user callback span. This field is a member of `oneof`_ `identifier`.   
`type_` |  `[google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency.Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency.Type)`   
Output only. The type of span.   
`display_name` |  `str`   
Output only. The display name of the span. Applicable to tool and guardrail spans.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The start time of span.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The end time of span.   
`execution_latency` |  `google.protobuf.duration_pb2.Duration`   
Output only. The latency of span.   
  
## Classes 

### Type
    
    
    Type(value)

The type of span. Additional values may be added in the future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
