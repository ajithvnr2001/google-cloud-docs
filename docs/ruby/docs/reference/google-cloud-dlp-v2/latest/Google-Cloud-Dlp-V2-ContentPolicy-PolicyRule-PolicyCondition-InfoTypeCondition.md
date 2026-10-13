---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ContentPolicy-PolicyRule-PolicyCondition-InfoTypeCondition/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:11.963119+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ContentPolicy-PolicyRule-PolicyCondition-InfoTypeCondition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition.

A info type based condition.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #any_info_type
    
    
    def any_info_type() -> ::Google::Protobuf::Empty

**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Empty)) — match any info types.

Note: The following fields are mutually exclusive: `any_info_type`, `info_types`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #any_info_type=
    
    
    def any_info_type=(value) -> ::Google::Protobuf::Empty

**Parameter**

  * **value** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Empty)) — match any info types.

Note: The following fields are mutually exclusive: `any_info_type`, `info_types`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Empty)) — match any info types.

Note: The following fields are mutually exclusive: `any_info_type`, `info_types`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #info_types
    
    
    def info_types() -> ::Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition::InfoTypes

**Returns**

  * ([::Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition::InfoTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ContentPolicy-PolicyRule-PolicyCondition-InfoTypeCondition-InfoTypes)) — match any of these info types.

Note: The following fields are mutually exclusive: `info_types`, `any_info_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #info_types=
    
    
    def info_types=(value) -> ::Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition::InfoTypes

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition::InfoTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ContentPolicy-PolicyRule-PolicyCondition-InfoTypeCondition-InfoTypes)) — match any of these info types.

Note: The following fields are mutually exclusive: `info_types`, `any_info_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::ContentPolicy::PolicyRule::PolicyCondition::InfoTypeCondition::InfoTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ContentPolicy-PolicyRule-PolicyCondition-InfoTypeCondition-InfoTypes)) — match any of these info types.

Note: The following fields are mutually exclusive: `info_types`, `any_info_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #min_count
    
    
    def min_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. The minimum total number of findings of all matching info types required for this condition to evaluate to true. Defaults to 1 if unset. 



### #min_count=
    
    
    def min_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The minimum total number of findings of all matching info types required for this condition to evaluate to true. Defaults to 1 if unset. 



**Returns**

  * (::Integer) — Optional. The minimum total number of findings of all matching info types required for this condition to evaluate to true. Defaults to 1 if unset. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
