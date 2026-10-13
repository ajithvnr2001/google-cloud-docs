---
url: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource
title: Class QueuedResource (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:53.167338+00:00
---

# Class QueuedResource (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class QueuedResource (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.5  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.1  1.9.0  1.8.0  1.7.2  1.6.0  1.5.2  1.4.1  1.3.4  1.2.1  1.1.0  1.0.2  0.2.2  0.1.0 
    
    
    QueuedResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Immutable. The name of the QueuedResource.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the QueuedResource was created.   
`tpu` |  `[google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu)`   
Defines a TPU resource. This field is a member of `oneof`_ `resource`.   
`best_effort` |  `[google.cloud.tpu_v2alpha1.types.QueuedResource.BestEffort](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.BestEffort)`   
The BestEffort tier. This field is a member of `oneof`_ `tier`.   
`guaranteed` |  `[google.cloud.tpu_v2alpha1.types.QueuedResource.Guaranteed](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Guaranteed)`   
The Guaranteed tier. This field is a member of `oneof`_ `tier`.   
`spot` |  `[google.cloud.tpu_v2alpha1.types.QueuedResource.Spot](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Spot)`   
Optional. The Spot tier. This field is a member of `oneof`_ `tier`.   
`queueing_policy` |  `[google.cloud.tpu_v2alpha1.types.QueuedResource.QueueingPolicy](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.QueueingPolicy)`   
The queueing policy of the QueuedRequest.   
`state` |  `[google.cloud.tpu_v2alpha1.types.QueuedResourceState](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResourceState)`   
Output only. State of the QueuedResource request.   
`reservation_name` |  `str`   
Name of the reservation in which the resource should be provisioned. Format: projects/{project}/locations/{zone}/reservations/{reservation}   
  
## Classes 

### BestEffort
    
    
    BestEffort(mapping=None, *, ignore_unknown_fields=False, **kwargs)

BestEffort tier definition.

### Guaranteed
    
    
    Guaranteed(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Guaranteed tier definition.

### QueueingPolicy
    
    
    QueueingPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines the policy of the QueuedRequest.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### Spot
    
    
    Spot(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Spot tier definition.

### Tpu
    
    
    Tpu(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Details of the TPU resource(s) being requested.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
