---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools
title: REST Resource: projects.zones.clusters.nodePools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:11.130668+00:00
---

# REST Resource: projects.zones.clusters.nodePools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  REST Resource: projects.zones.clusters.nodePools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NodePool
    * JSON representation
  * Methods



## Resource: NodePool

NodePool contains the name and configuration for a cluster's node pool. Node pools are a set of nodes (i.e. VM's), with a common configuration and specification, under the control of the cluster master. They may have a set of Kubernetes labels applied to them, which may be used to reference them during pod scheduling. They may also be resized up or down, to accommodate the workload.

JSON representation  
---  
      
    
    {
      "name": string,
      "config": {
        object ([NodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/NodeConfig))
      },
      "initialNodeCount": integer,
      "locations": [
        string
      ],
      "networkConfig": {
        object ([NodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig))
      },
      "selfLink": string,
      "version": string,
      "instanceGroupUrls": [
        string
      ],
      "status": enum ([Status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.Status)),
      "statusMessage": string,
      "autoscaling": {
        object ([NodePoolAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling))
      },
      "management": {
        object ([NodeManagement](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/NodeManagement))
      },
      "maxPodsConstraint": {
        object ([MaxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/MaxPodsConstraint))
      },
      "conditions": [
        {
          object ([StatusCondition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/StatusCondition))
        }
      ],
      "podIpv4CidrSize": integer,
      "upgradeSettings": {
        object ([UpgradeSettings](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/UpgradeSettings))
      },
      "placementPolicy": {
        object ([PlacementPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy))
      },
      "updateInfo": {
        object ([UpdateInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.UpdateInfo))
      },
      "etag": string,
      "queuedProvisioning": {
        object ([QueuedProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.QueuedProvisioning))
      },
      "bestEffortProvisioning": {
        object ([BestEffortProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.BestEffortProvisioning))
      },
      "nodeDrainConfig": {
        object ([NodeDrainConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodeDrainConfig))
      },
      "maintenancePolicy": {
        object ([NodePoolMaintenancePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodePoolMaintenancePolicy))
      },
      "kubeletCertInfo": {
        object ([KubeletCertInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.KubeletCertInfo))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the node pool.  
`config` |  `object (`[NodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/NodeConfig)`)` The node configuration of the pool.  
`initialNodeCount` |  `integer` The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota.  
`locations[]` |  `string` The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located.If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead.Warning: changing node pool locations will result in nodes being added and/or removed.  
`networkConfig` |  `object (`[NodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig)`)` Networking configuration for this NodePool. If specified, it overrides the cluster-level defaults.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`version` |  `string` The version of Kubernetes running on this NodePool's nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version).  
`instanceGroupUrls[]` |  `string` Output only. The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool. During the node pool blue-green upgrade operation, the URLs contain both blue and green resources.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.Status)`)` Output only. The status of the nodes in this pool instance.  
`statusMessage  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available.  
`autoscaling` |  `object (`[NodePoolAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling)`)` Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present.  
`management` |  `object (`[NodeManagement](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/NodeManagement)`)` NodeManagement configuration for this NodePool.  
`maxPodsConstraint` |  `object (`[MaxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/MaxPodsConstraint)`)` The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool.  
`conditions[]` |  `object (`[StatusCondition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/StatusCondition)`)` Which conditions caused the current node pool state.  
`podIpv4CidrSize` |  `integer` Output only. The pod CIDR block size per node in this node pool.  
`upgradeSettings` |  `object (`[UpgradeSettings](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/UpgradeSettings)`)` Upgrade settings control disruption and speed of the upgrade.  
`placementPolicy` |  `object (`[PlacementPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy)`)` Specifies the node placement policy.  
`updateInfo` |  `object (`[UpdateInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.UpdateInfo)`)` Output only. Update info contains relevant information during a node pool update.  
`etag` |  `string` This checksum is computed by the server based on the value of node pool fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding.  
`queuedProvisioning` |  `object (`[QueuedProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.QueuedProvisioning)`)` Specifies the configuration of queued provisioning.  
`bestEffortProvisioning` |  `object (`[BestEffortProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.BestEffortProvisioning)`)` Enable best effort provisioning for nodes  
`nodeDrainConfig` |  `object (`[NodeDrainConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodeDrainConfig)`)` Specifies the node drain configuration for this node pool.  
`maintenancePolicy` |  `object (`[NodePoolMaintenancePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.NodePoolMaintenancePolicy)`)` Optional. Specifies the maintenance policy for the node pool.  
`kubeletCertInfo` |  `object (`[KubeletCertInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool.KubeletCertInfo)`)` Output only. Contains expiry information about the kubelet certificate.  
  
## Methods  
  
---  
  
### `[autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/autoscaling)`

|  Sets the autoscaling settings of a specific node pool.  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/create)`

|  Creates a node pool for a cluster.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/delete)`

|  Deletes a node pool from a cluster.  
  
### `[fetchNodePoolUpgradeInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/fetchNodePoolUpgradeInfo)`

|  Fetch upgrade information of a specific node pool.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/get)`

|  Retrieves the requested node pool.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/list)`

|  Lists the node pools for a cluster.  
  
### `[rollback](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/rollback)`

|  Rolls back a previously Aborted or Failed NodePool upgrade.  
  
### `[setManagement](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/setManagement)`

|  Sets the NodeManagement options for a node pool.  
  
### `[setSize](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/setSize)`

|  SetNodePoolSizeRequest sets the size of a node pool.  
  
### `[update](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/update)`

|  Updates the version and/or image type of a specific node pool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
