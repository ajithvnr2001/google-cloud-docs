---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudIdentityInfo (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:16.726366+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudIdentityInfo (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudIdentityInfo (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CloudIdentityInfo.

Cloud Identity information for the Cloud Channel Customer.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #admin_console_uri
    
    
    def admin_console_uri() -> ::String

**Returns**

  * (::String) — Output only. URI of Customer's Admin console dashboard. 



### #alternate_email
    
    
    def alternate_email() -> ::String

**Returns**

  * (::String) — The alternate email. 



### #alternate_email=
    
    
    def alternate_email=(value) -> ::String

**Parameter**

  * **value** (::String) — The alternate email. 



**Returns**

  * (::String) — The alternate email. 



### #customer_type
    
    
    def customer_type() -> ::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType

**Returns**

  * ([::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo-CustomerType)) — CustomerType indicates verification type needed for using services. 



### #customer_type=
    
    
    def customer_type=(value) -> ::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo-CustomerType)) — CustomerType indicates verification type needed for using services. 



**Returns**

  * ([::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo-CustomerType)) — CustomerType indicates verification type needed for using services. 



### #edu_data
    
    
    def edu_data() -> ::Google::Cloud::Channel::V1::EduData

**Returns**

  * ([::Google::Cloud::Channel::V1::EduData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EduData)) — Edu information about the customer. 



### #edu_data=
    
    
    def edu_data=(value) -> ::Google::Cloud::Channel::V1::EduData

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::EduData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EduData)) — Edu information about the customer. 



**Returns**

  * ([::Google::Cloud::Channel::V1::EduData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EduData)) — Edu information about the customer. 



### #is_domain_verified
    
    
    def is_domain_verified() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether the domain is verified. This field is not returned for a Customer's cloud_identity_info resource. Partners can use the domains.get() method of the Workspace SDK's Directory API, or listen to the PRIMARY_DOMAIN_VERIFIED Pub/Sub event in to track domain verification of their resolve Workspace customers. 



### #language_code
    
    
    def language_code() -> ::String

**Returns**

  * (::String) — Language code. 



### #language_code=
    
    
    def language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — Language code. 



**Returns**

  * (::String) — Language code. 



### #phone_number
    
    
    def phone_number() -> ::String

**Returns**

  * (::String) — Phone number associated with the Cloud Identity. 



### #phone_number=
    
    
    def phone_number=(value) -> ::String

**Parameter**

  * **value** (::String) — Phone number associated with the Cloud Identity. 



**Returns**

  * (::String) — Phone number associated with the Cloud Identity. 



### #primary_domain
    
    
    def primary_domain() -> ::String

**Returns**

  * (::String) — Output only. The primary domain name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
