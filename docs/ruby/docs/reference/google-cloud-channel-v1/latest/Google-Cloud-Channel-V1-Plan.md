---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Plan/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Plan (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:56.751982+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Plan (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Plan (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::Plan.

The payment plan for the Offer. Describes how to make a payment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #billing_account
    
    
    def billing_account() -> ::String

**Returns**

  * (::String) — Reseller Billing account to charge after an offer transaction. Only present for Google Cloud offers. 



### #billing_account=
    
    
    def billing_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Reseller Billing account to charge after an offer transaction. Only present for Google Cloud offers. 



**Returns**

  * (::String) — Reseller Billing account to charge after an offer transaction. Only present for Google Cloud offers. 



### #payment_cycle
    
    
    def payment_cycle() -> ::Google::Cloud::Channel::V1::Period

**Returns**

  * ([::Google::Cloud::Channel::V1::Period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Period)) — Describes how frequently the reseller will be billed, such as once per month. 



### #payment_cycle=
    
    
    def payment_cycle=(value) -> ::Google::Cloud::Channel::V1::Period

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::Period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Period)) — Describes how frequently the reseller will be billed, such as once per month. 



**Returns**

  * ([::Google::Cloud::Channel::V1::Period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Period)) — Describes how frequently the reseller will be billed, such as once per month. 



### #payment_plan
    
    
    def payment_plan() -> ::Google::Cloud::Channel::V1::PaymentPlan

**Returns**

  * ([::Google::Cloud::Channel::V1::PaymentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PaymentPlan)) — Describes how a reseller will be billed. 



### #payment_plan=
    
    
    def payment_plan=(value) -> ::Google::Cloud::Channel::V1::PaymentPlan

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::PaymentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PaymentPlan)) — Describes how a reseller will be billed. 



**Returns**

  * ([::Google::Cloud::Channel::V1::PaymentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PaymentPlan)) — Describes how a reseller will be billed. 



### #payment_type
    
    
    def payment_type() -> ::Google::Cloud::Channel::V1::PaymentType

**Returns**

  * ([::Google::Cloud::Channel::V1::PaymentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PaymentType)) — Specifies when the payment needs to happen. 



### #payment_type=
    
    
    def payment_type=(value) -> ::Google::Cloud::Channel::V1::PaymentType

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::PaymentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PaymentType)) — Specifies when the payment needs to happen. 



**Returns**

  * ([::Google::Cloud::Channel::V1::PaymentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PaymentType)) — Specifies when the payment needs to happen. 



### #trial_period
    
    
    def trial_period() -> ::Google::Cloud::Channel::V1::Period

**Returns**

  * ([::Google::Cloud::Channel::V1::Period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Period)) — Present for Offers with a trial period. For trial-only Offers, a paid service needs to start before the trial period ends for continued service. For Regular Offers with a trial period, the regular pricing goes into effect when trial period ends, or if paid service is started before the end of the trial period. 



### #trial_period=
    
    
    def trial_period=(value) -> ::Google::Cloud::Channel::V1::Period

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::Period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Period)) — Present for Offers with a trial period. For trial-only Offers, a paid service needs to start before the trial period ends for continued service. For Regular Offers with a trial period, the regular pricing goes into effect when trial period ends, or if paid service is started before the end of the trial period. 



**Returns**

  * ([::Google::Cloud::Channel::V1::Period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Period)) — Present for Offers with a trial period. For trial-only Offers, a paid service needs to start before the trial period ends for continued service. For Regular Offers with a trial period, the regular pricing goes into effect when trial period ends, or if paid service is started before the end of the trial period. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
