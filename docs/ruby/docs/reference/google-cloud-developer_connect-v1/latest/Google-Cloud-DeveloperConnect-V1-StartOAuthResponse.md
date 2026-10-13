---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-StartOAuthResponse/
title: Developer Connect V1 API - Class Google::Cloud::DeveloperConnect::V1::StartOAuthResponse (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:16.558638+00:00
---

# Developer Connect V1 API - Class Google::Cloud::DeveloperConnect::V1::StartOAuthResponse (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-StartOAuthResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Developer Connect V1 API - Class Google::Cloud::DeveloperConnect::V1::StartOAuthResponse (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Developer Connect V1 API class Google::Cloud::DeveloperConnect::V1::StartOAuthResponse.

Message for responding to starting an OAuth flow.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_uri
    
    
    def auth_uri() -> ::String

**Returns**

  * (::String) — The authorization server URL to the OAuth flow of the service provider. 



### #auth_uri=
    
    
    def auth_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The authorization server URL to the OAuth flow of the service provider. 



**Returns**

  * (::String) — The authorization server URL to the OAuth flow of the service provider. 



### #client_id
    
    
    def client_id() -> ::String

**Returns**

  * (::String) — The client ID to the OAuth App of the service provider. 



### #client_id=
    
    
    def client_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The client ID to the OAuth App of the service provider. 



**Returns**

  * (::String) — The client ID to the OAuth App of the service provider. 



### #code_challenge
    
    
    def code_challenge() -> ::String

**Returns**

  * (::String) — Please refer to https://datatracker.ietf.org/doc/html/rfc7636#section-4.1 



### #code_challenge=
    
    
    def code_challenge=(value) -> ::String

**Parameter**

  * **value** (::String) — Please refer to https://datatracker.ietf.org/doc/html/rfc7636#section-4.1 



**Returns**

  * (::String) — Please refer to https://datatracker.ietf.org/doc/html/rfc7636#section-4.1 



### #code_challenge_method
    
    
    def code_challenge_method() -> ::String

**Returns**

  * (::String) — Please refer to https://datatracker.ietf.org/doc/html/rfc7636#section-4.2 



### #code_challenge_method=
    
    
    def code_challenge_method=(value) -> ::String

**Parameter**

  * **value** (::String) — Please refer to https://datatracker.ietf.org/doc/html/rfc7636#section-4.2 



**Returns**

  * (::String) — Please refer to https://datatracker.ietf.org/doc/html/rfc7636#section-4.2 



### #scopes
    
    
    def scopes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of scopes requested by the application. 



### #scopes=
    
    
    def scopes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of scopes requested by the application. 



**Returns**

  * (::Array<::String>) — The list of scopes requested by the application. 



### #system_provider_id
    
    
    def system_provider_id() -> ::Google::Cloud::DeveloperConnect::V1::SystemProvider

**Returns**

  * ([::Google::Cloud::DeveloperConnect::V1::SystemProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-SystemProvider)) — The ID of the system provider. 



### #system_provider_id=
    
    
    def system_provider_id=(value) -> ::Google::Cloud::DeveloperConnect::V1::SystemProvider

**Parameter**

  * **value** ([::Google::Cloud::DeveloperConnect::V1::SystemProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-SystemProvider)) — The ID of the system provider. 



**Returns**

  * ([::Google::Cloud::DeveloperConnect::V1::SystemProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-SystemProvider)) — The ID of the system provider. 



### #ticket
    
    
    def ticket() -> ::String

**Returns**

  * (::String) — The ticket to be used for post processing the callback from the service provider. 



### #ticket=
    
    
    def ticket=(value) -> ::String

**Parameter**

  * **value** (::String) — The ticket to be used for post processing the callback from the service provider. 



**Returns**

  * (::String) — The ticket to be used for post processing the callback from the service provider. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
