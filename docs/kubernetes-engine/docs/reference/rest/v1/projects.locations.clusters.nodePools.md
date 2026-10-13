---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools
title: REST Resource: projects.locations.clusters.nodePools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:52.604837+00:00
---

# REST Resource: projects.locations.clusters.nodePools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.clusters.nodePools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NodePool
    * JSON representation
    * NodeNetworkConfig
      * JSON representation
    * NetworkPerformanceConfig
      * JSON representation
    * Tier
    * AdditionalNodeNetworkConfig
      * JSON representation
    * AdditionalPodNetworkConfig
      * JSON representation
    * Status
    * NodePoolAutoscaling
      * JSON representation
    * LocationPolicy
    * PlacementPolicy
      * JSON representation
    * Type
    * UpdateInfo
      * JSON representation
    * BlueGreenInfo
      * JSON representation
    * Phase
    * QueuedProvisioning
      * JSON representation
    * BestEffortProvisioning
      * JSON representation
    * NodeDrainConfig
      * JSON representation
    * NodePoolMaintenancePolicy
      * JSON representation
    * ExclusionUntilEndOfSupport
      * JSON representation
    * KubeletCertInfo
      * JSON representation
  * Methods



## Resource: NodePool

NodePool contains the name and configuration for a cluster's node pool. Node pools are a set of nodes (i.e. VM's), with a common configuration and specification, under the control of the cluster master. They may have a set of Kubernetes labels applied to them, which may be used to reference them during pod scheduling. They may also be resized up or down, to accommodate the workload.

JSON representation  
---  
      
    
    {
      "name": string,
      "config": {
        object ([NodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig))
      },
      "initialNodeCount": integer,
      "locations": [
        string
      ],
      "networkConfig": {
        object ([NodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig))
      },
      "selfLink": string,
      "version": string,
      "instanceGroupUrls": [
        string
      ],
      "status": enum ([Status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Status)),
      "statusMessage": string,
      "autoscaling": {
        object ([NodePoolAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling))
      },
      "management": {
        object ([NodeManagement](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeManagement))
      },
      "maxPodsConstraint": {
        object ([MaxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/MaxPodsConstraint))
      },
      "conditions": [
        {
          object ([StatusCondition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/StatusCondition))
        }
      ],
      "podIpv4CidrSize": integer,
      "upgradeSettings": {
        object ([UpgradeSettings](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeSettings))
      },
      "placementPolicy": {
        object ([PlacementPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy))
      },
      "updateInfo": {
        object ([UpdateInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.UpdateInfo))
      },
      "etag": string,
      "queuedProvisioning": {
        object ([QueuedProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.QueuedProvisioning))
      },
      "bestEffortProvisioning": {
        object ([BestEffortProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.BestEffortProvisioning))
      },
      "nodeDrainConfig": {
        object ([NodeDrainConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeDrainConfig))
      },
      "maintenancePolicy": {
        object ([NodePoolMaintenancePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolMaintenancePolicy))
      },
      "kubeletCertInfo": {
        object ([KubeletCertInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.KubeletCertInfo))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the node pool.  
`config` |  `object (`[NodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig)`)` The node configuration of the pool.  
`initialNodeCount` |  `integer` The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota.  
`locations[]` |  `string` The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located.If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead.Warning: changing node pool locations will result in nodes being added and/or removed.  
`networkConfig` |  `object (`[NodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig)`)` Networking configuration for this NodePool. If specified, it overrides the cluster-level defaults.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`version` |  `string` The version of Kubernetes running on this NodePool's nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version).  
`instanceGroupUrls[]` |  `string` Output only. The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool. During the node pool blue-green upgrade operation, the URLs contain both blue and green resources.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Status)`)` Output only. The status of the nodes in this pool instance.  
`statusMessage  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available.  
`autoscaling` |  `object (`[NodePoolAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling)`)` Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present.  
`management` |  `object (`[NodeManagement](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeManagement)`)` NodeManagement configuration for this NodePool.  
`maxPodsConstraint` |  `object (`[MaxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/MaxPodsConstraint)`)` The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool.  
`conditions[]` |  `object (`[StatusCondition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/StatusCondition)`)` Output only. Which conditions caused the current node pool state.  
`podIpv4CidrSize` |  `integer` Output only. The pod CIDR block size per node in this node pool.  
`upgradeSettings` |  `object (`[UpgradeSettings](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeSettings)`)` Upgrade settings control disruption and speed of the upgrade.  
`placementPolicy` |  `object (`[PlacementPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy)`)` Specifies the node placement policy.  
`updateInfo` |  `object (`[UpdateInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.UpdateInfo)`)` Output only. Update info contains relevant information during a node pool update.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of node pool fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding.  
`queuedProvisioning` |  `object (`[QueuedProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.QueuedProvisioning)`)` Specifies the configuration of queued provisioning.  
`bestEffortProvisioning` |  `object (`[BestEffortProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.BestEffortProvisioning)`)` Enable best effort provisioning for nodes  
`nodeDrainConfig` |  `object (`[NodeDrainConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeDrainConfig)`)` Specifies the node drain configuration for this node pool.  
`maintenancePolicy` |  `object (`[NodePoolMaintenancePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolMaintenancePolicy)`)` Optional. Specifies the maintenance policy for the node pool.  
`kubeletCertInfo` |  `object (`[KubeletCertInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.KubeletCertInfo)`)` Output only. Contains expiry information about the kubelet certificate.  
  
### NodeNetworkConfig

Parameters for node pool-level network config.

JSON representation  
---  
      
    
    {
      "createPodRange": boolean,
      "podRange": string,
      "podIpv4CidrBlock": string,
      "podCidrOverprovisionConfig": {
        object ([PodCIDROverprovisionConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/PodCIDROverprovisionConfig))
      },
      "additionalNodeNetworkConfigs": [
        {
          object ([AdditionalNodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.AdditionalNodeNetworkConfig))
        }
      ],
      "additionalPodNetworkConfigs": [
        {
          object ([AdditionalPodNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.AdditionalPodNetworkConfig))
        }
      ],
      "podIpv4RangeUtilization": number,
      "subnetwork": string,
      "networkTierConfig": {
        object ([NetworkTierConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NetworkTierConfig))
      },
      "acceleratorNetworkProfile": string,
      "enablePrivateNodes": boolean,
      "networkPerformanceConfig": {
        object ([NetworkPerformanceConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NetworkPerformanceConfig))
      }
    }  
  
Fields  
---  
`createPodRange` |  `boolean` Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for `podRange` and `podIpv4CidrBlock` if they are not specified.If neither `createPodRange` or `podRange` are specified, the cluster-level default (`ipAllocationPolicy.cluster_ipv4_cidr_block`) is used.Only applicable if `ipAllocationPolicy.use_ip_aliases` is true.This field cannot be changed after the node pool has been created.  
`podRange` |  `string` The ID of the secondary range for pod IPs. If `createPodRange` is true, this ID is used for the new range. If `createPodRange` is false, uses an existing secondary range with this ID.Only applicable if `ipAllocationPolicy.use_ip_aliases` is true.This field cannot be changed after the node pool has been created.  
`podIpv4CidrBlock` |  `string` The IP address range for pod IPs in this node pool.Only applicable if `createPodRange` is true.Set to blank to have a range chosen with the default size.Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask.Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) to pick a specific range to use.Only applicable if `ipAllocationPolicy.use_ip_aliases` is true.This field cannot be changed after the node pool has been created.  
`podCidrOverprovisionConfig` |  `object (`[PodCIDROverprovisionConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/PodCIDROverprovisionConfig)`)` [PRIVATE FIELD] Pod CIDR size overprovisioning config for the node pool.Pod CIDR size per node depends on maxPodsPerNode. By default, the value of maxPodsPerNode is rounded off to next power of 2 and we then double that to get the size of pod CIDR block per node. Example: maxPodsPerNode of 30 would result in 64 IPs (/26).This config can disable the doubling of IPs (we still round off to next power of 2) Example: maxPodsPerNode of 30 will result in 32 IPs (/27) when overprovisioning is disabled.  
`additionalNodeNetworkConfigs[]` |  `object (`[AdditionalNodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.AdditionalNodeNetworkConfig)`)` We specify the additional node networks for this node pool using this list. Each node network corresponds to an additional interface  
`additionalPodNetworkConfigs[]` |  `object (`[AdditionalPodNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.AdditionalPodNetworkConfig)`)` We specify the additional pod networks for this node pool using this list. Each pod network corresponds to an additional alias IP range for the node  
`podIpv4RangeUtilization` |  `number` Output only. The utilization of the IPv4 range for the pod. The ratio is Usage/[Total number of IPs in the secondary range], Usage=numNodes*numZones*podIPsPerNode.  
`subnetwork` |  `string` Optional. The subnetwork name/path for the node pool. Format: projects/{project}/regions/{region}/subnetworks/{subnetwork} If the cluster is associated with multiple subnetworks, the subnetwork can be either: - A user supplied subnetwork name during node pool creation (e.g., `my-subnet`). The name must be between 1 and 63 characters long, start with a letter, contain only letters, numbers, and hyphens, and end with a letter or a number. - A full subnetwork path during node pool creation, such as `projects/gke-project/regions/us-central1/subnetworks/my-subnet` \- A subnetwork path picked based on the IP utilization during node pool creation and is immutable.  
`networkTierConfig` |  `object (`[NetworkTierConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NetworkTierConfig)`)` Output only. The network tier configuration for the node pool inherits from the cluster-level configuration and remains immutable throughout the node pool's lifecycle, including during upgrades.  
`acceleratorNetworkProfile` |  `string` Immutable. The accelerator network profile for the node pool. For now the only valid value is "auto". If specified, the network configuration of the nodes in this node pool will be managed by this profile for the supported machine types, zone, etc.  
`enablePrivateNodes` |  `boolean` Whether nodes have internal IP addresses only. If enablePrivateNodes is not specified, then the value is derived from [Cluster.NetworkConfig.default_enable_private_nodes][]  
`networkPerformanceConfig` |  `object (`[NetworkPerformanceConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NetworkPerformanceConfig)`)` Network bandwidth tier configuration.  
  
### NetworkPerformanceConfig

Configuration of all network bandwidth tiers

JSON representation  
---  
      
    
    {
      "totalEgressBandwidthTier": enum ([Tier](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Tier))
    }  
  
Fields  
---  
`totalEgressBandwidthTier` |  `enum (`[Tier](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Tier)`)` Specifies the total network bandwidth tier for the NodePool.  
  
### Tier

Node network tier

Enums  
---  
`TIER_UNSPECIFIED` | Default value  
`TIER_1` | Higher bandwidth, actual values based on VM size.  
  
### AdditionalNodeNetworkConfig

AdditionalNodeNetworkConfig is the configuration for additional node networks within the NodeNetworkConfig message

JSON representation  
---  
      
    
    {
      "network": string,
      "subnetwork": string
    }  
  
Fields  
---  
`network` |  `string` Name of the VPC where the additional interface belongs  
`subnetwork` |  `string` Name of the subnetwork where the additional interface belongs  
  
### AdditionalPodNetworkConfig

AdditionalPodNetworkConfig is the configuration for additional pod networks within the NodeNetworkConfig message

JSON representation  
---  
      
    
    {
      "subnetwork": string,
      "secondaryPodRange": string,
      "maxPodsPerNode": {
        object ([MaxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/MaxPodsConstraint))
      }
    }  
  
Fields  
---  
`subnetwork` |  `string` Name of the subnetwork where the additional pod network belongs.  
`secondaryPodRange` |  `string` The name of the secondary range on the subnet which provides IP address for this pod range.  
`maxPodsPerNode` |  `object (`[MaxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/MaxPodsConstraint)`)` The maximum number of pods per node which use this pod network.  
  
### Status

The current status of the node pool instance.

Enums  
---  
`STATUS_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the node pool is being created.  
`RUNNING` | The RUNNING state indicates the node pool has been created and is fully usable.  
`RUNNING_WITH_ERROR` | The RUNNING_WITH_ERROR state indicates the node pool has been created and is partially usable. Some error state has occurred and some functionality may be impaired. Customer may need to reissue a request or trigger a new update.  
`RECONCILING` | The RECONCILING state indicates that some work is actively being done on the node pool, such as upgrading node software. Details can be found in the `statusMessage` field.  
`STOPPING` | The STOPPING state indicates the node pool is being deleted.  
`ERROR` | The ERROR state indicates the node pool may be unusable. Details can be found in the `statusMessage` field.  
  
### NodePoolAutoscaling

NodePoolAutoscaling contains information required by cluster autoscaler to adjust the size of the node pool to the current cluster usage.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "minNodeCount": integer,
      "maxNodeCount": integer,
      "autoprovisioned": boolean,
      "locationPolicy": enum ([LocationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.LocationPolicy)),
      "totalMinNodeCount": integer,
      "totalMaxNodeCount": integer
    }  
  
Fields  
---  
`enabled` |  `boolean` Is autoscaling enabled for this node pool.  
`minNodeCount` |  `integer` Minimum number of nodes for one location in the node pool. Must be greater than or equal to 0 and less than or equal to maxNodeCount.  
`maxNodeCount` |  `integer` Maximum number of nodes for one location in the node pool. Must be >= minNodeCount. There has to be enough quota to scale up the cluster.  
`autoprovisioned` |  `boolean` Can this node pool be deleted automatically.  
`locationPolicy` |  `enum (`[LocationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.LocationPolicy)`)` Location policy used when scaling up a node pool.  
`totalMinNodeCount` |  `integer` Minimum number of nodes in the node pool. Must be greater than or equal to 0 and less than or equal to totalMaxNodeCount. The total_*_node_count fields are mutually exclusive with the *_node_count fields.  
`totalMaxNodeCount` |  `integer` Maximum number of nodes in the node pool. Must be greater than or equal to totalMinNodeCount. There has to be enough quota to scale up the cluster. The total_*_node_count fields are mutually exclusive with the *_node_count fields.  
  
### LocationPolicy

Location policy specifies how zones are picked when scaling up the node pool.

Enums  
---  
`LOCATION_POLICY_UNSPECIFIED` | Not set.  
`BALANCED` | BALANCED is a best effort policy that aims to balance the sizes of different zones.  
`ANY` | ANY policy picks zones that have the highest capacity available.  
  
### PlacementPolicy

PlacementPolicy defines the placement policy used by the node pool.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Type)),
      "tpuTopology": string,
      "policyName": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Type)`)` The type of placement.  
`tpuTopology` |  `string` Optional. TPU placement topology for pod slice node pool. <https://cloud.google.com/tpu/docs/types-topologies#tpu_topologies>  
`policyName` |  `string` If set, refers to the name of a custom resource policy supplied by the user. The resource policy must be in the same project and region as the node pool. If not found, InvalidArgument error is returned.  
  
### Type

Type defines the type of placement policy.

Enums  
---  
`TYPE_UNSPECIFIED` | TYPE_UNSPECIFIED specifies no requirements on nodes placement.  
`COMPACT` | COMPACT specifies node placement in the same availability domain to ensure low communication latency.  
  
### UpdateInfo

UpdateInfo contains resource (instance groups, etc), status and other intermediate information relevant to a node pool upgrade.

JSON representation  
---  
      
    
    {
      "blueGreenInfo": {
        object ([BlueGreenInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.BlueGreenInfo))
      }
    }  
  
Fields  
---  
`blueGreenInfo` |  `object (`[BlueGreenInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.BlueGreenInfo)`)` Information of a blue-green upgrade.  
  
### BlueGreenInfo

Information relevant to blue-green upgrade.

JSON representation  
---  
      
    
    {
      "phase": enum ([Phase](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Phase)),
      "blueInstanceGroupUrls": [
        string
      ],
      "greenInstanceGroupUrls": [
        string
      ],
      "bluePoolDeletionStartTime": string,
      "greenPoolVersion": string
    }  
  
Fields  
---  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.Phase)`)` Current blue-green upgrade phase.  
`blueInstanceGroupUrls[]` |  `string` The resource URLs of the [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with blue pool.  
`greenInstanceGroupUrls[]` |  `string` The resource URLs of the [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with green pool.  
`bluePoolDeletionStartTime` |  `string` Time to start deleting blue pool to complete blue-green upgrade, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`greenPoolVersion` |  `string` Version of green pool.  
  
### Phase

Phase represents the different stages blue-green upgrade is running in.

Enums  
---  
`PHASE_UNSPECIFIED` | Unspecified phase.  
`UPDATE_STARTED` | blue-green upgrade has been initiated.  
`CREATING_GREEN_POOL` | Start creating green pool nodes.  
`CORDONING_BLUE_POOL` | Start cordoning blue pool nodes.  
`DRAINING_BLUE_POOL` | Start draining blue pool nodes.  
`NODE_POOL_SOAKING` | Start soaking time after draining entire blue pool.  
`DELETING_BLUE_POOL` | Start deleting blue nodes.  
`ROLLBACK_STARTED` | Rollback has been initiated.  
  
### QueuedProvisioning

QueuedProvisioning defines the queued provisioning used by the node pool.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Denotes that this node pool is QRM specific, meaning nodes can be only obtained through queuing via the Cluster Autoscaler ProvisioningRequest API.  
  
### BestEffortProvisioning

Best effort provisioning.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "minProvisionNodes": integer
    }  
  
Fields  
---  
`enabled` |  `boolean` When this is enabled, cluster/node pool creations will ignore non-fatal errors like stockout to best provision as many nodes as possible right now and eventually bring up all target number of nodes  
`minProvisionNodes` |  `integer` Minimum number of nodes to be provisioned to be considered as succeeded, and the rest of nodes will be provisioned gradually and eventually when stockout issue has been resolved.  
  
### NodeDrainConfig

NodeDrainConfig contains the node drain related configurations for this node pool.

JSON representation  
---  
      
    
    {
      "pdbTimeoutDuration": string,
      "graceTerminationDuration": string,
      "respectPdbDuringNodePoolDeletion": boolean
    }  
  
Fields  
---  
`pdbTimeoutDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration of the PDB timeout period for node drain.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`graceTerminationDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration of the grace termination period for node drain.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`respectPdbDuringNodePoolDeletion` |  `boolean` Whether to respect PDB during node pool deletion.  
  
### NodePoolMaintenancePolicy

Defines the maintenance policy for the node pool.

JSON representation  
---  
      
    
    {
      "exclusionUntilEndOfSupport": {
        object ([ExclusionUntilEndOfSupport](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.ExclusionUntilEndOfSupport))
      }
    }  
  
Fields  
---  
`exclusionUntilEndOfSupport` |  `object (`[ExclusionUntilEndOfSupport](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.ExclusionUntilEndOfSupport)`)` Optional. The exclusion until end of support for the node pool.  
  
### ExclusionUntilEndOfSupport

Defines the maintenance exclusion for the node pool.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Indicates whether the exclusion is enabled.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the maintenance exclusion. It is output only. It is the exclusion creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the maintenance exclusion. It is output only. It is the cluster control plane version's end of support time, or end of extended support time when the cluster is on extended support channel.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### KubeletCertInfo

Contains expiry information about the kubelet certificate.

JSON representation  
---  
      
    
    {
      "tpmBootstrapCertExpireTime": string,
      "nonTpmBootstrapCertExpireTime": string
    }  
  
Fields  
---  
`tpmBootstrapCertExpireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nonTpmBootstrapCertExpireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[completeUpgrade](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/completeUpgrade)`

|  CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete.  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/create)`

|  Creates a node pool for a cluster.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/delete)`

|  Deletes a node pool from a cluster.  
  
### `[fetchNodePoolUpgradeInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/fetchNodePoolUpgradeInfo)`

|  Fetch upgrade information of a specific node pool.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/get)`

|  Retrieves the requested node pool.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/list)`

|  Lists the node pools for a cluster.  
  
### `[rollback](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/rollback)`

|  Rolls back a previously Aborted or Failed NodePool upgrade.  
  
### `[setAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setAutoscaling)`

|  Sets the autoscaling settings for the specified node pool.  
  
### `[setManagement](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setManagement)`

|  Sets the NodeManagement options for a node pool.  
  
### `[setSize](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setSize)`

|  Sets the size for a specific node pool.  
  
### `[update](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/update)`

|  Updates the version and/or image type for the specified node pool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
