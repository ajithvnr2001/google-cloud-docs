---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-OrganizationSettings-AssetDiscoveryConfig/
title: Cloud Security Command Center V1p1beta1 API - Class Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:30.110638+00:00
---

# Cloud Security Command Center V1p1beta1 API - Class Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-OrganizationSettings-AssetDiscoveryConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Command Center V1p1beta1 API - Class Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.2  0.13.2  0.12.0  0.11.2  0.10.0  0.9.0  0.8.0  0.7.5 

Reference documentation and code samples for the Cloud Security Command Center V1p1beta1 API class Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig.

The configuration used for Asset Discovery runs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #folder_ids
    
    
    def folder_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The folder ids to use for filtering asset discovery. It consists of only digits, e.g., 756619654966. 



### #folder_ids=
    
    
    def folder_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The folder ids to use for filtering asset discovery. It consists of only digits, e.g., 756619654966. 



**Returns**

  * (::Array<::String>) — The folder ids to use for filtering asset discovery. It consists of only digits, e.g., 756619654966. 



### #inclusion_mode
    
    
    def inclusion_mode() -> ::Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig::InclusionMode

**Returns**

  * ([::Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig::InclusionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-OrganizationSettings-AssetDiscoveryConfig-InclusionMode)) — The mode to use for filtering asset discovery. 



### #inclusion_mode=
    
    
    def inclusion_mode=(value) -> ::Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig::InclusionMode

**Parameter**

  * **value** ([::Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig::InclusionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-OrganizationSettings-AssetDiscoveryConfig-InclusionMode)) — The mode to use for filtering asset discovery. 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V1p1beta1::OrganizationSettings::AssetDiscoveryConfig::InclusionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-OrganizationSettings-AssetDiscoveryConfig-InclusionMode)) — The mode to use for filtering asset discovery. 



### #project_ids
    
    
    def project_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The project ids to use for filtering asset discovery. 



### #project_ids=
    
    
    def project_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The project ids to use for filtering asset discovery. 



**Returns**

  * (::Array<::String>) — The project ids to use for filtering asset discovery. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
