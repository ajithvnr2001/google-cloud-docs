---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ReportValue/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ReportValue (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:03.344999+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ReportValue (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ReportValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ReportValue (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ReportValue.

A single report value.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #date_time_value
    
    
    def date_time_value() -> ::Google::Type::DateTime

**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — A value of type `google.type.DateTime` (year, month, day, hour, minute, second, and UTC offset or timezone.)

Note: The following fields are mutually exclusive: `date_time_value`, `string_value`, `int_value`, `decimal_value`, `money_value`, `date_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #date_time_value=
    
    
    def date_time_value=(value) -> ::Google::Type::DateTime

**Parameter**

  * **value** ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — A value of type `google.type.DateTime` (year, month, day, hour, minute, second, and UTC offset or timezone.)

Note: The following fields are mutually exclusive: `date_time_value`, `string_value`, `int_value`, `decimal_value`, `money_value`, `date_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-DateTime)) — A value of type `google.type.DateTime` (year, month, day, hour, minute, second, and UTC offset or timezone.)

Note: The following fields are mutually exclusive: `date_time_value`, `string_value`, `int_value`, `decimal_value`, `money_value`, `date_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #date_value
    
    
    def date_value() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — A value of type `google.type.Date` (year, month, day).

Note: The following fields are mutually exclusive: `date_value`, `string_value`, `int_value`, `decimal_value`, `money_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #date_value=
    
    
    def date_value=(value) -> ::Google::Type::Date

**Parameter**

  * **value** ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — A value of type `google.type.Date` (year, month, day).

Note: The following fields are mutually exclusive: `date_value`, `string_value`, `int_value`, `decimal_value`, `money_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Date)) — A value of type `google.type.Date` (year, month, day).

Note: The following fields are mutually exclusive: `date_value`, `string_value`, `int_value`, `decimal_value`, `money_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #decimal_value
    
    
    def decimal_value() -> ::Google::Type::Decimal

**Returns**

  * ([::Google::Type::Decimal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Decimal)) — A value of type `google.type.Decimal`, representing non-integer numeric values.

Note: The following fields are mutually exclusive: `decimal_value`, `string_value`, `int_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #decimal_value=
    
    
    def decimal_value=(value) -> ::Google::Type::Decimal

**Parameter**

  * **value** ([::Google::Type::Decimal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Decimal)) — A value of type `google.type.Decimal`, representing non-integer numeric values.

Note: The following fields are mutually exclusive: `decimal_value`, `string_value`, `int_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Type::Decimal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Decimal)) — A value of type `google.type.Decimal`, representing non-integer numeric values.

Note: The following fields are mutually exclusive: `decimal_value`, `string_value`, `int_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #int_value
    
    
    def int_value() -> ::Integer

**Returns**

  * (::Integer) — A value of type `int`.

Note: The following fields are mutually exclusive: `int_value`, `string_value`, `decimal_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #int_value=
    
    
    def int_value=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — A value of type `int`.

Note: The following fields are mutually exclusive: `int_value`, `string_value`, `decimal_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Integer) — A value of type `int`.

Note: The following fields are mutually exclusive: `int_value`, `string_value`, `decimal_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #money_value
    
    
    def money_value() -> ::Google::Type::Money

**Returns**

  * ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Money)) — A value of type `google.type.Money` (currency code, whole units, decimal units).

Note: The following fields are mutually exclusive: `money_value`, `string_value`, `int_value`, `decimal_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #money_value=
    
    
    def money_value=(value) -> ::Google::Type::Money

**Parameter**

  * **value** ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Money)) — A value of type `google.type.Money` (currency code, whole units, decimal units).

Note: The following fields are mutually exclusive: `money_value`, `string_value`, `int_value`, `decimal_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Money)) — A value of type `google.type.Money` (currency code, whole units, decimal units).

Note: The following fields are mutually exclusive: `money_value`, `string_value`, `int_value`, `decimal_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_value
    
    
    def string_value() -> ::String

**Returns**

  * (::String) — A value of type `string`.

Note: The following fields are mutually exclusive: `string_value`, `int_value`, `decimal_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_value=
    
    
    def string_value=(value) -> ::String

**Parameter**

  * **value** (::String) — A value of type `string`.

Note: The following fields are mutually exclusive: `string_value`, `int_value`, `decimal_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — A value of type `string`.

Note: The following fields are mutually exclusive: `string_value`, `int_value`, `decimal_value`, `money_value`, `date_value`, `date_time_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
