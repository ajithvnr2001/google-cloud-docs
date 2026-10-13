---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeIdentityMappingsRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:47.245381+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeIdentityMappingsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest.

Request message for [IdentityMappingStoreService.PurgeIdentityMappings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-IdentityMappingStoreService-Client#Google__Cloud__DiscoveryEngine__V1beta__IdentityMappingStoreService__Client_purge_identity_mappings_instance_ "Google::Cloud::DiscoveryEngine::V1beta::IdentityMappingStoreService::Client#purge_identity_mappings \(method\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Filter matching identity mappings to purge. The eligible field for filtering is:

    * `update_time`: in ISO 8601 "zulu" format.
    * `external_id`

Examples:

    * Deleting all identity mappings updated in a time range: `update_time > "2012-04-23T18:25:43.511Z" AND update_time < "2012-04-23T18:30:43.511Z"`
    * Deleting all identity mappings for a given external_id: `external_id = "id1"`
    * Deleting all identity mappings inside an identity mapping store: `*`

The filtering fields are assumed to have an implicit AND. Should not be used with source. An error will be thrown, if both are provided. 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Filter matching identity mappings to purge. The eligible field for filtering is:

    * `update_time`: in ISO 8601 "zulu" format.
    * `external_id`

Examples:

    * Deleting all identity mappings updated in a time range: `update_time > "2012-04-23T18:25:43.511Z" AND update_time < "2012-04-23T18:30:43.511Z"`
    * Deleting all identity mappings for a given external_id: `external_id = "id1"`
    * Deleting all identity mappings inside an identity mapping store: `*`

The filtering fields are assumed to have an implicit AND. Should not be used with source. An error will be thrown, if both are provided. 




**Returns**

  * (::String) — Filter matching identity mappings to purge. The eligible field for filtering is:

    * `update_time`: in ISO 8601 "zulu" format.
    * `external_id`

Examples:

    * Deleting all identity mappings updated in a time range: `update_time > "2012-04-23T18:25:43.511Z" AND update_time < "2012-04-23T18:30:43.511Z"`
    * Deleting all identity mappings for a given external_id: `external_id = "id1"`
    * Deleting all identity mappings inside an identity mapping store: `*`

The filtering fields are assumed to have an implicit AND. Should not be used with source. An error will be thrown, if both are provided. 




### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Actually performs the purge. If `force` is set to false, return the expected purge count without deleting any identity mappings. This field is only supported for purge with filter. For input source this field is ignored and data will be purged regardless of the value of this field. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Actually performs the purge. If `force` is set to false, return the expected purge count without deleting any identity mappings. This field is only supported for purge with filter. For input source this field is ignored and data will be purged regardless of the value of this field. 



**Returns**

  * (::Boolean) — Actually performs the purge. If `force` is set to false, return the expected purge count without deleting any identity mappings. This field is only supported for purge with filter. For input source this field is ignored and data will be purged regardless of the value of this field. 



### #identity_mapping_store
    
    
    def identity_mapping_store() -> ::String

**Returns**

  * (::String) — Required. The name of the Identity Mapping Store to purge Identity Mapping Entries from. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`



### #identity_mapping_store=
    
    
    def identity_mapping_store=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the Identity Mapping Store to purge Identity Mapping Entries from. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`



**Returns**

  * (::String) — Required. The name of the Identity Mapping Store to purge Identity Mapping Entries from. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`



### #inline_source
    
    
    def inline_source() -> ::Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest::InlineSource

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest::InlineSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeIdentityMappingsRequest-InlineSource)) — The inline source to purge identity mapping entries from. 



### #inline_source=
    
    
    def inline_source=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest::InlineSource

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest::InlineSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeIdentityMappingsRequest-InlineSource)) — The inline source to purge identity mapping entries from. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeIdentityMappingsRequest::InlineSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeIdentityMappingsRequest-InlineSource)) — The inline source to purge identity mapping entries from. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
