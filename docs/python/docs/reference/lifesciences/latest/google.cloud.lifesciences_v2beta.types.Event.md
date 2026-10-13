---
url: https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.Event
title: Class Event (0.12.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:53.858576+00:00
---

# Class Event (0.12.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.Event

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Event (0.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.2 (latest)  0.12.1  0.11.0  0.10.0  0.9.18  0.8.0  0.7.2  0.6.2  0.5.2  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    Event(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Carries information about events that occur during pipeline execution.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`timestamp` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time at which the event occurred.   
`description` |  `str`   
A human-readable description of the event. Note that these strings can change at any time without notice. Any application logic must use the information in the `details` field.   
`delayed` |  `[google.cloud.lifesciences_v2beta.types.DelayedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.DelayedEvent)`   
See google.cloud.lifesciences.v2beta.DelayedEvent. This field is a member of `oneof`_ `details`.   
`worker_assigned` |  `[google.cloud.lifesciences_v2beta.types.WorkerAssignedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.WorkerAssignedEvent)`   
See google.cloud.lifesciences.v2beta.WorkerAssignedEvent. This field is a member of `oneof`_ `details`.   
`worker_released` |  `[google.cloud.lifesciences_v2beta.types.WorkerReleasedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.WorkerReleasedEvent)`   
See google.cloud.lifesciences.v2beta.WorkerReleasedEvent. This field is a member of `oneof`_ `details`.   
`pull_started` |  `[google.cloud.lifesciences_v2beta.types.PullStartedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.PullStartedEvent)`   
See google.cloud.lifesciences.v2beta.PullStartedEvent. This field is a member of `oneof`_ `details`.   
`pull_stopped` |  `[google.cloud.lifesciences_v2beta.types.PullStoppedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.PullStoppedEvent)`   
See google.cloud.lifesciences.v2beta.PullStoppedEvent. This field is a member of `oneof`_ `details`.   
`container_started` |  `[google.cloud.lifesciences_v2beta.types.ContainerStartedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.ContainerStartedEvent)`   
See google.cloud.lifesciences.v2beta.ContainerStartedEvent. This field is a member of `oneof`_ `details`.   
`container_stopped` |  `[google.cloud.lifesciences_v2beta.types.ContainerStoppedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.ContainerStoppedEvent)`   
See google.cloud.lifesciences.v2beta.ContainerStoppedEvent. This field is a member of `oneof`_ `details`.   
`container_killed` |  `[google.cloud.lifesciences_v2beta.types.ContainerKilledEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.ContainerKilledEvent)`   
See google.cloud.lifesciences.v2beta.ContainerKilledEvent. This field is a member of `oneof`_ `details`.   
`unexpected_exit_status` |  `[google.cloud.lifesciences_v2beta.types.UnexpectedExitStatusEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.UnexpectedExitStatusEvent)`   
See google.cloud.lifesciences.v2beta.UnexpectedExitStatusEvent. This field is a member of `oneof`_ `details`.   
`failed` |  `[google.cloud.lifesciences_v2beta.types.FailedEvent](https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.FailedEvent)`   
See google.cloud.lifesciences.v2beta.FailedEvent. This field is a member of `oneof`_ `details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
