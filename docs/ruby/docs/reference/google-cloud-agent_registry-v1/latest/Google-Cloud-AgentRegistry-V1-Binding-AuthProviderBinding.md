---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-Binding-AuthProviderBinding/
title: Agent Registry V1 API - Class Google::Cloud::AgentRegistry::V1::Binding::AuthProviderBinding (v0.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:05.938723+00:00
---

# Agent Registry V1 API - Class Google::Cloud::AgentRegistry::V1::Binding::AuthProviderBinding (v0.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-Binding-AuthProviderBinding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Agent Registry V1 API - Class Google::Cloud::AgentRegistry::V1::Binding::AuthProviderBinding (v0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.1 

Reference documentation and code samples for the Agent Registry V1 API class Google::Cloud::AgentRegistry::V1::Binding::AuthProviderBinding.

The AuthProvider of the Binding.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_provider
    
    
    def auth_provider() -> ::String

**Returns**

  * (::String) — 

Required. The resource name of the target AuthProvider. Format:

    * `projects/{project}/locations/{location}/authProviders/{auth_provider}`



### #auth_provider=
    
    
    def auth_provider=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The resource name of the target AuthProvider. Format:

    * `projects/{project}/locations/{location}/authProviders/{auth_provider}`



**Returns**

  * (::String) — 

Required. The resource name of the target AuthProvider. Format:

    * `projects/{project}/locations/{location}/authProviders/{auth_provider}`



### #continue_uri
    
    
    def continue_uri() -> ::String

**Returns**

  * (::String) — Optional. The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow. 



### #continue_uri=
    
    
    def continue_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow. 



**Returns**

  * (::String) — Optional. The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow. 



### #scopes
    
    
    def scopes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The list of OAuth2 scopes of the AuthProvider. 



### #scopes=
    
    
    def scopes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The list of OAuth2 scopes of the AuthProvider. 



**Returns**

  * (::Array<::String>) — Optional. The list of OAuth2 scopes of the AuthProvider. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
