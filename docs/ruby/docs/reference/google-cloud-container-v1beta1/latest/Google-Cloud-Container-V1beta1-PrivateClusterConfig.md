---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-PrivateClusterConfig/
title: Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::PrivateClusterConfig (v0.57.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:47.726216+00:00
---

# Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::PrivateClusterConfig (v0.57.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-PrivateClusterConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::PrivateClusterConfig (v0.57.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.57.1 (latest)  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.1  0.50.0  0.49.1  0.48.0  0.47.0  0.46.0  0.45.1  0.44.0  0.43.0  0.42.1  0.41.0  0.40.1  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.3  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.3 

Reference documentation and code samples for the Kubernetes Engine V1beta1 API class Google::Cloud::Container::V1beta1::PrivateClusterConfig.

Configuration options for private clusters.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #enable_private_endpoint
    
    
    def enable_private_endpoint() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the master's internal IP address is used as the cluster endpoint. Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.enable_public_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_enable_public_endpoint_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#enable_public_endpoint \(method\)") instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true. 



### #enable_private_endpoint=
    
    
    def enable_private_endpoint=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the master's internal IP address is used as the cluster endpoint. Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.enable_public_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_enable_public_endpoint_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#enable_public_endpoint \(method\)") instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true. 



**Returns**

  * (::Boolean) — Whether the master's internal IP address is used as the cluster endpoint. Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.enable_public_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_enable_public_endpoint_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#enable_public_endpoint \(method\)") instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true. 



### #enable_private_nodes
    
    
    def enable_private_nodes() -> ::Boolean

**Returns**

  * (::Boolean) — Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking.

Deprecated: Use [NetworkConfig.default_enable_private_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NetworkConfig#Google__Cloud__Container__V1beta1__NetworkConfig_default_enable_private_nodes_instance_ "Google::Cloud::Container::V1beta1::NetworkConfig#default_enable_private_nodes \(method\)") instead. 




### #enable_private_nodes=
    
    
    def enable_private_nodes=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking.

Deprecated: Use [NetworkConfig.default_enable_private_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NetworkConfig#Google__Cloud__Container__V1beta1__NetworkConfig_default_enable_private_nodes_instance_ "Google::Cloud::Container::V1beta1::NetworkConfig#default_enable_private_nodes \(method\)") instead. 




**Returns**

  * (::Boolean) — Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking.

Deprecated: Use [NetworkConfig.default_enable_private_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NetworkConfig#Google__Cloud__Container__V1beta1__NetworkConfig_default_enable_private_nodes_instance_ "Google::Cloud::Container::V1beta1::NetworkConfig#default_enable_private_nodes \(method\)") instead. 




### #master_global_access_config
    
    
    def master_global_access_config() -> ::Google::Cloud::Container::V1beta1::PrivateClusterMasterGlobalAccessConfig

**Returns**

  * ([::Google::Cloud::Container::V1beta1::PrivateClusterMasterGlobalAccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-PrivateClusterMasterGlobalAccessConfig)) — Controls master global access settings.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.enable_global_access][] instead. 




### #master_global_access_config=
    
    
    def master_global_access_config=(value) -> ::Google::Cloud::Container::V1beta1::PrivateClusterMasterGlobalAccessConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::PrivateClusterMasterGlobalAccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-PrivateClusterMasterGlobalAccessConfig)) — Controls master global access settings.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.enable_global_access][] instead. 




**Returns**

  * ([::Google::Cloud::Container::V1beta1::PrivateClusterMasterGlobalAccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-PrivateClusterMasterGlobalAccessConfig)) — Controls master global access settings.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.enable_global_access][] instead. 




### #master_ipv4_cidr_block
    
    
    def master_ipv4_cidr_block() -> ::String

**Returns**

  * (::String) — The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network. 



### #master_ipv4_cidr_block=
    
    
    def master_ipv4_cidr_block=(value) -> ::String

**Parameter**

  * **value** (::String) — The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network. 



**Returns**

  * (::String) — The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network. 



### #peering_name
    
    
    def peering_name() -> ::String

**Returns**

  * (::String) — Output only. The peering name in the customer VPC used by this cluster. 



### #private_endpoint
    
    
    def private_endpoint() -> ::String

**Returns**

  * (::String) — Output only. The internal IP address of this cluster's master endpoint.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.private_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_private_endpoint_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#private_endpoint \(method\)") instead. 




### #private_endpoint_subnetwork
    
    
    def private_endpoint_subnetwork() -> ::String

**Returns**

  * (::String) — Subnet to provision the master's private endpoint during cluster creation. Specified in projects/_/regions/_ /subnetworks/* format.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.private_endpoint_subnetwork](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_private_endpoint_subnetwork_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#private_endpoint_subnetwork \(method\)") instead. 




### #private_endpoint_subnetwork=
    
    
    def private_endpoint_subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — Subnet to provision the master's private endpoint during cluster creation. Specified in projects/_/regions/_ /subnetworks/* format.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.private_endpoint_subnetwork](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_private_endpoint_subnetwork_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#private_endpoint_subnetwork \(method\)") instead. 




**Returns**

  * (::String) — Subnet to provision the master's private endpoint during cluster creation. Specified in projects/_/regions/_ /subnetworks/* format.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.private_endpoint_subnetwork](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_private_endpoint_subnetwork_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#private_endpoint_subnetwork \(method\)") instead. 




### #public_endpoint
    
    
    def public_endpoint() -> ::String

**Returns**

  * (::String) — Output only. The external IP address of this cluster's master endpoint.

Deprecated: Use [ControlPlaneEndpointsConfig.IPEndpointsConfig.public_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-ControlPlaneEndpointsConfig-IPEndpointsConfig#Google__Cloud__Container__V1beta1__ControlPlaneEndpointsConfig__IPEndpointsConfig_public_endpoint_instance_ "Google::Cloud::Container::V1beta1::ControlPlaneEndpointsConfig::IPEndpointsConfig#public_endpoint \(method\)") instead. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
