---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-SingleProductOffer-Installment/
title: Cloud Commerce Producer V1BETA API - Class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::Installment (v0.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:54.155824+00:00
---

# Cloud Commerce Producer V1BETA API - Class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::Installment (v0.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-SingleProductOffer-Installment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Commerce Producer V1BETA API - Class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::Installment (v0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Reference documentation and code samples for the Cloud Commerce Producer V1BETA API class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::Installment.

An installment of the offer.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #price_model
    
    
    def price_model() -> ::Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::PriceModel

**Returns**

  * ([::Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::PriceModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-SingleProductOffer-PriceModel)) — Optional. The price model of the installment. All installments must have the same form of price model. 



### #price_model=
    
    
    def price_model=(value) -> ::Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::PriceModel

**Parameter**

  * **value** ([::Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::PriceModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-SingleProductOffer-PriceModel)) — Optional. The price model of the installment. All installments must have the same form of price model. 



**Returns**

  * ([::Google::Cloud::CommerceProducer::V1beta::PrivateOffer::SingleProductOffer::PriceModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-SingleProductOffer-PriceModel)) — Optional. The price model of the installment. All installments must have the same form of price model. 



### #start_time
    
    
    def start_time() -> ::Google::Type::DateTime

**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Type-DateTime)) — Optional. The start time of the installment. Each installment must have a unique start time with one exception: When the `term.start_policy` of the offer's term is `IMMEDIATE`, the `start_time` of the first installment must be unset. The actual start time is not recorded in the offer and instead is determined by the time the resulting order became active.

When the `term.start_policy` of the offer's term is `SCHEDULED_START_TIME`, then the first installment's `start_time` must match `term.scheduled_start_time`.

If the `term.end_policy` of the offer's term is `SCHEDULED_END_TIME`, then installment `start_time` must be before `term.scheduled_end_time`. If it's `AFTER_DURATION`, then installment `start_time` must be before the time calculated by adding the `term.duration_months` to the start time of the offer.

The `start_time` of the installments cannot be before the `accept_deadline_time` of the offer.

Installment start times must be in strictly increasing chronological order. 




### #start_time=
    
    
    def start_time=(value) -> ::Google::Type::DateTime

**Parameter**

  * **value** ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Type-DateTime)) — Optional. The start time of the installment. Each installment must have a unique start time with one exception: When the `term.start_policy` of the offer's term is `IMMEDIATE`, the `start_time` of the first installment must be unset. The actual start time is not recorded in the offer and instead is determined by the time the resulting order became active.

When the `term.start_policy` of the offer's term is `SCHEDULED_START_TIME`, then the first installment's `start_time` must match `term.scheduled_start_time`.

If the `term.end_policy` of the offer's term is `SCHEDULED_END_TIME`, then installment `start_time` must be before `term.scheduled_end_time`. If it's `AFTER_DURATION`, then installment `start_time` must be before the time calculated by adding the `term.duration_months` to the start time of the offer.

The `start_time` of the installments cannot be before the `accept_deadline_time` of the offer.

Installment start times must be in strictly increasing chronological order. 




**Returns**

  * ([::Google::Type::DateTime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Type-DateTime)) — Optional. The start time of the installment. Each installment must have a unique start time with one exception: When the `term.start_policy` of the offer's term is `IMMEDIATE`, the `start_time` of the first installment must be unset. The actual start time is not recorded in the offer and instead is determined by the time the resulting order became active.

When the `term.start_policy` of the offer's term is `SCHEDULED_START_TIME`, then the first installment's `start_time` must match `term.scheduled_start_time`.

If the `term.end_policy` of the offer's term is `SCHEDULED_END_TIME`, then installment `start_time` must be before `term.scheduled_end_time`. If it's `AFTER_DURATION`, then installment `start_time` must be before the time calculated by adding the `term.duration_months` to the start time of the offer.

The `start_time` of the installments cannot be before the `accept_deadline_time` of the offer.

Installment start times must be in strictly increasing chronological order. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
