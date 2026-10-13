---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-UpdateEnrollmentRequest/
title: Eventarc V1 API - Class Google::Cloud::Eventarc::V1::UpdateEnrollmentRequest (v2.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:08.249610+00:00
---

# Eventarc V1 API - Class Google::Cloud::Eventarc::V1::UpdateEnrollmentRequest (v2.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-UpdateEnrollmentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Eventarc V1 API - Class Google::Cloud::Eventarc::V1::UpdateEnrollmentRequest (v2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.1  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.4 

Reference documentation and code samples for the Eventarc V1 API class Google::Cloud::Eventarc::V1::UpdateEnrollmentRequest.

The request message for the UpdateEnrollment method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, and the Enrollment is not found, a new Enrollment will be created. In this situation, `update_mask` is ignored. 



### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, and the Enrollment is not found, a new Enrollment will be created. In this situation, `update_mask` is ignored. 



**Returns**

  * (::Boolean) — Optional. If set to true, and the Enrollment is not found, a new Enrollment will be created. In this situation, `update_mask` is ignored. 



### #enrollment
    
    
    def enrollment() -> ::Google::Cloud::Eventarc::V1::Enrollment

**Returns**

  * ([::Google::Cloud::Eventarc::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Enrollment)) — Required. The Enrollment to be updated. 



### #enrollment=
    
    
    def enrollment=(value) -> ::Google::Cloud::Eventarc::V1::Enrollment

**Parameter**

  * **value** ([::Google::Cloud::Eventarc::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Enrollment)) — Required. The Enrollment to be updated. 



**Returns**

  * ([::Google::Cloud::Eventarc::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Enrollment)) — Required. The Enrollment to be updated. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Protobuf-FieldMask)) — Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*". 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Protobuf-FieldMask)) — Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*". 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Protobuf-FieldMask)) — Optional. The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "*". 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set, validate the request and preview the review, but do not post it. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set, validate the request and preview the review, but do not post it. 



**Returns**

  * (::Boolean) — Optional. If set, validate the request and preview the review, but do not post it. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
