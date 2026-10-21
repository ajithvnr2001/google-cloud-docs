---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type
title: Package google.type \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:22.473161+00:00
---

# Package google.type  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Package google.type Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[CalendarPeriod](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.CalendarPeriod)` (enum)
  * `[Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.Interval)` (message)
  * `[TimeOfDay](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.TimeOfDay)` (message)



## CalendarPeriod

A `CalendarPeriod` represents the abstract concept of a time period that has a canonical start. Grammatically, "the start of the current `CalendarPeriod`." All calendar times begin at midnight UTC.

Enums  
---  
`CALENDAR_PERIOD_UNSPECIFIED` | Undefined period, raises an error.  
`DAY` | A day.  
`WEEK` | A week. Weeks begin on Monday, following [ISO 8601](https://en.wikipedia.org/wiki/ISO_week_date).  
`FORTNIGHT` | A fortnight. The first calendar fortnight of the year begins at the start of week 1 according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_week_date).  
`MONTH` | A month.  
`QUARTER` | A quarter. Quarters start on dates 1-Jan, 1-Apr, 1-Jul, and 1-Oct of each year.  
`HALF` | A half-year. Half-years start on dates 1-Jan and 1-Jul.  
`YEAR` | A year.  
  
## Interval

Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).

The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `google.type.Date` and `google.protobuf.Timestamp`.

Fields  
---  
`hours` |  `int32` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `int32` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `int32` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `int32` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
