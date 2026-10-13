---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendationService-Paths/
title: Discovery Engine V1BETA API - Module Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Paths (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:21.112992+00:00
---

# Discovery Engine V1BETA API - Module Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Paths (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendationService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Module Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Paths (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API module Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Paths.

Path helper methods for the RecommendationService API.

## Extended By

  * [Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendationService-Paths)



## Included In

  * [Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendationService-Client)
  * [Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendationService-Paths)
  * [Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendationService-Rest-Client)



## Methods 

### #data_store_path
    
    
    def data_store_path(project:, location:, data_store:) -> ::String
    def data_store_path(project:, location:, collection:, data_store:) -> ::String

Create a fully-qualified DataStore resource string.

**Overloads**
    
    
    def data_store_path(project:, location:, data_store:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/dataStores/{data_store}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_store** (String) 


    
    
    def data_store_path(project:, location:, collection:, data_store:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **collection** (String) 
  * **data_store** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #document_path
    
    
    def document_path(project:, location:, data_store:, branch:, document:) -> ::String
    def document_path(project:, location:, collection:, data_store:, branch:, document:) -> ::String

Create a fully-qualified Document resource string.

**Overloads**
    
    
    def document_path(project:, location:, data_store:, branch:, document:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_store** (String) 
  * **branch** (String) 
  * **document** (String) 


    
    
    def document_path(project:, location:, collection:, data_store:, branch:, document:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **collection** (String) 
  * **data_store** (String) 
  * **branch** (String) 
  * **document** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #engine_path
    
    
    def engine_path(project:, location:, collection:, engine:) -> ::String

Create a fully-qualified Engine resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **collection** (String) 
  * **engine** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #serving_config_path
    
    
    def serving_config_path(project:, location:, data_store:, serving_config:) -> ::String
    def serving_config_path(project:, location:, collection:, data_store:, serving_config:) -> ::String
    def serving_config_path(project:, location:, collection:, engine:, serving_config:) -> ::String

Create a fully-qualified ServingConfig resource string.

**Overloads**
    
    
    def serving_config_path(project:, location:, data_store:, serving_config:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/dataStores/{data_store}/servingConfigs/{serving_config}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_store** (String) 
  * **serving_config** (String) 


    
    
    def serving_config_path(project:, location:, collection:, data_store:, serving_config:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/servingConfigs/{serving_config}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **collection** (String) 
  * **data_store** (String) 
  * **serving_config** (String) 


    
    
    def serving_config_path(project:, location:, collection:, engine:, serving_config:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/servingConfigs/{serving_config}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **collection** (String) 
  * **engine** (String) 
  * **serving_config** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
