---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IPAllocationPolicyOrBuilder
title: Interface IPAllocationPolicyOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:30.086408+00:00
---

# Interface IPAllocationPolicyOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IPAllocationPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface IPAllocationPolicyOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface IPAllocationPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalIpRangesConfigs(int index)
    
    
    public abstract AdditionalIPRangesConfig getAdditionalIpRangesConfigs(int index)

Output only. The additional IP ranges that are added to the cluster. These IP ranges can be used by new node pools to allocate node and pod IPs automatically. Each AdditionalIPRangesConfig corresponds to a single subnetwork. Once a range is removed it will not show up in IPAllocationPolicy.

` repeated .google.container.v1.AdditionalIPRangesConfig additional_ip_ranges_configs = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdditionalIPRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalIPRangesConfig)` |   
  
### getAdditionalIpRangesConfigsCount()
    
    
    public abstract int getAdditionalIpRangesConfigsCount()

Output only. The additional IP ranges that are added to the cluster. These IP ranges can be used by new node pools to allocate node and pod IPs automatically. Each AdditionalIPRangesConfig corresponds to a single subnetwork. Once a range is removed it will not show up in IPAllocationPolicy.

` repeated .google.container.v1.AdditionalIPRangesConfig additional_ip_ranges_configs = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdditionalIpRangesConfigsList()
    
    
    public abstract List<AdditionalIPRangesConfig> getAdditionalIpRangesConfigsList()

Output only. The additional IP ranges that are added to the cluster. These IP ranges can be used by new node pools to allocate node and pod IPs automatically. Each AdditionalIPRangesConfig corresponds to a single subnetwork. Once a range is removed it will not show up in IPAllocationPolicy.

` repeated .google.container.v1.AdditionalIPRangesConfig additional_ip_ranges_configs = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AdditionalIPRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalIPRangesConfig)>` |   
  
### getAdditionalIpRangesConfigsOrBuilder(int index)
    
    
    public abstract AdditionalIPRangesConfigOrBuilder getAdditionalIpRangesConfigsOrBuilder(int index)

Output only. The additional IP ranges that are added to the cluster. These IP ranges can be used by new node pools to allocate node and pod IPs automatically. Each AdditionalIPRangesConfig corresponds to a single subnetwork. Once a range is removed it will not show up in IPAllocationPolicy.

` repeated .google.container.v1.AdditionalIPRangesConfig additional_ip_ranges_configs = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdditionalIPRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalIPRangesConfigOrBuilder)` |   
  
### getAdditionalIpRangesConfigsOrBuilderList()
    
    
    public abstract List<? extends AdditionalIPRangesConfigOrBuilder> getAdditionalIpRangesConfigsOrBuilderList()

Output only. The additional IP ranges that are added to the cluster. These IP ranges can be used by new node pools to allocate node and pod IPs automatically. Each AdditionalIPRangesConfig corresponds to a single subnetwork. Once a range is removed it will not show up in IPAllocationPolicy.

` repeated .google.container.v1.AdditionalIPRangesConfig additional_ip_ranges_configs = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.AdditionalIPRangesConfigOrBuilder>` |   
  
### getAdditionalPodRangesConfig()
    
    
    public abstract AdditionalPodRangesConfig getAdditionalPodRangesConfig()

Output only. The additional pod ranges that are added to the cluster. These pod ranges can be used by new node pools to allocate pod IPs automatically. Once the range is removed it will not show up in IPAllocationPolicy.

` .google.container.v1.AdditionalPodRangesConfig additional_pod_ranges_config = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalPodRangesConfig)` | The additionalPodRangesConfig.  
  
### getAdditionalPodRangesConfigOrBuilder()
    
    
    public abstract AdditionalPodRangesConfigOrBuilder getAdditionalPodRangesConfigOrBuilder()

Output only. The additional pod ranges that are added to the cluster. These pod ranges can be used by new node pools to allocate pod IPs automatically. Once the range is removed it will not show up in IPAllocationPolicy.

` .google.container.v1.AdditionalPodRangesConfig additional_pod_ranges_config = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalPodRangesConfigOrBuilder)` |   
  
### getAutoIpamConfig()
    
    
    public abstract AutoIpamConfig getAutoIpamConfig()

Optional. AutoIpamConfig contains all information related to Auto IPAM

` .google.container.v1.AutoIpamConfig auto_ipam_config = 30 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoIpamConfig)` | The autoIpamConfig.  
  
### getAutoIpamConfigOrBuilder()
    
    
    public abstract AutoIpamConfigOrBuilder getAutoIpamConfigOrBuilder()

Optional. AutoIpamConfig contains all information related to Auto IPAM

` .google.container.v1.AutoIpamConfig auto_ipam_config = 30 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoIpamConfigOrBuilder)` |   
  
### getClusterIpv4Cidr() (deprecated)
    
    
    public abstract String getClusterIpv4Cidr()

**Deprecated.** _google.container.v1.IPAllocationPolicy.cluster_ipv4_cidr is deprecated. See google/container/v1/cluster_service.proto;l=2720_

This field is deprecated, use cluster_ipv4_cidr_block.

`string cluster_ipv4_cidr = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterIpv4Cidr.  
  
### getClusterIpv4CidrBlock()
    
    
    public abstract String getClusterIpv4CidrBlock()

The IP address range for the cluster pod IPs. If this field is set, then `cluster.cluster_ipv4_cidr` must be left blank.

This field is only applicable when `use_ip_aliases` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

`string cluster_ipv4_cidr_block = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterIpv4CidrBlock.  
  
### getClusterIpv4CidrBlockBytes()
    
    
    public abstract ByteString getClusterIpv4CidrBlockBytes()

The IP address range for the cluster pod IPs. If this field is set, then `cluster.cluster_ipv4_cidr` must be left blank.

This field is only applicable when `use_ip_aliases` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

`string cluster_ipv4_cidr_block = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterIpv4CidrBlock.  
  
### getClusterIpv4CidrBytes() (deprecated)
    
    
    public abstract ByteString getClusterIpv4CidrBytes()

**Deprecated.** _google.container.v1.IPAllocationPolicy.cluster_ipv4_cidr is deprecated. See google/container/v1/cluster_service.proto;l=2720_

This field is deprecated, use cluster_ipv4_cidr_block.

`string cluster_ipv4_cidr = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterIpv4Cidr.  
  
### getClusterSecondaryRangeName()
    
    
    public abstract String getClusterSecondaryRangeName()

The name of the secondary range to be used for the cluster CIDR block. The secondary range will be used for pod IP addresses. This must be an existing secondary range associated with the cluster subnetwork.

This field is only applicable with use_ip_aliases is true and create_subnetwork is false.

`string cluster_secondary_range_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterSecondaryRangeName.  
  
### getClusterSecondaryRangeNameBytes()
    
    
    public abstract ByteString getClusterSecondaryRangeNameBytes()

The name of the secondary range to be used for the cluster CIDR block. The secondary range will be used for pod IP addresses. This must be an existing secondary range associated with the cluster subnetwork.

This field is only applicable with use_ip_aliases is true and create_subnetwork is false.

`string cluster_secondary_range_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterSecondaryRangeName.  
  
### getCreateSubnetwork()
    
    
    public abstract boolean getCreateSubnetwork()

Whether a new subnetwork will be created automatically for the cluster.

This field is only applicable when `use_ip_aliases` is true.

`bool create_subnetwork = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The createSubnetwork.  
  
### getDefaultPodIpv4RangeUtilization()
    
    
    public abstract double getDefaultPodIpv4RangeUtilization()

Output only. The utilization of the cluster default IPv4 range for the pod. The ratio is Usage/[Total number of IPs in the secondary range], Usage=numNodes _numZones_ podIPsPerNode.

` double default_pod_ipv4_range_utilization = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The defaultPodIpv4RangeUtilization.  
  
### getIpv6AccessType()
    
    
    public abstract IPv6AccessType getIpv6AccessType()

The ipv6 access type (internal or external) when create_subnetwork is true

`.google.container.v1.IPv6AccessType ipv6_access_type = 17;`

**Returns**  
---  
**Type** | **Description**  
`[IPv6AccessType](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IPv6AccessType)` | The ipv6AccessType.  
  
### getIpv6AccessTypeValue()
    
    
    public abstract int getIpv6AccessTypeValue()

The ipv6 access type (internal or external) when create_subnetwork is true

`.google.container.v1.IPv6AccessType ipv6_access_type = 17;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for ipv6AccessType.  
  
### getNetworkTierConfig()
    
    
    public abstract NetworkTierConfig getNetworkTierConfig()

Cluster-level network tier configuration is used to determine the default network tier for external IP addresses on cluster resources, such as node pools and load balancers.

`.google.container.v1.NetworkTierConfig network_tier_config = 31;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTierConfig)` | The networkTierConfig.  
  
### getNetworkTierConfigOrBuilder()
    
    
    public abstract NetworkTierConfigOrBuilder getNetworkTierConfigOrBuilder()

Cluster-level network tier configuration is used to determine the default network tier for external IP addresses on cluster resources, such as node pools and load balancers.

`.google.container.v1.NetworkTierConfig network_tier_config = 31;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTierConfigOrBuilder)` |   
  
### getNodeIpv4Cidr() (deprecated)
    
    
    public abstract String getNodeIpv4Cidr()

**Deprecated.** _google.container.v1.IPAllocationPolicy.node_ipv4_cidr is deprecated. See google/container/v1/cluster_service.proto;l=2723_

This field is deprecated, use node_ipv4_cidr_block.

`string node_ipv4_cidr = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodeIpv4Cidr.  
  
### getNodeIpv4CidrBlock()
    
    
    public abstract String getNodeIpv4CidrBlock()

The IP address range of the instance IPs in this cluster.

This is applicable only if `create_subnetwork` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

`string node_ipv4_cidr_block = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodeIpv4CidrBlock.  
  
### getNodeIpv4CidrBlockBytes()
    
    
    public abstract ByteString getNodeIpv4CidrBlockBytes()

The IP address range of the instance IPs in this cluster.

This is applicable only if `create_subnetwork` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

`string node_ipv4_cidr_block = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodeIpv4CidrBlock.  
  
### getNodeIpv4CidrBytes() (deprecated)
    
    
    public abstract ByteString getNodeIpv4CidrBytes()

**Deprecated.** _google.container.v1.IPAllocationPolicy.node_ipv4_cidr is deprecated. See google/container/v1/cluster_service.proto;l=2723_

This field is deprecated, use node_ipv4_cidr_block.

`string node_ipv4_cidr = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodeIpv4Cidr.  
  
### getPodCidrOverprovisionConfig()
    
    
    public abstract PodCIDROverprovisionConfig getPodCidrOverprovisionConfig()

[PRIVATE FIELD] Pod CIDR size overprovisioning config for the cluster.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is doubled and then rounded off to next power of 2 to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled.

`.google.container.v1.PodCIDROverprovisionConfig pod_cidr_overprovision_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[PodCIDROverprovisionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodCIDROverprovisionConfig)` | The podCidrOverprovisionConfig.  
  
### getPodCidrOverprovisionConfigOrBuilder()
    
    
    public abstract PodCIDROverprovisionConfigOrBuilder getPodCidrOverprovisionConfigOrBuilder()

[PRIVATE FIELD] Pod CIDR size overprovisioning config for the cluster.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is doubled and then rounded off to next power of 2 to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled.

`.google.container.v1.PodCIDROverprovisionConfig pod_cidr_overprovision_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[PodCIDROverprovisionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodCIDROverprovisionConfigOrBuilder)` |   
  
### getServicesIpv4Cidr() (deprecated)
    
    
    public abstract String getServicesIpv4Cidr()

**Deprecated.** _google.container.v1.IPAllocationPolicy.services_ipv4_cidr is deprecated. See google/container/v1/cluster_service.proto;l=2726_

This field is deprecated, use services_ipv4_cidr_block.

`string services_ipv4_cidr = 6 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servicesIpv4Cidr.  
  
### getServicesIpv4CidrBlock()
    
    
    public abstract String getServicesIpv4CidrBlock()

The IP address range of the services IPs in this cluster. If blank, a range will be automatically chosen with the default size.

This field is only applicable when `use_ip_aliases` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

`string services_ipv4_cidr_block = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servicesIpv4CidrBlock.  
  
### getServicesIpv4CidrBlockBytes()
    
    
    public abstract ByteString getServicesIpv4CidrBlockBytes()

The IP address range of the services IPs in this cluster. If blank, a range will be automatically chosen with the default size.

This field is only applicable when `use_ip_aliases` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

`string services_ipv4_cidr_block = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servicesIpv4CidrBlock.  
  
### getServicesIpv4CidrBytes() (deprecated)
    
    
    public abstract ByteString getServicesIpv4CidrBytes()

**Deprecated.** _google.container.v1.IPAllocationPolicy.services_ipv4_cidr is deprecated. See google/container/v1/cluster_service.proto;l=2726_

This field is deprecated, use services_ipv4_cidr_block.

`string services_ipv4_cidr = 6 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servicesIpv4Cidr.  
  
### getServicesIpv6CidrBlock()
    
    
    public abstract String getServicesIpv6CidrBlock()

Output only. The services IPv6 CIDR block for the cluster.

`string services_ipv6_cidr_block = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servicesIpv6CidrBlock.  
  
### getServicesIpv6CidrBlockBytes()
    
    
    public abstract ByteString getServicesIpv6CidrBlockBytes()

Output only. The services IPv6 CIDR block for the cluster.

`string services_ipv6_cidr_block = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servicesIpv6CidrBlock.  
  
### getServicesSecondaryRangeName()
    
    
    public abstract String getServicesSecondaryRangeName()

The name of the secondary range to be used as for the services CIDR block. The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork.

This field is only applicable with use_ip_aliases is true and create_subnetwork is false.

`string services_secondary_range_name = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servicesSecondaryRangeName.  
  
### getServicesSecondaryRangeNameBytes()
    
    
    public abstract ByteString getServicesSecondaryRangeNameBytes()

The name of the secondary range to be used as for the services CIDR block. The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork.

This field is only applicable with use_ip_aliases is true and create_subnetwork is false.

`string services_secondary_range_name = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servicesSecondaryRangeName.  
  
### getStackType()
    
    
    public abstract StackType getStackType()

The IP stack type of the cluster

`.google.container.v1.StackType stack_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[StackType](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StackType)` | The stackType.  
  
### getStackTypeValue()
    
    
    public abstract int getStackTypeValue()

The IP stack type of the cluster

`.google.container.v1.StackType stack_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for stackType.  
  
### getSubnetIpv6CidrBlock()
    
    
    public abstract String getSubnetIpv6CidrBlock()

Output only. The subnet's IPv6 CIDR block used by nodes and pods.

`string subnet_ipv6_cidr_block = 22 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetIpv6CidrBlock.  
  
### getSubnetIpv6CidrBlockBytes()
    
    
    public abstract ByteString getSubnetIpv6CidrBlockBytes()

Output only. The subnet's IPv6 CIDR block used by nodes and pods.

`string subnet_ipv6_cidr_block = 22 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetIpv6CidrBlock.  
  
### getSubnetworkName()
    
    
    public abstract String getSubnetworkName()

A custom subnetwork name to be used if `create_subnetwork` is true. If this field is empty, then an automatic name will be chosen for the new subnetwork.

`string subnetwork_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetworkName.  
  
### getSubnetworkNameBytes()
    
    
    public abstract ByteString getSubnetworkNameBytes()

A custom subnetwork name to be used if `create_subnetwork` is true. If this field is empty, then an automatic name will be chosen for the new subnetwork.

`string subnetwork_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetworkName.  
  
### getTpuIpv4CidrBlock() (deprecated)
    
    
    public abstract String getTpuIpv4CidrBlock()

**Deprecated.** _google.container.v1.IPAllocationPolicy.tpu_ipv4_cidr_block is deprecated. See google/container/v1/cluster_service.proto;l=2814_

The IP address range of the Cloud TPUs in this cluster. If unspecified, a range will be automatically chosen with the default size.

This field is only applicable when `use_ip_aliases` is true.

If unspecified, the range will use the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`string tpu_ipv4_cidr_block = 13 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tpuIpv4CidrBlock.  
  
### getTpuIpv4CidrBlockBytes() (deprecated)
    
    
    public abstract ByteString getTpuIpv4CidrBlockBytes()

**Deprecated.** _google.container.v1.IPAllocationPolicy.tpu_ipv4_cidr_block is deprecated. See google/container/v1/cluster_service.proto;l=2814_

The IP address range of the Cloud TPUs in this cluster. If unspecified, a range will be automatically chosen with the default size.

This field is only applicable when `use_ip_aliases` is true.

If unspecified, the range will use the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.

This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`string tpu_ipv4_cidr_block = 13 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tpuIpv4CidrBlock.  
  
### getUseIpAliases()
    
    
    public abstract boolean getUseIpAliases()

Whether alias IPs will be used for pod IPs in the cluster. This is used in conjunction with use_routes. It cannot be true if use_routes is true. If both use_ip_aliases and use_routes are false, then the server picks the default IP allocation mode

`bool use_ip_aliases = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The useIpAliases.  
  
### getUseRoutes()
    
    
    public abstract boolean getUseRoutes()

Whether routes will be used for pod IPs in the cluster. This is used in conjunction with use_ip_aliases. It cannot be true if use_ip_aliases is true. If both use_ip_aliases and use_routes are false, then the server picks the default IP allocation mode

`bool use_routes = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The useRoutes.  
  
### hasAdditionalPodRangesConfig()
    
    
    public abstract boolean hasAdditionalPodRangesConfig()

Output only. The additional pod ranges that are added to the cluster. These pod ranges can be used by new node pools to allocate pod IPs automatically. Once the range is removed it will not show up in IPAllocationPolicy.

` .google.container.v1.AdditionalPodRangesConfig additional_pod_ranges_config = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the additionalPodRangesConfig field is set.  
  
### hasAutoIpamConfig()
    
    
    public abstract boolean hasAutoIpamConfig()

Optional. AutoIpamConfig contains all information related to Auto IPAM

` .google.container.v1.AutoIpamConfig auto_ipam_config = 30 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoIpamConfig field is set.  
  
### hasNetworkTierConfig()
    
    
    public abstract boolean hasNetworkTierConfig()

Cluster-level network tier configuration is used to determine the default network tier for external IP addresses on cluster resources, such as node pools and load balancers.

`.google.container.v1.NetworkTierConfig network_tier_config = 31;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkTierConfig field is set.  
  
### hasPodCidrOverprovisionConfig()
    
    
    public abstract boolean hasPodCidrOverprovisionConfig()

[PRIVATE FIELD] Pod CIDR size overprovisioning config for the cluster.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is doubled and then rounded off to next power of 2 to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled.

`.google.container.v1.PodCIDROverprovisionConfig pod_cidr_overprovision_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the podCidrOverprovisionConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
