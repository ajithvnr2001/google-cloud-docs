---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To/
title: Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:17.648184+00:00
---

# Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Network Security V1 API class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To.

Describes properties of one or more targets of a request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #not_operations
    
    
    def not_operations() -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation>

**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation)>) — Optional. Describes the negated properties of the targets of a request. Matches requests for operations that do not match the criteria specified in this field. At least one of operations or notOperations must be specified. 



### #not_operations=
    
    
    def not_operations=(value) -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation)>) — Optional. Describes the negated properties of the targets of a request. Matches requests for operations that do not match the criteria specified in this field. At least one of operations or notOperations must be specified. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation)>) — Optional. Describes the negated properties of the targets of a request. Matches requests for operations that do not match the criteria specified in this field. At least one of operations or notOperations must be specified. 



### #operations
    
    
    def operations() -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation>

**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation)>) — Optional. Describes properties of one or more targets of a request. At least one of operations or notOperations must be specified. Limited to 1 operation. A match occurs when ANY operation (in operations or notOperations) matches. Within an operation, the match follows AND semantics across fields and OR semantics within a field, i.e. a match occurs when ANY path matches AND ANY header matches and ANY method matches. 



### #operations=
    
    
    def operations=(value) -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation)>) — Optional. Describes properties of one or more targets of a request. At least one of operations or notOperations must be specified. Limited to 1 operation. A match occurs when ANY operation (in operations or notOperations) matches. Within an operation, the match follows AND semantics across fields and OR semantics within a field, i.e. a match occurs when ANY path matches AND ANY header matches and ANY method matches. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation)>) — Optional. Describes properties of one or more targets of a request. At least one of operations or notOperations must be specified. Limited to 1 operation. A match occurs when ANY operation (in operations or notOperations) matches. Within an operation, the match follows AND semantics across fields and OR semantics within a field, i.e. a match occurs when ANY path matches AND ANY header matches and ANY method matches. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
