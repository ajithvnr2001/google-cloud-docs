---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date/
title: Cloud Channel V1 API - Class Google::Type::Date (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:37.620265+00:00
---

# Cloud Channel V1 API - Class Google::Type::Date (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Type::Date (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Type::Date.

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * [google.type.TimeOfDay][google.type.TimeOfDay]
  * [google.type.DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime "Google::Type::DateTime \(class\)")
  * [google.protobuf.Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp "Google::Protobuf::Timestamp \(class\)")



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

  * (::Integer) — Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant. 



### #day=
    
    
    def day=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant. 



**Returns**

  * (::Integer) — Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant. 



### #month
    
    
    def month() -> ::Integer

**Returns**

  * (::Integer) — Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. 



### #month=
    
    
    def month=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. 



**Returns**

  * (::Integer) — Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. 



### #year
    
    
    def year() -> ::Integer

**Returns**

  * (::Integer) — Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. 



### #year=
    
    
    def year=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. 



**Returns**

  * (::Integer) — Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
