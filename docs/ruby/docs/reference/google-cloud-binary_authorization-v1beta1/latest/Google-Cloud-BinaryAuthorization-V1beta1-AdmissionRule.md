---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule/
title: Binary Authorization V1beta1 API - Class Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:56.389672+00:00
---

# Binary Authorization V1beta1 API - Class Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Binary Authorization V1beta1 API - Class Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1 

Reference documentation and code samples for the Binary Authorization V1beta1 API class Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule.

An [admission rule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule "Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule \(class\)") specifies either that all container images used in a pod creation request must be attested to by one or more [attestors](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-Attestor "Google::Cloud::BinaryAuthorization::V1beta1::Attestor \(class\)"), that all pod creations will be allowed, or that all pod creations will be denied.

Images matching an [admission allowlist pattern][google.cloud.binaryauthorization.v1beta1.AdmissionWhitelistPattern] are exempted from admission rules and will never block a pod creation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #enforcement_mode
    
    
    def enforcement_mode() -> ::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EnforcementMode

**Returns**

  * ([::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EnforcementMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule-EnforcementMode)) — Required. The action when a pod creation is denied by the admission rule. 



### #enforcement_mode=
    
    
    def enforcement_mode=(value) -> ::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EnforcementMode

**Parameter**

  * **value** ([::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EnforcementMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule-EnforcementMode)) — Required. The action when a pod creation is denied by the admission rule. 



**Returns**

  * ([::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EnforcementMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule-EnforcementMode)) — Required. The action when a pod creation is denied by the admission rule. 



### #evaluation_mode
    
    
    def evaluation_mode() -> ::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EvaluationMode

**Returns**

  * ([::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EvaluationMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule-EvaluationMode)) — Required. How this admission rule will be evaluated. 



### #evaluation_mode=
    
    
    def evaluation_mode=(value) -> ::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EvaluationMode

**Parameter**

  * **value** ([::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EvaluationMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule-EvaluationMode)) — Required. How this admission rule will be evaluated. 



**Returns**

  * ([::Google::Cloud::BinaryAuthorization::V1beta1::AdmissionRule::EvaluationMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1beta1/latest/Google-Cloud-BinaryAuthorization-V1beta1-AdmissionRule-EvaluationMode)) — Required. How this admission rule will be evaluated. 



### #require_attestations_by
    
    
    def require_attestations_by() -> ::Array<::String>

**Returns**

  * (::Array<::String>) 



### #require_attestations_by=
    
    
    def require_attestations_by=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) 



**Returns**

  * (::Array<::String>) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
