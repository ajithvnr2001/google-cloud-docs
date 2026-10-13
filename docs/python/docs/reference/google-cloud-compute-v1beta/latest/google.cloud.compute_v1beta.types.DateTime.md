---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DateTime
title: Class DateTime (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:07.565697+00:00
---

# Class DateTime (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DateTime

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DateTime (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    DateTime(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents civil time (or occasionally physical time).

This type can represent a civil time in one of a few possible ways:

  * When utc_offset is set and time_zone is unset: a civil time on a calendar day with a particular offset from UTC.
  * When time_zone is set and utc_offset is unset: a civil time on a calendar day in a particular time zone.
  * When neither time_zone nor utc_offset is set: a civil time on a calendar day in local time.



The date is relative to the Proleptic Gregorian Calendar.

If year, month, or day are 0, the DateTime is considered not to have a specific year, month, or day respectively.

This type may also be used to represent a physical time if all the date and time fields are set and either case of the `time_offset` oneof is set. Consider using `Timestamp` message for physical time instead. If your use case also would like to store the user's timezone, that can be done in another field.

This type is more flexible than some applications may want. Make sure to document and validate your application's limitations.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`day` |  `int`   
Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. This field is a member of `oneof`_ `_day`.   
`hours` |  `int`   
Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time. This field is a member of `oneof`_ `_hours`.   
`minutes` |  `int`   
Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. This field is a member of `oneof`_ `_minutes`.   
`month` |  `int`   
Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. This field is a member of `oneof`_ `_month`.   
`nanos` |  `int`   
Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. This field is a member of `oneof`_ `_nanos`.   
`seconds` |  `int`   
Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. This field is a member of `oneof`_ `_seconds`.   
`time_zone` |  `[google.cloud.compute_v1beta.types.TimeZone](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TimeZone)`   
Time zone. This field is a member of `oneof`_ `_time_zone`.   
`utc_offset` |  `str`   
UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. This field is a member of `oneof`_ `_utc_offset`.   
`year` |  `int`   
Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. This field is a member of `oneof`_ `_year`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
