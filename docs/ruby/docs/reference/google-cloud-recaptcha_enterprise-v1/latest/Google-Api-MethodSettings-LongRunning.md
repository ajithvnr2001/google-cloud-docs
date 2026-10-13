---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Api-MethodSettings-LongRunning/
title: reCAPTCHA Enterprise V1 API - Class Google::Api::MethodSettings::LongRunning (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:35.184389+00:00
---

# reCAPTCHA Enterprise V1 API - Class Google::Api::MethodSettings::LongRunning (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Api-MethodSettings-LongRunning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  reCAPTCHA Enterprise V1 API - Class Google::Api::MethodSettings::LongRunning (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.0  1.11.0  1.9.1  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.0  1.2.0  1.1.0  1.0.0  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.3  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.1 

Reference documentation and code samples for the reCAPTCHA Enterprise V1 API class Google::Api::MethodSettings::LongRunning.

Describes settings to use when generating API methods that use the long-running operation pattern. All default values below are from those used in the client library generators (e.g. [Java](https://github.com/googleapis/gapic-generator-java/blob/04c2faa191a9b5a10b92392fe8482279c4404803/src/main/java/com/google/api/generator/gapic/composer/common/RetrySettingsComposer.java)).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #initial_poll_delay
    
    
    def initial_poll_delay() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Initial delay after which the first poll request will be made. Default value: 5 seconds. 



### #initial_poll_delay=
    
    
    def initial_poll_delay=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Initial delay after which the first poll request will be made. Default value: 5 seconds. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Initial delay after which the first poll request will be made. Default value: 5 seconds. 



### #max_poll_delay
    
    
    def max_poll_delay() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Maximum time between two subsequent poll requests. Default value: 45 seconds. 



### #max_poll_delay=
    
    
    def max_poll_delay=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Maximum time between two subsequent poll requests. Default value: 45 seconds. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Maximum time between two subsequent poll requests. Default value: 45 seconds. 



### #poll_delay_multiplier
    
    
    def poll_delay_multiplier() -> ::Float

**Returns**

  * (::Float) — Multiplier to gradually increase delay between subsequent polls until it reaches max_poll_delay. Default value: 1.5. 



### #poll_delay_multiplier=
    
    
    def poll_delay_multiplier=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Multiplier to gradually increase delay between subsequent polls until it reaches max_poll_delay. Default value: 1.5. 



**Returns**

  * (::Float) — Multiplier to gradually increase delay between subsequent polls until it reaches max_poll_delay. Default value: 1.5. 



### #total_poll_timeout
    
    
    def total_poll_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Total polling timeout. Default value: 5 minutes. 



### #total_poll_timeout=
    
    
    def total_poll_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Total polling timeout. Default value: 5 minutes. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Protobuf-Duration)) — Total polling timeout. Default value: 5 minutes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
