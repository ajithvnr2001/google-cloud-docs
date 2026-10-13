---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Type-TimeOfDay/
title: Cloud Talent Solution V4beta1 API - Class Google::Type::TimeOfDay (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:04.620199+00:00
---

# Cloud Talent Solution V4beta1 API - Class Google::Type::TimeOfDay (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Type-TimeOfDay/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4beta1 API - Class Google::Type::TimeOfDay (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.1 (latest)  0.19.0  0.18.1  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Talent Solution V4beta1 API class Google::Type::TimeOfDay.

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are [google.type.Date][google.type.Date] and `google.protobuf.Timestamp`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #hours
    
    
    def hours() -> ::Integer

**Returns**

  * (::Integer) — Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. 



### #hours=
    
    
    def hours=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. 



**Returns**

  * (::Integer) — Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. 



### #minutes
    
    
    def minutes() -> ::Integer

**Returns**

  * (::Integer) — Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59. 



### #minutes=
    
    
    def minutes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59. 



**Returns**

  * (::Integer) — Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59. 



### #nanos
    
    
    def nanos() -> ::Integer

**Returns**

  * (::Integer) — Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999. 



### #nanos=
    
    
    def nanos=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999. 



**Returns**

  * (::Integer) — Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999. 



### #seconds
    
    
    def seconds() -> ::Integer

**Returns**

  * (::Integer) — Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds. 



### #seconds=
    
    
    def seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds. 



**Returns**

  * (::Integer) — Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
