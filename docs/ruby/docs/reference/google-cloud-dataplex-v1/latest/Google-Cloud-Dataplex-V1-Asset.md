---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Asset (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:54.092601+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Asset (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Asset (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::Asset.

An asset represents a cloud resource that is being managed within a lake as a member of a zone.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the asset was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the asset. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the asset. 



**Returns**

  * (::String) — Optional. Description of the asset. 



### #discovery_spec
    
    
    def discovery_spec() -> ::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec)) — Optional. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone. 



### #discovery_spec=
    
    
    def discovery_spec=(value) -> ::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec)) — Optional. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec)) — Optional. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone. 



### #discovery_status
    
    
    def discovery_status() -> ::Google::Cloud::Dataplex::V1::Asset::DiscoveryStatus

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoveryStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoveryStatus)) — Output only. Status of the discovery feature applied to data referenced by this asset. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. User friendly display name. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. User friendly display name. 



**Returns**

  * (::String) — Optional. User friendly display name. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User defined labels for the asset. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User defined labels for the asset. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User defined labels for the asset. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the asset, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`. 



### #resource_spec
    
    
    def resource_spec() -> ::Google::Cloud::Dataplex::V1::Asset::ResourceSpec

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::ResourceSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-ResourceSpec)) — Required. Specification of the resource that is referenced by this asset. 



### #resource_spec=
    
    
    def resource_spec=(value) -> ::Google::Cloud::Dataplex::V1::Asset::ResourceSpec

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Asset::ResourceSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-ResourceSpec)) — Required. Specification of the resource that is referenced by this asset. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::ResourceSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-ResourceSpec)) — Required. Specification of the resource that is referenced by this asset. 



### #resource_status
    
    
    def resource_status() -> ::Google::Cloud::Dataplex::V1::Asset::ResourceStatus

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::ResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-ResourceStatus)) — Output only. Status of the resource referenced by this asset. 



### #security_status
    
    
    def security_status() -> ::Google::Cloud::Dataplex::V1::Asset::SecurityStatus

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::SecurityStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-SecurityStatus)) — Output only. Status of the security policy applied to resource referenced by this asset. 



### #state
    
    
    def state() -> ::Google::Cloud::Dataplex::V1::State

**Returns**

  * ([::Google::Cloud::Dataplex::V1::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-State)) — Output only. Current state of the asset. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the asset was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
