---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DateRange/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::DateRange (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:19.510617+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::DateRange (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DateRange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::DateRange (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::DateRange.

A representation of usage or invoice date ranges.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #invoice_end_date
    
    
    def invoice_end_date() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — The latest invoice date (inclusive).

If this value is not the last day of a month, this will move it forward to the last day of the given month. 




### #invoice_end_date=
    
    
    def invoice_end_date=(value) -> ::Google::Type::Date

**Parameter**

  * **value** ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — The latest invoice date (inclusive).

If this value is not the last day of a month, this will move it forward to the last day of the given month. 




**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — The latest invoice date (inclusive).

If this value is not the last day of a month, this will move it forward to the last day of the given month. 




### #invoice_start_date
    
    
    def invoice_start_date() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — The earliest invoice date (inclusive).

If this value is not the first day of a month, this will move it back to the first day of the given month. 




### #invoice_start_date=
    
    
    def invoice_start_date=(value) -> ::Google::Type::Date

**Parameter**

  * **value** ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — The earliest invoice date (inclusive).

If this value is not the first day of a month, this will move it back to the first day of the given month. 




**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — The earliest invoice date (inclusive).

If this value is not the first day of a month, this will move it back to the first day of the given month. 




### #usage_end_date_time
    
    
    def usage_end_date_time() -> ::Google::Type::DateTime

**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — The latest usage date time (exclusive).

If you use time groupings (daily, weekly, etc), each group uses midnight to midnight (Pacific time). The usage end date is rounded down to include all usage from the specified date. We recommend that clients pass `usage_start_date_time` in Pacific time. 




### #usage_end_date_time=
    
    
    def usage_end_date_time=(value) -> ::Google::Type::DateTime

**Parameter**

  * **value** ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — The latest usage date time (exclusive).

If you use time groupings (daily, weekly, etc), each group uses midnight to midnight (Pacific time). The usage end date is rounded down to include all usage from the specified date. We recommend that clients pass `usage_start_date_time` in Pacific time. 




**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — The latest usage date time (exclusive).

If you use time groupings (daily, weekly, etc), each group uses midnight to midnight (Pacific time). The usage end date is rounded down to include all usage from the specified date. We recommend that clients pass `usage_start_date_time` in Pacific time. 




### #usage_start_date_time
    
    
    def usage_start_date_time() -> ::Google::Type::DateTime

**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — The earliest usage date time (inclusive).

If you use time groupings (daily, weekly, etc), each group uses midnight to midnight (Pacific time). The usage start date is rounded down to include all usage from the specified date. We recommend that clients pass `usage_start_date_time` in Pacific time. 




### #usage_start_date_time=
    
    
    def usage_start_date_time=(value) -> ::Google::Type::DateTime

**Parameter**

  * **value** ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — The earliest usage date time (inclusive).

If you use time groupings (daily, weekly, etc), each group uses midnight to midnight (Pacific time). The usage start date is rounded down to include all usage from the specified date. We recommend that clients pass `usage_start_date_time` in Pacific time. 




**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — The earliest usage date time (inclusive).

If you use time groupings (daily, weekly, etc), each group uses midnight to midnight (Pacific time). The usage start date is rounded down to include all usage from the specified date. We recommend that clients pass `usage_start_date_time` in Pacific time. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
