---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig/
title: Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::NodeNetworkConfig (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:01.132414+00:00
---

# Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::NodeNetworkConfig (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::NodeNetworkConfig (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.1  0.33.1  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.3 

Reference documentation and code samples for the Kubernetes Engine V1 API class Google::Cloud::Container::V1::NodeNetworkConfig.

Parameters for node pool-level network config.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #accelerator_network_profile
    
    
    def accelerator_network_profile() -> ::String

**Returns**

  * (::String) — Immutable. The accelerator network profile for the node pool. For now the only valid value is "auto". If specified, the network configuration of the nodes in this node pool will be managed by this profile for the supported machine types, zone, etc. 



### #accelerator_network_profile=
    
    
    def accelerator_network_profile=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The accelerator network profile for the node pool. For now the only valid value is "auto". If specified, the network configuration of the nodes in this node pool will be managed by this profile for the supported machine types, zone, etc. 



**Returns**

  * (::String) — Immutable. The accelerator network profile for the node pool. For now the only valid value is "auto". If specified, the network configuration of the nodes in this node pool will be managed by this profile for the supported machine types, zone, etc. 



### #additional_node_network_configs
    
    
    def additional_node_network_configs() -> ::Array<::Google::Cloud::Container::V1::AdditionalNodeNetworkConfig>

**Returns**

  * (::Array<[::Google::Cloud::Container::V1::AdditionalNodeNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalNodeNetworkConfig)>) — We specify the additional node networks for this node pool using this list. Each node network corresponds to an additional interface 



### #additional_node_network_configs=
    
    
    def additional_node_network_configs=(value) -> ::Array<::Google::Cloud::Container::V1::AdditionalNodeNetworkConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Container::V1::AdditionalNodeNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalNodeNetworkConfig)>) — We specify the additional node networks for this node pool using this list. Each node network corresponds to an additional interface 



**Returns**

  * (::Array<[::Google::Cloud::Container::V1::AdditionalNodeNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalNodeNetworkConfig)>) — We specify the additional node networks for this node pool using this list. Each node network corresponds to an additional interface 



### #additional_pod_network_configs
    
    
    def additional_pod_network_configs() -> ::Array<::Google::Cloud::Container::V1::AdditionalPodNetworkConfig>

**Returns**

  * (::Array<[::Google::Cloud::Container::V1::AdditionalPodNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodNetworkConfig)>) — We specify the additional pod networks for this node pool using this list. Each pod network corresponds to an additional alias IP range for the node 



### #additional_pod_network_configs=
    
    
    def additional_pod_network_configs=(value) -> ::Array<::Google::Cloud::Container::V1::AdditionalPodNetworkConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Container::V1::AdditionalPodNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodNetworkConfig)>) — We specify the additional pod networks for this node pool using this list. Each pod network corresponds to an additional alias IP range for the node 



**Returns**

  * (::Array<[::Google::Cloud::Container::V1::AdditionalPodNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodNetworkConfig)>) — We specify the additional pod networks for this node pool using this list. Each pod network corresponds to an additional alias IP range for the node 



### #create_pod_range
    
    
    def create_pod_range() -> ::Boolean

**Returns**

  * (::Boolean) — Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for `pod_range` and `pod_ipv4_cidr_block` if they are not specified.

If neither `create_pod_range` or `pod_range` are specified, the cluster-level default (`ip_allocation_policy.cluster_ipv4_cidr_block`) is used.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




### #create_pod_range=
    
    
    def create_pod_range=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for `pod_range` and `pod_ipv4_cidr_block` if they are not specified.

If neither `create_pod_range` or `pod_range` are specified, the cluster-level default (`ip_allocation_policy.cluster_ipv4_cidr_block`) is used.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




**Returns**

  * (::Boolean) — Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for `pod_range` and `pod_ipv4_cidr_block` if they are not specified.

If neither `create_pod_range` or `pod_range` are specified, the cluster-level default (`ip_allocation_policy.cluster_ipv4_cidr_block`) is used.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




### #enable_private_nodes
    
    
    def enable_private_nodes() -> ::Boolean

**Returns**

  * (::Boolean) — Whether nodes have internal IP addresses only. If enable_private_nodes is not specified, then the value is derived from [Cluster.NetworkConfig.default_enable_private_nodes][] 



### #enable_private_nodes=
    
    
    def enable_private_nodes=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether nodes have internal IP addresses only. If enable_private_nodes is not specified, then the value is derived from [Cluster.NetworkConfig.default_enable_private_nodes][] 



**Returns**

  * (::Boolean) — Whether nodes have internal IP addresses only. If enable_private_nodes is not specified, then the value is derived from [Cluster.NetworkConfig.default_enable_private_nodes][] 



### #network_performance_config
    
    
    def network_performance_config() -> ::Google::Cloud::Container::V1::NodeNetworkConfig::NetworkPerformanceConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodeNetworkConfig::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig-NetworkPerformanceConfig)) — Network bandwidth tier configuration. 



### #network_performance_config=
    
    
    def network_performance_config=(value) -> ::Google::Cloud::Container::V1::NodeNetworkConfig::NetworkPerformanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeNetworkConfig::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig-NetworkPerformanceConfig)) — Network bandwidth tier configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeNetworkConfig::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig-NetworkPerformanceConfig)) — Network bandwidth tier configuration. 



### #network_tier_config
    
    
    def network_tier_config() -> ::Google::Cloud::Container::V1::NetworkTierConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NetworkTierConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTierConfig)) — Output only. The network tier configuration for the node pool inherits from the cluster-level configuration and remains immutable throughout the node pool's lifecycle, including during upgrades. 



### #pod_cidr_overprovision_config
    
    
    def pod_cidr_overprovision_config() -> ::Google::Cloud::Container::V1::PodCIDROverprovisionConfig

**Returns**

  * ([::Google::Cloud::Container::V1::PodCIDROverprovisionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PodCIDROverprovisionConfig)) — [PRIVATE FIELD] Pod CIDR size overprovisioning config for the node pool.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is rounded off to next power of 2 and we then double that to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled. 




### #pod_cidr_overprovision_config=
    
    
    def pod_cidr_overprovision_config=(value) -> ::Google::Cloud::Container::V1::PodCIDROverprovisionConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::PodCIDROverprovisionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PodCIDROverprovisionConfig)) — [PRIVATE FIELD] Pod CIDR size overprovisioning config for the node pool.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is rounded off to next power of 2 and we then double that to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled. 




**Returns**

  * ([::Google::Cloud::Container::V1::PodCIDROverprovisionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PodCIDROverprovisionConfig)) — [PRIVATE FIELD] Pod CIDR size overprovisioning config for the node pool.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is rounded off to next power of 2 and we then double that to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled. 




### #pod_ipv4_cidr_block
    
    
    def pod_ipv4_cidr_block() -> ::String

**Returns**

  * (::String) — The IP address range for pod IPs in this node pool.

Only applicable if `create_pod_range` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) to pick a specific range to use.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




### #pod_ipv4_cidr_block=
    
    
    def pod_ipv4_cidr_block=(value) -> ::String

**Parameter**

  * **value** (::String) — The IP address range for pod IPs in this node pool.

Only applicable if `create_pod_range` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) to pick a specific range to use.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




**Returns**

  * (::String) — The IP address range for pod IPs in this node pool.

Only applicable if `create_pod_range` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) to pick a specific range to use.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




### #pod_ipv4_range_utilization
    
    
    def pod_ipv4_range_utilization() -> ::Float

**Returns**

  * (::Float) — Output only. The utilization of the IPv4 range for the pod. The ratio is Usage/[Total number of IPs in the secondary range], Usage=numNodes*numZones*podIPsPerNode. 



### #pod_range
    
    
    def pod_range() -> ::String

**Returns**

  * (::String) — The ID of the secondary range for pod IPs. If `create_pod_range` is true, this ID is used for the new range. If `create_pod_range` is false, uses an existing secondary range with this ID.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




### #pod_range=
    
    
    def pod_range=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the secondary range for pod IPs. If `create_pod_range` is true, this ID is used for the new range. If `create_pod_range` is false, uses an existing secondary range with this ID.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




**Returns**

  * (::String) — The ID of the secondary range for pod IPs. If `create_pod_range` is true, this ID is used for the new range. If `create_pod_range` is false, uses an existing secondary range with this ID.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created. 




### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — 

Optional. The subnetwork name/path for the node pool. Format: projects/{project}/regions/{region}/subnetworks/{subnetwork} If the cluster is associated with multiple subnetworks, the subnetwork can be either:

    * A user supplied subnetwork name during node pool creation (e.g., `my-subnet`). The name must be between 1 and 63 characters long, start with a letter, contain only letters, numbers, and hyphens, and end with a letter or a number.
    * A full subnetwork path during node pool creation, such as `projects/gke-project/regions/us-central1/subnetworks/my-subnet`
    * A subnetwork path picked based on the IP utilization during node pool creation and is immutable.



### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The subnetwork name/path for the node pool. Format: projects/{project}/regions/{region}/subnetworks/{subnetwork} If the cluster is associated with multiple subnetworks, the subnetwork can be either:

    * A user supplied subnetwork name during node pool creation (e.g., `my-subnet`). The name must be between 1 and 63 characters long, start with a letter, contain only letters, numbers, and hyphens, and end with a letter or a number.
    * A full subnetwork path during node pool creation, such as `projects/gke-project/regions/us-central1/subnetworks/my-subnet`
    * A subnetwork path picked based on the IP utilization during node pool creation and is immutable.



**Returns**

  * (::String) — 

Optional. The subnetwork name/path for the node pool. Format: projects/{project}/regions/{region}/subnetworks/{subnetwork} If the cluster is associated with multiple subnetworks, the subnetwork can be either:

    * A user supplied subnetwork name during node pool creation (e.g., `my-subnet`). The name must be between 1 and 63 characters long, start with a letter, contain only letters, numbers, and hyphens, and end with a letter or a number.
    * A full subnetwork path during node pool creation, such as `projects/gke-project/regions/us-central1/subnetworks/my-subnet`
    * A subnetwork path picked based on the IP utilization during node pool creation and is immutable.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
