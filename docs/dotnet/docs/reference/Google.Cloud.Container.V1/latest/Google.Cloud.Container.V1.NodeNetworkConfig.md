---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig
title: Google Kubernetes Engine v1 API - Class NodeNetworkConfig (3.40.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:57.569195+00:00
---

# Google Kubernetes Engine v1 API - Class NodeNetworkConfig (3.40.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Kubernetes Engine v1 API - Class NodeNetworkConfig (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class NodeNetworkConfig : IMessage<NodeNetworkConfig>, IEquatable<NodeNetworkConfig>, IDeepCloneable<NodeNetworkConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Kubernetes Engine v1 API class NodeNetworkConfig.

Parameters for node pool-level network config.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > NodeNetworkConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[NodeNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[NodeNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[NodeNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Container.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1)

## Assembly

Google.Cloud.Container.V1.dll

## Constructors 

### NodeNetworkConfig()
    
    
    public NodeNetworkConfig()

### NodeNetworkConfig(NodeNetworkConfig)
    
    
    public NodeNetworkConfig(NodeNetworkConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[NodeNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig)`  
  
  
## Properties 

### AcceleratorNetworkProfile
    
    
    public string AcceleratorNetworkProfile { get; set; }

Immutable. The accelerator network profile for the node pool. For now the only valid value is "auto". If specified, the network configuration of the nodes in this node pool will be managed by this profile for the supported machine types, zone, etc.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AdditionalNodeNetworkConfigs
    
    
    public RepeatedField<AdditionalNodeNetworkConfig> AdditionalNodeNetworkConfigs { get; }

We specify the additional node networks for this node pool using this list. Each node network corresponds to an additional interface

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdditionalNodeNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.AdditionalNodeNetworkConfig)` |   
  
### AdditionalPodNetworkConfigs
    
    
    public RepeatedField<AdditionalPodNetworkConfig> AdditionalPodNetworkConfigs { get; }

We specify the additional pod networks for this node pool using this list. Each pod network corresponds to an additional alias IP range for the node

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdditionalPodNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.AdditionalPodNetworkConfig)` |   
  
### CreatePodRange
    
    
    public bool CreatePodRange { get; set; }

Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for `pod_range` and `pod_ipv4_cidr_block` if they are not specified.

If neither `create_pod_range` or `pod_range` are specified, the cluster-level default (`ip_allocation_policy.cluster_ipv4_cidr_block`) is used.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnablePrivateNodes
    
    
    public bool EnablePrivateNodes { get; set; }

Whether nodes have internal IP addresses only. If enable_private_nodes is not specified, then the value is derived from [Cluster.NetworkConfig.default_enable_private_nodes][]

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEnablePrivateNodes
    
    
    public bool HasEnablePrivateNodes { get; }

Gets whether the "enable_private_nodes" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NetworkPerformanceConfig
    
    
    public NodeNetworkConfig.Types.NetworkPerformanceConfig NetworkPerformanceConfig { get; set; }

Network bandwidth tier configuration.

**Property Value**  
---  
**Type** | **Description**  
`[NodeNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig.Types)[NetworkPerformanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig.Types.NetworkPerformanceConfig)` |   
  
### NetworkTierConfig
    
    
    public NetworkTierConfig NetworkTierConfig { get; set; }

Output only. The network tier configuration for the node pool inherits from the cluster-level configuration and remains immutable throughout the node pool's lifecycle, including during upgrades.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkTierConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NetworkTierConfig)` |   
  
### PodCidrOverprovisionConfig
    
    
    public PodCIDROverprovisionConfig PodCidrOverprovisionConfig { get; set; }

[PRIVATE FIELD] Pod CIDR size overprovisioning config for the node pool.

Pod CIDR size per node depends on max_pods_per_node. By default, the value of max_pods_per_node is rounded off to next power of 2 and we then double that to get the size of pod CIDR block per node. Example: max_pods_per_node of 30 would result in 64 IPs (/26).

This config can disable the doubling of IPs (we still round off to next power of 2) Example: max_pods_per_node of 30 will result in 32 IPs (/27) when overprovisioning is disabled.

**Property Value**  
---  
**Type** | **Description**  
`[PodCIDROverprovisionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.PodCIDROverprovisionConfig)` |   
  
### PodIpv4CidrBlock
    
    
    public string PodIpv4CidrBlock { get; set; }

The IP address range for pod IPs in this node pool.

Only applicable if `create_pod_range` is true.

Set to blank to have a range chosen with the default size.

Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.

Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) to pick a specific range to use.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PodIpv4RangeUtilization
    
    
    public double PodIpv4RangeUtilization { get; set; }

Output only. The utilization of the IPv4 range for the pod. The ratio is Usage/[Total number of IPs in the secondary range], Usage=numNodes _numZones_ podIPsPerNode.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### PodRange
    
    
    public string PodRange { get; set; }

The ID of the secondary range for pod IPs. If `create_pod_range` is true, this ID is used for the new range. If `create_pod_range` is false, uses an existing secondary range with this ID.

Only applicable if `ip_allocation_policy.use_ip_aliases` is true.

This field cannot be changed after the node pool has been created.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Subnetwork
    
    
    public string Subnetwork { get; set; }

Optional. The subnetwork name/path for the node pool. Format: projects/{project}/regions/{region}/subnetworks/{subnetwork} If the cluster is associated with multiple subnetworks, the subnetwork can be either:

  * A user supplied subnetwork name during node pool creation (e.g., `my-subnet`). The name must be between 1 and 63 characters long, start with a letter, contain only letters, numbers, and hyphens, and end with a letter or a number.
  * A full subnetwork path during node pool creation, such as `projects/gke-project/regions/us-central1/subnetworks/my-subnet`
  * A subnetwork path picked based on the IP utilization during node pool creation and is immutable.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubnetworkAsSubnetworkName
    
    
    public SubnetworkName SubnetworkAsSubnetworkName { get; set; }

[SubnetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SubnetworkName)-typed view over the [Subnetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodeNetworkConfig#Google_Cloud_Container_V1_NodeNetworkConfig_Subnetwork) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SubnetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SubnetworkName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
