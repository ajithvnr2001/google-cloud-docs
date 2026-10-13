---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.MembershipSpecOrBuilder
title: Interface MembershipSpecOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:13.312245+00:00
---

# Interface MembershipSpecOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.MembershipSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MembershipSpecOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.6  1.2.1  1.1.0  1.0.1  0.5.4 
    
    
    public interface MembershipSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBinauthz() (deprecated)
    
    
    public abstract BinauthzConfig getBinauthz()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.binauthz is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=109_

Optional. Deprecated: Binauthz configuration will be ignored and should not be set.

` .google.cloud.gkehub.configmanagement.v1beta.BinauthzConfig binauthz = 3 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BinauthzConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.BinauthzConfig)` | The binauthz.  
  
### getBinauthzOrBuilder() (deprecated)
    
    
    public abstract BinauthzConfigOrBuilder getBinauthzOrBuilder()

Optional. Deprecated: Binauthz configuration will be ignored and should not be set.

` .google.cloud.gkehub.configmanagement.v1beta.BinauthzConfig binauthz = 3 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BinauthzConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.BinauthzConfigOrBuilder)` |   
  
### getCluster()
    
    
    public abstract String getCluster()

Optional. User-specified cluster name used by the Config Sync cluster-name-selector annotation or ClusterSelector object, for applying configs to only a subset of clusters. Read more about the cluster-name-selector annotation and ClusterSelector object at <https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#limiting-configs>. Only set this field if a name different from the cluster's fleet membership name is used by the Config Sync cluster-name-selector annotation or ClusterSelector.

`string cluster = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cluster.  
  
### getClusterBytes()
    
    
    public abstract ByteString getClusterBytes()

Optional. User-specified cluster name used by the Config Sync cluster-name-selector annotation or ClusterSelector object, for applying configs to only a subset of clusters. Read more about the cluster-name-selector annotation and ClusterSelector object at <https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#limiting-configs>. Only set this field if a name different from the cluster's fleet membership name is used by the Config Sync cluster-name-selector annotation or ClusterSelector.

`string cluster = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cluster.  
  
### getConfigSync()
    
    
    public abstract ConfigSync getConfigSync()

Optional. Config Sync configuration for the cluster.

` .google.cloud.gkehub.configmanagement.v1beta.ConfigSync config_sync = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConfigSync](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.ConfigSync)` | The configSync.  
  
### getConfigSyncOrBuilder()
    
    
    public abstract ConfigSyncOrBuilder getConfigSyncOrBuilder()

Optional. Config Sync configuration for the cluster.

` .google.cloud.gkehub.configmanagement.v1beta.ConfigSync config_sync = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConfigSyncOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.ConfigSyncOrBuilder)` |   
  
### getHierarchyController() (deprecated)
    
    
    public abstract HierarchyControllerConfig getHierarchyController()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.hierarchy_controller is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=116_

Optional. Hierarchy Controller configuration for the cluster. Deprecated: Configuring Hierarchy Controller through the configmanagement feature is no longer recommended. Use <https://github.com/kubernetes-sigs/hierarchical-namespaces> instead.

` .google.cloud.gkehub.configmanagement.v1beta.HierarchyControllerConfig hierarchy_controller = 4 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[HierarchyControllerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.HierarchyControllerConfig)` | The hierarchyController.  
  
### getHierarchyControllerOrBuilder() (deprecated)
    
    
    public abstract HierarchyControllerConfigOrBuilder getHierarchyControllerOrBuilder()

Optional. Hierarchy Controller configuration for the cluster. Deprecated: Configuring Hierarchy Controller through the configmanagement feature is no longer recommended. Use <https://github.com/kubernetes-sigs/hierarchical-namespaces> instead.

` .google.cloud.gkehub.configmanagement.v1beta.HierarchyControllerConfig hierarchy_controller = 4 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[HierarchyControllerConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.HierarchyControllerConfigOrBuilder)` |   
  
### getManagement() (deprecated)
    
    
    public abstract MembershipSpec.Management getManagement()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.management is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=137_

Optional. Deprecated: From version 1.21.0, automatic Feature management is unavailable, and Config Sync only supports manual upgrades.

` .google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.Management management = 12 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MembershipSpec.Management](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.Management)` | The management.  
  
### getManagementValue() (deprecated)
    
    
    public abstract int getManagementValue()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.management is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=137_

Optional. Deprecated: From version 1.21.0, automatic Feature management is unavailable, and Config Sync only supports manual upgrades.

` .google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.Management management = 12 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for management.  
  
### getPolicyController() (deprecated)
    
    
    public abstract PolicyController getPolicyController()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.policy_controller is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=104_

Optional. Policy Controller configuration for the cluster. Deprecated: Configuring Policy Controller through the configmanagement feature is no longer recommended. Use the policycontroller feature instead.

` .google.cloud.gkehub.configmanagement.v1beta.PolicyController policy_controller = 2 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyController](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.PolicyController)` | The policyController.  
  
### getPolicyControllerOrBuilder() (deprecated)
    
    
    public abstract PolicyControllerOrBuilder getPolicyControllerOrBuilder()

Optional. Policy Controller configuration for the cluster. Deprecated: Configuring Policy Controller through the configmanagement feature is no longer recommended. Use the policycontroller feature instead.

` .google.cloud.gkehub.configmanagement.v1beta.PolicyController policy_controller = 2 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyControllerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.configmanagement.v1beta.PolicyControllerOrBuilder)` |   
  
### getVersion()
    
    
    public abstract String getVersion()

Optional. Version of Config Sync to install. Defaults to the latest supported Config Sync version if the config_sync field is enabled. See supported versions at <https://cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync#version_support_policy>.

`string version = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The version.  
  
### getVersionBytes()
    
    
    public abstract ByteString getVersionBytes()

Optional. Version of Config Sync to install. Defaults to the latest supported Config Sync version if the config_sync field is enabled. See supported versions at <https://cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync#version_support_policy>.

`string version = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for version.  
  
### hasBinauthz() (deprecated)
    
    
    public abstract boolean hasBinauthz()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.binauthz is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=109_

Optional. Deprecated: Binauthz configuration will be ignored and should not be set.

` .google.cloud.gkehub.configmanagement.v1beta.BinauthzConfig binauthz = 3 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the binauthz field is set.  
  
### hasConfigSync()
    
    
    public abstract boolean hasConfigSync()

Optional. Config Sync configuration for the cluster.

` .google.cloud.gkehub.configmanagement.v1beta.ConfigSync config_sync = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the configSync field is set.  
  
### hasHierarchyController() (deprecated)
    
    
    public abstract boolean hasHierarchyController()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.hierarchy_controller is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=116_

Optional. Hierarchy Controller configuration for the cluster. Deprecated: Configuring Hierarchy Controller through the configmanagement feature is no longer recommended. Use <https://github.com/kubernetes-sigs/hierarchical-namespaces> instead.

` .google.cloud.gkehub.configmanagement.v1beta.HierarchyControllerConfig hierarchy_controller = 4 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hierarchyController field is set.  
  
### hasPolicyController() (deprecated)
    
    
    public abstract boolean hasPolicyController()

**Deprecated.** _google.cloud.gkehub.configmanagement.v1beta.MembershipSpec.policy_controller is deprecated. See google/cloud/gkehub/v1beta/configmanagement/configmanagement.proto;l=104_

Optional. Policy Controller configuration for the cluster. Deprecated: Configuring Policy Controller through the configmanagement feature is no longer recommended. Use the policycontroller feature instead.

` .google.cloud.gkehub.configmanagement.v1beta.PolicyController policy_controller = 2 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policyController field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
