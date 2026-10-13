---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod/
title: TimePeriod \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:28.882872+00:00
---

# TimePeriod  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/apis)



Send feedback 

#  TimePeriod Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TimeOfDay
    * JSON representation
  * DayOfWeek



Represents a time period in a week.

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod#TimeOfDay))
      },
      "endTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod#TimeOfDay))
      },
      "days": [
        enum ([DayOfWeek](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod#DayOfWeek))
      ]
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod#TimeOfDay)`)` Required. The start of the time period.  
`endTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod#TimeOfDay)`)` Required. The end of the time period.  
`days[]` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/TimePeriod#DayOfWeek)`)` Required. The days of the week that the time period is active.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `[google.type.Date](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/Date)` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
## DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
