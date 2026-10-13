---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation.Types.Type
title: Google Kubernetes Engine v1 API - Enum Operation.Types.Type (3.40.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:19.003725+00:00
---

# Google Kubernetes Engine v1 API - Enum Operation.Types.Type (3.40.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation.Types.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Kubernetes Engine v1 API - Enum Operation.Types.Type (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public enum Operation.Types.Type

Reference documentation and code samples for the Google Kubernetes Engine v1 API enum Operation.Types.Type.

Operation type categorizes the operation.

## Namespace

[Google.Cloud.Container.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1)

## Assembly

Google.Cloud.Container.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`AutoRepairNodes` | A problem has been detected with nodes and [they are being repaired](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair). This operation type is initiated by GKE, typically automatically. This operation may be concurrent with other operations and there may be multiple repairs occurring on the same node pool.  
`AutoUpgradeNodes` | Unused. Automatic node upgrade uses [UPGRADE_NODES][google.container.v1.Operation.Type.UPGRADE_NODES].  
`CreateCluster` | The cluster is being created. The cluster should be assumed to be unusable until the operation finishes. In the event of the operation failing, the cluster will enter the [ERROR state][google.container.v1.Cluster.Status.ERROR] and eventually be deleted.  
`CreateNodePool` | A node pool is being created. The node pool should be assumed to be unusable until this operation finishes. In the event of an error, the node pool may be partially created. If enabled, [node autoprovisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) may have automatically initiated such operations.  
`DeleteCluster` | The cluster is being deleted. The cluster should be assumed to be unusable as soon as this operation starts. In the event of the operation failing, the cluster will enter the [ERROR state][google.container.v1.Cluster.Status.ERROR] and the deletion will be automatically retried until completed.  
`DeleteNodePool` | The node pool is being deleted. The node pool should be assumed to be unusable as soon as this operation starts.  
`FleetFeatureUpgrade` | Fleet features of GKE Enterprise are being upgraded. The cluster should be assumed to be blocked for other upgrades until the operation finishes.  
`RepairCluster` | A problem has been detected with the control plane and is being repaired. This operation type is initiated by GKE. For more details, see [documentation on repairs](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs).  
`ResizeCluster` | The control plane is being resized. This operation type is initiated by GKE. These operations are often performed preemptively to ensure that the control plane has sufficient resources and is not typically an indication of issues. For more details, see [documentation on resizes](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs).  
`SetLabels` | Unused. Updating labels uses [UPDATE_CLUSTER][google.container.v1.Operation.Type.UPDATE_CLUSTER].  
`SetMaintenancePolicy` | Unused. Updating maintenance policy uses [UPDATE_CLUSTER][google.container.v1.Operation.Type.UPDATE_CLUSTER].  
`SetMasterAuth` | Unused. Updating master auth uses [UPDATE_CLUSTER][google.container.v1.Operation.Type.UPDATE_CLUSTER].  
`SetNetworkPolicy` | Unused. Updating network policy uses [UPDATE_CLUSTER][google.container.v1.Operation.Type.UPDATE_CLUSTER].  
`SetNodePoolManagement` | The node pool's [manamagent][google.container.v1.NodePool.management] field is being updated. These operations only update metadata and may be concurrent with most other operations.  
`SetNodePoolSize` | The node pool is being resized. With the exception of resizing to or from size zero, the node pool is generally usable during this operation.  
`Unspecified` | Not set.  
`UpdateCluster` | The cluster is being updated. This is a broad category of operations and includes operations that only change metadata as well as those that must recreate the entire cluster. If the control plane must be recreated, this will cause temporary downtime for zonal clusters. Some features require recreating the nodes as well. Those will be recreated as separate operations and the update may not be completely functional until the node pools recreations finish. Node recreations will generally follow [maintenance policies](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions). Some GKE-initiated operations use this type. This includes certain types of auto-upgrades and incident mitigations.  
`UpgradeMaster` | The [cluster version][google.container.v1.ClusterUpdate.desired_master_version] is being updated. Note that this includes "upgrades" to the same version, which are simply a recreation. This also includes [auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically). For more details, see [documentation on cluster upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#cluster_upgrades).  
`UpgradeNodes` | A node pool is being updated. Despite calling this an "upgrade", this includes most forms of updates to node pools. This also includes [auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades). This operation sets the [progress][google.container.v1.Operation.progress] field and may be [canceled][google.container.v1.ClusterManager.CancelOperation]. The upgrade strategy depends on [node pool configuration](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies). The nodes are generally still usable during this operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
