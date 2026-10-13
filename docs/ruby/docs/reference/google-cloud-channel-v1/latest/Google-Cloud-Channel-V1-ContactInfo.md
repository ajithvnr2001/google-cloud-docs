---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ContactInfo/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ContactInfo (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:17.203890+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ContactInfo (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ContactInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ContactInfo (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ContactInfo.

Contact information for a customer account.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Output only. The customer account contact's display name, formatted as a combination of the customer's first and last name. 



### #email
    
    
    def email() -> ::String

**Returns**

  * (::String) — The customer account's contact email. Required for entitlements that create admin.google.com accounts, and serves as the customer's username for those accounts. Use this email to invite Team customers. 



### #email=
    
    
    def email=(value) -> ::String

**Parameter**

  * **value** (::String) — The customer account's contact email. Required for entitlements that create admin.google.com accounts, and serves as the customer's username for those accounts. Use this email to invite Team customers. 



**Returns**

  * (::String) — The customer account's contact email. Required for entitlements that create admin.google.com accounts, and serves as the customer's username for those accounts. Use this email to invite Team customers. 



### #first_name
    
    
    def first_name() -> ::String

**Returns**

  * (::String) — The customer account contact's first name. Optional for Team customers. 



### #first_name=
    
    
    def first_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The customer account contact's first name. Optional for Team customers. 



**Returns**

  * (::String) — The customer account contact's first name. Optional for Team customers. 



### #last_name
    
    
    def last_name() -> ::String

**Returns**

  * (::String) — The customer account contact's last name. Optional for Team customers. 



### #last_name=
    
    
    def last_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The customer account contact's last name. Optional for Team customers. 



**Returns**

  * (::String) — The customer account contact's last name. Optional for Team customers. 



### #phone
    
    
    def phone() -> ::String

**Returns**

  * (::String) — The customer account's contact phone number. 



### #phone=
    
    
    def phone=(value) -> ::String

**Parameter**

  * **value** (::String) — The customer account's contact phone number. 



**Returns**

  * (::String) — The customer account's contact phone number. 



### #title
    
    
    def title() -> ::String

**Returns**

  * (::String) — Optional. The customer account contact's job title. 



### #title=
    
    
    def title=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The customer account contact's job title. 



**Returns**

  * (::String) — Optional. The customer account contact's job title. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
