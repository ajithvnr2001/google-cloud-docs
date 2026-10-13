---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DiscountComponent/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::DiscountComponent (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:19.324832+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::DiscountComponent (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DiscountComponent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::DiscountComponent (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::DiscountComponent.

Represents a single component of the total discount applicable on a Price.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #discount_absolute
    
    
    def discount_absolute() -> ::Google::Type::Money

**Returns**

  * ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Money)) — Fixed value discount.

Note: The following fields are mutually exclusive: `discount_absolute`, `discount_percentage`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discount_absolute=
    
    
    def discount_absolute=(value) -> ::Google::Type::Money

**Parameter**

  * **value** ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Money)) — Fixed value discount.

Note: The following fields are mutually exclusive: `discount_absolute`, `discount_percentage`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-Money)) — Fixed value discount.

Note: The following fields are mutually exclusive: `discount_absolute`, `discount_percentage`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discount_percentage
    
    
    def discount_percentage() -> ::Float

**Returns**

  * (::Float) — Discount percentage, represented as decimal. For example, a 20% discount will be represented as 0.2.

Note: The following fields are mutually exclusive: `discount_percentage`, `discount_absolute`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discount_percentage=
    
    
    def discount_percentage=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Discount percentage, represented as decimal. For example, a 20% discount will be represented as 0.2.

Note: The following fields are mutually exclusive: `discount_percentage`, `discount_absolute`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Float) — Discount percentage, represented as decimal. For example, a 20% discount will be represented as 0.2.

Note: The following fields are mutually exclusive: `discount_percentage`, `discount_absolute`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discount_type
    
    
    def discount_type() -> ::Google::Cloud::Channel::V1::DiscountType

**Returns**

  * ([::Google::Cloud::Channel::V1::DiscountType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DiscountType)) — Type of the discount. 



### #discount_type=
    
    
    def discount_type=(value) -> ::Google::Cloud::Channel::V1::DiscountType

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::DiscountType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DiscountType)) — Type of the discount. 



**Returns**

  * ([::Google::Cloud::Channel::V1::DiscountType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DiscountType)) — Type of the discount. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
