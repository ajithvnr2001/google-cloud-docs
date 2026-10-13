---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-Principal/
title: Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:38.510349+00:00
---

# Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-Principal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Network Security V1 API class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal.

Describes the properties of a principal to be matched against.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #principal
    
    
    def principal() -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch

**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)) — Required. A non-empty string whose value is matched against the principal value based on the principal_selector. Only exact match can be applied for CLIENT_CERT_URI_SAN, CLIENT_CERT_DNS_NAME_SAN, CLIENT_CERT_COMMON_NAME selectors. 



### #principal=
    
    
    def principal=(value) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch

**Parameter**

  * **value** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)) — Required. A non-empty string whose value is matched against the principal value based on the principal_selector. Only exact match can be applied for CLIENT_CERT_URI_SAN, CLIENT_CERT_DNS_NAME_SAN, CLIENT_CERT_COMMON_NAME selectors. 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)) — Required. A non-empty string whose value is matched against the principal value based on the principal_selector. Only exact match can be applied for CLIENT_CERT_URI_SAN, CLIENT_CERT_DNS_NAME_SAN, CLIENT_CERT_COMMON_NAME selectors. 



### #principal_selector
    
    
    def principal_selector() -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal::PrincipalSelector

**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal::PrincipalSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-Principal-PrincipalSelector)) — Optional. An enum to decide what principal value the principal rule will match against. If not specified, the PrincipalSelector is CLIENT_CERT_URI_SAN. 



### #principal_selector=
    
    
    def principal_selector=(value) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal::PrincipalSelector

**Parameter**

  * **value** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal::PrincipalSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-Principal-PrincipalSelector)) — Optional. An enum to decide what principal value the principal rule will match against. If not specified, the PrincipalSelector is CLIENT_CERT_URI_SAN. 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::Principal::PrincipalSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-Principal-PrincipalSelector)) — Optional. An enum to decide what principal value the principal rule will match against. If not specified, the PrincipalSelector is CLIENT_CERT_URI_SAN. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
