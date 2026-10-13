---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Warehouse-Rest-Client-Configuration-Rpcs/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::Warehouse::Rest::Client::Configuration::Rpcs (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:30.253028+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::Warehouse::Rest::Client::Configuration::Rpcs (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Warehouse-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::Warehouse::Rest::Client::Configuration::Rpcs (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::Warehouse::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the Warehouse API.

Includes fields providing the configuration for each RPC in this service. Each configuration object is of type `Gapic::Config::Method` and includes the following configuration fields:

  * `timeout` (_type:_ `Numeric`) - The call timeout in seconds
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers
  * `retry_policy (_type:_`Hash`) - The retry policy. The policy fields include the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



## Inherits

  * Object 



## Methods 

### #add_collection_item
    
    
    def add_collection_item() -> ::Gapic::Config::Method

RPC-specific configuration for `add_collection_item`

**Returns**

  * (::Gapic::Config::Method) 



### #analyze_asset
    
    
    def analyze_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `analyze_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #analyze_corpus
    
    
    def analyze_corpus() -> ::Gapic::Config::Method

RPC-specific configuration for `analyze_corpus`

**Returns**

  * (::Gapic::Config::Method) 



### #clip_asset
    
    
    def clip_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `clip_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #create_annotation
    
    
    def create_annotation() -> ::Gapic::Config::Method

RPC-specific configuration for `create_annotation`

**Returns**

  * (::Gapic::Config::Method) 



### #create_asset
    
    
    def create_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `create_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #create_collection
    
    
    def create_collection() -> ::Gapic::Config::Method

RPC-specific configuration for `create_collection`

**Returns**

  * (::Gapic::Config::Method) 



### #create_corpus
    
    
    def create_corpus() -> ::Gapic::Config::Method

RPC-specific configuration for `create_corpus`

**Returns**

  * (::Gapic::Config::Method) 



### #create_data_schema
    
    
    def create_data_schema() -> ::Gapic::Config::Method

RPC-specific configuration for `create_data_schema`

**Returns**

  * (::Gapic::Config::Method) 



### #create_index
    
    
    def create_index() -> ::Gapic::Config::Method

RPC-specific configuration for `create_index`

**Returns**

  * (::Gapic::Config::Method) 



### #create_index_endpoint
    
    
    def create_index_endpoint() -> ::Gapic::Config::Method

RPC-specific configuration for `create_index_endpoint`

**Returns**

  * (::Gapic::Config::Method) 



### #create_search_config
    
    
    def create_search_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_search_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_search_hypernym
    
    
    def create_search_hypernym() -> ::Gapic::Config::Method

RPC-specific configuration for `create_search_hypernym`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_annotation
    
    
    def delete_annotation() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_annotation`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_asset
    
    
    def delete_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_collection
    
    
    def delete_collection() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_collection`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_corpus
    
    
    def delete_corpus() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_corpus`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_data_schema
    
    
    def delete_data_schema() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_data_schema`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_index
    
    
    def delete_index() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_index`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_index_endpoint
    
    
    def delete_index_endpoint() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_index_endpoint`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_search_config
    
    
    def delete_search_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_search_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_search_hypernym
    
    
    def delete_search_hypernym() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_search_hypernym`

**Returns**

  * (::Gapic::Config::Method) 



### #deploy_index
    
    
    def deploy_index() -> ::Gapic::Config::Method

RPC-specific configuration for `deploy_index`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_hls_uri
    
    
    def generate_hls_uri() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_hls_uri`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_retrieval_url
    
    
    def generate_retrieval_url() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_retrieval_url`

**Returns**

  * (::Gapic::Config::Method) 



### #get_annotation
    
    
    def get_annotation() -> ::Gapic::Config::Method

RPC-specific configuration for `get_annotation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_asset
    
    
    def get_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `get_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #get_collection
    
    
    def get_collection() -> ::Gapic::Config::Method

RPC-specific configuration for `get_collection`

**Returns**

  * (::Gapic::Config::Method) 



### #get_corpus
    
    
    def get_corpus() -> ::Gapic::Config::Method

RPC-specific configuration for `get_corpus`

**Returns**

  * (::Gapic::Config::Method) 



### #get_data_schema
    
    
    def get_data_schema() -> ::Gapic::Config::Method

RPC-specific configuration for `get_data_schema`

**Returns**

  * (::Gapic::Config::Method) 



### #get_index
    
    
    def get_index() -> ::Gapic::Config::Method

RPC-specific configuration for `get_index`

**Returns**

  * (::Gapic::Config::Method) 



### #get_index_endpoint
    
    
    def get_index_endpoint() -> ::Gapic::Config::Method

RPC-specific configuration for `get_index_endpoint`

**Returns**

  * (::Gapic::Config::Method) 



### #get_search_config
    
    
    def get_search_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_search_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_search_hypernym
    
    
    def get_search_hypernym() -> ::Gapic::Config::Method

RPC-specific configuration for `get_search_hypernym`

**Returns**

  * (::Gapic::Config::Method) 



### #import_assets
    
    
    def import_assets() -> ::Gapic::Config::Method

RPC-specific configuration for `import_assets`

**Returns**

  * (::Gapic::Config::Method) 



### #index_asset
    
    
    def index_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `index_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #list_annotations
    
    
    def list_annotations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_annotations`

**Returns**

  * (::Gapic::Config::Method) 



### #list_assets
    
    
    def list_assets() -> ::Gapic::Config::Method

RPC-specific configuration for `list_assets`

**Returns**

  * (::Gapic::Config::Method) 



### #list_collections
    
    
    def list_collections() -> ::Gapic::Config::Method

RPC-specific configuration for `list_collections`

**Returns**

  * (::Gapic::Config::Method) 



### #list_corpora
    
    
    def list_corpora() -> ::Gapic::Config::Method

RPC-specific configuration for `list_corpora`

**Returns**

  * (::Gapic::Config::Method) 



### #list_data_schemas
    
    
    def list_data_schemas() -> ::Gapic::Config::Method

RPC-specific configuration for `list_data_schemas`

**Returns**

  * (::Gapic::Config::Method) 



### #list_index_endpoints
    
    
    def list_index_endpoints() -> ::Gapic::Config::Method

RPC-specific configuration for `list_index_endpoints`

**Returns**

  * (::Gapic::Config::Method) 



### #list_indexes
    
    
    def list_indexes() -> ::Gapic::Config::Method

RPC-specific configuration for `list_indexes`

**Returns**

  * (::Gapic::Config::Method) 



### #list_search_configs
    
    
    def list_search_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_search_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_search_hypernyms
    
    
    def list_search_hypernyms() -> ::Gapic::Config::Method

RPC-specific configuration for `list_search_hypernyms`

**Returns**

  * (::Gapic::Config::Method) 



### #remove_collection_item
    
    
    def remove_collection_item() -> ::Gapic::Config::Method

RPC-specific configuration for `remove_collection_item`

**Returns**

  * (::Gapic::Config::Method) 



### #remove_index_asset
    
    
    def remove_index_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `remove_index_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #search_assets
    
    
    def search_assets() -> ::Gapic::Config::Method

RPC-specific configuration for `search_assets`

**Returns**

  * (::Gapic::Config::Method) 



### #search_index_endpoint
    
    
    def search_index_endpoint() -> ::Gapic::Config::Method

RPC-specific configuration for `search_index_endpoint`

**Returns**

  * (::Gapic::Config::Method) 



### #undeploy_index
    
    
    def undeploy_index() -> ::Gapic::Config::Method

RPC-specific configuration for `undeploy_index`

**Returns**

  * (::Gapic::Config::Method) 



### #update_annotation
    
    
    def update_annotation() -> ::Gapic::Config::Method

RPC-specific configuration for `update_annotation`

**Returns**

  * (::Gapic::Config::Method) 



### #update_asset
    
    
    def update_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `update_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #update_collection
    
    
    def update_collection() -> ::Gapic::Config::Method

RPC-specific configuration for `update_collection`

**Returns**

  * (::Gapic::Config::Method) 



### #update_corpus
    
    
    def update_corpus() -> ::Gapic::Config::Method

RPC-specific configuration for `update_corpus`

**Returns**

  * (::Gapic::Config::Method) 



### #update_data_schema
    
    
    def update_data_schema() -> ::Gapic::Config::Method

RPC-specific configuration for `update_data_schema`

**Returns**

  * (::Gapic::Config::Method) 



### #update_index
    
    
    def update_index() -> ::Gapic::Config::Method

RPC-specific configuration for `update_index`

**Returns**

  * (::Gapic::Config::Method) 



### #update_index_endpoint
    
    
    def update_index_endpoint() -> ::Gapic::Config::Method

RPC-specific configuration for `update_index_endpoint`

**Returns**

  * (::Gapic::Config::Method) 



### #update_search_config
    
    
    def update_search_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_search_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_search_hypernym
    
    
    def update_search_hypernym() -> ::Gapic::Config::Method

RPC-specific configuration for `update_search_hypernym`

**Returns**

  * (::Gapic::Config::Method) 



### #upload_asset
    
    
    def upload_asset() -> ::Gapic::Config::Method

RPC-specific configuration for `upload_asset`

**Returns**

  * (::Gapic::Config::Method) 



### #view_collection_items
    
    
    def view_collection_items() -> ::Gapic::Config::Method

RPC-specific configuration for `view_collection_items`

**Returns**

  * (::Gapic::Config::Method) 



### #view_indexed_assets
    
    
    def view_indexed_assets() -> ::Gapic::Config::Method

RPC-specific configuration for `view_indexed_assets`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
