---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateDataStoreRequest/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:31.216398+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateDataStoreRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest.

Request for [DataStoreService.CreateDataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStoreService-Client#Google__Cloud__DiscoveryEngine__V1__DataStoreService__Client_create_data_store_instance_ "Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store \(method\)") method.

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

  * (::String) — Resource name of the CmekConfig to use for protecting this DataStore.

Note: The following fields are mutually exclusive: `cmek_config_name`, `disable_cmek`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cmek_config_name=
    
    
    def cmek_config_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Resource name of the CmekConfig to use for protecting this DataStore.

Note: The following fields are mutually exclusive: `cmek_config_name`, `disable_cmek`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Resource name of the CmekConfig to use for protecting this DataStore.

Note: The following fields are mutually exclusive: `cmek_config_name`, `disable_cmek`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_advanced_site_search
    
    
    def create_advanced_site_search() -> ::Boolean

**Returns**

  * (::Boolean) — A boolean flag indicating whether user want to directly create an advanced data store for site search. If the data store is not configured as site search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will be ignored. 



### #create_advanced_site_search=
    
    
    def create_advanced_site_search=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — A boolean flag indicating whether user want to directly create an advanced data store for site search. If the data store is not configured as site search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will be ignored. 



**Returns**

  * (::Boolean) — A boolean flag indicating whether user want to directly create an advanced data store for site search. If the data store is not configured as site search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will be ignored. 



### #data_store
    
    
    def data_store() -> ::Google::Cloud::DiscoveryEngine::V1::DataStore

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore)) — Required. The [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)") to create. 



### #data_store=
    
    
    def data_store=(value) -> ::Google::Cloud::DiscoveryEngine::V1::DataStore

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore)) — Required. The [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)") to create. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore)) — Required. The [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)") to create. 



### #data_store_id
    
    
    def data_store_id() -> ::String

**Returns**

  * (::String) — Required. The ID to use for the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)"), which will become the final component of the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)")'s resource name.

This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned. 




### #data_store_id=
    
    
    def data_store_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID to use for the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)"), which will become the final component of the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)")'s resource name.

This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned. 




**Returns**

  * (::String) — Required. The ID to use for the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)"), which will become the final component of the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)")'s resource name.

This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned. 




### #disable_cmek
    
    
    def disable_cmek() -> ::Boolean

**Returns**

  * (::Boolean) — DataStore without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

Note: The following fields are mutually exclusive: `disable_cmek`, `cmek_config_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disable_cmek=
    
    
    def disable_cmek=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — DataStore without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

Note: The following fields are mutually exclusive: `disable_cmek`, `cmek_config_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — DataStore without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

Note: The following fields are mutually exclusive: `disable_cmek`, `cmek_config_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`. 



**Returns**

  * (::String) — Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`. 



### #skip_default_schema_creation
    
    
    def skip_default_schema_creation() -> ::Boolean

**Returns**

  * (::Boolean) — A boolean flag indicating whether to skip the default schema creation for the data store. Only enable this flag if you are certain that the default schema is incompatible with your use case.

If set to true, you must manually create a schema for the data store before any documents can be ingested.

This flag cannot be specified if `data_store.starting_schema` is specified. 




### #skip_default_schema_creation=
    
    
    def skip_default_schema_creation=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — A boolean flag indicating whether to skip the default schema creation for the data store. Only enable this flag if you are certain that the default schema is incompatible with your use case.

If set to true, you must manually create a schema for the data store before any documents can be ingested.

This flag cannot be specified if `data_store.starting_schema` is specified. 




**Returns**

  * (::Boolean) — A boolean flag indicating whether to skip the default schema creation for the data store. Only enable this flag if you are certain that the default schema is incompatible with your use case.

If set to true, you must manually create a schema for the data store before any documents can be ingested.

This flag cannot be specified if `data_store.starting_schema` is specified. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
