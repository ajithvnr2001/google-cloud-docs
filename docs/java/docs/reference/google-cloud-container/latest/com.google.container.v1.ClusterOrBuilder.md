---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterOrBuilder
title: Interface ClusterOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:03.983437+00:00
---

# Interface ClusterOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClusterOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface ClusterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsResourceLabels(String key)
    
    
    public abstract boolean containsResourceLabels(String key)

The resource labels for the cluster to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 15;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAddonsConfig()
    
    
    public abstract AddonsConfig getAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1.AddonsConfig addons_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfig)` | The addonsConfig.  
  
### getAddonsConfigOrBuilder()
    
    
    public abstract AddonsConfigOrBuilder getAddonsConfigOrBuilder()

Configurations for the various addons available to run in the cluster.

`.google.container.v1.AddonsConfig addons_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfigOrBuilder)` |   
  
### getAlphaClusterFeatureGates(int index)
    
    
    public abstract String getAlphaClusterFeatureGates(int index)

The list of user specified Kubernetes feature gates. Each string represents the activation status of a feature gate (e.g. "featureX=true" or "featureX=false")

`repeated string alpha_cluster_feature_gates = 160;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The alphaClusterFeatureGates at the given index.  
  
### getAlphaClusterFeatureGatesBytes(int index)
    
    
    public abstract ByteString getAlphaClusterFeatureGatesBytes(int index)

The list of user specified Kubernetes feature gates. Each string represents the activation status of a feature gate (e.g. "featureX=true" or "featureX=false")

`repeated string alpha_cluster_feature_gates = 160;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the alphaClusterFeatureGates at the given index.  
  
### getAlphaClusterFeatureGatesCount()
    
    
    public abstract int getAlphaClusterFeatureGatesCount()

The list of user specified Kubernetes feature gates. Each string represents the activation status of a feature gate (e.g. "featureX=true" or "featureX=false")

`repeated string alpha_cluster_feature_gates = 160;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of alphaClusterFeatureGates.  
  
### getAlphaClusterFeatureGatesList()
    
    
    public abstract List<String> getAlphaClusterFeatureGatesList()

The list of user specified Kubernetes feature gates. Each string represents the activation status of a feature gate (e.g. "featureX=true" or "featureX=false")

`repeated string alpha_cluster_feature_gates = 160;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the alphaClusterFeatureGates.  
  
### getAnonymousAuthenticationConfig()
    
    
    public abstract AnonymousAuthenticationConfig getAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

`.google.container.v1.AnonymousAuthenticationConfig anonymous_authentication_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AnonymousAuthenticationConfig)` | The anonymousAuthenticationConfig.  
  
### getAnonymousAuthenticationConfigOrBuilder()
    
    
    public abstract AnonymousAuthenticationConfigOrBuilder getAnonymousAuthenticationConfigOrBuilder()

Configuration for limiting anonymous access to all endpoints except the health checks.

`.google.container.v1.AnonymousAuthenticationConfig anonymous_authentication_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AnonymousAuthenticationConfigOrBuilder)` |   
  
### getAuthenticatorGroupsConfig()
    
    
    public abstract AuthenticatorGroupsConfig getAuthenticatorGroupsConfig()

Configuration controlling RBAC group membership information.

`.google.container.v1.AuthenticatorGroupsConfig authenticator_groups_config = 34;`

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AuthenticatorGroupsConfig)` | The authenticatorGroupsConfig.  
  
### getAuthenticatorGroupsConfigOrBuilder()
    
    
    public abstract AuthenticatorGroupsConfigOrBuilder getAuthenticatorGroupsConfigOrBuilder()

Configuration controlling RBAC group membership information.

`.google.container.v1.AuthenticatorGroupsConfig authenticator_groups_config = 34;`

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AuthenticatorGroupsConfigOrBuilder)` |   
  
### getAutopilot()
    
    
    public abstract Autopilot getAutopilot()

Autopilot configuration for the cluster.

`.google.container.v1.Autopilot autopilot = 128;`

**Returns**  
---  
**Type** | **Description**  
`[Autopilot](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Autopilot)` | The autopilot.  
  
### getAutopilotOrBuilder()
    
    
    public abstract AutopilotOrBuilder getAutopilotOrBuilder()

Autopilot configuration for the cluster.

`.google.container.v1.Autopilot autopilot = 128;`

**Returns**  
---  
**Type** | **Description**  
`[AutopilotOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutopilotOrBuilder)` |   
  
### getAutoscaling()
    
    
    public abstract ClusterAutoscaling getAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1.ClusterAutoscaling autoscaling = 26;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscaling)` | The autoscaling.  
  
### getAutoscalingOrBuilder()
    
    
    public abstract ClusterAutoscalingOrBuilder getAutoscalingOrBuilder()

Cluster-level autoscaling configuration.

`.google.container.v1.ClusterAutoscaling autoscaling = 26;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscalingOrBuilder)` |   
  
### getBinaryAuthorization()
    
    
    public abstract BinaryAuthorization getBinaryAuthorization()

Configuration for Binary Authorization.

`.google.container.v1.BinaryAuthorization binary_authorization = 24;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.BinaryAuthorization)` | The binaryAuthorization.  
  
### getBinaryAuthorizationOrBuilder()
    
    
    public abstract BinaryAuthorizationOrBuilder getBinaryAuthorizationOrBuilder()

Configuration for Binary Authorization.

`.google.container.v1.BinaryAuthorization binary_authorization = 24;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorizationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.BinaryAuthorizationOrBuilder)` |   
  
### getClusterIpv4Cidr()
    
    
    public abstract String getClusterIpv4Cidr()

The IP address range of the container pods in this cluster, in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`). Leave blank to have one automatically chosen or specify a `/14` block in `10.0.0.0/8`.

`string cluster_ipv4_cidr = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterIpv4Cidr.  
  
### getClusterIpv4CidrBytes()
    
    
    public abstract ByteString getClusterIpv4CidrBytes()

The IP address range of the container pods in this cluster, in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`). Leave blank to have one automatically chosen or specify a `/14` block in `10.0.0.0/8`.

`string cluster_ipv4_cidr = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterIpv4Cidr.  
  
### getCompliancePostureConfig() (deprecated)
    
    
    public abstract CompliancePostureConfig getCompliancePostureConfig()

**Deprecated.** _google.container.v1.Cluster.compliance_posture_config is deprecated. See google/container/v1/cluster_service.proto;l=3294_

Optional. Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` .google.container.v1.CompliancePostureConfig compliance_posture_config = 151 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompliancePostureConfig)` | The compliancePostureConfig.  
  
### getCompliancePostureConfigOrBuilder() (deprecated)
    
    
    public abstract CompliancePostureConfigOrBuilder getCompliancePostureConfigOrBuilder()

Optional. Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` .google.container.v1.CompliancePostureConfig compliance_posture_config = 151 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompliancePostureConfigOrBuilder)` |   
  
### getConditions(int index)
    
    
    public abstract StatusCondition getConditions(int index)

Which conditions caused the current cluster state.

`repeated .google.container.v1.StatusCondition conditions = 118;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatusCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StatusCondition)` |   
  
### getConditionsCount()
    
    
    public abstract int getConditionsCount()

Which conditions caused the current cluster state.

`repeated .google.container.v1.StatusCondition conditions = 118;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConditionsList()
    
    
    public abstract List<StatusCondition> getConditionsList()

Which conditions caused the current cluster state.

`repeated .google.container.v1.StatusCondition conditions = 118;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StatusCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StatusCondition)>` |   
  
### getConditionsOrBuilder(int index)
    
    
    public abstract StatusConditionOrBuilder getConditionsOrBuilder(int index)

Which conditions caused the current cluster state.

`repeated .google.container.v1.StatusCondition conditions = 118;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatusConditionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StatusConditionOrBuilder)` |   
  
### getConditionsOrBuilderList()
    
    
    public abstract List<? extends StatusConditionOrBuilder> getConditionsOrBuilderList()

Which conditions caused the current cluster state.

`repeated .google.container.v1.StatusCondition conditions = 118;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.StatusConditionOrBuilder>` |   
  
### getConfidentialNodes()
    
    
    public abstract ConfidentialNodes getConfidentialNodes()

Configuration of Confidential Nodes. All the nodes in the cluster will be Confidential VM once enabled.

`.google.container.v1.ConfidentialNodes confidential_nodes = 50;`

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ConfidentialNodes)` | The confidentialNodes.  
  
### getConfidentialNodesOrBuilder()
    
    
    public abstract ConfidentialNodesOrBuilder getConfidentialNodesOrBuilder()

Configuration of Confidential Nodes. All the nodes in the cluster will be Confidential VM once enabled.

`.google.container.v1.ConfidentialNodes confidential_nodes = 50;`

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialNodesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ConfidentialNodesOrBuilder)` |   
  
### getControlPlaneEgress()
    
    
    public abstract ControlPlaneEgress getControlPlaneEgress()

Configuration for control plane egress control.

`.google.container.v1.ControlPlaneEgress control_plane_egress = 169;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEgress)` | The controlPlaneEgress.  
  
### getControlPlaneEgressOrBuilder()
    
    
    public abstract ControlPlaneEgressOrBuilder getControlPlaneEgressOrBuilder()

Configuration for control plane egress control.

`.google.container.v1.ControlPlaneEgress control_plane_egress = 169;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEgressOrBuilder)` |   
  
### getControlPlaneEndpointsConfig()
    
    
    public abstract ControlPlaneEndpointsConfig getControlPlaneEndpointsConfig()

Configuration for all cluster's control plane endpoints.

`.google.container.v1.ControlPlaneEndpointsConfig control_plane_endpoints_config = 146; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEndpointsConfig)` | The controlPlaneEndpointsConfig.  
  
### getControlPlaneEndpointsConfigOrBuilder()
    
    
    public abstract ControlPlaneEndpointsConfigOrBuilder getControlPlaneEndpointsConfigOrBuilder()

Configuration for all cluster's control plane endpoints.

`.google.container.v1.ControlPlaneEndpointsConfig control_plane_endpoints_config = 146; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ControlPlaneEndpointsConfigOrBuilder)` |   
  
### getCostManagementConfig()
    
    
    public abstract CostManagementConfig getCostManagementConfig()

Configuration for the fine-grained cost management feature.

`.google.container.v1.CostManagementConfig cost_management_config = 45;`

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CostManagementConfig)` | The costManagementConfig.  
  
### getCostManagementConfigOrBuilder()
    
    
    public abstract CostManagementConfigOrBuilder getCostManagementConfigOrBuilder()

Configuration for the fine-grained cost management feature.

`.google.container.v1.CostManagementConfig cost_management_config = 45;`

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CostManagementConfigOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract String getCreateTime()

Output only. The time the cluster was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

`string create_time = 106 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The createTime.  
  
### getCreateTimeBytes()
    
    
    public abstract ByteString getCreateTimeBytes()

Output only. The time the cluster was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

`string create_time = 106 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for createTime.  
  
### getCurrentEmulatedVersion()
    
    
    public abstract String getCurrentEmulatedVersion()

Output only. The current emulated version of the master endpoint. The version is in minor version format, e.g. 1.30. No value or empty string means the cluster has no emulated version.

`string current_emulated_version = 167 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The currentEmulatedVersion.  
  
### getCurrentEmulatedVersionBytes()
    
    
    public abstract ByteString getCurrentEmulatedVersionBytes()

Output only. The current emulated version of the master endpoint. The version is in minor version format, e.g. 1.30. No value or empty string means the cluster has no emulated version.

`string current_emulated_version = 167 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for currentEmulatedVersion.  
  
### getCurrentMasterVersion()
    
    
    public abstract String getCurrentMasterVersion()

Output only. The current software version of the master endpoint.

`string current_master_version = 104 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The currentMasterVersion.  
  
### getCurrentMasterVersionBytes()
    
    
    public abstract ByteString getCurrentMasterVersionBytes()

Output only. The current software version of the master endpoint.

`string current_master_version = 104 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for currentMasterVersion.  
  
### getCurrentNodeCount() (deprecated)
    
    
    public abstract int getCurrentNodeCount()

**Deprecated.** _google.container.v1.Cluster.current_node_count is deprecated. See google/container/v1/cluster_service.proto;l=3209_

Output only. The number of nodes currently in the cluster. Deprecated. Call Kubernetes API directly to retrieve node information.

` int32 current_node_count = 112 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The currentNodeCount.  
  
### getCurrentNodeVersion() (deprecated)
    
    
    public abstract String getCurrentNodeVersion()

**Deprecated.** _google.container.v1.Cluster.current_node_version is deprecated. See google/container/v1/cluster_service.proto;l=3174_

Output only. Deprecated, use [NodePools.version](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) instead. The current version of the node software components. If they are currently at multiple versions because they're in the process of being upgraded, this reflects the minimum version of all nodes.

` string current_node_version = 105 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The currentNodeVersion.  
  
### getCurrentNodeVersionBytes() (deprecated)
    
    
    public abstract ByteString getCurrentNodeVersionBytes()

**Deprecated.** _google.container.v1.Cluster.current_node_version is deprecated. See google/container/v1/cluster_service.proto;l=3174_

Output only. Deprecated, use [NodePools.version](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) instead. The current version of the node software components. If they are currently at multiple versions because they're in the process of being upgraded, this reflects the minimum version of all nodes.

` string current_node_version = 105 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for currentNodeVersion.  
  
### getDatabaseEncryption()
    
    
    public abstract DatabaseEncryption getDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1.DatabaseEncryption database_encryption = 38;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption)` | The databaseEncryption.  
  
### getDatabaseEncryptionOrBuilder()
    
    
    public abstract DatabaseEncryptionOrBuilder getDatabaseEncryptionOrBuilder()

Configuration of etcd encryption.

`.google.container.v1.DatabaseEncryption database_encryption = 38;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryptionOrBuilder)` |   
  
### getDefaultMaxPodsConstraint()
    
    
    public abstract MaxPodsConstraint getDefaultMaxPodsConstraint()

The default constraint on the maximum number of pods that can be run simultaneously on a node in the node pool of this cluster. Only honored if cluster created with IP Alias support.

`.google.container.v1.MaxPodsConstraint default_max_pods_constraint = 30;`

**Returns**  
---  
**Type** | **Description**  
`[MaxPodsConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaxPodsConstraint)` | The defaultMaxPodsConstraint.  
  
### getDefaultMaxPodsConstraintOrBuilder()
    
    
    public abstract MaxPodsConstraintOrBuilder getDefaultMaxPodsConstraintOrBuilder()

The default constraint on the maximum number of pods that can be run simultaneously on a node in the node pool of this cluster. Only honored if cluster created with IP Alias support.

`.google.container.v1.MaxPodsConstraint default_max_pods_constraint = 30;`

**Returns**  
---  
**Type** | **Description**  
`[MaxPodsConstraintOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaxPodsConstraintOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

An optional description of this cluster.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

An optional description of this cluster.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEnableK8SBetaApis()
    
    
    public abstract K8sBetaAPIConfig getEnableK8SBetaApis()

Beta APIs Config

`.google.container.v1.K8sBetaAPIConfig enable_k8s_beta_apis = 143;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.K8sBetaAPIConfig)` | The enableK8sBetaApis.  
  
### getEnableK8SBetaApisOrBuilder()
    
    
    public abstract K8sBetaAPIConfigOrBuilder getEnableK8SBetaApisOrBuilder()

Beta APIs Config

`.google.container.v1.K8sBetaAPIConfig enable_k8s_beta_apis = 143;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.K8sBetaAPIConfigOrBuilder)` |   
  
### getEnableKubernetesAlpha()
    
    
    public abstract boolean getEnableKubernetesAlpha()

Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes. The cluster has no SLA for uptime and master/node upgrades are disabled. Alpha enabled clusters are automatically deleted thirty days after creation.

`bool enable_kubernetes_alpha = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableKubernetesAlpha.  
  
### getEnableTpu() (deprecated)
    
    
    public abstract boolean getEnableTpu()

**Deprecated.** _google.container.v1.Cluster.enable_tpu is deprecated. See google/container/v1/cluster_service.proto;l=3226_

Enable the ability to use Cloud TPUs in this cluster. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`bool enable_tpu = 115 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableTpu.  
  
### getEndpoint()
    
    
    public abstract String getEndpoint()

Output only. The IP address of this cluster's master endpoint. The endpoint can be accessed from the internet at `https://username:password@endpoint/`.

See the `masterAuth` property of this resource for username and password information.

`string endpoint = 102 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpoint.  
  
### getEndpointBytes()
    
    
    public abstract ByteString getEndpointBytes()

Output only. The IP address of this cluster's master endpoint. The endpoint can be accessed from the internet at `https://username:password@endpoint/`.

See the `masterAuth` property of this resource for username and password information.

`string endpoint = 102 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpoint.  
  
### getEnterpriseConfig() (deprecated)
    
    
    public abstract EnterpriseConfig getEnterpriseConfig()

**Deprecated.** _google.container.v1.Cluster.enterprise_config is deprecated. See google/container/v1/cluster_service.proto;l=3284_

GKE Enterprise Configuration.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

`.google.container.v1.EnterpriseConfig enterprise_config = 149 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[EnterpriseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.EnterpriseConfig)` | The enterpriseConfig.  
  
### getEnterpriseConfigOrBuilder() (deprecated)
    
    
    public abstract EnterpriseConfigOrBuilder getEnterpriseConfigOrBuilder()

GKE Enterprise Configuration.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

`.google.container.v1.EnterpriseConfig enterprise_config = 149 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[EnterpriseConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.EnterpriseConfigOrBuilder)` |   
  
### getEtag()
    
    
    public abstract String getEtag()

This checksum is computed by the server based on the value of cluster fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding.

`string etag = 139;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

This checksum is computed by the server based on the value of cluster fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding.

`string etag = 139;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getExpireTime()
    
    
    public abstract String getExpireTime()

Output only. The time the cluster will be automatically deleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

`string expire_time = 113 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The expireTime.  
  
### getExpireTimeBytes()
    
    
    public abstract ByteString getExpireTimeBytes()

Output only. The time the cluster will be automatically deleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

`string expire_time = 113 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for expireTime.  
  
### getFleet()
    
    
    public abstract Fleet getFleet()

Fleet information for the cluster.

`.google.container.v1.Fleet fleet = 140;`

**Returns**  
---  
**Type** | **Description**  
`[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Fleet)` | The fleet.  
  
### getFleetOrBuilder()
    
    
    public abstract FleetOrBuilder getFleetOrBuilder()

Fleet information for the cluster.

`.google.container.v1.Fleet fleet = 140;`

**Returns**  
---  
**Type** | **Description**  
`[FleetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FleetOrBuilder)` |   
  
### getGkeAutoUpgradeConfig()
    
    
    public abstract GkeAutoUpgradeConfig getGkeAutoUpgradeConfig()

Configuration for GKE auto upgrades.

`.google.container.v1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 163;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GkeAutoUpgradeConfig)` | The gkeAutoUpgradeConfig.  
  
### getGkeAutoUpgradeConfigOrBuilder()
    
    
    public abstract GkeAutoUpgradeConfigOrBuilder getGkeAutoUpgradeConfigOrBuilder()

Configuration for GKE auto upgrades.

`.google.container.v1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 163;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GkeAutoUpgradeConfigOrBuilder)` |   
  
### getId()
    
    
    public abstract String getId()

Output only. Unique id for the cluster.

`string id = 129 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Output only. Unique id for the cluster.

`string id = 129 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getIdentityServiceConfig()
    
    
    public abstract IdentityServiceConfig getIdentityServiceConfig()

Configuration for Identity Service component.

`.google.container.v1.IdentityServiceConfig identity_service_config = 54;`

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IdentityServiceConfig)` | The identityServiceConfig.  
  
### getIdentityServiceConfigOrBuilder()
    
    
    public abstract IdentityServiceConfigOrBuilder getIdentityServiceConfigOrBuilder()

Configuration for Identity Service component.

`.google.container.v1.IdentityServiceConfig identity_service_config = 54;`

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IdentityServiceConfigOrBuilder)` |   
  
### getInitialClusterVersion()
    
    
    public abstract String getInitialClusterVersion()

The initial Kubernetes version for this cluster. Valid versions are those found in validMasterVersions returned by getServerConfig. The version can be upgraded over time; such upgrades are reflected in currentMasterVersion and currentNodeVersion.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "","-": picks the default Kubernetes version



`string initial_cluster_version = 103;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The initialClusterVersion.  
  
### getInitialClusterVersionBytes()
    
    
    public abstract ByteString getInitialClusterVersionBytes()

The initial Kubernetes version for this cluster. Valid versions are those found in validMasterVersions returned by getServerConfig. The version can be upgraded over time; such upgrades are reflected in currentMasterVersion and currentNodeVersion.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "","-": picks the default Kubernetes version



`string initial_cluster_version = 103;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for initialClusterVersion.  
  
### getInitialNodeCount() (deprecated)
    
    
    public abstract int getInitialNodeCount()

**Deprecated.** _google.container.v1.Cluster.initial_node_count is deprecated. See google/container/v1/cluster_service.proto;l=2934_

The number of nodes to create in this cluster. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "node_config") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time.

This field is deprecated, use node_pool.initial_node_count instead.

`int32 initial_node_count = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The initialNodeCount.  
  
### getInstanceGroupUrls(int index) (deprecated)
    
    
    public abstract String getInstanceGroupUrls(int index)

**Deprecated.** _google.container.v1.Cluster.instance_group_urls is deprecated. See google/container/v1/cluster_service.proto;l=3204_

Output only. Deprecated. Use node_pools.instance_group_urls.

` repeated string instance_group_urls = 111 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceGroupUrls at the given index.  
  
### getInstanceGroupUrlsBytes(int index) (deprecated)
    
    
    public abstract ByteString getInstanceGroupUrlsBytes(int index)

**Deprecated.** _google.container.v1.Cluster.instance_group_urls is deprecated. See google/container/v1/cluster_service.proto;l=3204_

Output only. Deprecated. Use node_pools.instance_group_urls.

` repeated string instance_group_urls = 111 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the instanceGroupUrls at the given index.  
  
### getInstanceGroupUrlsCount() (deprecated)
    
    
    public abstract int getInstanceGroupUrlsCount()

**Deprecated.** _google.container.v1.Cluster.instance_group_urls is deprecated. See google/container/v1/cluster_service.proto;l=3204_

Output only. Deprecated. Use node_pools.instance_group_urls.

` repeated string instance_group_urls = 111 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of instanceGroupUrls.  
  
### getInstanceGroupUrlsList() (deprecated)
    
    
    public abstract List<String> getInstanceGroupUrlsList()

**Deprecated.** _google.container.v1.Cluster.instance_group_urls is deprecated. See google/container/v1/cluster_service.proto;l=3204_

Output only. Deprecated. Use node_pools.instance_group_urls.

` repeated string instance_group_urls = 111 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the instanceGroupUrls.  
  
### getIpAllocationPolicy()
    
    
    public abstract IPAllocationPolicy getIpAllocationPolicy()

Configuration for cluster IP allocation.

`.google.container.v1.IPAllocationPolicy ip_allocation_policy = 20;`

**Returns**  
---  
**Type** | **Description**  
`[IPAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IPAllocationPolicy)` | The ipAllocationPolicy.  
  
### getIpAllocationPolicyOrBuilder()
    
    
    public abstract IPAllocationPolicyOrBuilder getIpAllocationPolicyOrBuilder()

Configuration for cluster IP allocation.

`.google.container.v1.IPAllocationPolicy ip_allocation_policy = 20;`

**Returns**  
---  
**Type** | **Description**  
`[IPAllocationPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.IPAllocationPolicyOrBuilder)` |   
  
### getLabelFingerprint()
    
    
    public abstract String getLabelFingerprint()

The fingerprint of the set of labels for this cluster.

`string label_fingerprint = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The labelFingerprint.  
  
### getLabelFingerprintBytes()
    
    
    public abstract ByteString getLabelFingerprintBytes()

The fingerprint of the set of labels for this cluster.

`string label_fingerprint = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for labelFingerprint.  
  
### getLegacyAbac()
    
    
    public abstract LegacyAbac getLegacyAbac()

Configuration for the legacy ABAC authorization mode.

`.google.container.v1.LegacyAbac legacy_abac = 18;`

**Returns**  
---  
**Type** | **Description**  
`[LegacyAbac](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LegacyAbac)` | The legacyAbac.  
  
### getLegacyAbacOrBuilder()
    
    
    public abstract LegacyAbacOrBuilder getLegacyAbacOrBuilder()

Configuration for the legacy ABAC authorization mode.

`.google.container.v1.LegacyAbac legacy_abac = 18;`

**Returns**  
---  
**Type** | **Description**  
`[LegacyAbacOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LegacyAbacOrBuilder)` |   
  
### getLocation()
    
    
    public abstract String getLocation()

Output only. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides.

`string location = 114 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The location.  
  
### getLocationBytes()
    
    
    public abstract ByteString getLocationBytes()

Output only. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides.

`string location = 114 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for location.  
  
### getLocations(int index)
    
    
    public abstract String getLocations(int index)

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation.

Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed.

`repeated string locations = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The locations at the given index.  
  
### getLocationsBytes(int index)
    
    
    public abstract ByteString getLocationsBytes(int index)

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation.

Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed.

`repeated string locations = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the locations at the given index.  
  
### getLocationsCount()
    
    
    public abstract int getLocationsCount()

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation.

Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed.

`repeated string locations = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of locations.  
  
### getLocationsList()
    
    
    public abstract List<String> getLocationsList()

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation.

Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed.

`repeated string locations = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the locations.  
  
### getLoggingConfig()
    
    
    public abstract LoggingConfig getLoggingConfig()

Logging configuration for the cluster.

`.google.container.v1.LoggingConfig logging_config = 132;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LoggingConfig)` | The loggingConfig.  
  
### getLoggingConfigOrBuilder()
    
    
    public abstract LoggingConfigOrBuilder getLoggingConfigOrBuilder()

Logging configuration for the cluster.

`.google.container.v1.LoggingConfig logging_config = 132;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LoggingConfigOrBuilder)` |   
  
### getLoggingService()
    
    
    public abstract String getLoggingService()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string logging_service = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The loggingService.  
  
### getLoggingServiceBytes()
    
    
    public abstract ByteString getLoggingServiceBytes()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string logging_service = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for loggingService.  
  
### getMaintenancePolicy()
    
    
    public abstract MaintenancePolicy getMaintenancePolicy()

Configure the maintenance policy for this cluster.

`.google.container.v1.MaintenancePolicy maintenance_policy = 23;`

**Returns**  
---  
**Type** | **Description**  
`[MaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenancePolicy)` | The maintenancePolicy.  
  
### getMaintenancePolicyOrBuilder()
    
    
    public abstract MaintenancePolicyOrBuilder getMaintenancePolicyOrBuilder()

Configure the maintenance policy for this cluster.

`.google.container.v1.MaintenancePolicy maintenance_policy = 23;`

**Returns**  
---  
**Type** | **Description**  
`[MaintenancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenancePolicyOrBuilder)` |   
  
### getManagedMachineLearningDiagnosticsConfig()
    
    
    public abstract ManagedMachineLearningDiagnosticsConfig getManagedMachineLearningDiagnosticsConfig()

Configuration for Managed Machine Learning Diagnostics.

` .google.container.v1.ManagedMachineLearningDiagnosticsConfig managed_machine_learning_diagnostics_config = 171; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedMachineLearningDiagnosticsConfig)` | The managedMachineLearningDiagnosticsConfig.  
  
### getManagedMachineLearningDiagnosticsConfigOrBuilder()
    
    
    public abstract ManagedMachineLearningDiagnosticsConfigOrBuilder getManagedMachineLearningDiagnosticsConfigOrBuilder()

Configuration for Managed Machine Learning Diagnostics.

` .google.container.v1.ManagedMachineLearningDiagnosticsConfig managed_machine_learning_diagnostics_config = 171; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedMachineLearningDiagnosticsConfigOrBuilder)` |   
  
### getManagedOpentelemetryConfig()
    
    
    public abstract ManagedOpenTelemetryConfig getManagedOpentelemetryConfig()

Configuration for Managed OpenTelemetry pipeline.

`.google.container.v1.ManagedOpenTelemetryConfig managed_opentelemetry_config = 168; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedOpenTelemetryConfig)` | The managedOpentelemetryConfig.  
  
### getManagedOpentelemetryConfigOrBuilder()
    
    
    public abstract ManagedOpenTelemetryConfigOrBuilder getManagedOpentelemetryConfigOrBuilder()

Configuration for Managed OpenTelemetry pipeline.

`.google.container.v1.ManagedOpenTelemetryConfig managed_opentelemetry_config = 168; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ManagedOpenTelemetryConfigOrBuilder)` |   
  
### getMasterAuth()
    
    
    public abstract MasterAuth getMasterAuth()

The authentication information for accessing the master endpoint. If unspecified, the defaults are used: For clusters before v1.12, if master_auth is unspecified, `username` will be set to "admin", a random password will be generated, and a client certificate will be issued.

`.google.container.v1.MasterAuth master_auth = 5;`

**Returns**  
---  
**Type** | **Description**  
`[MasterAuth](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuth)` | The masterAuth.  
  
### getMasterAuthOrBuilder()
    
    
    public abstract MasterAuthOrBuilder getMasterAuthOrBuilder()

The authentication information for accessing the master endpoint. If unspecified, the defaults are used: For clusters before v1.12, if master_auth is unspecified, `username` will be set to "admin", a random password will be generated, and a client certificate will be issued.

`.google.container.v1.MasterAuth master_auth = 5;`

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthOrBuilder)` |   
  
### getMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public abstract MasterAuthorizedNetworksConfig getMasterAuthorizedNetworksConfig()

**Deprecated.** _google.container.v1.Cluster.master_authorized_networks_config is deprecated. See google/container/v1/cluster_service.proto;l=3054_

The configuration options for master authorized networks feature.

Deprecated: Use ControlPlaneEndpointsConfig.IPEndpointsConfig.authorized_networks_config instead.

` .google.container.v1.MasterAuthorizedNetworksConfig master_authorized_networks_config = 22 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthorizedNetworksConfig)` | The masterAuthorizedNetworksConfig.  
  
### getMasterAuthorizedNetworksConfigOrBuilder() (deprecated)
    
    
    public abstract MasterAuthorizedNetworksConfigOrBuilder getMasterAuthorizedNetworksConfigOrBuilder()

The configuration options for master authorized networks feature.

Deprecated: Use ControlPlaneEndpointsConfig.IPEndpointsConfig.authorized_networks_config instead.

` .google.container.v1.MasterAuthorizedNetworksConfig master_authorized_networks_config = 22 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthorizedNetworksConfigOrBuilder)` |   
  
### getMeshCertificates()
    
    
    public abstract MeshCertificates getMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1.MeshCertificates mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MeshCertificates)` | The meshCertificates.  
  
### getMeshCertificatesOrBuilder()
    
    
    public abstract MeshCertificatesOrBuilder getMeshCertificatesOrBuilder()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1.MeshCertificates mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificatesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MeshCertificatesOrBuilder)` |   
  
### getMonitoringConfig()
    
    
    public abstract MonitoringConfig getMonitoringConfig()

Monitoring configuration for the cluster.

`.google.container.v1.MonitoringConfig monitoring_config = 133;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MonitoringConfig)` | The monitoringConfig.  
  
### getMonitoringConfigOrBuilder()
    
    
    public abstract MonitoringConfigOrBuilder getMonitoringConfigOrBuilder()

Monitoring configuration for the cluster.

`.google.container.v1.MonitoringConfig monitoring_config = 133;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MonitoringConfigOrBuilder)` |   
  
### getMonitoringService()
    
    
    public abstract String getMonitoringService()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string monitoring_service = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The monitoringService.  
  
### getMonitoringServiceBytes()
    
    
    public abstract ByteString getMonitoringServiceBytes()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string monitoring_service = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for monitoringService.  
  
### getName()
    
    
    public abstract String getName()

The name of this cluster. The name must be unique within this project and location (e.g. zone or region), and can be up to 40 characters with the following restrictions:

  * Lowercase letters, numbers, and hyphens only.
  * Must start with a letter.
  * Must end with a number or a letter.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The name of this cluster. The name must be unique within this project and location (e.g. zone or region), and can be up to 40 characters with the following restrictions:

  * Lowercase letters, numbers, and hyphens only.
  * Must start with a letter.
  * Must end with a number or a letter.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

The name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. If left unspecified, the `default` network will be used.

`string network = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

The name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. If left unspecified, the `default` network will be used.

`string network = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNetworkConfig()
    
    
    public abstract NetworkConfig getNetworkConfig()

Configuration for cluster networking.

`.google.container.v1.NetworkConfig network_config = 27;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkConfig)` | The networkConfig.  
  
### getNetworkConfigOrBuilder()
    
    
    public abstract NetworkConfigOrBuilder getNetworkConfigOrBuilder()

Configuration for cluster networking.

`.google.container.v1.NetworkConfig network_config = 27;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkConfigOrBuilder)` |   
  
### getNetworkPolicy()
    
    
    public abstract NetworkPolicy getNetworkPolicy()

Configuration options for the NetworkPolicy feature.

`.google.container.v1.NetworkPolicy network_policy = 19;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkPolicy)` | The networkPolicy.  
  
### getNetworkPolicyOrBuilder()
    
    
    public abstract NetworkPolicyOrBuilder getNetworkPolicyOrBuilder()

Configuration options for the NetworkPolicy feature.

`.google.container.v1.NetworkPolicy network_policy = 19;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkPolicyOrBuilder)` |   
  
### getNodeConfig() (deprecated)
    
    
    public abstract NodeConfig getNodeConfig()

**Deprecated.** _google.container.v1.Cluster.node_config is deprecated. See google/container/v1/cluster_service.proto;l=2947_

Parameters used in creating the cluster's nodes. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "initial_node_count") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. For responses, this field will be populated with the node configuration of the first node pool. (For configuration of each node pool, see `node_pool.config`)

If unspecified, the defaults are used. This field is deprecated, use node_pool.config instead.

`.google.container.v1.NodeConfig node_config = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[NodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeConfig)` | The nodeConfig.  
  
### getNodeConfigOrBuilder() (deprecated)
    
    
    public abstract NodeConfigOrBuilder getNodeConfigOrBuilder()

Parameters used in creating the cluster's nodes. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "initial_node_count") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. For responses, this field will be populated with the node configuration of the first node pool. (For configuration of each node pool, see `node_pool.config`)

If unspecified, the defaults are used. This field is deprecated, use node_pool.config instead.

`.google.container.v1.NodeConfig node_config = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[NodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeConfigOrBuilder)` |   
  
### getNodeCreationConfig()
    
    
    public abstract NodeCreationConfig getNodeCreationConfig()

Optional. Configuration for Node Creation Mode.

` .google.container.v1.NodeCreationConfig node_creation_config = 174 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeCreationConfig)` | The nodeCreationConfig.  
  
### getNodeCreationConfigOrBuilder()
    
    
    public abstract NodeCreationConfigOrBuilder getNodeCreationConfigOrBuilder()

Optional. Configuration for Node Creation Mode.

` .google.container.v1.NodeCreationConfig node_creation_config = 174 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeCreationConfigOrBuilder)` |   
  
### getNodeIpv4CidrSize()
    
    
    public abstract int getNodeIpv4CidrSize()

Output only. The size of the address space on each node for hosting containers. This is provisioned from within the `container_ipv4_cidr` range. This field will only be set when cluster is in route-based network mode.

`int32 node_ipv4_cidr_size = 109 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The nodeIpv4CidrSize.  
  
### getNodePoolAutoConfig()
    
    
    public abstract NodePoolAutoConfig getNodePoolAutoConfig()

Node pool configs that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1.NodePoolAutoConfig node_pool_auto_config = 136;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolAutoConfig)` | The nodePoolAutoConfig.  
  
### getNodePoolAutoConfigOrBuilder()
    
    
    public abstract NodePoolAutoConfigOrBuilder getNodePoolAutoConfigOrBuilder()

Node pool configs that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1.NodePoolAutoConfig node_pool_auto_config = 136;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolAutoConfigOrBuilder)` |   
  
### getNodePoolDefaults()
    
    
    public abstract NodePoolDefaults getNodePoolDefaults()

Default NodePool settings for the entire cluster. These settings are overridden if specified on the specific NodePool object.

`optional .google.container.v1.NodePoolDefaults node_pool_defaults = 131;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolDefaults](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolDefaults)` | The nodePoolDefaults.  
  
### getNodePoolDefaultsOrBuilder()
    
    
    public abstract NodePoolDefaultsOrBuilder getNodePoolDefaultsOrBuilder()

Default NodePool settings for the entire cluster. These settings are overridden if specified on the specific NodePool object.

`optional .google.container.v1.NodePoolDefaults node_pool_defaults = 131;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolDefaultsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolDefaultsOrBuilder)` |   
  
### getNodePools(int index)
    
    
    public abstract NodePool getNodePools(int index)

The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified.

`repeated .google.container.v1.NodePool node_pools = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)` |   
  
### getNodePoolsCount()
    
    
    public abstract int getNodePoolsCount()

The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified.

`repeated .google.container.v1.NodePool node_pools = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNodePoolsList()
    
    
    public abstract List<NodePool> getNodePoolsList()

The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified.

`repeated .google.container.v1.NodePool node_pools = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)>` |   
  
### getNodePoolsOrBuilder(int index)
    
    
    public abstract NodePoolOrBuilder getNodePoolsOrBuilder(int index)

The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified.

`repeated .google.container.v1.NodePool node_pools = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NodePoolOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolOrBuilder)` |   
  
### getNodePoolsOrBuilderList()
    
    
    public abstract List<? extends NodePoolOrBuilder> getNodePoolsOrBuilderList()

The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified.

`repeated .google.container.v1.NodePool node_pools = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.NodePoolOrBuilder>` |   
  
### getNotificationConfig()
    
    
    public abstract NotificationConfig getNotificationConfig()

Notification configuration of the cluster.

`.google.container.v1.NotificationConfig notification_config = 49;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NotificationConfig)` | The notificationConfig.  
  
### getNotificationConfigOrBuilder()
    
    
    public abstract NotificationConfigOrBuilder getNotificationConfigOrBuilder()

Notification configuration of the cluster.

`.google.container.v1.NotificationConfig notification_config = 49;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NotificationConfigOrBuilder)` |   
  
### getPodAutoscaling()
    
    
    public abstract PodAutoscaling getPodAutoscaling()

The config for pod autoscaling.

`.google.container.v1.PodAutoscaling pod_autoscaling = 138;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodAutoscaling)` | The podAutoscaling.  
  
### getPodAutoscalingOrBuilder()
    
    
    public abstract PodAutoscalingOrBuilder getPodAutoscalingOrBuilder()

The config for pod autoscaling.

`.google.container.v1.PodAutoscaling pod_autoscaling = 138;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodAutoscalingOrBuilder)` |   
  
### getPrivateClusterConfig()
    
    
    public abstract PrivateClusterConfig getPrivateClusterConfig()

Configuration for private cluster.

`.google.container.v1.PrivateClusterConfig private_cluster_config = 37;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivateClusterConfig)` | The privateClusterConfig.  
  
### getPrivateClusterConfigOrBuilder()
    
    
    public abstract PrivateClusterConfigOrBuilder getPrivateClusterConfigOrBuilder()

Configuration for private cluster.

`.google.container.v1.PrivateClusterConfig private_cluster_config = 37;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PrivateClusterConfigOrBuilder)` |   
  
### getRbacBindingConfig()
    
    
    public abstract RBACBindingConfig getRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1.RBACBindingConfig rbac_binding_config = 156;`

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RBACBindingConfig)` | The rbacBindingConfig.  
  
### getRbacBindingConfigOrBuilder()
    
    
    public abstract RBACBindingConfigOrBuilder getRbacBindingConfigOrBuilder()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1.RBACBindingConfig rbac_binding_config = 156;`

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RBACBindingConfigOrBuilder)` |   
  
### getReleaseChannel()
    
    
    public abstract ReleaseChannel getReleaseChannel()

Release channel configuration. If left unspecified on cluster creation and a version is specified, the cluster is enrolled in the most mature release channel where the version is available (first checking STABLE, then REGULAR, and finally RAPID). Otherwise, if no release channel configuration and no version is specified, the cluster is enrolled in the REGULAR channel with its default version.

`.google.container.v1.ReleaseChannel release_channel = 41;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ReleaseChannel)` | The releaseChannel.  
  
### getReleaseChannelOrBuilder()
    
    
    public abstract ReleaseChannelOrBuilder getReleaseChannelOrBuilder()

Release channel configuration. If left unspecified on cluster creation and a version is specified, the cluster is enrolled in the most mature release channel where the version is available (first checking STABLE, then REGULAR, and finally RAPID). Otherwise, if no release channel configuration and no version is specified, the cluster is enrolled in the REGULAR channel with its default version.

`.google.container.v1.ReleaseChannel release_channel = 41;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannelOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ReleaseChannelOrBuilder)` |   
  
### getResourceLabels() (deprecated)
    
    
    public abstract Map<String,String> getResourceLabels()

Use [#getResourceLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterOrBuilder#com_google_container_v1_ClusterOrBuilder_getResourceLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourceLabelsCount()
    
    
    public abstract int getResourceLabelsCount()

The resource labels for the cluster to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 15;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourceLabelsMap()
    
    
    public abstract Map<String,String> getResourceLabelsMap()

The resource labels for the cluster to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 15;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourceLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getResourceLabelsOrDefault(String key, String defaultValue)

The resource labels for the cluster to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 15;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourceLabelsOrThrow(String key)
    
    
    public abstract String getResourceLabelsOrThrow(String key)

The resource labels for the cluster to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 15;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourceUsageExportConfig()
    
    
    public abstract ResourceUsageExportConfig getResourceUsageExportConfig()

Configuration for exporting resource usages. Resource usage export is disabled when this config is unspecified.

`.google.container.v1.ResourceUsageExportConfig resource_usage_export_config = 33;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceUsageExportConfig)` | The resourceUsageExportConfig.  
  
### getResourceUsageExportConfigOrBuilder()
    
    
    public abstract ResourceUsageExportConfigOrBuilder getResourceUsageExportConfigOrBuilder()

Configuration for exporting resource usages. Resource usage export is disabled when this config is unspecified.

`.google.container.v1.ResourceUsageExportConfig resource_usage_export_config = 33;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceUsageExportConfigOrBuilder)` |   
  
### getRollbackSafeUpgrade()
    
    
    public abstract RollbackSafeUpgrade getRollbackSafeUpgrade()

Optional. The rollback safe upgrade information of the cluster. This field is used when user manually triggers a rollback safe upgrade.

` .google.container.v1.RollbackSafeUpgrade rollback_safe_upgrade = 170 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgrade](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackSafeUpgrade)` | The rollbackSafeUpgrade.  
  
### getRollbackSafeUpgradeOrBuilder()
    
    
    public abstract RollbackSafeUpgradeOrBuilder getRollbackSafeUpgradeOrBuilder()

Optional. The rollback safe upgrade information of the cluster. This field is used when user manually triggers a rollback safe upgrade.

` .google.container.v1.RollbackSafeUpgrade rollback_safe_upgrade = 170 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgradeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackSafeUpgradeOrBuilder)` |   
  
### getSatisfiesPzi()
    
    
    public abstract boolean getSatisfiesPzi()

Output only. Reserved for future use.

`optional bool satisfies_pzi = 153 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public abstract boolean getSatisfiesPzs()

Output only. Reserved for future use.

`optional bool satisfies_pzs = 152 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getScheduleUpgradeConfig()
    
    
    public abstract ScheduleUpgradeConfig getScheduleUpgradeConfig()

Optional. Configuration for scheduled upgrades.

` .google.container.v1.ScheduleUpgradeConfig schedule_upgrade_config = 165 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ScheduleUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ScheduleUpgradeConfig)` | The scheduleUpgradeConfig.  
  
### getScheduleUpgradeConfigOrBuilder()
    
    
    public abstract ScheduleUpgradeConfigOrBuilder getScheduleUpgradeConfigOrBuilder()

Optional. Configuration for scheduled upgrades.

` .google.container.v1.ScheduleUpgradeConfig schedule_upgrade_config = 165 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ScheduleUpgradeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ScheduleUpgradeConfigOrBuilder)` |   
  
### getSecretManagerConfig()
    
    
    public abstract SecretManagerConfig getSecretManagerConfig()

Secret CSI driver configuration.

`.google.container.v1.SecretManagerConfig secret_manager_config = 150;`

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretManagerConfig)` | The secretManagerConfig.  
  
### getSecretManagerConfigOrBuilder()
    
    
    public abstract SecretManagerConfigOrBuilder getSecretManagerConfigOrBuilder()

Secret CSI driver configuration.

`.google.container.v1.SecretManagerConfig secret_manager_config = 150;`

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretManagerConfigOrBuilder)` |   
  
### getSecretSyncConfig()
    
    
    public abstract SecretSyncConfig getSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1.SecretSyncConfig secret_sync_config = 166;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretSyncConfig)` | The secretSyncConfig.  
  
### getSecretSyncConfigOrBuilder()
    
    
    public abstract SecretSyncConfigOrBuilder getSecretSyncConfigOrBuilder()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1.SecretSyncConfig secret_sync_config = 166;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecretSyncConfigOrBuilder)` |   
  
### getSecurityPostureConfig()
    
    
    public abstract SecurityPostureConfig getSecurityPostureConfig()

Optional. Enable/Disable Security Posture API features for the cluster.

` .google.container.v1.SecurityPostureConfig security_posture_config = 145 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecurityPostureConfig)` | The securityPostureConfig.  
  
### getSecurityPostureConfigOrBuilder()
    
    
    public abstract SecurityPostureConfigOrBuilder getSecurityPostureConfigOrBuilder()

Optional. Enable/Disable Security Posture API features for the cluster.

` .google.container.v1.SecurityPostureConfig security_posture_config = 145 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SecurityPostureConfigOrBuilder)` |   
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. Server-defined URL for the resource.

`string self_link = 100 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. Server-defined URL for the resource.

`string self_link = 100 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getServicesIpv4Cidr()
    
    
    public abstract String getServicesIpv4Cidr()

Output only. The IP address range of the Kubernetes services in this cluster, in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last `/16` from the container CIDR.

`string services_ipv4_cidr = 110 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servicesIpv4Cidr.  
  
### getServicesIpv4CidrBytes()
    
    
    public abstract ByteString getServicesIpv4CidrBytes()

Output only. The IP address range of the Kubernetes services in this cluster, in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last `/16` from the container CIDR.

`string services_ipv4_cidr = 110 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servicesIpv4Cidr.  
  
### getShieldedNodes()
    
    
    public abstract ShieldedNodes getShieldedNodes()

Shielded Nodes configuration.

`.google.container.v1.ShieldedNodes shielded_nodes = 40;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ShieldedNodes)` | The shieldedNodes.  
  
### getShieldedNodesOrBuilder()
    
    
    public abstract ShieldedNodesOrBuilder getShieldedNodesOrBuilder()

Shielded Nodes configuration.

`.google.container.v1.ShieldedNodes shielded_nodes = 40;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ShieldedNodesOrBuilder)` |   
  
### getStatus()
    
    
    public abstract Cluster.Status getStatus()

Output only. The current status of this cluster.

` .google.container.v1.Cluster.Status status = 107 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster.Status)` | The status.  
  
### getStatusMessage() (deprecated)
    
    
    public abstract String getStatusMessage()

**Deprecated.** _google.container.v1.Cluster.status_message is deprecated. See google/container/v1/cluster_service.proto;l=3187_

Output only. Deprecated. Use conditions instead. Additional information about the current status of this cluster, if available.

` string status_message = 108 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The statusMessage.  
  
### getStatusMessageBytes() (deprecated)
    
    
    public abstract ByteString getStatusMessageBytes()

**Deprecated.** _google.container.v1.Cluster.status_message is deprecated. See google/container/v1/cluster_service.proto;l=3187_

Output only. Deprecated. Use conditions instead. Additional information about the current status of this cluster, if available.

` string status_message = 108 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for statusMessage.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Output only. The current status of this cluster.

` .google.container.v1.Cluster.Status status = 107 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getSubnetwork()
    
    
    public abstract String getSubnetwork()

The name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/subnetworks) to which the cluster is connected.

`string subnetwork = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetwork.  
  
### getSubnetworkBytes()
    
    
    public abstract ByteString getSubnetworkBytes()

The name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/subnetworks) to which the cluster is connected.

`string subnetwork = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetwork.  
  
### getTpuIpv4CidrBlock() (deprecated)
    
    
    public abstract String getTpuIpv4CidrBlock()

**Deprecated.** _google.container.v1.Cluster.tpu_ipv4_cidr_block is deprecated. See google/container/v1/cluster_service.proto;l=3233_

Output only. The IP address range of the Cloud TPUs in this cluster, in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

` string tpu_ipv4_cidr_block = 116 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tpuIpv4CidrBlock.  
  
### getTpuIpv4CidrBlockBytes() (deprecated)
    
    
    public abstract ByteString getTpuIpv4CidrBlockBytes()

**Deprecated.** _google.container.v1.Cluster.tpu_ipv4_cidr_block is deprecated. See google/container/v1/cluster_service.proto;l=3233_

Output only. The IP address range of the Cloud TPUs in this cluster, in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

` string tpu_ipv4_cidr_block = 116 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tpuIpv4CidrBlock.  
  
### getUserManagedKeysConfig()
    
    
    public abstract UserManagedKeysConfig getUserManagedKeysConfig()

The Custom keys configuration for the cluster.

`optional .google.container.v1.UserManagedKeysConfig user_managed_keys_config = 154; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UserManagedKeysConfig)` | The userManagedKeysConfig.  
  
### getUserManagedKeysConfigOrBuilder()
    
    
    public abstract UserManagedKeysConfigOrBuilder getUserManagedKeysConfigOrBuilder()

The Custom keys configuration for the cluster.

`optional .google.container.v1.UserManagedKeysConfig user_managed_keys_config = 154; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UserManagedKeysConfigOrBuilder)` |   
  
### getVerticalPodAutoscaling()
    
    
    public abstract VerticalPodAutoscaling getVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1.VerticalPodAutoscaling vertical_pod_autoscaling = 39;`

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.VerticalPodAutoscaling)` | The verticalPodAutoscaling.  
  
### getVerticalPodAutoscalingOrBuilder()
    
    
    public abstract VerticalPodAutoscalingOrBuilder getVerticalPodAutoscalingOrBuilder()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1.VerticalPodAutoscaling vertical_pod_autoscaling = 39;`

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.VerticalPodAutoscalingOrBuilder)` |   
  
### getWorkloadIdentityConfig()
    
    
    public abstract WorkloadIdentityConfig getWorkloadIdentityConfig()

Configuration for the use of Kubernetes Service Accounts in IAM policies.

`.google.container.v1.WorkloadIdentityConfig workload_identity_config = 43;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.WorkloadIdentityConfig)` | The workloadIdentityConfig.  
  
### getWorkloadIdentityConfigOrBuilder()
    
    
    public abstract WorkloadIdentityConfigOrBuilder getWorkloadIdentityConfigOrBuilder()

Configuration for the use of Kubernetes Service Accounts in IAM policies.

`.google.container.v1.WorkloadIdentityConfig workload_identity_config = 43;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.WorkloadIdentityConfigOrBuilder)` |   
  
### getZone() (deprecated)
    
    
    public abstract String getZone()

**Deprecated.** _google.container.v1.Cluster.zone is deprecated. See google/container/v1/cluster_service.proto;l=3128_

Output only. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field is deprecated, use location instead.

`string zone = 101 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes() (deprecated)
    
    
    public abstract ByteString getZoneBytes()

**Deprecated.** _google.container.v1.Cluster.zone is deprecated. See google/container/v1/cluster_service.proto;l=3128_

Output only. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field is deprecated, use location instead.

`string zone = 101 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasAddonsConfig()
    
    
    public abstract boolean hasAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1.AddonsConfig addons_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the addonsConfig field is set.  
  
### hasAnonymousAuthenticationConfig()
    
    
    public abstract boolean hasAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

`.google.container.v1.AnonymousAuthenticationConfig anonymous_authentication_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the anonymousAuthenticationConfig field is set.  
  
### hasAuthenticatorGroupsConfig()
    
    
    public abstract boolean hasAuthenticatorGroupsConfig()

Configuration controlling RBAC group membership information.

`.google.container.v1.AuthenticatorGroupsConfig authenticator_groups_config = 34;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the authenticatorGroupsConfig field is set.  
  
### hasAutopilot()
    
    
    public abstract boolean hasAutopilot()

Autopilot configuration for the cluster.

`.google.container.v1.Autopilot autopilot = 128;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autopilot field is set.  
  
### hasAutoscaling()
    
    
    public abstract boolean hasAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1.ClusterAutoscaling autoscaling = 26;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoscaling field is set.  
  
### hasBinaryAuthorization()
    
    
    public abstract boolean hasBinaryAuthorization()

Configuration for Binary Authorization.

`.google.container.v1.BinaryAuthorization binary_authorization = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the binaryAuthorization field is set.  
  
### hasCompliancePostureConfig() (deprecated)
    
    
    public abstract boolean hasCompliancePostureConfig()

**Deprecated.** _google.container.v1.Cluster.compliance_posture_config is deprecated. See google/container/v1/cluster_service.proto;l=3294_

Optional. Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` .google.container.v1.CompliancePostureConfig compliance_posture_config = 151 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the compliancePostureConfig field is set.  
  
### hasConfidentialNodes()
    
    
    public abstract boolean hasConfidentialNodes()

Configuration of Confidential Nodes. All the nodes in the cluster will be Confidential VM once enabled.

`.google.container.v1.ConfidentialNodes confidential_nodes = 50;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the confidentialNodes field is set.  
  
### hasControlPlaneEgress()
    
    
    public abstract boolean hasControlPlaneEgress()

Configuration for control plane egress control.

`.google.container.v1.ControlPlaneEgress control_plane_egress = 169;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the controlPlaneEgress field is set.  
  
### hasControlPlaneEndpointsConfig()
    
    
    public abstract boolean hasControlPlaneEndpointsConfig()

Configuration for all cluster's control plane endpoints.

`.google.container.v1.ControlPlaneEndpointsConfig control_plane_endpoints_config = 146; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the controlPlaneEndpointsConfig field is set.  
  
### hasCostManagementConfig()
    
    
    public abstract boolean hasCostManagementConfig()

Configuration for the fine-grained cost management feature.

`.google.container.v1.CostManagementConfig cost_management_config = 45;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the costManagementConfig field is set.  
  
### hasDatabaseEncryption()
    
    
    public abstract boolean hasDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1.DatabaseEncryption database_encryption = 38;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the databaseEncryption field is set.  
  
### hasDefaultMaxPodsConstraint()
    
    
    public abstract boolean hasDefaultMaxPodsConstraint()

The default constraint on the maximum number of pods that can be run simultaneously on a node in the node pool of this cluster. Only honored if cluster created with IP Alias support.

`.google.container.v1.MaxPodsConstraint default_max_pods_constraint = 30;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the defaultMaxPodsConstraint field is set.  
  
### hasEnableK8SBetaApis()
    
    
    public abstract boolean hasEnableK8SBetaApis()

Beta APIs Config

`.google.container.v1.K8sBetaAPIConfig enable_k8s_beta_apis = 143;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enableK8sBetaApis field is set.  
  
### hasEnterpriseConfig() (deprecated)
    
    
    public abstract boolean hasEnterpriseConfig()

**Deprecated.** _google.container.v1.Cluster.enterprise_config is deprecated. See google/container/v1/cluster_service.proto;l=3284_

GKE Enterprise Configuration.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

`.google.container.v1.EnterpriseConfig enterprise_config = 149 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enterpriseConfig field is set.  
  
### hasFleet()
    
    
    public abstract boolean hasFleet()

Fleet information for the cluster.

`.google.container.v1.Fleet fleet = 140;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fleet field is set.  
  
### hasGkeAutoUpgradeConfig()
    
    
    public abstract boolean hasGkeAutoUpgradeConfig()

Configuration for GKE auto upgrades.

`.google.container.v1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 163;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gkeAutoUpgradeConfig field is set.  
  
### hasIdentityServiceConfig()
    
    
    public abstract boolean hasIdentityServiceConfig()

Configuration for Identity Service component.

`.google.container.v1.IdentityServiceConfig identity_service_config = 54;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the identityServiceConfig field is set.  
  
### hasIpAllocationPolicy()
    
    
    public abstract boolean hasIpAllocationPolicy()

Configuration for cluster IP allocation.

`.google.container.v1.IPAllocationPolicy ip_allocation_policy = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ipAllocationPolicy field is set.  
  
### hasLegacyAbac()
    
    
    public abstract boolean hasLegacyAbac()

Configuration for the legacy ABAC authorization mode.

`.google.container.v1.LegacyAbac legacy_abac = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the legacyAbac field is set.  
  
### hasLoggingConfig()
    
    
    public abstract boolean hasLoggingConfig()

Logging configuration for the cluster.

`.google.container.v1.LoggingConfig logging_config = 132;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loggingConfig field is set.  
  
### hasMaintenancePolicy()
    
    
    public abstract boolean hasMaintenancePolicy()

Configure the maintenance policy for this cluster.

`.google.container.v1.MaintenancePolicy maintenance_policy = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenancePolicy field is set.  
  
### hasManagedMachineLearningDiagnosticsConfig()
    
    
    public abstract boolean hasManagedMachineLearningDiagnosticsConfig()

Configuration for Managed Machine Learning Diagnostics.

` .google.container.v1.ManagedMachineLearningDiagnosticsConfig managed_machine_learning_diagnostics_config = 171; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the managedMachineLearningDiagnosticsConfig field is set.  
  
### hasManagedOpentelemetryConfig()
    
    
    public abstract boolean hasManagedOpentelemetryConfig()

Configuration for Managed OpenTelemetry pipeline.

`.google.container.v1.ManagedOpenTelemetryConfig managed_opentelemetry_config = 168; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the managedOpentelemetryConfig field is set.  
  
### hasMasterAuth()
    
    
    public abstract boolean hasMasterAuth()

The authentication information for accessing the master endpoint. If unspecified, the defaults are used: For clusters before v1.12, if master_auth is unspecified, `username` will be set to "admin", a random password will be generated, and a client certificate will be issued.

`.google.container.v1.MasterAuth master_auth = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the masterAuth field is set.  
  
### hasMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public abstract boolean hasMasterAuthorizedNetworksConfig()

**Deprecated.** _google.container.v1.Cluster.master_authorized_networks_config is deprecated. See google/container/v1/cluster_service.proto;l=3054_

The configuration options for master authorized networks feature.

Deprecated: Use ControlPlaneEndpointsConfig.IPEndpointsConfig.authorized_networks_config instead.

` .google.container.v1.MasterAuthorizedNetworksConfig master_authorized_networks_config = 22 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the masterAuthorizedNetworksConfig field is set.  
  
### hasMeshCertificates()
    
    
    public abstract boolean hasMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1.MeshCertificates mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the meshCertificates field is set.  
  
### hasMonitoringConfig()
    
    
    public abstract boolean hasMonitoringConfig()

Monitoring configuration for the cluster.

`.google.container.v1.MonitoringConfig monitoring_config = 133;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monitoringConfig field is set.  
  
### hasNetworkConfig()
    
    
    public abstract boolean hasNetworkConfig()

Configuration for cluster networking.

`.google.container.v1.NetworkConfig network_config = 27;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkConfig field is set.  
  
### hasNetworkPolicy()
    
    
    public abstract boolean hasNetworkPolicy()

Configuration options for the NetworkPolicy feature.

`.google.container.v1.NetworkPolicy network_policy = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkPolicy field is set.  
  
### hasNodeConfig() (deprecated)
    
    
    public abstract boolean hasNodeConfig()

**Deprecated.** _google.container.v1.Cluster.node_config is deprecated. See google/container/v1/cluster_service.proto;l=2947_

Parameters used in creating the cluster's nodes. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "initial_node_count") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. For responses, this field will be populated with the node configuration of the first node pool. (For configuration of each node pool, see `node_pool.config`)

If unspecified, the defaults are used. This field is deprecated, use node_pool.config instead.

`.google.container.v1.NodeConfig node_config = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeConfig field is set.  
  
### hasNodeCreationConfig()
    
    
    public abstract boolean hasNodeCreationConfig()

Optional. Configuration for Node Creation Mode.

` .google.container.v1.NodeCreationConfig node_creation_config = 174 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeCreationConfig field is set.  
  
### hasNodePoolAutoConfig()
    
    
    public abstract boolean hasNodePoolAutoConfig()

Node pool configs that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1.NodePoolAutoConfig node_pool_auto_config = 136;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodePoolAutoConfig field is set.  
  
### hasNodePoolDefaults()
    
    
    public abstract boolean hasNodePoolDefaults()

Default NodePool settings for the entire cluster. These settings are overridden if specified on the specific NodePool object.

`optional .google.container.v1.NodePoolDefaults node_pool_defaults = 131;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodePoolDefaults field is set.  
  
### hasNotificationConfig()
    
    
    public abstract boolean hasNotificationConfig()

Notification configuration of the cluster.

`.google.container.v1.NotificationConfig notification_config = 49;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the notificationConfig field is set.  
  
### hasPodAutoscaling()
    
    
    public abstract boolean hasPodAutoscaling()

The config for pod autoscaling.

`.google.container.v1.PodAutoscaling pod_autoscaling = 138;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the podAutoscaling field is set.  
  
### hasPrivateClusterConfig()
    
    
    public abstract boolean hasPrivateClusterConfig()

Configuration for private cluster.

`.google.container.v1.PrivateClusterConfig private_cluster_config = 37;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateClusterConfig field is set.  
  
### hasRbacBindingConfig()
    
    
    public abstract boolean hasRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1.RBACBindingConfig rbac_binding_config = 156;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rbacBindingConfig field is set.  
  
### hasReleaseChannel()
    
    
    public abstract boolean hasReleaseChannel()

Release channel configuration. If left unspecified on cluster creation and a version is specified, the cluster is enrolled in the most mature release channel where the version is available (first checking STABLE, then REGULAR, and finally RAPID). Otherwise, if no release channel configuration and no version is specified, the cluster is enrolled in the REGULAR channel with its default version.

`.google.container.v1.ReleaseChannel release_channel = 41;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the releaseChannel field is set.  
  
### hasResourceUsageExportConfig()
    
    
    public abstract boolean hasResourceUsageExportConfig()

Configuration for exporting resource usages. Resource usage export is disabled when this config is unspecified.

`.google.container.v1.ResourceUsageExportConfig resource_usage_export_config = 33;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resourceUsageExportConfig field is set.  
  
### hasRollbackSafeUpgrade()
    
    
    public abstract boolean hasRollbackSafeUpgrade()

Optional. The rollback safe upgrade information of the cluster. This field is used when user manually triggers a rollback safe upgrade.

` .google.container.v1.RollbackSafeUpgrade rollback_safe_upgrade = 170 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rollbackSafeUpgrade field is set.  
  
### hasSatisfiesPzi()
    
    
    public abstract boolean hasSatisfiesPzi()

Output only. Reserved for future use.

`optional bool satisfies_pzi = 153 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzi field is set.  
  
### hasSatisfiesPzs()
    
    
    public abstract boolean hasSatisfiesPzs()

Output only. Reserved for future use.

`optional bool satisfies_pzs = 152 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzs field is set.  
  
### hasScheduleUpgradeConfig()
    
    
    public abstract boolean hasScheduleUpgradeConfig()

Optional. Configuration for scheduled upgrades.

` .google.container.v1.ScheduleUpgradeConfig schedule_upgrade_config = 165 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the scheduleUpgradeConfig field is set.  
  
### hasSecretManagerConfig()
    
    
    public abstract boolean hasSecretManagerConfig()

Secret CSI driver configuration.

`.google.container.v1.SecretManagerConfig secret_manager_config = 150;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the secretManagerConfig field is set.  
  
### hasSecretSyncConfig()
    
    
    public abstract boolean hasSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1.SecretSyncConfig secret_sync_config = 166;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the secretSyncConfig field is set.  
  
### hasSecurityPostureConfig()
    
    
    public abstract boolean hasSecurityPostureConfig()

Optional. Enable/Disable Security Posture API features for the cluster.

` .google.container.v1.SecurityPostureConfig security_posture_config = 145 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the securityPostureConfig field is set.  
  
### hasShieldedNodes()
    
    
    public abstract boolean hasShieldedNodes()

Shielded Nodes configuration.

`.google.container.v1.ShieldedNodes shielded_nodes = 40;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shieldedNodes field is set.  
  
### hasUserManagedKeysConfig()
    
    
    public abstract boolean hasUserManagedKeysConfig()

The Custom keys configuration for the cluster.

`optional .google.container.v1.UserManagedKeysConfig user_managed_keys_config = 154; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userManagedKeysConfig field is set.  
  
### hasVerticalPodAutoscaling()
    
    
    public abstract boolean hasVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1.VerticalPodAutoscaling vertical_pod_autoscaling = 39;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the verticalPodAutoscaling field is set.  
  
### hasWorkloadIdentityConfig()
    
    
    public abstract boolean hasWorkloadIdentityConfig()

Configuration for the use of Kubernetes Service Accounts in IAM policies.

`.google.container.v1.WorkloadIdentityConfig workload_identity_config = 43;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the workloadIdentityConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
