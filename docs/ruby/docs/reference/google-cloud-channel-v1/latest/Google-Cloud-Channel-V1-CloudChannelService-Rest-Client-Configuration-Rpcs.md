---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Rest-Client-Configuration-Rpcs/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Rest::Client::Configuration::Rpcs (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:13.760759+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Rest::Client::Configuration::Rpcs (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Rest::Client::Configuration::Rpcs (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CloudChannelService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the CloudChannelService API.

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

### #activate_entitlement
    
    
    def activate_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `activate_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #cancel_entitlement
    
    
    def cancel_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `cancel_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #change_offer
    
    
    def change_offer() -> ::Gapic::Config::Method

RPC-specific configuration for `change_offer`

**Returns**

  * (::Gapic::Config::Method) 



### #change_parameters
    
    
    def change_parameters() -> ::Gapic::Config::Method

RPC-specific configuration for `change_parameters`

**Returns**

  * (::Gapic::Config::Method) 



### #change_renewal_settings
    
    
    def change_renewal_settings() -> ::Gapic::Config::Method

RPC-specific configuration for `change_renewal_settings`

**Returns**

  * (::Gapic::Config::Method) 



### #check_cloud_identity_accounts_exist
    
    
    def check_cloud_identity_accounts_exist() -> ::Gapic::Config::Method

RPC-specific configuration for `check_cloud_identity_accounts_exist`

**Returns**

  * (::Gapic::Config::Method) 



### #create_channel_partner_link
    
    
    def create_channel_partner_link() -> ::Gapic::Config::Method

RPC-specific configuration for `create_channel_partner_link`

**Returns**

  * (::Gapic::Config::Method) 



### #create_channel_partner_repricing_config
    
    
    def create_channel_partner_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_channel_partner_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_customer
    
    
    def create_customer() -> ::Gapic::Config::Method

RPC-specific configuration for `create_customer`

**Returns**

  * (::Gapic::Config::Method) 



### #create_customer_repricing_config
    
    
    def create_customer_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_customer_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_entitlement
    
    
    def create_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `create_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_channel_partner_repricing_config
    
    
    def delete_channel_partner_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_channel_partner_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_customer
    
    
    def delete_customer() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_customer`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_customer_repricing_config
    
    
    def delete_customer_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_customer_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_channel_partner_link
    
    
    def get_channel_partner_link() -> ::Gapic::Config::Method

RPC-specific configuration for `get_channel_partner_link`

**Returns**

  * (::Gapic::Config::Method) 



### #get_channel_partner_repricing_config
    
    
    def get_channel_partner_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_channel_partner_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_customer
    
    
    def get_customer() -> ::Gapic::Config::Method

RPC-specific configuration for `get_customer`

**Returns**

  * (::Gapic::Config::Method) 



### #get_customer_repricing_config
    
    
    def get_customer_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_customer_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_entitlement
    
    
    def get_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `get_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #import_customer
    
    
    def import_customer() -> ::Gapic::Config::Method

RPC-specific configuration for `import_customer`

**Returns**

  * (::Gapic::Config::Method) 



### #list_channel_partner_links
    
    
    def list_channel_partner_links() -> ::Gapic::Config::Method

RPC-specific configuration for `list_channel_partner_links`

**Returns**

  * (::Gapic::Config::Method) 



### #list_channel_partner_repricing_configs
    
    
    def list_channel_partner_repricing_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_channel_partner_repricing_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_customer_repricing_configs
    
    
    def list_customer_repricing_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_customer_repricing_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_customers
    
    
    def list_customers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_customers`

**Returns**

  * (::Gapic::Config::Method) 



### #list_entitlement_changes
    
    
    def list_entitlement_changes() -> ::Gapic::Config::Method

RPC-specific configuration for `list_entitlement_changes`

**Returns**

  * (::Gapic::Config::Method) 



### #list_entitlements
    
    
    def list_entitlements() -> ::Gapic::Config::Method

RPC-specific configuration for `list_entitlements`

**Returns**

  * (::Gapic::Config::Method) 



### #list_offers
    
    
    def list_offers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_offers`

**Returns**

  * (::Gapic::Config::Method) 



### #list_products
    
    
    def list_products() -> ::Gapic::Config::Method

RPC-specific configuration for `list_products`

**Returns**

  * (::Gapic::Config::Method) 



### #list_purchasable_offers
    
    
    def list_purchasable_offers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_purchasable_offers`

**Returns**

  * (::Gapic::Config::Method) 



### #list_purchasable_skus
    
    
    def list_purchasable_skus() -> ::Gapic::Config::Method

RPC-specific configuration for `list_purchasable_skus`

**Returns**

  * (::Gapic::Config::Method) 



### #list_sku_group_billable_skus
    
    
    def list_sku_group_billable_skus() -> ::Gapic::Config::Method

RPC-specific configuration for `list_sku_group_billable_skus`

**Returns**

  * (::Gapic::Config::Method) 



### #list_sku_groups
    
    
    def list_sku_groups() -> ::Gapic::Config::Method

RPC-specific configuration for `list_sku_groups`

**Returns**

  * (::Gapic::Config::Method) 



### #list_skus
    
    
    def list_skus() -> ::Gapic::Config::Method

RPC-specific configuration for `list_skus`

**Returns**

  * (::Gapic::Config::Method) 



### #list_subscribers
    
    
    def list_subscribers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_subscribers`

**Returns**

  * (::Gapic::Config::Method) 



### #list_transferable_offers
    
    
    def list_transferable_offers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_transferable_offers`

**Returns**

  * (::Gapic::Config::Method) 



### #list_transferable_skus
    
    
    def list_transferable_skus() -> ::Gapic::Config::Method

RPC-specific configuration for `list_transferable_skus`

**Returns**

  * (::Gapic::Config::Method) 



### #lookup_offer
    
    
    def lookup_offer() -> ::Gapic::Config::Method

RPC-specific configuration for `lookup_offer`

**Returns**

  * (::Gapic::Config::Method) 



### #provision_cloud_identity
    
    
    def provision_cloud_identity() -> ::Gapic::Config::Method

RPC-specific configuration for `provision_cloud_identity`

**Returns**

  * (::Gapic::Config::Method) 



### #query_eligible_billing_accounts
    
    
    def query_eligible_billing_accounts() -> ::Gapic::Config::Method

RPC-specific configuration for `query_eligible_billing_accounts`

**Returns**

  * (::Gapic::Config::Method) 



### #register_subscriber
    
    
    def register_subscriber() -> ::Gapic::Config::Method

RPC-specific configuration for `register_subscriber`

**Returns**

  * (::Gapic::Config::Method) 



### #start_paid_service
    
    
    def start_paid_service() -> ::Gapic::Config::Method

RPC-specific configuration for `start_paid_service`

**Returns**

  * (::Gapic::Config::Method) 



### #suspend_entitlement
    
    
    def suspend_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `suspend_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #transfer_entitlements
    
    
    def transfer_entitlements() -> ::Gapic::Config::Method

RPC-specific configuration for `transfer_entitlements`

**Returns**

  * (::Gapic::Config::Method) 



### #transfer_entitlements_to_google
    
    
    def transfer_entitlements_to_google() -> ::Gapic::Config::Method

RPC-specific configuration for `transfer_entitlements_to_google`

**Returns**

  * (::Gapic::Config::Method) 



### #unregister_subscriber
    
    
    def unregister_subscriber() -> ::Gapic::Config::Method

RPC-specific configuration for `unregister_subscriber`

**Returns**

  * (::Gapic::Config::Method) 



### #update_channel_partner_link
    
    
    def update_channel_partner_link() -> ::Gapic::Config::Method

RPC-specific configuration for `update_channel_partner_link`

**Returns**

  * (::Gapic::Config::Method) 



### #update_channel_partner_repricing_config
    
    
    def update_channel_partner_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_channel_partner_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_customer
    
    
    def update_customer() -> ::Gapic::Config::Method

RPC-specific configuration for `update_customer`

**Returns**

  * (::Gapic::Config::Method) 



### #update_customer_repricing_config
    
    
    def update_customer_repricing_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_customer_repricing_config`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
