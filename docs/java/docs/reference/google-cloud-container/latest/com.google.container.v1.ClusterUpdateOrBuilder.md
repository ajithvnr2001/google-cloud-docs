---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpdateOrBuilder
title: Interface ClusterUpdateOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:06.664535+00:00
---

# Interface ClusterUpdateOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpdateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClusterUpdateOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface ClusterUpdateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalPodRangesConfig()
    
    
    public abstract AdditionalPodRangesConfig getAdditionalPodRangesConfig()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1.AdditionalPodRangesConfig additional_pod_ranges_config = 120;`

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalPodRangesConfig)` | The additionalPodRangesConfig.  
  
### getAdditionalPodRangesConfigOrBuilder()
    
    
    public abstract AdditionalPodRangesConfigOrBuilder getAdditionalPodRangesConfigOrBuilder()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1.AdditionalPodRangesConfig additional_pod_ranges_config = 120;`

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalPodRangesConfigOrBuilder)` |   
  
### getDesiredAdditionalIpRangesConfig()
    
    
    public abstract DesiredAdditionalIPRangesConfig getDesiredAdditionalIpRangesConfig()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DesiredAdditionalIPRangesConfig)` | The desiredAdditionalIpRangesConfig.  
  
### getDesiredAdditionalIpRangesConfigOrBuilder()
    
    
    public abstract DesiredAdditionalIPRangesConfigOrBuilder getDesiredAdditionalIpRangesConfigOrBuilder()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredAdditionalIPRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DesiredAdditionalIPRangesConfigOrBuilder)` |   
  
### getDesiredAddonsConfig()
    
    
    public abstract AddonsConfig getDesiredAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfig)` | The desiredAddonsConfig.  
  
### getDesiredAddonsConfigOrBuilder()
    
    
    public abstract AddonsConfigOrBuilder getDesiredAddonsConfigOrBuilder()

Configurations for the various addons available to run in the cluster.

`.google.container.v1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfigOrBuilder)` |   
  
### getDesiredAnonymousAuthenticationConfig()
    
    
    public abstract AnonymousAuthenticationConfig getDesiredAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AnonymousAuthenticationConfig)` | The desiredAnonymousAuthenticationConfig.  
  
### getDesiredAnonymousAuthenticationConfigOrBuilder()
    
    
    public abstract AnonymousAuthenticationConfigOrBuilder getDesiredAnonymousAuthenticationConfigOrBuilder()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AnonymousAuthenticationConfigOrBuilder)` |   
  
### getDesiredAuthenticatorGroupsConfig()
    
    
    public abstract AuthenticatorGroupsConfig getDesiredAuthenticatorGroupsConfig()

The desired authenticator groups config for the cluster.

`.google.container.v1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AuthenticatorGroupsConfig)` | The desiredAuthenticatorGroupsConfig.  
  
### getDesiredAuthenticatorGroupsConfigOrBuilder()
    
    
    public abstract AuthenticatorGroupsConfigOrBuilder getDesiredAuthenticatorGroupsConfigOrBuilder()

The desired authenticator groups config for the cluster.

`.google.container.v1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AuthenticatorGroupsConfigOrBuilder)` |   
  
### getDesiredAutoIpamConfig()
    
    
    public abstract AutoIpamConfig getDesiredAutoIpamConfig()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoIpamConfig)` | The desiredAutoIpamConfig.  
  
### getDesiredAutoIpamConfigOrBuilder()
    
    
    public abstract AutoIpamConfigOrBuilder getDesiredAutoIpamConfigOrBuilder()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoIpamConfigOrBuilder)` |   
  
### getDesiredAutopilotClusterPolicyConfig()
    
    
    public abstract ClusterPolicyConfig getDesiredAutopilotClusterPolicyConfig()

The desired autopilot cluster policies that to be enforced in the cluster.

`.google.container.v1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterPolicyConfig)` | The desiredAutopilotClusterPolicyConfig.  
  
### getDesiredAutopilotClusterPolicyConfigOrBuilder()
    
    
    public abstract ClusterPolicyConfigOrBuilder getDesiredAutopilotClusterPolicyConfigOrBuilder()

The desired autopilot cluster policies that to be enforced in the cluster.

`.google.container.v1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPolicyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterPolicyConfigOrBuilder)` |   
  
### getDesiredAutopilotWorkloadPolicyConfig()
    
    
    public abstract WorkloadPolicyConfig getDesiredAutopilotWorkloadPolicyConfig()

WorkloadPolicyConfig is the configuration related to GCW workload policy

`.google.container.v1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.WorkloadPolicyConfig)` | The desiredAutopilotWorkloadPolicyConfig.  
  
### getDesiredAutopilotWorkloadPolicyConfigOrBuilder()
    
    
    public abstract WorkloadPolicyConfigOrBuilder getDesiredAutopilotWorkloadPolicyConfigOrBuilder()

WorkloadPolicyConfig is the configuration related to GCW workload policy

`.google.container.v1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadPolicyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.WorkloadPolicyConfigOrBuilder)` |   
  
### getDesiredBinaryAuthorization()
    
    
    public abstract BinaryAuthorization getDesiredBinaryAuthorization()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.BinaryAuthorization)` | The desiredBinaryAuthorization.  
  
### getDesiredBinaryAuthorizationOrBuilder()
    
    
    public abstract BinaryAuthorizationOrBuilder getDesiredBinaryAuthorizationOrBuilder()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorizationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.BinaryAuthorizationOrBuilder)` |   
  
### getDesiredClusterAutoscaling()
    
    
    public abstract ClusterAutoscaling getDesiredClusterAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscaling)` | The desiredClusterAutoscaling.  
  
### getDesiredClusterAutoscalingOrBuilder()
    
    
    public abstract ClusterAutoscalingOrBuilder getDesiredClusterAutoscalingOrBuilder()

Cluster-level autoscaling configuration.

`.google.container.v1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscalingOrBuilder)` |   
  
### getDesiredCompliancePostureConfig() (deprecated)
    
    
    public abstract CompliancePostureConfig getDesiredCompliancePostureConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_compliance_posture_config is deprecated. See google/container/v1/cluster_service.proto;l=3892_

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompliancePostureConfig)` | The desiredCompliancePostureConfig.  
  
### getDesiredCompliancePostureConfigOrBuilder() (deprecated)
    
    
    public abstract CompliancePostureConfigOrBuilder getDesiredCompliancePostureConfigOrBuilder()

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompliancePostureConfigOrBuilder)` |   
  
### getDesiredContainerdConfig()
    
    
    public abstract ContainerdConfig getDesiredContainerdConfig()

The desired containerd config for the cluster.

`.google.container.v1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig)` | The desiredContainerdConfig.  
  
### getDesiredContainerdConfigOrBuilder()
    
    
    public abstract ContainerdConfigOrBuilder getDesiredContainerdConfigOrBuilder()

The desired containerd config for the cluster.

`.google.container.v1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfigOrBuilder)` |   
  
### getDesiredControlPlaneEgress()
    
    
    public abstract ControlPlaneEgress getDesiredControlPlaneEgress()

The desired control plane egress control config for the cluster.

`.google.container.v1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEgress)` | The desiredControlPlaneEgress.  
  
### getDesiredControlPlaneEgressOrBuilder()
    
    
    public abstract ControlPlaneEgressOrBuilder getDesiredControlPlaneEgressOrBuilder()

The desired control plane egress control config for the cluster.

`.google.container.v1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEgressOrBuilder)` |   
  
### getDesiredControlPlaneEndpointsConfig()
    
    
    public abstract ControlPlaneEndpointsConfig getDesiredControlPlaneEndpointsConfig()

Control plane endpoints configuration.

` .google.container.v1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEndpointsConfig)` | The desiredControlPlaneEndpointsConfig.  
  
### getDesiredControlPlaneEndpointsConfigOrBuilder()
    
    
    public abstract ControlPlaneEndpointsConfigOrBuilder getDesiredControlPlaneEndpointsConfigOrBuilder()

Control plane endpoints configuration.

` .google.container.v1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEndpointsConfigOrBuilder)` |   
  
### getDesiredCostManagementConfig()
    
    
    public abstract CostManagementConfig getDesiredCostManagementConfig()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1.CostManagementConfig desired_cost_management_config = 49;`

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CostManagementConfig)` | The desiredCostManagementConfig.  
  
### getDesiredCostManagementConfigOrBuilder()
    
    
    public abstract CostManagementConfigOrBuilder getDesiredCostManagementConfigOrBuilder()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1.CostManagementConfig desired_cost_management_config = 49;`

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CostManagementConfigOrBuilder)` |   
  
### getDesiredDatabaseEncryption()
    
    
    public abstract DatabaseEncryption getDesiredDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption)` | The desiredDatabaseEncryption.  
  
### getDesiredDatabaseEncryptionOrBuilder()
    
    
    public abstract DatabaseEncryptionOrBuilder getDesiredDatabaseEncryptionOrBuilder()

Configuration of etcd encryption.

`.google.container.v1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryptionOrBuilder)` |   
  
### getDesiredDatapathProvider()
    
    
    public abstract DatapathProvider getDesiredDatapathProvider()

The desired datapath provider for the cluster.

`.google.container.v1.DatapathProvider desired_datapath_provider = 50;`

**Returns**  
---  
**Type** | **Description**  
`[DatapathProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatapathProvider)` | The desiredDatapathProvider.  
  
### getDesiredDatapathProviderValue()
    
    
    public abstract int getDesiredDatapathProviderValue()

The desired datapath provider for the cluster.

`.google.container.v1.DatapathProvider desired_datapath_provider = 50;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredDatapathProvider.  
  
### getDesiredDefaultEnablePrivateNodes()
    
    
    public abstract boolean getDesiredDefaultEnablePrivateNodes()

Override the default setting of whether future created nodes have private IP addresses only, namely NetworkConfig.default_enable_private_nodes

`optional bool desired_default_enable_private_nodes = 72;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredDefaultEnablePrivateNodes.  
  
### getDesiredDefaultSnatStatus()
    
    
    public abstract DefaultSnatStatus getDesiredDefaultSnatStatus()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultSnatStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DefaultSnatStatus)` | The desiredDefaultSnatStatus.  
  
### getDesiredDefaultSnatStatusOrBuilder()
    
    
    public abstract DefaultSnatStatusOrBuilder getDesiredDefaultSnatStatusOrBuilder()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultSnatStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DefaultSnatStatusOrBuilder)` |   
  
### getDesiredDisableL4LbFirewallReconciliation()
    
    
    public abstract boolean getDesiredDisableL4LbFirewallReconciliation()

Enable/Disable L4 LB VPC firewall reconciliation for the cluster.

`optional bool desired_disable_l4_lb_firewall_reconciliation = 149;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredDisableL4LbFirewallReconciliation.  
  
### getDesiredDnsConfig()
    
    
    public abstract DNSConfig getDesiredDnsConfig()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[DNSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DNSConfig)` | The desiredDnsConfig.  
  
### getDesiredDnsConfigOrBuilder()
    
    
    public abstract DNSConfigOrBuilder getDesiredDnsConfigOrBuilder()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[DNSConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DNSConfigOrBuilder)` |   
  
### getDesiredEmulatedVersion()
    
    
    public abstract String getDesiredEmulatedVersion()

Optional. The desired emulated version for the cluster.

`optional string desired_emulated_version = 182 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredEmulatedVersion.  
  
### getDesiredEmulatedVersionBytes()
    
    
    public abstract ByteString getDesiredEmulatedVersionBytes()

Optional. The desired emulated version for the cluster.

`optional string desired_emulated_version = 182 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredEmulatedVersion.  
  
### getDesiredEnableCiliumClusterwideNetworkPolicy()
    
    
    public abstract boolean getDesiredEnableCiliumClusterwideNetworkPolicy()

Enable/Disable Cilium Clusterwide Network Policy for the cluster.

`optional bool desired_enable_cilium_clusterwide_network_policy = 138;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnableCiliumClusterwideNetworkPolicy.  
  
### getDesiredEnableFqdnNetworkPolicy()
    
    
    public abstract boolean getDesiredEnableFqdnNetworkPolicy()

Enable/Disable FQDN Network Policy for the cluster.

`optional bool desired_enable_fqdn_network_policy = 126;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnableFqdnNetworkPolicy.  
  
### getDesiredEnableMultiNetworking()
    
    
    public abstract boolean getDesiredEnableMultiNetworking()

Enable/Disable Multi-Networking for the cluster

`optional bool desired_enable_multi_networking = 135;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnableMultiNetworking.  
  
### getDesiredEnablePrivateEndpoint() (deprecated)
    
    
    public abstract boolean getDesiredEnablePrivateEndpoint()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_enable_private_endpoint is deprecated. See google/container/v1/cluster_service.proto;l=3787_

Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true.

`optional bool desired_enable_private_endpoint = 71 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnablePrivateEndpoint.  
  
### getDesiredEnterpriseConfig() (deprecated)
    
    
    public abstract DesiredEnterpriseConfig getDesiredEnterpriseConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_enterprise_config is deprecated. See google/container/v1/cluster_service.proto;l=3921_

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredEnterpriseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DesiredEnterpriseConfig)` | The desiredEnterpriseConfig.  
  
### getDesiredEnterpriseConfigOrBuilder() (deprecated)
    
    
    public abstract DesiredEnterpriseConfigOrBuilder getDesiredEnterpriseConfigOrBuilder()

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredEnterpriseConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DesiredEnterpriseConfigOrBuilder)` |   
  
### getDesiredFleet()
    
    
    public abstract Fleet getDesiredFleet()

The desired fleet configuration for the cluster.

`.google.container.v1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Fleet)` | The desiredFleet.  
  
### getDesiredFleetOrBuilder()
    
    
    public abstract FleetOrBuilder getDesiredFleetOrBuilder()

The desired fleet configuration for the cluster.

`.google.container.v1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[FleetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FleetOrBuilder)` |   
  
### getDesiredGatewayApiConfig()
    
    
    public abstract GatewayAPIConfig getDesiredGatewayApiConfig()

The desired config of Gateway API on this cluster.

`.google.container.v1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[GatewayAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GatewayAPIConfig)` | The desiredGatewayApiConfig.  
  
### getDesiredGatewayApiConfigOrBuilder()
    
    
    public abstract GatewayAPIConfigOrBuilder getDesiredGatewayApiConfigOrBuilder()

The desired config of Gateway API on this cluster.

`.google.container.v1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[GatewayAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GatewayAPIConfigOrBuilder)` |   
  
### getDesiredGcfsConfig()
    
    
    public abstract GcfsConfig getDesiredGcfsConfig()

The desired GCFS config for the cluster

`.google.container.v1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcfsConfig)` | The desiredGcfsConfig.  
  
### getDesiredGcfsConfigOrBuilder()
    
    
    public abstract GcfsConfigOrBuilder getDesiredGcfsConfigOrBuilder()

The desired GCFS config for the cluster

`.google.container.v1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcfsConfigOrBuilder)` |   
  
### getDesiredIdentityServiceConfig()
    
    
    public abstract IdentityServiceConfig getDesiredIdentityServiceConfig()

The desired Identity Service component configuration.

`.google.container.v1.IdentityServiceConfig desired_identity_service_config = 66;`

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IdentityServiceConfig)` | The desiredIdentityServiceConfig.  
  
### getDesiredIdentityServiceConfigOrBuilder()
    
    
    public abstract IdentityServiceConfigOrBuilder getDesiredIdentityServiceConfigOrBuilder()

The desired Identity Service component configuration.

`.google.container.v1.IdentityServiceConfig desired_identity_service_config = 66;`

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IdentityServiceConfigOrBuilder)` |   
  
### getDesiredImage()
    
    
    public abstract String getDesiredImage()

The desired name of the image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well.

`string desired_image = 44;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredImage.  
  
### getDesiredImageBytes()
    
    
    public abstract ByteString getDesiredImageBytes()

The desired name of the image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well.

`string desired_image = 44;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredImage.  
  
### getDesiredImageProject()
    
    
    public abstract String getDesiredImageProject()

The project containing the desired image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_project = 45;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredImageProject.  
  
### getDesiredImageProjectBytes()
    
    
    public abstract ByteString getDesiredImageProjectBytes()

The project containing the desired image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_project = 45;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredImageProject.  
  
### getDesiredImageType()
    
    
    public abstract String getDesiredImageType()

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredImageType.  
  
### getDesiredImageTypeBytes()
    
    
    public abstract ByteString getDesiredImageTypeBytes()

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredImageType.  
  
### getDesiredInTransitEncryptionConfig()
    
    
    public abstract InTransitEncryptionConfig getDesiredInTransitEncryptionConfig()

Specify the details of in-transit encryption.

` optional .google.container.v1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[InTransitEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.InTransitEncryptionConfig)` | The desiredInTransitEncryptionConfig.  
  
### getDesiredInTransitEncryptionConfigValue()
    
    
    public abstract int getDesiredInTransitEncryptionConfigValue()

Specify the details of in-transit encryption.

` optional .google.container.v1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredInTransitEncryptionConfig.  
  
### getDesiredIntraNodeVisibilityConfig()
    
    
    public abstract IntraNodeVisibilityConfig getDesiredIntraNodeVisibilityConfig()

The desired config of Intra-node visibility.

`.google.container.v1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[IntraNodeVisibilityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IntraNodeVisibilityConfig)` | The desiredIntraNodeVisibilityConfig.  
  
### getDesiredIntraNodeVisibilityConfigOrBuilder()
    
    
    public abstract IntraNodeVisibilityConfigOrBuilder getDesiredIntraNodeVisibilityConfigOrBuilder()

The desired config of Intra-node visibility.

`.google.container.v1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[IntraNodeVisibilityConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IntraNodeVisibilityConfigOrBuilder)` |   
  
### getDesiredK8SBetaApis()
    
    
    public abstract K8sBetaAPIConfig getDesiredK8SBetaApis()

Desired Beta APIs to be enabled for cluster.

`.google.container.v1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.K8sBetaAPIConfig)` | The desiredK8sBetaApis.  
  
### getDesiredK8SBetaApisOrBuilder()
    
    
    public abstract K8sBetaAPIConfigOrBuilder getDesiredK8SBetaApisOrBuilder()

Desired Beta APIs to be enabled for cluster.

`.google.container.v1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.K8sBetaAPIConfigOrBuilder)` |   
  
### getDesiredL4IlbSubsettingConfig()
    
    
    public abstract ILBSubsettingConfig getDesiredL4IlbSubsettingConfig()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[ILBSubsettingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ILBSubsettingConfig)` | The desiredL4ilbSubsettingConfig.  
  
### getDesiredL4IlbSubsettingConfigOrBuilder()
    
    
    public abstract ILBSubsettingConfigOrBuilder getDesiredL4IlbSubsettingConfigOrBuilder()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[ILBSubsettingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ILBSubsettingConfigOrBuilder)` |   
  
### getDesiredLocations(int index)
    
    
    public abstract String getDesiredLocations(int index)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredLocations at the given index.  
  
### getDesiredLocationsBytes(int index)
    
    
    public abstract ByteString getDesiredLocationsBytes(int index)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the desiredLocations at the given index.  
  
### getDesiredLocationsCount()
    
    
    public abstract int getDesiredLocationsCount()

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of desiredLocations.  
  
### getDesiredLocationsList()
    
    
    public abstract List<String> getDesiredLocationsList()

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the desiredLocations.  
  
### getDesiredLoggingConfig()
    
    
    public abstract LoggingConfig getDesiredLoggingConfig()

The desired logging configuration.

`.google.container.v1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LoggingConfig)` | The desiredLoggingConfig.  
  
### getDesiredLoggingConfigOrBuilder()
    
    
    public abstract LoggingConfigOrBuilder getDesiredLoggingConfigOrBuilder()

The desired logging configuration.

`.google.container.v1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LoggingConfigOrBuilder)` |   
  
### getDesiredLoggingService()
    
    
    public abstract String getDesiredLoggingService()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredLoggingService.  
  
### getDesiredLoggingServiceBytes()
    
    
    public abstract ByteString getDesiredLoggingServiceBytes()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredLoggingService.  
  
### getDesiredManagedMachineLearningDiagnosticsConfig()
    
    
    public abstract ManagedMachineLearningDiagnosticsConfig getDesiredManagedMachineLearningDiagnosticsConfig()

The desired managed machine learning diagnostics configuration.

` .google.container.v1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedMachineLearningDiagnosticsConfig)` | The desiredManagedMachineLearningDiagnosticsConfig.  
  
### getDesiredManagedMachineLearningDiagnosticsConfigOrBuilder()
    
    
    public abstract ManagedMachineLearningDiagnosticsConfigOrBuilder getDesiredManagedMachineLearningDiagnosticsConfigOrBuilder()

The desired managed machine learning diagnostics configuration.

` .google.container.v1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedMachineLearningDiagnosticsConfigOrBuilder)` |   
  
### getDesiredManagedOpentelemetryConfig()
    
    
    public abstract ManagedOpenTelemetryConfig getDesiredManagedOpentelemetryConfig()

The desired managed open telemetry configuration.

` .google.container.v1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedOpenTelemetryConfig)` | The desiredManagedOpentelemetryConfig.  
  
### getDesiredManagedOpentelemetryConfigOrBuilder()
    
    
    public abstract ManagedOpenTelemetryConfigOrBuilder getDesiredManagedOpentelemetryConfigOrBuilder()

The desired managed open telemetry configuration.

` .google.container.v1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedOpenTelemetryConfigOrBuilder)` |   
  
### getDesiredMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public abstract MasterAuthorizedNetworksConfig getDesiredMasterAuthorizedNetworksConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_master_authorized_networks_config is deprecated. See google/container/v1/cluster_service.proto;l=3704_

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthorizedNetworksConfig)` | The desiredMasterAuthorizedNetworksConfig.  
  
### getDesiredMasterAuthorizedNetworksConfigOrBuilder() (deprecated)
    
    
    public abstract MasterAuthorizedNetworksConfigOrBuilder getDesiredMasterAuthorizedNetworksConfigOrBuilder()

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthorizedNetworksConfigOrBuilder)` |   
  
### getDesiredMasterVersion()
    
    
    public abstract String getDesiredMasterVersion()

The Kubernetes version to change the master to.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredMasterVersion.  
  
### getDesiredMasterVersionBytes()
    
    
    public abstract ByteString getDesiredMasterVersionBytes()

The Kubernetes version to change the master to.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredMasterVersion.  
  
### getDesiredMeshCertificates()
    
    
    public abstract MeshCertificates getDesiredMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MeshCertificates)` | The desiredMeshCertificates.  
  
### getDesiredMeshCertificatesOrBuilder()
    
    
    public abstract MeshCertificatesOrBuilder getDesiredMeshCertificatesOrBuilder()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificatesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MeshCertificatesOrBuilder)` |   
  
### getDesiredMonitoringConfig()
    
    
    public abstract MonitoringConfig getDesiredMonitoringConfig()

The desired monitoring configuration.

`.google.container.v1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MonitoringConfig)` | The desiredMonitoringConfig.  
  
### getDesiredMonitoringConfigOrBuilder()
    
    
    public abstract MonitoringConfigOrBuilder getDesiredMonitoringConfigOrBuilder()

The desired monitoring configuration.

`.google.container.v1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MonitoringConfigOrBuilder)` |   
  
### getDesiredMonitoringService()
    
    
    public abstract String getDesiredMonitoringService()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredMonitoringService.  
  
### getDesiredMonitoringServiceBytes()
    
    
    public abstract ByteString getDesiredMonitoringServiceBytes()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredMonitoringService.  
  
### getDesiredNetworkPerformanceConfig()
    
    
    public abstract NetworkConfig.ClusterNetworkPerformanceConfig getDesiredNetworkPerformanceConfig()

The desired network performance config.

` .google.container.v1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig.ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkConfig.ClusterNetworkPerformanceConfig)` | The desiredNetworkPerformanceConfig.  
  
### getDesiredNetworkPerformanceConfigOrBuilder()
    
    
    public abstract NetworkConfig.ClusterNetworkPerformanceConfigOrBuilder getDesiredNetworkPerformanceConfigOrBuilder()

The desired network performance config.

` .google.container.v1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig.ClusterNetworkPerformanceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkConfig.ClusterNetworkPerformanceConfigOrBuilder)` |   
  
### getDesiredNetworkTierConfig()
    
    
    public abstract NetworkTierConfig getDesiredNetworkTierConfig()

The desired network tier configuration for the cluster.

`.google.container.v1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTierConfig)` | The desiredNetworkTierConfig.  
  
### getDesiredNetworkTierConfigOrBuilder()
    
    
    public abstract NetworkTierConfigOrBuilder getDesiredNetworkTierConfigOrBuilder()

The desired network tier configuration for the cluster.

`.google.container.v1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTierConfigOrBuilder)` |   
  
### getDesiredNodeCreationConfig()
    
    
    public abstract NodeCreationConfig getDesiredNodeCreationConfig()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeCreationConfig)` | The desiredNodeCreationConfig.  
  
### getDesiredNodeCreationConfigOrBuilder()
    
    
    public abstract NodeCreationConfigOrBuilder getDesiredNodeCreationConfigOrBuilder()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeCreationConfigOrBuilder)` |   
  
### getDesiredNodeKubeletConfig()
    
    
    public abstract NodeKubeletConfig getDesiredNodeKubeletConfig()

The desired node kubelet config for the cluster.

`.google.container.v1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeKubeletConfig)` | The desiredNodeKubeletConfig.  
  
### getDesiredNodeKubeletConfigOrBuilder()
    
    
    public abstract NodeKubeletConfigOrBuilder getDesiredNodeKubeletConfigOrBuilder()

The desired node kubelet config for the cluster.

`.google.container.v1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeKubeletConfigOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigKubeletConfig()
    
    
    public abstract NodeKubeletConfig getDesiredNodePoolAutoConfigKubeletConfig()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeKubeletConfig)` | The desiredNodePoolAutoConfigKubeletConfig.  
  
### getDesiredNodePoolAutoConfigKubeletConfigOrBuilder()
    
    
    public abstract NodeKubeletConfigOrBuilder getDesiredNodePoolAutoConfigKubeletConfigOrBuilder()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeKubeletConfigOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigLinuxNodeConfig()
    
    
    public abstract LinuxNodeConfig getDesiredNodePoolAutoConfigLinuxNodeConfig()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig)` | The desiredNodePoolAutoConfigLinuxNodeConfig.  
  
### getDesiredNodePoolAutoConfigLinuxNodeConfigOrBuilder()
    
    
    public abstract LinuxNodeConfigOrBuilder getDesiredNodePoolAutoConfigLinuxNodeConfigOrBuilder()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfigOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigNetworkTags()
    
    
    public abstract NetworkTags getDesiredNodePoolAutoConfigNetworkTags()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1.NetworkTags desired_node_pool_auto_config_network_tags = 110;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTags)` | The desiredNodePoolAutoConfigNetworkTags.  
  
### getDesiredNodePoolAutoConfigNetworkTagsOrBuilder()
    
    
    public abstract NetworkTagsOrBuilder getDesiredNodePoolAutoConfigNetworkTagsOrBuilder()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1.NetworkTags desired_node_pool_auto_config_network_tags = 110;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTagsOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigResourceManagerTags()
    
    
    public abstract ResourceManagerTags getDesiredNodePoolAutoConfigResourceManagerTags()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceManagerTags)` | The desiredNodePoolAutoConfigResourceManagerTags.  
  
### getDesiredNodePoolAutoConfigResourceManagerTagsOrBuilder()
    
    
    public abstract ResourceManagerTagsOrBuilder getDesiredNodePoolAutoConfigResourceManagerTagsOrBuilder()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceManagerTagsOrBuilder)` |   
  
### getDesiredNodePoolAutoscaling()
    
    
    public abstract NodePoolAutoscaling getDesiredNodePoolAutoscaling()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolAutoscaling)` | The desiredNodePoolAutoscaling.  
  
### getDesiredNodePoolAutoscalingOrBuilder()
    
    
    public abstract NodePoolAutoscalingOrBuilder getDesiredNodePoolAutoscalingOrBuilder()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolAutoscalingOrBuilder)` |   
  
### getDesiredNodePoolId()
    
    
    public abstract String getDesiredNodePoolId()

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family" or "desired_node_pool_autoscaling" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredNodePoolId.  
  
### getDesiredNodePoolIdBytes()
    
    
    public abstract ByteString getDesiredNodePoolIdBytes()

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family" or "desired_node_pool_autoscaling" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredNodePoolId.  
  
### getDesiredNodePoolLoggingConfig()
    
    
    public abstract NodePoolLoggingConfig getDesiredNodePoolLoggingConfig()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1.NodePoolLoggingConfig desired_node_pool_logging_config = 116;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolLoggingConfig)` | The desiredNodePoolLoggingConfig.  
  
### getDesiredNodePoolLoggingConfigOrBuilder()
    
    
    public abstract NodePoolLoggingConfigOrBuilder getDesiredNodePoolLoggingConfigOrBuilder()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1.NodePoolLoggingConfig desired_node_pool_logging_config = 116;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolLoggingConfigOrBuilder)` |   
  
### getDesiredNodeVersion()
    
    
    public abstract String getDesiredNodeVersion()

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredNodeVersion.  
  
### getDesiredNodeVersionBytes()
    
    
    public abstract ByteString getDesiredNodeVersionBytes()

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredNodeVersion.  
  
### getDesiredNotificationConfig()
    
    
    public abstract NotificationConfig getDesiredNotificationConfig()

The desired notification configuration.

`.google.container.v1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NotificationConfig)` | The desiredNotificationConfig.  
  
### getDesiredNotificationConfigOrBuilder()
    
    
    public abstract NotificationConfigOrBuilder getDesiredNotificationConfigOrBuilder()

The desired notification configuration.

`.google.container.v1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NotificationConfigOrBuilder)` |   
  
### getDesiredPodAutoscaling()
    
    
    public abstract PodAutoscaling getDesiredPodAutoscaling()

The desired config for pod autoscaling.

`.google.container.v1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodAutoscaling)` | The desiredPodAutoscaling.  
  
### getDesiredPodAutoscalingOrBuilder()
    
    
    public abstract PodAutoscalingOrBuilder getDesiredPodAutoscalingOrBuilder()

The desired config for pod autoscaling.

`.google.container.v1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodAutoscalingOrBuilder)` |   
  
### getDesiredPrivateClusterConfig() (deprecated)
    
    
    public abstract PrivateClusterConfig getDesiredPrivateClusterConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_private_cluster_config is deprecated. See google/container/v1/cluster_service.proto;l=3742_

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivateClusterConfig)` | The desiredPrivateClusterConfig.  
  
### getDesiredPrivateClusterConfigOrBuilder() (deprecated)
    
    
    public abstract PrivateClusterConfigOrBuilder getDesiredPrivateClusterConfigOrBuilder()

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivateClusterConfigOrBuilder)` |   
  
### getDesiredPrivateIpv6GoogleAccess()
    
    
    public abstract PrivateIPv6GoogleAccess getDesiredPrivateIpv6GoogleAccess()

The desired state of IPv6 connectivity to Google Services.

`.google.container.v1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateIPv6GoogleAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivateIPv6GoogleAccess)` | The desiredPrivateIpv6GoogleAccess.  
  
### getDesiredPrivateIpv6GoogleAccessValue()
    
    
    public abstract int getDesiredPrivateIpv6GoogleAccessValue()

The desired state of IPv6 connectivity to Google Services.

`.google.container.v1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredPrivateIpv6GoogleAccess.  
  
### getDesiredPrivilegedAdmissionConfig()
    
    
    public abstract PrivilegedAdmissionConfig getDesiredPrivilegedAdmissionConfig()

The desired privileged admission config for the cluster.

`.google.container.v1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAdmissionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivilegedAdmissionConfig)` | The desiredPrivilegedAdmissionConfig.  
  
### getDesiredPrivilegedAdmissionConfigOrBuilder()
    
    
    public abstract PrivilegedAdmissionConfigOrBuilder getDesiredPrivilegedAdmissionConfigOrBuilder()

The desired privileged admission config for the cluster.

`.google.container.v1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAdmissionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivilegedAdmissionConfigOrBuilder)` |   
  
### getDesiredRbacBindingConfig()
    
    
    public abstract RBACBindingConfig getDesiredRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1.RBACBindingConfig desired_rbac_binding_config = 144;`

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RBACBindingConfig)` | The desiredRbacBindingConfig.  
  
### getDesiredRbacBindingConfigOrBuilder()
    
    
    public abstract RBACBindingConfigOrBuilder getDesiredRbacBindingConfigOrBuilder()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1.RBACBindingConfig desired_rbac_binding_config = 144;`

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RBACBindingConfigOrBuilder)` |   
  
### getDesiredReleaseChannel()
    
    
    public abstract ReleaseChannel getDesiredReleaseChannel()

The desired release channel configuration.

`.google.container.v1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ReleaseChannel)` | The desiredReleaseChannel.  
  
### getDesiredReleaseChannelOrBuilder()
    
    
    public abstract ReleaseChannelOrBuilder getDesiredReleaseChannelOrBuilder()

The desired release channel configuration.

`.google.container.v1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannelOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ReleaseChannelOrBuilder)` |   
  
### getDesiredResourceUsageExportConfig()
    
    
    public abstract ResourceUsageExportConfig getDesiredResourceUsageExportConfig()

The desired configuration for exporting resource usage.

`.google.container.v1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceUsageExportConfig)` | The desiredResourceUsageExportConfig.  
  
### getDesiredResourceUsageExportConfigOrBuilder()
    
    
    public abstract ResourceUsageExportConfigOrBuilder getDesiredResourceUsageExportConfigOrBuilder()

The desired configuration for exporting resource usage.

`.google.container.v1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceUsageExportConfigOrBuilder)` |   
  
### getDesiredRollbackSafeUpgrade()
    
    
    public abstract RollbackSafeUpgrade getDesiredRollbackSafeUpgrade()

Optional. The desired rollback safe upgrade configuration.

` .google.container.v1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgrade](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackSafeUpgrade)` | The desiredRollbackSafeUpgrade.  
  
### getDesiredRollbackSafeUpgradeOrBuilder()
    
    
    public abstract RollbackSafeUpgradeOrBuilder getDesiredRollbackSafeUpgradeOrBuilder()

Optional. The desired rollback safe upgrade configuration.

` .google.container.v1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgradeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackSafeUpgradeOrBuilder)` |   
  
### getDesiredSecretManagerConfig()
    
    
    public abstract SecretManagerConfig getDesiredSecretManagerConfig()

Enable/Disable Secret Manager Config.

`optional .google.container.v1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretManagerConfig)` | The desiredSecretManagerConfig.  
  
### getDesiredSecretManagerConfigOrBuilder()
    
    
    public abstract SecretManagerConfigOrBuilder getDesiredSecretManagerConfigOrBuilder()

Enable/Disable Secret Manager Config.

`optional .google.container.v1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretManagerConfigOrBuilder)` |   
  
### getDesiredSecretSyncConfig()
    
    
    public abstract SecretSyncConfig getDesiredSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretSyncConfig)` | The desiredSecretSyncConfig.  
  
### getDesiredSecretSyncConfigOrBuilder()
    
    
    public abstract SecretSyncConfigOrBuilder getDesiredSecretSyncConfigOrBuilder()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretSyncConfigOrBuilder)` |   
  
### getDesiredSecurityPostureConfig()
    
    
    public abstract SecurityPostureConfig getDesiredSecurityPostureConfig()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1.SecurityPostureConfig desired_security_posture_config = 124;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecurityPostureConfig)` | The desiredSecurityPostureConfig.  
  
### getDesiredSecurityPostureConfigOrBuilder()
    
    
    public abstract SecurityPostureConfigOrBuilder getDesiredSecurityPostureConfigOrBuilder()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1.SecurityPostureConfig desired_security_posture_config = 124;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecurityPostureConfigOrBuilder)` |   
  
### getDesiredServiceExternalIpsConfig()
    
    
    public abstract ServiceExternalIPsConfig getDesiredServiceExternalIpsConfig()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

`.google.container.v1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceExternalIPsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServiceExternalIPsConfig)` | The desiredServiceExternalIpsConfig.  
  
### getDesiredServiceExternalIpsConfigOrBuilder()
    
    
    public abstract ServiceExternalIPsConfigOrBuilder getDesiredServiceExternalIpsConfigOrBuilder()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

`.google.container.v1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceExternalIPsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServiceExternalIPsConfigOrBuilder)` |   
  
### getDesiredShieldedNodes()
    
    
    public abstract ShieldedNodes getDesiredShieldedNodes()

Configuration for Shielded Nodes.

`.google.container.v1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ShieldedNodes)` | The desiredShieldedNodes.  
  
### getDesiredShieldedNodesOrBuilder()
    
    
    public abstract ShieldedNodesOrBuilder getDesiredShieldedNodesOrBuilder()

Configuration for Shielded Nodes.

`.google.container.v1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ShieldedNodesOrBuilder)` |   
  
### getDesiredStackType()
    
    
    public abstract StackType getDesiredStackType()

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1.StackType desired_stack_type = 119;`

**Returns**  
---  
**Type** | **Description**  
`[StackType](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StackType)` | The desiredStackType.  
  
### getDesiredStackTypeValue()
    
    
    public abstract int getDesiredStackTypeValue()

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1.StackType desired_stack_type = 119;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredStackType.  
  
### getDesiredUserManagedKeysConfig()
    
    
    public abstract UserManagedKeysConfig getDesiredUserManagedKeysConfig()

The desired user managed keys config for the cluster.

`.google.container.v1.UserManagedKeysConfig desired_user_managed_keys_config = 152;`

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UserManagedKeysConfig)` | The desiredUserManagedKeysConfig.  
  
### getDesiredUserManagedKeysConfigOrBuilder()
    
    
    public abstract UserManagedKeysConfigOrBuilder getDesiredUserManagedKeysConfigOrBuilder()

The desired user managed keys config for the cluster.

`.google.container.v1.UserManagedKeysConfig desired_user_managed_keys_config = 152;`

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UserManagedKeysConfigOrBuilder)` |   
  
### getDesiredVerticalPodAutoscaling()
    
    
    public abstract VerticalPodAutoscaling getDesiredVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22;`

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.VerticalPodAutoscaling)` | The desiredVerticalPodAutoscaling.  
  
### getDesiredVerticalPodAutoscalingOrBuilder()
    
    
    public abstract VerticalPodAutoscalingOrBuilder getDesiredVerticalPodAutoscalingOrBuilder()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22;`

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.VerticalPodAutoscalingOrBuilder)` |   
  
### getDesiredWorkloadIdentityConfig()
    
    
    public abstract WorkloadIdentityConfig getDesiredWorkloadIdentityConfig()

Configuration for Workload Identity.

`.google.container.v1.WorkloadIdentityConfig desired_workload_identity_config = 47;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.WorkloadIdentityConfig)` | The desiredWorkloadIdentityConfig.  
  
### getDesiredWorkloadIdentityConfigOrBuilder()
    
    
    public abstract WorkloadIdentityConfigOrBuilder getDesiredWorkloadIdentityConfigOrBuilder()

Configuration for Workload Identity.

`.google.container.v1.WorkloadIdentityConfig desired_workload_identity_config = 47;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.WorkloadIdentityConfigOrBuilder)` |   
  
### getEnableK8SBetaApis()
    
    
    public abstract K8sBetaAPIConfig getEnableK8SBetaApis()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.K8sBetaAPIConfig)` | The enableK8sBetaApis.  
  
### getEnableK8SBetaApisOrBuilder()
    
    
    public abstract K8sBetaAPIConfigOrBuilder getEnableK8SBetaApisOrBuilder()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.K8sBetaAPIConfigOrBuilder)` |   
  
### getEtag()
    
    
    public abstract String getEtag()

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGkeAutoUpgradeConfig()
    
    
    public abstract GkeAutoUpgradeConfig getGkeAutoUpgradeConfig()

Configuration for GKE auto upgrade.

`.google.container.v1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GkeAutoUpgradeConfig)` | The gkeAutoUpgradeConfig.  
  
### getGkeAutoUpgradeConfigOrBuilder()
    
    
    public abstract GkeAutoUpgradeConfigOrBuilder getGkeAutoUpgradeConfigOrBuilder()

Configuration for GKE auto upgrade.

`.google.container.v1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GkeAutoUpgradeConfigOrBuilder)` |   
  
### getRemovedAdditionalPodRangesConfig()
    
    
    public abstract AdditionalPodRangesConfig getRemovedAdditionalPodRangesConfig()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalPodRangesConfig)` | The removedAdditionalPodRangesConfig.  
  
### getRemovedAdditionalPodRangesConfigOrBuilder()
    
    
    public abstract AdditionalPodRangesConfigOrBuilder getRemovedAdditionalPodRangesConfigOrBuilder()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalPodRangesConfigOrBuilder)` |   
  
### getUserManagedKeysConfig() (deprecated)
    
    
    public abstract UserManagedKeysConfig getUserManagedKeysConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.user_managed_keys_config is deprecated. See google/container/v1/cluster_service.proto;l=3908_

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UserManagedKeysConfig)` | The userManagedKeysConfig.  
  
### getUserManagedKeysConfigOrBuilder() (deprecated)
    
    
    public abstract UserManagedKeysConfigOrBuilder getUserManagedKeysConfigOrBuilder()

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UserManagedKeysConfigOrBuilder)` |   
  
### hasAdditionalPodRangesConfig()
    
    
    public abstract boolean hasAdditionalPodRangesConfig()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1.AdditionalPodRangesConfig additional_pod_ranges_config = 120;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the additionalPodRangesConfig field is set.  
  
### hasDesiredAdditionalIpRangesConfig()
    
    
    public abstract boolean hasDesiredAdditionalIpRangesConfig()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAdditionalIpRangesConfig field is set.  
  
### hasDesiredAddonsConfig()
    
    
    public abstract boolean hasDesiredAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAddonsConfig field is set.  
  
### hasDesiredAnonymousAuthenticationConfig()
    
    
    public abstract boolean hasDesiredAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAnonymousAuthenticationConfig field is set.  
  
### hasDesiredAuthenticatorGroupsConfig()
    
    
    public abstract boolean hasDesiredAuthenticatorGroupsConfig()

The desired authenticator groups config for the cluster.

`.google.container.v1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAuthenticatorGroupsConfig field is set.  
  
### hasDesiredAutoIpamConfig()
    
    
    public abstract boolean hasDesiredAutoIpamConfig()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAutoIpamConfig field is set.  
  
### hasDesiredAutopilotClusterPolicyConfig()
    
    
    public abstract boolean hasDesiredAutopilotClusterPolicyConfig()

The desired autopilot cluster policies that to be enforced in the cluster.

`.google.container.v1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAutopilotClusterPolicyConfig field is set.  
  
### hasDesiredAutopilotWorkloadPolicyConfig()
    
    
    public abstract boolean hasDesiredAutopilotWorkloadPolicyConfig()

WorkloadPolicyConfig is the configuration related to GCW workload policy

`.google.container.v1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAutopilotWorkloadPolicyConfig field is set.  
  
### hasDesiredBinaryAuthorization()
    
    
    public abstract boolean hasDesiredBinaryAuthorization()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredBinaryAuthorization field is set.  
  
### hasDesiredClusterAutoscaling()
    
    
    public abstract boolean hasDesiredClusterAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredClusterAutoscaling field is set.  
  
### hasDesiredCompliancePostureConfig() (deprecated)
    
    
    public abstract boolean hasDesiredCompliancePostureConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_compliance_posture_config is deprecated. See google/container/v1/cluster_service.proto;l=3892_

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredCompliancePostureConfig field is set.  
  
### hasDesiredContainerdConfig()
    
    
    public abstract boolean hasDesiredContainerdConfig()

The desired containerd config for the cluster.

`.google.container.v1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredContainerdConfig field is set.  
  
### hasDesiredControlPlaneEgress()
    
    
    public abstract boolean hasDesiredControlPlaneEgress()

The desired control plane egress control config for the cluster.

`.google.container.v1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredControlPlaneEgress field is set.  
  
### hasDesiredControlPlaneEndpointsConfig()
    
    
    public abstract boolean hasDesiredControlPlaneEndpointsConfig()

Control plane endpoints configuration.

` .google.container.v1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredControlPlaneEndpointsConfig field is set.  
  
### hasDesiredCostManagementConfig()
    
    
    public abstract boolean hasDesiredCostManagementConfig()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1.CostManagementConfig desired_cost_management_config = 49;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredCostManagementConfig field is set.  
  
### hasDesiredDatabaseEncryption()
    
    
    public abstract boolean hasDesiredDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDatabaseEncryption field is set.  
  
### hasDesiredDefaultEnablePrivateNodes()
    
    
    public abstract boolean hasDesiredDefaultEnablePrivateNodes()

Override the default setting of whether future created nodes have private IP addresses only, namely NetworkConfig.default_enable_private_nodes

`optional bool desired_default_enable_private_nodes = 72;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDefaultEnablePrivateNodes field is set.  
  
### hasDesiredDefaultSnatStatus()
    
    
    public abstract boolean hasDesiredDefaultSnatStatus()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDefaultSnatStatus field is set.  
  
### hasDesiredDisableL4LbFirewallReconciliation()
    
    
    public abstract boolean hasDesiredDisableL4LbFirewallReconciliation()

Enable/Disable L4 LB VPC firewall reconciliation for the cluster.

`optional bool desired_disable_l4_lb_firewall_reconciliation = 149;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDisableL4LbFirewallReconciliation field is set.  
  
### hasDesiredDnsConfig()
    
    
    public abstract boolean hasDesiredDnsConfig()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDnsConfig field is set.  
  
### hasDesiredEmulatedVersion()
    
    
    public abstract boolean hasDesiredEmulatedVersion()

Optional. The desired emulated version for the cluster.

`optional string desired_emulated_version = 182 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEmulatedVersion field is set.  
  
### hasDesiredEnableCiliumClusterwideNetworkPolicy()
    
    
    public abstract boolean hasDesiredEnableCiliumClusterwideNetworkPolicy()

Enable/Disable Cilium Clusterwide Network Policy for the cluster.

`optional bool desired_enable_cilium_clusterwide_network_policy = 138;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnableCiliumClusterwideNetworkPolicy field is set.  
  
### hasDesiredEnableFqdnNetworkPolicy()
    
    
    public abstract boolean hasDesiredEnableFqdnNetworkPolicy()

Enable/Disable FQDN Network Policy for the cluster.

`optional bool desired_enable_fqdn_network_policy = 126;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnableFqdnNetworkPolicy field is set.  
  
### hasDesiredEnableMultiNetworking()
    
    
    public abstract boolean hasDesiredEnableMultiNetworking()

Enable/Disable Multi-Networking for the cluster

`optional bool desired_enable_multi_networking = 135;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnableMultiNetworking field is set.  
  
### hasDesiredEnablePrivateEndpoint() (deprecated)
    
    
    public abstract boolean hasDesiredEnablePrivateEndpoint()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_enable_private_endpoint is deprecated. See google/container/v1/cluster_service.proto;l=3787_

Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true.

`optional bool desired_enable_private_endpoint = 71 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnablePrivateEndpoint field is set.  
  
### hasDesiredEnterpriseConfig() (deprecated)
    
    
    public abstract boolean hasDesiredEnterpriseConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_enterprise_config is deprecated. See google/container/v1/cluster_service.proto;l=3921_

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnterpriseConfig field is set.  
  
### hasDesiredFleet()
    
    
    public abstract boolean hasDesiredFleet()

The desired fleet configuration for the cluster.

`.google.container.v1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredFleet field is set.  
  
### hasDesiredGatewayApiConfig()
    
    
    public abstract boolean hasDesiredGatewayApiConfig()

The desired config of Gateway API on this cluster.

`.google.container.v1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredGatewayApiConfig field is set.  
  
### hasDesiredGcfsConfig()
    
    
    public abstract boolean hasDesiredGcfsConfig()

The desired GCFS config for the cluster

`.google.container.v1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredGcfsConfig field is set.  
  
### hasDesiredIdentityServiceConfig()
    
    
    public abstract boolean hasDesiredIdentityServiceConfig()

The desired Identity Service component configuration.

`.google.container.v1.IdentityServiceConfig desired_identity_service_config = 66;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredIdentityServiceConfig field is set.  
  
### hasDesiredInTransitEncryptionConfig()
    
    
    public abstract boolean hasDesiredInTransitEncryptionConfig()

Specify the details of in-transit encryption.

` optional .google.container.v1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredInTransitEncryptionConfig field is set.  
  
### hasDesiredIntraNodeVisibilityConfig()
    
    
    public abstract boolean hasDesiredIntraNodeVisibilityConfig()

The desired config of Intra-node visibility.

`.google.container.v1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredIntraNodeVisibilityConfig field is set.  
  
### hasDesiredK8SBetaApis()
    
    
    public abstract boolean hasDesiredK8SBetaApis()

Desired Beta APIs to be enabled for cluster.

`.google.container.v1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredK8sBetaApis field is set.  
  
### hasDesiredL4IlbSubsettingConfig()
    
    
    public abstract boolean hasDesiredL4IlbSubsettingConfig()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredL4ilbSubsettingConfig field is set.  
  
### hasDesiredLoggingConfig()
    
    
    public abstract boolean hasDesiredLoggingConfig()

The desired logging configuration.

`.google.container.v1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredLoggingConfig field is set.  
  
### hasDesiredManagedMachineLearningDiagnosticsConfig()
    
    
    public abstract boolean hasDesiredManagedMachineLearningDiagnosticsConfig()

The desired managed machine learning diagnostics configuration.

` .google.container.v1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredManagedMachineLearningDiagnosticsConfig field is set.  
  
### hasDesiredManagedOpentelemetryConfig()
    
    
    public abstract boolean hasDesiredManagedOpentelemetryConfig()

The desired managed open telemetry configuration.

` .google.container.v1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredManagedOpentelemetryConfig field is set.  
  
### hasDesiredMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public abstract boolean hasDesiredMasterAuthorizedNetworksConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_master_authorized_networks_config is deprecated. See google/container/v1/cluster_service.proto;l=3704_

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMasterAuthorizedNetworksConfig field is set.  
  
### hasDesiredMeshCertificates()
    
    
    public abstract boolean hasDesiredMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMeshCertificates field is set.  
  
### hasDesiredMonitoringConfig()
    
    
    public abstract boolean hasDesiredMonitoringConfig()

The desired monitoring configuration.

`.google.container.v1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMonitoringConfig field is set.  
  
### hasDesiredNetworkPerformanceConfig()
    
    
    public abstract boolean hasDesiredNetworkPerformanceConfig()

The desired network performance config.

` .google.container.v1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNetworkPerformanceConfig field is set.  
  
### hasDesiredNetworkTierConfig()
    
    
    public abstract boolean hasDesiredNetworkTierConfig()

The desired network tier configuration for the cluster.

`.google.container.v1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNetworkTierConfig field is set.  
  
### hasDesiredNodeCreationConfig()
    
    
    public abstract boolean hasDesiredNodeCreationConfig()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodeCreationConfig field is set.  
  
### hasDesiredNodeKubeletConfig()
    
    
    public abstract boolean hasDesiredNodeKubeletConfig()

The desired node kubelet config for the cluster.

`.google.container.v1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodeKubeletConfig field is set.  
  
### hasDesiredNodePoolAutoConfigKubeletConfig()
    
    
    public abstract boolean hasDesiredNodePoolAutoConfigKubeletConfig()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigKubeletConfig field is set.  
  
### hasDesiredNodePoolAutoConfigLinuxNodeConfig()
    
    
    public abstract boolean hasDesiredNodePoolAutoConfigLinuxNodeConfig()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigLinuxNodeConfig field is set.  
  
### hasDesiredNodePoolAutoConfigNetworkTags()
    
    
    public abstract boolean hasDesiredNodePoolAutoConfigNetworkTags()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1.NetworkTags desired_node_pool_auto_config_network_tags = 110;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigNetworkTags field is set.  
  
### hasDesiredNodePoolAutoConfigResourceManagerTags()
    
    
    public abstract boolean hasDesiredNodePoolAutoConfigResourceManagerTags()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigResourceManagerTags field is set.  
  
### hasDesiredNodePoolAutoscaling()
    
    
    public abstract boolean hasDesiredNodePoolAutoscaling()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoscaling field is set.  
  
### hasDesiredNodePoolLoggingConfig()
    
    
    public abstract boolean hasDesiredNodePoolLoggingConfig()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1.NodePoolLoggingConfig desired_node_pool_logging_config = 116;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolLoggingConfig field is set.  
  
### hasDesiredNotificationConfig()
    
    
    public abstract boolean hasDesiredNotificationConfig()

The desired notification configuration.

`.google.container.v1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNotificationConfig field is set.  
  
### hasDesiredPodAutoscaling()
    
    
    public abstract boolean hasDesiredPodAutoscaling()

The desired config for pod autoscaling.

`.google.container.v1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPodAutoscaling field is set.  
  
### hasDesiredPrivateClusterConfig() (deprecated)
    
    
    public abstract boolean hasDesiredPrivateClusterConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.desired_private_cluster_config is deprecated. See google/container/v1/cluster_service.proto;l=3742_

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPrivateClusterConfig field is set.  
  
### hasDesiredPrivilegedAdmissionConfig()
    
    
    public abstract boolean hasDesiredPrivilegedAdmissionConfig()

The desired privileged admission config for the cluster.

`.google.container.v1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPrivilegedAdmissionConfig field is set.  
  
### hasDesiredRbacBindingConfig()
    
    
    public abstract boolean hasDesiredRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1.RBACBindingConfig desired_rbac_binding_config = 144;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredRbacBindingConfig field is set.  
  
### hasDesiredReleaseChannel()
    
    
    public abstract boolean hasDesiredReleaseChannel()

The desired release channel configuration.

`.google.container.v1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredReleaseChannel field is set.  
  
### hasDesiredResourceUsageExportConfig()
    
    
    public abstract boolean hasDesiredResourceUsageExportConfig()

The desired configuration for exporting resource usage.

`.google.container.v1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredResourceUsageExportConfig field is set.  
  
### hasDesiredRollbackSafeUpgrade()
    
    
    public abstract boolean hasDesiredRollbackSafeUpgrade()

Optional. The desired rollback safe upgrade configuration.

` .google.container.v1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredRollbackSafeUpgrade field is set.  
  
### hasDesiredSecretManagerConfig()
    
    
    public abstract boolean hasDesiredSecretManagerConfig()

Enable/Disable Secret Manager Config.

`optional .google.container.v1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredSecretManagerConfig field is set.  
  
### hasDesiredSecretSyncConfig()
    
    
    public abstract boolean hasDesiredSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredSecretSyncConfig field is set.  
  
### hasDesiredSecurityPostureConfig()
    
    
    public abstract boolean hasDesiredSecurityPostureConfig()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1.SecurityPostureConfig desired_security_posture_config = 124;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredSecurityPostureConfig field is set.  
  
### hasDesiredServiceExternalIpsConfig()
    
    
    public abstract boolean hasDesiredServiceExternalIpsConfig()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

`.google.container.v1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredServiceExternalIpsConfig field is set.  
  
### hasDesiredShieldedNodes()
    
    
    public abstract boolean hasDesiredShieldedNodes()

Configuration for Shielded Nodes.

`.google.container.v1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredShieldedNodes field is set.  
  
### hasDesiredUserManagedKeysConfig()
    
    
    public abstract boolean hasDesiredUserManagedKeysConfig()

The desired user managed keys config for the cluster.

`.google.container.v1.UserManagedKeysConfig desired_user_managed_keys_config = 152;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredUserManagedKeysConfig field is set.  
  
### hasDesiredVerticalPodAutoscaling()
    
    
    public abstract boolean hasDesiredVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredVerticalPodAutoscaling field is set.  
  
### hasDesiredWorkloadIdentityConfig()
    
    
    public abstract boolean hasDesiredWorkloadIdentityConfig()

Configuration for Workload Identity.

`.google.container.v1.WorkloadIdentityConfig desired_workload_identity_config = 47;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredWorkloadIdentityConfig field is set.  
  
### hasEnableK8SBetaApis()
    
    
    public abstract boolean hasEnableK8SBetaApis()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enableK8sBetaApis field is set.  
  
### hasGkeAutoUpgradeConfig()
    
    
    public abstract boolean hasGkeAutoUpgradeConfig()

Configuration for GKE auto upgrade.

`.google.container.v1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gkeAutoUpgradeConfig field is set.  
  
### hasRemovedAdditionalPodRangesConfig()
    
    
    public abstract boolean hasRemovedAdditionalPodRangesConfig()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the removedAdditionalPodRangesConfig field is set.  
  
### hasUserManagedKeysConfig() (deprecated)
    
    
    public abstract boolean hasUserManagedKeysConfig()

**Deprecated.** _google.container.v1.ClusterUpdate.user_managed_keys_config is deprecated. See google/container/v1/cluster_service.proto;l=3908_

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userManagedKeysConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
