---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value/
title: Value \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:51.705783+00:00
---

# Value  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Value Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TimeOfDay
    * JSON representation
  * Date
    * JSON representation
  * DayOfWeek



Set of primitive values supported by the system. Note that for the purposes of inspection or transformation, the number of bytes considered to comprise a 'Value' is based on its representation as a UTF-8 encoded string. For example, if 'integerValue' is set to 123456789, the number of bytes would be counted as 9, even though an int64 only holds up to 8 bytes of data.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "integerValue": string,
      "floatValue": number,
      "stringValue": string,
      "booleanValue": boolean,
      "timestampValue": string,
      "timeValue": {
        object ([TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#TimeOfDay))
      },
      "dateValue": {
        object ([Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#Date))
      },
      "dayOfWeekValue": enum ([DayOfWeek](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#DayOfWeek))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Value types The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`integerValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` integer  
`floatValue` |  `number` float  
`stringValue` |  `string` string  
`booleanValue` |  `boolean` boolean  
`timestampValue` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeValue` |  `object (`[TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#TimeOfDay)`)` time of day  
`dateValue` |  `object (`[Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#Date)`)` date  
`dayOfWeekValue` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#DayOfWeek)`)` day of week  
End of mutually exclusive fields.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `[google.type.Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#Date)` and `google.protobuf.Timestamp`.

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
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `[google.type.TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#TimeOfDay)`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
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

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
