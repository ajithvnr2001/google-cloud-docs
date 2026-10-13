---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AutoscalingPolicyScalingSchedule
title: Class AutoscalingPolicyScalingSchedule (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:10.444808+00:00
---

# Class AutoscalingPolicyScalingSchedule (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AutoscalingPolicyScalingSchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutoscalingPolicyScalingSchedule (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    AutoscalingPolicyScalingSchedule(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Scaling based on user-defined schedule. The message describes a single scaling schedule. A scaling schedule changes the minimum number of VM instances an autoscaler can recommend, which can trigger scaling out.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`description` |  `str`   
A description of a scaling schedule. This field is a member of `oneof`_ `_description`.   
`disabled` |  `bool`   
A boolean value that specifies whether a scaling schedule can influence autoscaler recommendations. If set to true, then a scaling schedule has no effect. This field is optional, and its value is false by default. This field is a member of `oneof`_ `_disabled`.   
`duration_sec` |  `int`   
The duration of time intervals, in seconds, for which this scaling schedule is to run. The minimum allowed value is 300. This field is required. This field is a member of `oneof`_ `_duration_sec`.   
`min_required_replicas` |  `int`   
The minimum number of VM instances that the autoscaler will recommend in time intervals starting according to schedule. This field is required. This field is a member of `oneof`_ `_min_required_replicas`.   
`schedule` |  `str`   
The start timestamps of time intervals when this scaling schedule is to provide a scaling signal. This field uses the extended cron format (with an optional year field). The expression can describe a single timestamp if the optional year is set, in which case the scaling schedule runs once. The schedule is interpreted with respect to time_zone. This field is required. Note: These timestamps only describe when autoscaler starts providing the scaling signal. The VMs need additional time to become serving. This field is a member of `oneof`_ `_schedule`.   
`time_zone` |  `str`   
The time zone to use when interpreting the schedule. The value of this field must be a time zone name from the tz database: https://en.wikipedia.org/wiki/Tz_database. This field is assigned a default value of "UTC" if left empty. This field is a member of `oneof`_ `_time_zone`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
