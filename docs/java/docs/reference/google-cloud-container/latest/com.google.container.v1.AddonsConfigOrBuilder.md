---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfigOrBuilder
title: Interface AddonsConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:56.578431+00:00
---

# Interface AddonsConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AddonsConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface AddonsConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAgentSandboxConfig()
    
    
    public abstract AgentSandboxConfig getAgentSandboxConfig()

Optional. Configuration for the AgentSandbox addon.

` .google.container.v1.AgentSandboxConfig agent_sandbox_config = 28 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AgentSandboxConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AgentSandboxConfig)` | The agentSandboxConfig.  
  
### getAgentSandboxConfigOrBuilder()
    
    
    public abstract AgentSandboxConfigOrBuilder getAgentSandboxConfigOrBuilder()

Optional. Configuration for the AgentSandbox addon.

` .google.container.v1.AgentSandboxConfig agent_sandbox_config = 28 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AgentSandboxConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AgentSandboxConfigOrBuilder)` |   
  
### getCloudRunConfig()
    
    
    public abstract CloudRunConfig getCloudRunConfig()

Configuration for the Cloud Run addon, which allows the user to use a managed Knative service.

`.google.container.v1.CloudRunConfig cloud_run_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CloudRunConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CloudRunConfig)` | The cloudRunConfig.  
  
### getCloudRunConfigOrBuilder()
    
    
    public abstract CloudRunConfigOrBuilder getCloudRunConfigOrBuilder()

Configuration for the Cloud Run addon, which allows the user to use a managed Knative service.

`.google.container.v1.CloudRunConfig cloud_run_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CloudRunConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CloudRunConfigOrBuilder)` |   
  
### getConfigConnectorConfig()
    
    
    public abstract ConfigConnectorConfig getConfigConnectorConfig()

Configuration for the ConfigConnector add-on, a Kubernetes extension to manage hosted Google Cloud services through the Kubernetes API.

`.google.container.v1.ConfigConnectorConfig config_connector_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ConfigConnectorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ConfigConnectorConfig)` | The configConnectorConfig.  
  
### getConfigConnectorConfigOrBuilder()
    
    
    public abstract ConfigConnectorConfigOrBuilder getConfigConnectorConfigOrBuilder()

Configuration for the ConfigConnector add-on, a Kubernetes extension to manage hosted Google Cloud services through the Kubernetes API.

`.google.container.v1.ConfigConnectorConfig config_connector_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ConfigConnectorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ConfigConnectorConfigOrBuilder)` |   
  
### getDnsCacheConfig()
    
    
    public abstract DnsCacheConfig getDnsCacheConfig()

Configuration for NodeLocalDNS, a dns cache running on cluster nodes

`.google.container.v1.DnsCacheConfig dns_cache_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DnsCacheConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DnsCacheConfig)` | The dnsCacheConfig.  
  
### getDnsCacheConfigOrBuilder()
    
    
    public abstract DnsCacheConfigOrBuilder getDnsCacheConfigOrBuilder()

Configuration for NodeLocalDNS, a dns cache running on cluster nodes

`.google.container.v1.DnsCacheConfig dns_cache_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DnsCacheConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DnsCacheConfigOrBuilder)` |   
  
### getGcePersistentDiskCsiDriverConfig()
    
    
    public abstract GcePersistentDiskCsiDriverConfig getGcePersistentDiskCsiDriverConfig()

Configuration for the Compute Engine Persistent Disk CSI driver.

` .google.container.v1.GcePersistentDiskCsiDriverConfig gce_persistent_disk_csi_driver_config = 11; `

**Returns**  
---  
**Type** | **Description**  
`[GcePersistentDiskCsiDriverConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcePersistentDiskCsiDriverConfig)` | The gcePersistentDiskCsiDriverConfig.  
  
### getGcePersistentDiskCsiDriverConfigOrBuilder()
    
    
    public abstract GcePersistentDiskCsiDriverConfigOrBuilder getGcePersistentDiskCsiDriverConfigOrBuilder()

Configuration for the Compute Engine Persistent Disk CSI driver.

` .google.container.v1.GcePersistentDiskCsiDriverConfig gce_persistent_disk_csi_driver_config = 11; `

**Returns**  
---  
**Type** | **Description**  
`[GcePersistentDiskCsiDriverConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcePersistentDiskCsiDriverConfigOrBuilder)` |   
  
### getGcpFilestoreCsiDriverConfig()
    
    
    public abstract GcpFilestoreCsiDriverConfig getGcpFilestoreCsiDriverConfig()

Configuration for the Filestore CSI driver.

`.google.container.v1.GcpFilestoreCsiDriverConfig gcp_filestore_csi_driver_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[GcpFilestoreCsiDriverConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcpFilestoreCsiDriverConfig)` | The gcpFilestoreCsiDriverConfig.  
  
### getGcpFilestoreCsiDriverConfigOrBuilder()
    
    
    public abstract GcpFilestoreCsiDriverConfigOrBuilder getGcpFilestoreCsiDriverConfigOrBuilder()

Configuration for the Filestore CSI driver.

`.google.container.v1.GcpFilestoreCsiDriverConfig gcp_filestore_csi_driver_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[GcpFilestoreCsiDriverConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcpFilestoreCsiDriverConfigOrBuilder)` |   
  
### getGcsFuseCsiDriverConfig()
    
    
    public abstract GcsFuseCsiDriverConfig getGcsFuseCsiDriverConfig()

Configuration for the Cloud Storage Fuse CSI driver.

`.google.container.v1.GcsFuseCsiDriverConfig gcs_fuse_csi_driver_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFuseCsiDriverConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcsFuseCsiDriverConfig)` | The gcsFuseCsiDriverConfig.  
  
### getGcsFuseCsiDriverConfigOrBuilder()
    
    
    public abstract GcsFuseCsiDriverConfigOrBuilder getGcsFuseCsiDriverConfigOrBuilder()

Configuration for the Cloud Storage Fuse CSI driver.

`.google.container.v1.GcsFuseCsiDriverConfig gcs_fuse_csi_driver_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFuseCsiDriverConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GcsFuseCsiDriverConfigOrBuilder)` |   
  
### getGkeBackupAgentConfig()
    
    
    public abstract GkeBackupAgentConfig getGkeBackupAgentConfig()

Configuration for the Backup for GKE agent addon.

`.google.container.v1.GkeBackupAgentConfig gke_backup_agent_config = 16;`

**Returns**  
---  
**Type** | **Description**  
`[GkeBackupAgentConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GkeBackupAgentConfig)` | The gkeBackupAgentConfig.  
  
### getGkeBackupAgentConfigOrBuilder()
    
    
    public abstract GkeBackupAgentConfigOrBuilder getGkeBackupAgentConfigOrBuilder()

Configuration for the Backup for GKE agent addon.

`.google.container.v1.GkeBackupAgentConfig gke_backup_agent_config = 16;`

**Returns**  
---  
**Type** | **Description**  
`[GkeBackupAgentConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GkeBackupAgentConfigOrBuilder)` |   
  
### getHighScaleCheckpointingConfig()
    
    
    public abstract HighScaleCheckpointingConfig getHighScaleCheckpointingConfig()

Configuration for the High Scale Checkpointing add-on.

`.google.container.v1.HighScaleCheckpointingConfig high_scale_checkpointing_config = 22; `

**Returns**  
---  
**Type** | **Description**  
`[HighScaleCheckpointingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.HighScaleCheckpointingConfig)` | The highScaleCheckpointingConfig.  
  
### getHighScaleCheckpointingConfigOrBuilder()
    
    
    public abstract HighScaleCheckpointingConfigOrBuilder getHighScaleCheckpointingConfigOrBuilder()

Configuration for the High Scale Checkpointing add-on.

`.google.container.v1.HighScaleCheckpointingConfig high_scale_checkpointing_config = 22; `

**Returns**  
---  
**Type** | **Description**  
`[HighScaleCheckpointingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.HighScaleCheckpointingConfigOrBuilder)` |   
  
### getHorizontalPodAutoscaling()
    
    
    public abstract HorizontalPodAutoscaling getHorizontalPodAutoscaling()

Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods.

`.google.container.v1.HorizontalPodAutoscaling horizontal_pod_autoscaling = 2;`

**Returns**  
---  
**Type** | **Description**  
`[HorizontalPodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.HorizontalPodAutoscaling)` | The horizontalPodAutoscaling.  
  
### getHorizontalPodAutoscalingOrBuilder()
    
    
    public abstract HorizontalPodAutoscalingOrBuilder getHorizontalPodAutoscalingOrBuilder()

Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods.

`.google.container.v1.HorizontalPodAutoscaling horizontal_pod_autoscaling = 2;`

**Returns**  
---  
**Type** | **Description**  
`[HorizontalPodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.HorizontalPodAutoscalingOrBuilder)` |   
  
### getHttpLoadBalancing()
    
    
    public abstract HttpLoadBalancing getHttpLoadBalancing()

Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.

`.google.container.v1.HttpLoadBalancing http_load_balancing = 1;`

**Returns**  
---  
**Type** | **Description**  
`[HttpLoadBalancing](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.HttpLoadBalancing)` | The httpLoadBalancing.  
  
### getHttpLoadBalancingOrBuilder()
    
    
    public abstract HttpLoadBalancingOrBuilder getHttpLoadBalancingOrBuilder()

Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.

`.google.container.v1.HttpLoadBalancing http_load_balancing = 1;`

**Returns**  
---  
**Type** | **Description**  
`[HttpLoadBalancingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.HttpLoadBalancingOrBuilder)` |   
  
### getKubernetesDashboard() (deprecated)
    
    
    public abstract KubernetesDashboard getKubernetesDashboard()

**Deprecated.** _google.container.v1.AddonsConfig.kubernetes_dashboard is deprecated. See google/container/v1/cluster_service.proto;l=2288_

Configuration for the Kubernetes Dashboard. This addon is deprecated, and will be disabled in 1.15. It is recommended to use the Cloud Console to manage and monitor your Kubernetes clusters, workloads and applications. For more information, see: <https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards>

`.google.container.v1.KubernetesDashboard kubernetes_dashboard = 3 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[KubernetesDashboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.KubernetesDashboard)` | The kubernetesDashboard.  
  
### getKubernetesDashboardOrBuilder() (deprecated)
    
    
    public abstract KubernetesDashboardOrBuilder getKubernetesDashboardOrBuilder()

Configuration for the Kubernetes Dashboard. This addon is deprecated, and will be disabled in 1.15. It is recommended to use the Cloud Console to manage and monitor your Kubernetes clusters, workloads and applications. For more information, see: <https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards>

`.google.container.v1.KubernetesDashboard kubernetes_dashboard = 3 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[KubernetesDashboardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.KubernetesDashboardOrBuilder)` |   
  
### getLustreCsiDriverConfig()
    
    
    public abstract LustreCsiDriverConfig getLustreCsiDriverConfig()

Configuration for the Lustre CSI driver.

`.google.container.v1.LustreCsiDriverConfig lustre_csi_driver_config = 23;`

**Returns**  
---  
**Type** | **Description**  
`[LustreCsiDriverConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LustreCsiDriverConfig)` | The lustreCsiDriverConfig.  
  
### getLustreCsiDriverConfigOrBuilder()
    
    
    public abstract LustreCsiDriverConfigOrBuilder getLustreCsiDriverConfigOrBuilder()

Configuration for the Lustre CSI driver.

`.google.container.v1.LustreCsiDriverConfig lustre_csi_driver_config = 23;`

**Returns**  
---  
**Type** | **Description**  
`[LustreCsiDriverConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LustreCsiDriverConfigOrBuilder)` |   
  
### getNetworkPolicyConfig()
    
    
    public abstract NetworkPolicyConfig getNetworkPolicyConfig()

Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes.

`.google.container.v1.NetworkPolicyConfig network_policy_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkPolicyConfig)` | The networkPolicyConfig.  
  
### getNetworkPolicyConfigOrBuilder()
    
    
    public abstract NetworkPolicyConfigOrBuilder getNetworkPolicyConfigOrBuilder()

Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes.

`.google.container.v1.NetworkPolicyConfig network_policy_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkPolicyConfigOrBuilder)` |   
  
### getNodeReadinessConfig()
    
    
    public abstract NodeReadinessConfig getNodeReadinessConfig()

Optional. Configuration for NodeReadinessController add-on.

` .google.container.v1.NodeReadinessConfig node_readiness_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeReadinessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeReadinessConfig)` | The nodeReadinessConfig.  
  
### getNodeReadinessConfigOrBuilder()
    
    
    public abstract NodeReadinessConfigOrBuilder getNodeReadinessConfigOrBuilder()

Optional. Configuration for NodeReadinessController add-on.

` .google.container.v1.NodeReadinessConfig node_readiness_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeReadinessConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeReadinessConfigOrBuilder)` |   
  
### getParallelstoreCsiDriverConfig()
    
    
    public abstract ParallelstoreCsiDriverConfig getParallelstoreCsiDriverConfig()

Configuration for the Cloud Storage Parallelstore CSI driver.

`.google.container.v1.ParallelstoreCsiDriverConfig parallelstore_csi_driver_config = 19; `

**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreCsiDriverConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ParallelstoreCsiDriverConfig)` | The parallelstoreCsiDriverConfig.  
  
### getParallelstoreCsiDriverConfigOrBuilder()
    
    
    public abstract ParallelstoreCsiDriverConfigOrBuilder getParallelstoreCsiDriverConfigOrBuilder()

Configuration for the Cloud Storage Parallelstore CSI driver.

`.google.container.v1.ParallelstoreCsiDriverConfig parallelstore_csi_driver_config = 19; `

**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreCsiDriverConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ParallelstoreCsiDriverConfigOrBuilder)` |   
  
### getPodSnapshotConfig()
    
    
    public abstract PodSnapshotConfig getPodSnapshotConfig()

Optional. Configuration for the Pod Snapshot feature.

` .google.container.v1.PodSnapshotConfig pod_snapshot_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PodSnapshotConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodSnapshotConfig)` | The podSnapshotConfig.  
  
### getPodSnapshotConfigOrBuilder()
    
    
    public abstract PodSnapshotConfigOrBuilder getPodSnapshotConfigOrBuilder()

Optional. Configuration for the Pod Snapshot feature.

` .google.container.v1.PodSnapshotConfig pod_snapshot_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PodSnapshotConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.PodSnapshotConfigOrBuilder)` |   
  
### getRayOperatorConfig()
    
    
    public abstract RayOperatorConfig getRayOperatorConfig()

Optional. Configuration for Ray Operator addon.

` .google.container.v1.RayOperatorConfig ray_operator_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RayOperatorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RayOperatorConfig)` | The rayOperatorConfig.  
  
### getRayOperatorConfigOrBuilder()
    
    
    public abstract RayOperatorConfigOrBuilder getRayOperatorConfigOrBuilder()

Optional. Configuration for Ray Operator addon.

` .google.container.v1.RayOperatorConfig ray_operator_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RayOperatorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RayOperatorConfigOrBuilder)` |   
  
### getSliceControllerConfig()
    
    
    public abstract SliceControllerConfig getSliceControllerConfig()

Optional. Configuration for the slice controller add-on.

` .google.container.v1.SliceControllerConfig slice_controller_config = 26 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SliceControllerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SliceControllerConfig)` | The sliceControllerConfig.  
  
### getSliceControllerConfigOrBuilder()
    
    
    public abstract SliceControllerConfigOrBuilder getSliceControllerConfigOrBuilder()

Optional. Configuration for the slice controller add-on.

` .google.container.v1.SliceControllerConfig slice_controller_config = 26 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SliceControllerConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SliceControllerConfigOrBuilder)` |   
  
### getSlurmOperatorConfig()
    
    
    public abstract SlurmOperatorConfig getSlurmOperatorConfig()

Configuration for the Slurm Operator.

`.google.container.v1.SlurmOperatorConfig slurm_operator_config = 25;`

**Returns**  
---  
**Type** | **Description**  
`[SlurmOperatorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SlurmOperatorConfig)` | The slurmOperatorConfig.  
  
### getSlurmOperatorConfigOrBuilder()
    
    
    public abstract SlurmOperatorConfigOrBuilder getSlurmOperatorConfigOrBuilder()

Configuration for the Slurm Operator.

`.google.container.v1.SlurmOperatorConfig slurm_operator_config = 25;`

**Returns**  
---  
**Type** | **Description**  
`[SlurmOperatorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SlurmOperatorConfigOrBuilder)` |   
  
### getStatefulHaConfig()
    
    
    public abstract StatefulHAConfig getStatefulHaConfig()

Optional. Configuration for the StatefulHA add-on.

` .google.container.v1.StatefulHAConfig stateful_ha_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StatefulHAConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StatefulHAConfig)` | The statefulHaConfig.  
  
### getStatefulHaConfigOrBuilder()
    
    
    public abstract StatefulHAConfigOrBuilder getStatefulHaConfigOrBuilder()

Optional. Configuration for the StatefulHA add-on.

` .google.container.v1.StatefulHAConfig stateful_ha_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StatefulHAConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StatefulHAConfigOrBuilder)` |   
  
### hasAgentSandboxConfig()
    
    
    public abstract boolean hasAgentSandboxConfig()

Optional. Configuration for the AgentSandbox addon.

` .google.container.v1.AgentSandboxConfig agent_sandbox_config = 28 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the agentSandboxConfig field is set.  
  
### hasCloudRunConfig()
    
    
    public abstract boolean hasCloudRunConfig()

Configuration for the Cloud Run addon, which allows the user to use a managed Knative service.

`.google.container.v1.CloudRunConfig cloud_run_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudRunConfig field is set.  
  
### hasConfigConnectorConfig()
    
    
    public abstract boolean hasConfigConnectorConfig()

Configuration for the ConfigConnector add-on, a Kubernetes extension to manage hosted Google Cloud services through the Kubernetes API.

`.google.container.v1.ConfigConnectorConfig config_connector_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the configConnectorConfig field is set.  
  
### hasDnsCacheConfig()
    
    
    public abstract boolean hasDnsCacheConfig()

Configuration for NodeLocalDNS, a dns cache running on cluster nodes

`.google.container.v1.DnsCacheConfig dns_cache_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dnsCacheConfig field is set.  
  
### hasGcePersistentDiskCsiDriverConfig()
    
    
    public abstract boolean hasGcePersistentDiskCsiDriverConfig()

Configuration for the Compute Engine Persistent Disk CSI driver.

` .google.container.v1.GcePersistentDiskCsiDriverConfig gce_persistent_disk_csi_driver_config = 11; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcePersistentDiskCsiDriverConfig field is set.  
  
### hasGcpFilestoreCsiDriverConfig()
    
    
    public abstract boolean hasGcpFilestoreCsiDriverConfig()

Configuration for the Filestore CSI driver.

`.google.container.v1.GcpFilestoreCsiDriverConfig gcp_filestore_csi_driver_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcpFilestoreCsiDriverConfig field is set.  
  
### hasGcsFuseCsiDriverConfig()
    
    
    public abstract boolean hasGcsFuseCsiDriverConfig()

Configuration for the Cloud Storage Fuse CSI driver.

`.google.container.v1.GcsFuseCsiDriverConfig gcs_fuse_csi_driver_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsFuseCsiDriverConfig field is set.  
  
### hasGkeBackupAgentConfig()
    
    
    public abstract boolean hasGkeBackupAgentConfig()

Configuration for the Backup for GKE agent addon.

`.google.container.v1.GkeBackupAgentConfig gke_backup_agent_config = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gkeBackupAgentConfig field is set.  
  
### hasHighScaleCheckpointingConfig()
    
    
    public abstract boolean hasHighScaleCheckpointingConfig()

Configuration for the High Scale Checkpointing add-on.

`.google.container.v1.HighScaleCheckpointingConfig high_scale_checkpointing_config = 22; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the highScaleCheckpointingConfig field is set.  
  
### hasHorizontalPodAutoscaling()
    
    
    public abstract boolean hasHorizontalPodAutoscaling()

Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods.

`.google.container.v1.HorizontalPodAutoscaling horizontal_pod_autoscaling = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the horizontalPodAutoscaling field is set.  
  
### hasHttpLoadBalancing()
    
    
    public abstract boolean hasHttpLoadBalancing()

Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.

`.google.container.v1.HttpLoadBalancing http_load_balancing = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpLoadBalancing field is set.  
  
### hasKubernetesDashboard() (deprecated)
    
    
    public abstract boolean hasKubernetesDashboard()

**Deprecated.** _google.container.v1.AddonsConfig.kubernetes_dashboard is deprecated. See google/container/v1/cluster_service.proto;l=2288_

Configuration for the Kubernetes Dashboard. This addon is deprecated, and will be disabled in 1.15. It is recommended to use the Cloud Console to manage and monitor your Kubernetes clusters, workloads and applications. For more information, see: <https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards>

`.google.container.v1.KubernetesDashboard kubernetes_dashboard = 3 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kubernetesDashboard field is set.  
  
### hasLustreCsiDriverConfig()
    
    
    public abstract boolean hasLustreCsiDriverConfig()

Configuration for the Lustre CSI driver.

`.google.container.v1.LustreCsiDriverConfig lustre_csi_driver_config = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lustreCsiDriverConfig field is set.  
  
### hasNetworkPolicyConfig()
    
    
    public abstract boolean hasNetworkPolicyConfig()

Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes.

`.google.container.v1.NetworkPolicyConfig network_policy_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkPolicyConfig field is set.  
  
### hasNodeReadinessConfig()
    
    
    public abstract boolean hasNodeReadinessConfig()

Optional. Configuration for NodeReadinessController add-on.

` .google.container.v1.NodeReadinessConfig node_readiness_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeReadinessConfig field is set.  
  
### hasParallelstoreCsiDriverConfig()
    
    
    public abstract boolean hasParallelstoreCsiDriverConfig()

Configuration for the Cloud Storage Parallelstore CSI driver.

`.google.container.v1.ParallelstoreCsiDriverConfig parallelstore_csi_driver_config = 19; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parallelstoreCsiDriverConfig field is set.  
  
### hasPodSnapshotConfig()
    
    
    public abstract boolean hasPodSnapshotConfig()

Optional. Configuration for the Pod Snapshot feature.

` .google.container.v1.PodSnapshotConfig pod_snapshot_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the podSnapshotConfig field is set.  
  
### hasRayOperatorConfig()
    
    
    public abstract boolean hasRayOperatorConfig()

Optional. Configuration for Ray Operator addon.

` .google.container.v1.RayOperatorConfig ray_operator_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rayOperatorConfig field is set.  
  
### hasSliceControllerConfig()
    
    
    public abstract boolean hasSliceControllerConfig()

Optional. Configuration for the slice controller add-on.

` .google.container.v1.SliceControllerConfig slice_controller_config = 26 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sliceControllerConfig field is set.  
  
### hasSlurmOperatorConfig()
    
    
    public abstract boolean hasSlurmOperatorConfig()

Configuration for the Slurm Operator.

`.google.container.v1.SlurmOperatorConfig slurm_operator_config = 25;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the slurmOperatorConfig field is set.  
  
### hasStatefulHaConfig()
    
    
    public abstract boolean hasStatefulHaConfig()

Optional. Configuration for the StatefulHA add-on.

` .google.container.v1.StatefulHAConfig stateful_ha_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the statefulHaConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
