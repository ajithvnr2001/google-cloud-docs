---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserStore/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::UserStore (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:55.731880+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::UserStore (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserStore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::UserStore (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::UserStore.

Configures metadata that is used for End User entities.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #default_license_config
    
    
    def default_license_config() -> ::String

**Returns**

  * (::String) — Optional. The default subscription [LicenseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-LicenseConfig "Google::Cloud::DiscoveryEngine::V1beta::LicenseConfig \(class\)") for the UserStore, if [UserStore.enable_license_auto_register](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserStore#Google__Cloud__DiscoveryEngine__V1beta__UserStore_enable_license_auto_register_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserStore#enable_license_auto_register \(method\)") is true, new users will automatically register under the default subscription.

If default [LicenseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-LicenseConfig "Google::Cloud::DiscoveryEngine::V1beta::LicenseConfig \(class\)") doesn't have remaining license seats left, new users will not be assigned with license and will be blocked for Vertex AI Search features. This is used if `license_assignment_tier_rules` is not configured. 




### #default_license_config=
    
    
    def default_license_config=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The default subscription [LicenseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-LicenseConfig "Google::Cloud::DiscoveryEngine::V1beta::LicenseConfig \(class\)") for the UserStore, if [UserStore.enable_license_auto_register](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserStore#Google__Cloud__DiscoveryEngine__V1beta__UserStore_enable_license_auto_register_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserStore#enable_license_auto_register \(method\)") is true, new users will automatically register under the default subscription.

If default [LicenseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-LicenseConfig "Google::Cloud::DiscoveryEngine::V1beta::LicenseConfig \(class\)") doesn't have remaining license seats left, new users will not be assigned with license and will be blocked for Vertex AI Search features. This is used if `license_assignment_tier_rules` is not configured. 




**Returns**

  * (::String) — Optional. The default subscription [LicenseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-LicenseConfig "Google::Cloud::DiscoveryEngine::V1beta::LicenseConfig \(class\)") for the UserStore, if [UserStore.enable_license_auto_register](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserStore#Google__Cloud__DiscoveryEngine__V1beta__UserStore_enable_license_auto_register_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserStore#enable_license_auto_register \(method\)") is true, new users will automatically register under the default subscription.

If default [LicenseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-LicenseConfig "Google::Cloud::DiscoveryEngine::V1beta::LicenseConfig \(class\)") doesn't have remaining license seats left, new users will not be assigned with license and will be blocked for Vertex AI Search features. This is used if `license_assignment_tier_rules` is not configured. 




### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The display name of the User Store. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The display name of the User Store. 



**Returns**

  * (::String) — The display name of the User Store. 



### #enable_expired_license_auto_update
    
    
    def enable_expired_license_auto_update() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to enable license auto update for users in this User Store. If true, users with expired licenses will automatically be updated to use the default license config as long as the default license config has seats left. 



### #enable_expired_license_auto_update=
    
    
    def enable_expired_license_auto_update=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to enable license auto update for users in this User Store. If true, users with expired licenses will automatically be updated to use the default license config as long as the default license config has seats left. 



**Returns**

  * (::Boolean) — Optional. Whether to enable license auto update for users in this User Store. If true, users with expired licenses will automatically be updated to use the default license config as long as the default license config has seats left. 



### #enable_license_auto_register
    
    
    def enable_license_auto_register() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to enable license auto register for users in this User Store. If true, new users will automatically register under the default license config as long as the default license config has seats left. 



### #enable_license_auto_register=
    
    
    def enable_license_auto_register=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to enable license auto register for users in this User Store. If true, new users will automatically register under the default license config as long as the default license config has seats left. 



**Returns**

  * (::Boolean) — Optional. Whether to enable license auto register for users in this User Store. If true, new users will automatically register under the default license config as long as the default license config has seats left. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Immutable. The full resource name of the User Store, in the format of `projects/{project}/locations/{location}/userStores/{user_store}`.

This field must be a UTF-8 encoded string with a length limit of 1024 characters. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The full resource name of the User Store, in the format of `projects/{project}/locations/{location}/userStores/{user_store}`.

This field must be a UTF-8 encoded string with a length limit of 1024 characters. 




**Returns**

  * (::String) — Immutable. The full resource name of the User Store, in the format of `projects/{project}/locations/{location}/userStores/{user_store}`.

This field must be a UTF-8 encoded string with a length limit of 1024 characters. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
