---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.RecurringSchedule
title: Class RecurringSchedule (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:31.931760+00:00
---

# Class RecurringSchedule (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.RecurringSchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RecurringSchedule (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    RecurringSchedule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Sets the time for recurring patch deployments.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`time_zone` |  `google.type.datetime_pb2.TimeZone`   
Required. Defines the time zone that `time_of_day` is relative to. The rules for daylight saving time are determined by the chosen time zone.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The time that the recurring schedule becomes effective. Defaults to `create_time` of the patch deployment.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The end time at which a recurring patch deployment schedule is no longer active.   
`time_of_day` |  `google.type.timeofday_pb2.TimeOfDay`   
Required. Time of the day to run a recurring deployment.   
`frequency` |  `[google.cloud.osconfig_v1.types.RecurringSchedule.Frequency](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.RecurringSchedule.Frequency)`   
Required. The frequency unit of this recurring schedule.   
`weekly` |  `[google.cloud.osconfig_v1.types.WeeklySchedule](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.WeeklySchedule)`   
Required. Schedule with weekly executions. This field is a member of `oneof`_ `schedule_config`.   
`monthly` |  `[google.cloud.osconfig_v1.types.MonthlySchedule](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.MonthlySchedule)`   
Required. Schedule with monthly executions. This field is a member of `oneof`_ `schedule_config`.   
`last_execute_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time the last patch job ran successfully.   
`next_execute_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time the next patch job is scheduled to run.   
  
## Classes 

### Frequency
    
    
    Frequency(value)

Specifies the frequency of the recurring patch deployments.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
