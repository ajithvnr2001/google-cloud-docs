---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest/
title: reCAPTCHA Enterprise V1 API - Class Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:41.796540+00:00
---

# reCAPTCHA Enterprise V1 API - Class Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  reCAPTCHA Enterprise V1 API - Class Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.0  1.11.0  1.9.1  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.0  1.2.0  1.1.0  1.0.0  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.3  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.1 

Reference documentation and code samples for the reCAPTCHA Enterprise V1 API class Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest.

The request message to annotate an Assessment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #account_id
    
    
    def account_id() -> ::String

**Returns**

  * (::String) — Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request. 



### #account_id=
    
    
    def account_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request. 



**Returns**

  * (::String) — Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request. 



### #annotation
    
    
    def annotation() -> ::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Annotation

**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Annotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest-Annotation)) — Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent. 



### #annotation=
    
    
    def annotation=(value) -> ::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Annotation

**Parameter**

  * **value** ([::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Annotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest-Annotation)) — Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent. 



**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Annotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest-Annotation)) — Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent. 



### #hashed_account_id
    
    
    def hashed_account_id() -> ::String

**Returns**

  * (::String) — Optional. A stable hashed account identifier to apply to the assessment. This is an alternative to setting `hashed_account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request. 



### #hashed_account_id=
    
    
    def hashed_account_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A stable hashed account identifier to apply to the assessment. This is an alternative to setting `hashed_account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request. 



**Returns**

  * (::String) — Optional. A stable hashed account identifier to apply to the assessment. This is an alternative to setting `hashed_account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`. 



**Returns**

  * (::String) — Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`. 



### #phone_authentication_event
    
    
    def phone_authentication_event() -> ::Google::Cloud::RecaptchaEnterprise::V1::PhoneAuthenticationEvent

**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::PhoneAuthenticationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-PhoneAuthenticationEvent)) — Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes. 



### #phone_authentication_event=
    
    
    def phone_authentication_event=(value) -> ::Google::Cloud::RecaptchaEnterprise::V1::PhoneAuthenticationEvent

**Parameter**

  * **value** ([::Google::Cloud::RecaptchaEnterprise::V1::PhoneAuthenticationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-PhoneAuthenticationEvent)) — Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes. 



**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::PhoneAuthenticationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-PhoneAuthenticationEvent)) — Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes. 



### #reasons
    
    
    def reasons() -> ::Array<::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Reason>

**Returns**

  * (::Array<[::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Reason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest-Reason)>) — Optional. Reasons for the annotation that are assigned to the event. 



### #reasons=
    
    
    def reasons=(value) -> ::Array<::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Reason>

**Parameter**

  * **value** (::Array<[::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Reason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest-Reason)>) — Optional. Reasons for the annotation that are assigned to the event. 



**Returns**

  * (::Array<[::Google::Cloud::RecaptchaEnterprise::V1::AnnotateAssessmentRequest::Reason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-AnnotateAssessmentRequest-Reason)>) — Optional. Reasons for the annotation that are assigned to the event. 



### #transaction_event
    
    
    def transaction_event() -> ::Google::Cloud::RecaptchaEnterprise::V1::TransactionEvent

**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::TransactionEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-TransactionEvent)) — Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction. 



### #transaction_event=
    
    
    def transaction_event=(value) -> ::Google::Cloud::RecaptchaEnterprise::V1::TransactionEvent

**Parameter**

  * **value** ([::Google::Cloud::RecaptchaEnterprise::V1::TransactionEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-TransactionEvent)) — Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction. 



**Returns**

  * ([::Google::Cloud::RecaptchaEnterprise::V1::TransactionEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1/latest/Google-Cloud-RecaptchaEnterprise-V1-TransactionEvent)) — Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
