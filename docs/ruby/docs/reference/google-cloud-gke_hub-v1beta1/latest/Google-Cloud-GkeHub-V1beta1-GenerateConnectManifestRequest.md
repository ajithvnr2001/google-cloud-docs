---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-GenerateConnectManifestRequest/
title: GKE Hub V1beta1 API - Class Google::Cloud::GkeHub::V1beta1::GenerateConnectManifestRequest (v0.21.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:06.842675+00:00
---

# GKE Hub V1beta1 API - Class Google::Cloud::GkeHub::V1beta1::GenerateConnectManifestRequest (v0.21.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-GenerateConnectManifestRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GKE Hub V1beta1 API - Class Google::Cloud::GkeHub::V1beta1::GenerateConnectManifestRequest (v0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.20.1  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the GKE Hub V1beta1 API class Google::Cloud::GkeHub::V1beta1::GenerateConnectManifestRequest.

Request message for `GkeHubMembershipService.GenerateConnectManifest` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #connect_agent
    
    
    def connect_agent() -> ::Google::Cloud::GkeHub::V1beta1::ConnectAgent

**Returns**

  * ([::Google::Cloud::GkeHub::V1beta1::ConnectAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-ConnectAgent)) — Optional. The connect agent to generate manifest for. 



### #connect_agent=
    
    
    def connect_agent=(value) -> ::Google::Cloud::GkeHub::V1beta1::ConnectAgent

**Parameter**

  * **value** ([::Google::Cloud::GkeHub::V1beta1::ConnectAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-ConnectAgent)) — Optional. The connect agent to generate manifest for. 



**Returns**

  * ([::Google::Cloud::GkeHub::V1beta1::ConnectAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-ConnectAgent)) — Optional. The connect agent to generate manifest for. 



### #image_pull_secret_content
    
    
    def image_pull_secret_content() -> ::String

**Returns**

  * (::String) — Optional. The image pull secret content for the registry, if not public. 



### #image_pull_secret_content=
    
    
    def image_pull_secret_content=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The image pull secret content for the registry, if not public. 



**Returns**

  * (::String) — Optional. The image pull secret content for the registry, if not public. 



### #is_upgrade
    
    
    def is_upgrade() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If true, generate the resources for upgrade only. Some resources generated only for installation (e.g. secrets) will be excluded. 



### #is_upgrade=
    
    
    def is_upgrade=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If true, generate the resources for upgrade only. Some resources generated only for installation (e.g. secrets) will be excluded. 



**Returns**

  * (::Boolean) — Optional. If true, generate the resources for upgrade only. Some resources generated only for installation (e.g. secrets) will be excluded. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The Membership resource name the Agent will associate with, in the format `projects/*/locations/*/memberships/*`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The Membership resource name the Agent will associate with, in the format `projects/*/locations/*/memberships/*`. 



**Returns**

  * (::String) — Required. The Membership resource name the Agent will associate with, in the format `projects/*/locations/*/memberships/*`. 



### #registry
    
    
    def registry() -> ::String

**Returns**

  * (::String) — Optional. The registry to fetch the connect agent image from. Defaults to gcr.io/gkeconnect. 



### #registry=
    
    
    def registry=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The registry to fetch the connect agent image from. Defaults to gcr.io/gkeconnect. 



**Returns**

  * (::String) — Optional. The registry to fetch the connect agent image from. Defaults to gcr.io/gkeconnect. 



### #version
    
    
    def version() -> ::String

**Returns**

  * (::String) — Optional. The Connect agent version to use. Defaults to the most current version. 



### #version=
    
    
    def version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Connect agent version to use. Defaults to the most current version. 



**Returns**

  * (::String) — Optional. The Connect agent version to use. Defaults to the most current version. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
