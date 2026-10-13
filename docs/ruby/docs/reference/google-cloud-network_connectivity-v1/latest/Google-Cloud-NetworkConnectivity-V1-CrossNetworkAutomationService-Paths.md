---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CrossNetworkAutomationService-Paths/
title: Network Connectivity V1 API - Module Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Paths (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:14.546001+00:00
---

# Network Connectivity V1 API - Module Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Paths (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CrossNetworkAutomationService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Module Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Paths (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API module Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Paths.

Path helper methods for the CrossNetworkAutomationService API.

## Extended By

  * [Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CrossNetworkAutomationService-Paths)



## Included In

  * [Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CrossNetworkAutomationService-Client)
  * [Google::Cloud::NetworkConnectivity::V1::CrossNetworkAutomationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CrossNetworkAutomationService-Paths)



## Methods 

### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #network_path
    
    
    def network_path(project:, resource_id:) -> ::String

Create a fully-qualified Network resource string.

The resource will be in the following format:

`projects/{project}/global/networks/{resource_id}`

**Parameters**

  * **project** (String) 
  * **resource_id** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #project_path
    
    
    def project_path(project:) -> ::String

Create a fully-qualified Project resource string.

The resource will be in the following format:

`projects/{project}`

**Parameter**

  * **project** (String) 



**Returns**

  * (::String) 



### #service_attachment_path
    
    
    def service_attachment_path(project:, region:, service_attachment:) -> ::String

Create a fully-qualified ServiceAttachment resource string.

The resource will be in the following format:

`projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`

**Parameters**

  * **project** (String) 
  * **region** (String) 
  * **service_attachment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_class_path
    
    
    def service_class_path(project:, location:, service_class:) -> ::String

Create a fully-qualified ServiceClass resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/serviceClasses/{service_class}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service_class** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_connection_map_path
    
    
    def service_connection_map_path(project:, location:, service_connection_map:) -> ::String

Create a fully-qualified ServiceConnectionMap resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/serviceConnectionMaps/{service_connection_map}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service_connection_map** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_connection_policy_path
    
    
    def service_connection_policy_path(project:, location:, service_connection_policy:) -> ::String

Create a fully-qualified ServiceConnectionPolicy resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/serviceConnectionPolicies/{service_connection_policy}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service_connection_policy** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_connection_token_path
    
    
    def service_connection_token_path(project:, location:, service_connection_token:) -> ::String

Create a fully-qualified ServiceConnectionToken resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/serviceConnectionTokens/{service_connection_token}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service_connection_token** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #subnetwork_path
    
    
    def subnetwork_path(project:, region:, subnetwork:) -> ::String

Create a fully-qualified Subnetwork resource string.

The resource will be in the following format:

`projects/{project}/regions/{region}/subnetworks/{subnetwork}`

**Parameters**

  * **project** (String) 
  * **region** (String) 
  * **subnetwork** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
