---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateIdentityMappingStoreRequest/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::CreateIdentityMappingStoreRequest (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:48.241283+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::CreateIdentityMappingStoreRequest (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateIdentityMappingStoreRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::CreateIdentityMappingStoreRequest (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::CreateIdentityMappingStoreRequest.

Request message for [IdentityMappingStoreService.CreateIdentityMappingStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-IdentityMappingStoreService-Client#Google__Cloud__DiscoveryEngine__V1__IdentityMappingStoreService__Client_create_identity_mapping_store_instance_ "Google::Cloud::DiscoveryEngine::V1::IdentityMappingStoreService::Client#create_identity_mapping_store \(method\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cmek_config_name
    
    
    def cmek_config_name() -> ::String

**Returns**

  * (::String) — Resource name of the CmekConfig to use for protecting this Identity Mapping Store.

Note: The following fields are mutually exclusive: `cmek_config_name`, `disable_cmek`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cmek_config_name=
    
    
    def cmek_config_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Resource name of the CmekConfig to use for protecting this Identity Mapping Store.

Note: The following fields are mutually exclusive: `cmek_config_name`, `disable_cmek`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Resource name of the CmekConfig to use for protecting this Identity Mapping Store.

Note: The following fields are mutually exclusive: `cmek_config_name`, `disable_cmek`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disable_cmek
    
    
    def disable_cmek() -> ::Boolean

**Returns**

  * (::Boolean) — Identity Mapping Store without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

Note: The following fields are mutually exclusive: `disable_cmek`, `cmek_config_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disable_cmek=
    
    
    def disable_cmek=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Identity Mapping Store without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

Note: The following fields are mutually exclusive: `disable_cmek`, `cmek_config_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — Identity Mapping Store without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

Note: The following fields are mutually exclusive: `disable_cmek`, `cmek_config_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #identity_mapping_store
    
    
    def identity_mapping_store() -> ::Google::Cloud::DiscoveryEngine::V1::IdentityMappingStore

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::IdentityMappingStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-IdentityMappingStore)) — Required. The Identity Mapping Store to create. 



### #identity_mapping_store=
    
    
    def identity_mapping_store=(value) -> ::Google::Cloud::DiscoveryEngine::V1::IdentityMappingStore

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::IdentityMappingStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-IdentityMappingStore)) — Required. The Identity Mapping Store to create. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::IdentityMappingStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-IdentityMappingStore)) — Required. The Identity Mapping Store to create. 



### #identity_mapping_store_id
    
    
    def identity_mapping_store_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the Identity Mapping Store to create.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters. 




### #identity_mapping_store_id=
    
    
    def identity_mapping_store_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the Identity Mapping Store to create.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters. 




**Returns**

  * (::String) — Required. The ID of the Identity Mapping Store to create.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent collection resource name, such as `projects/{project}/locations/{location}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent collection resource name, such as `projects/{project}/locations/{location}`. 



**Returns**

  * (::String) — Required. The parent collection resource name, such as `projects/{project}/locations/{location}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
