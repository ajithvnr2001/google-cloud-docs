---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Type-DateTime/
title: GDC Hardware Management V1ALPHA API - Class Google::Type::DateTime (v0.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:37.904768+00:00
---

# GDC Hardware Management V1ALPHA API - Class Google::Type::DateTime (v0.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Type-DateTime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GDC Hardware Management V1ALPHA API - Class Google::Type::DateTime (v0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.14.1  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the GDC Hardware Management V1ALPHA API class Google::Type::DateTime.

Represents civil time (or occasionally physical time).

This type can represent a civil time in one of a few possible ways:

  * When utc_offset is set and time_zone is unset: a civil time on a calendar day with a particular offset from UTC.
  * When time_zone is set and utc_offset is unset: a civil time on a calendar day in a particular time zone.
  * When neither time_zone nor utc_offset is set: a civil time on a calendar day in local time.



The date is relative to the Proleptic Gregorian Calendar.

If year, month, or day are 0, the DateTime is considered not to have a specific year, month, or day respectively.

This type may also be used to represent a physical time if all the date and time fields are set and either case of the `time_offset` oneof is set. Consider using `Timestamp` message for physical time instead. If your use case also would like to store the user's timezone, that can be done in another field.

This type is more flexible than some applications may want. Make sure to document and validate your application's limitations.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #day
    
    
    def day() -> ::Integer

**Returns**

  * (::Integer) — Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. 



### #day=
    
    
    def day=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. 



**Returns**

  * (::Integer) — Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. 



### #hours
    
    
    def hours() -> ::Integer

**Returns**

  * (::Integer) — Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time. 



### #hours=
    
    
    def hours=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time. 



**Returns**

  * (::Integer) — Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time. 



### #minutes
    
    
    def minutes() -> ::Integer

**Returns**

  * (::Integer) — Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. 



### #minutes=
    
    
    def minutes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. 



**Returns**

  * (::Integer) — Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. 



### #month
    
    
    def month() -> ::Integer

**Returns**

  * (::Integer) — Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. 



### #month=
    
    
    def month=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. 



**Returns**

  * (::Integer) — Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. 



### #nanos
    
    
    def nanos() -> ::Integer

**Returns**

  * (::Integer) — Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. 



### #nanos=
    
    
    def nanos=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. 



**Returns**

  * (::Integer) — Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. 



### #seconds
    
    
    def seconds() -> ::Integer

**Returns**

  * (::Integer) — Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. 



### #seconds=
    
    
    def seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. 



**Returns**

  * (::Integer) — Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. 



### #time_zone
    
    
    def time_zone() -> ::Google::Type::TimeZone

**Returns**

  * ([::Google::Type::TimeZone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Type-TimeZone)) — Time zone.

Note: The following fields are mutually exclusive: `time_zone`, `utc_offset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #time_zone=
    
    
    def time_zone=(value) -> ::Google::Type::TimeZone

**Parameter**

  * **value** ([::Google::Type::TimeZone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Type-TimeZone)) — Time zone.

Note: The following fields are mutually exclusive: `time_zone`, `utc_offset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Type::TimeZone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Type-TimeZone)) — Time zone.

Note: The following fields are mutually exclusive: `time_zone`, `utc_offset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #utc_offset
    
    
    def utc_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Protobuf-Duration)) — UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.

Note: The following fields are mutually exclusive: `utc_offset`, `time_zone`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #utc_offset=
    
    
    def utc_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Protobuf-Duration)) — UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.

Note: The following fields are mutually exclusive: `utc_offset`, `time_zone`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Protobuf-Duration)) — UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.

Note: The following fields are mutually exclusive: `utc_offset`, `time_zone`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #year
    
    
    def year() -> ::Integer

**Returns**

  * (::Integer) — Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. 



### #year=
    
    
    def year=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. 



**Returns**

  * (::Integer) — Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
