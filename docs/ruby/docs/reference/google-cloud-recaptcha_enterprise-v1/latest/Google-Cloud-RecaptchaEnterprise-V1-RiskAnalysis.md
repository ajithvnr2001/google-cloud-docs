---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-RiskAnalysis/
title: reCAPTCHA Enterprise V1 API - Class Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:00.184329+00:00
---

# reCAPTCHA Enterprise V1 API - Class Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-RiskAnalysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  reCAPTCHA Enterprise V1 API - Class Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.0  1.11.0  1.9.1  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.0  1.2.0  1.1.0  1.0.0  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.3  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.1 

Reference documentation and code samples for the reCAPTCHA Enterprise V1 API class Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis.

Risk analysis result for an event.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #challenge
    
    
    def challenge() -> ::Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis::Challenge

**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis::Challenge](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-RiskAnalysis-Challenge)) — Output only. Challenge information for Universal, `POLICY_BASED_CHALLENGE` and `INVISIBLE` keys. 



### #extended_verdict_reasons
    
    
    def extended_verdict_reasons() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. Additional reasons contributing to the risk analysis verdict. These reasons are available to Enterprise tier projects only. Contact sales for more information. The set of reasons is subject to change. 



### #last_challenge_type
    
    
    def last_challenge_type() -> ::Google::Cloud::RecaptchaEnterprise::V1::ChallengeType

**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::ChallengeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-ChallengeType)) — Output only. Type of the last challenge presented to the user for Universal, `POLICY_BASED_CHALLENGE` and `INVISIBLE` keys. The field is only set when a challenge was presented to the user. 



### #reasons
    
    
    def reasons() -> ::Array<::Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis::ClassificationReason>

**Returns**

  * (::Array<[::Google::Cloud::RecaptchaEnterprise::V1::RiskAnalysis::ClassificationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-RiskAnalysis-ClassificationReason)>) — Output only. Reasons contributing to the risk analysis verdict. 



### #score
    
    
    def score() -> ::Float

**Returns**

  * (::Float) — Output only. Legitimate event score from 0.0 to 1.0. (1.0 means very likely legitimate traffic while 0.0 means very likely non-legitimate traffic). 



### #verified_bots
    
    
    def verified_bots() -> ::Array<::Google::Cloud::RecaptchaEnterprise::V1::Bot>

**Returns**

  * (::Array<[::Google::Cloud::RecaptchaEnterprise::V1::Bot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-Bot)>) — Output only. Bots with identities that have been verified by reCAPTCHA and detected in the event. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
