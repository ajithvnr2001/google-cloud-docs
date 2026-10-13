---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/DateTime/
title: DateTime \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:02.327647+00:00
---

# DateTime  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/DateTime/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  DateTime Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TimeZone
    * JSON representation



Represents civil time (or occasionally physical time).

This type can represent a civil time in one of a few possible ways:

  * When utcOffset is set and timeZone is unset: a civil time on a calendar day with a particular offset from UTC.
  * When timeZone is set and utcOffset is unset: a civil time on a calendar day in a particular time zone.
  * When neither timeZone nor utcOffset is set: a civil time on a calendar day in local time.



The date is relative to the Proleptic Gregorian Calendar.

If year, month, or day are 0, the DateTime is considered not to have a specific year, month, or day respectively.

This type may also be used to represent a physical time if all the date and time fields are set and either case of the `time_offset` oneof is set. Consider using `timestamp` message for physical time instead. If your use case also would like to store the user's timezone, that can be done in another field.

This type is more flexible than some applications may want. Make sure to document and validate your application's limitations.

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer,
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "utcOffset": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/DateTime#TimeZone))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`year` |  `integer` Optional. year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.  
`month` |  `integer` Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.  
`day` |  `integer` Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.  
`hours` |  `integer` Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.  
`seconds` |  `integer` Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.  
Optional. Specifies either the UTC offset or the time zone of the DateTime. Choose carefully between them, considering that time zone data may change in the future (for example, a country modifies their DST start/end dates, and future DateTimes in the affected range had already been stored). If omitted, the DateTime is considered to be in local time. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`utcOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/DateTime#TimeZone)`)` time zone.  
End of mutually exclusive fields.  
  
## TimeZone

Represents a time zone from the [IANA time Zone Database](https://www.iana.org/time-zones).

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA time Zone Database version number. For example "2019a".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
