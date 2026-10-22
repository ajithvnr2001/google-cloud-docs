---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/cluster/v1/cluster-v1/
title: KRM API cluster.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:11.021436+00:00
---

# KRM API cluster.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/cluster/v1/cluster-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API cluster.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## cluster.gdc.goog/v1

Contains API Schema definitions for the Cluster group.

### AcceleratorConfig

_Appears in:_ \- NodePool

Field | Description  
---|---  
`gpuPartitionScheme` _string_ | GPUPartitionScheme indicates the scheme that will be used to partition the GPUs into MIGs. This scheme and GPU DeviceModel jointly decide the MIG profiles. For example, mixed-1 on H100L 94GB together determines GPU to be partitioned into one 4g.47gb and one 3g.47gb.  
  
### Channel

_Underlying type:_ `string` Indicates a specific type of release channel.

_Appears in:_ \- ReleaseChannel

### Cluster

Specifies a GDC user cluster in an air-gapped configuration.

_Appears in:_ \- ClusterList

Field | Description  
---|---  
`apiVersion` _string_ | `cluster.gdc.goog/v1`  
`kind` _string_ | `Cluster`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterSpec_ |   
`status` _ClusterStatus_ |   
  
### ClusterList

Represents a collection of clusters.

Field | Description  
---|---  
`apiVersion` _string_ | `cluster.gdc.goog/v1`  
`kind` _string_ | `ClusterList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Cluster array_ |   
  
### ClusterNetwork

Specifies the cluster network configuration.

_Appears in:_ \- ClusterSpec

Field | Description  
---|---  
`podCIDRSize` _integer_ | The size of network ranges from which pod virtual IP addresses are allocated. If unset, a default value `21` is used.  
`serviceCIDRSize` _integer_ | The size of network ranges from which service virtual IP addresses are allocated. If unset, a default value `23` is used.  
  
### ClusterSpec

_Appears in:_ \- Cluster

Field | Description  
---|---  
`initialVersion` _ClusterVersion_ | The GDC air-gapped version information of the user cluster during cluster creation. Optional. Default to use the latest applicable version. Immutable.  
`releaseChannel` _ReleaseChannel_ | The release channel a cluster is subscribed to. When a cluster is subscribed to a release channel, GDC maintains the cluster versions for users. Optional. Mutable.  
`clusterNetwork` _ClusterNetwork_ | The cluster network configuration. If unset, the default configurations with pod and service CIDR sizes are used. Optional. Mutable.  
`loadBalancer` _LoadBalancer_ | The load balancer configuration. If unset, the default configuration with the ingress service IP address size is used. Optional. Mutable.  
`nodePools` _NodePool array_ | The list of node pools for the cluster worker nodes. Optional. Mutable.  
`nodePoolDefaults` _NodePoolDefaults_ | The cluster level configuration for all node pools. Optional. Mutable.  
  
### ClusterState

_Underlying type:_ `string` Indicates the state of the cluster.

_Appears in:_ \- ClusterStatus

### ClusterStatus

Defines the observed state of the cluster.

_Appears in:_ \- Cluster

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The latest observations of the cluster state. Conditions such as `Reconciling` and `Stalled` indicate whether the last cluster reconciliation succeeded.  
`errorStatus` _ErrorStatus_ | The observed error status of the cluster.  
`workerNodePoolStatuses` _NodePoolStatus array_ | A list of observed statuses of the worker node pools.  
`controlPlaneConditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Whether the control plane is ready.  
`componentsConditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Whether the user cluster components have successfully deployed.  
`versionStatus` _VersionStatus_ | The installed version information of the cluster.  
`clusterState` _ClusterState_ | The state of the cluster. The following states are available: 

  * `Running`: the cluster has been created and is usable.
  * `Reconciling`: some work is actively being done on the cluster.
  * `Deleting`: the cluster is being deleted.
  * `Error`: some errors occurred while reconciling/provisioning the cluster.

  
`subnets` _SubnetReference array_ | Subnets holds the list of subnets that are used for this cluster.  
  
### ClusterVersion

Specifies the version information of a GDC user cluster in an air-gapped configuration.

_Appears in:_ \- ClusterSpec

Field | Description  
---|---  
`kubernetesVersion` _string_ | The Kubernetes version of the GDC user cluster.  
  
### ContainerdConfig

_Appears in:_ \- NodeConfigDefaults

Field | Description  
---|---  
`privateRegistries` _PrivateRegistry array_ | Specifies private registries used to pull images on the node. Containerd is the only container runtime supported.  
  
### LoadBalancer

Specifies the load balancer configuration.

_Appears in:_ \- ClusterSpec

Field | Description  
---|---  
`ingressServiceIPSize` _integer_ | The size of non-overlapping IP pools used by the load balancer typed services. If unset, a default value `20` is used.  
  
### NodeConfigDefaults

_Appears in:_ \- NodePoolDefaults

Field | Description  
---|---  
`containerdConfig` _ContainerdConfig_ | Specifies the containerd config for all node. Optional. Mutable.  
  
### NodePool

Specifies the `NodePool` custom resource configuration.

_Appears in:_ \- ClusterSpec

Field | Description  
---|---  
`name` _string_ | The name of the node pool.  
`nodeCount` _integer_ | The desired number of nodes in the provisioned node pool.  
`machineTypeName` _string_ | The name of the machine types that are used to provision nodes.  
`taints` _[Taint](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#taint-v1-core) array_ | The taints assigned to the nodes of this node pool.  
`labels` _object (keys:string, values:string)_ | The labels assigned to nodes of this node pool. It contains a list of key/value pairs.  
`acceleratorOptions` _AcceleratorConfig_ | AcceleratorOptions indicates the desired configuration of accelerators within the NodePool. It's only valid if the chosen MachineType contains accelerators.  
  
### NodePoolDefaults

_Appears in:_ \- ClusterSpec

Field | Description  
---|---  
`nodeConfigDefaults` _NodeConfigDefaults_ | The cluster level configuration for all nodes. Optional. Mutable.  
  
### NodePoolStatus

Defines the observed state of a `NodePool` resource.

_Appears in:_ \- ClusterStatus

Field | Description  
---|---  
`name` _string_ | The name of the node pool.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The latest observations of the node pool's state.  
`readyNodes` _integer_ | The number of nodes that are ready to serve.  
`reconcilingNodes` _integer_ | The number of nodes that are reconciling.  
`stalledNodes` _integer_ | The number of nodes that are stalled.  
`unknownNodes` _integer_ | The number of nodes whose statuses are unknown.  
`readyTimestamp` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time a node pool is in `ready` status. This value will never change once it's set.  
`kubernetesVersion` _string_ | The version of Kubernetes running on this node pool's nodes.  
  
### PrivateRegistry

_Appears in:_ \- ContainerdConfig

Field | Description  
---|---  
`host` _string_ | Specifies the private registry host. This must consist of the host or host:port.  
`caCertSecretRef` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | Specifies the secret that stores the private registry's CA bundle. The secret must be either in the cluster namespace, or have the annotation `baremetal.cluster.gke.io/mark-source` so it can be forwarded to the cluster namespace.  
`pullCredentialSecretRef` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | Specifies the secret for the private registry access credential. The secret must be either in the cluster namespace, or have the annotation `baremetal.cluster.gke.io/mark-source` so it can be forwarded to the cluster namespace.  
  
### ReleaseChannel

Indicates which release channel a cluster is subscribed to.

_Appears in:_ \- ClusterSpec

Field | Description  
---|---  
`channel` _Channel_ | If unset, defaults to be `UNSPECIFIED`.  
  
### SubnetReference

SubnetReference holds the reference to a subnet.

_Appears in:_ \- ClusterStatus

Field | Description  
---|---  
`name` _string_ |   
`namespace` _string_ |   
  
### UpgradePhaseConfig

_Appears in:_ \- UserClusterUpgradeRequestSpec

Field | Description  
---|---  
`maxConcurrency` _integer_ | Maximum number of elements to upgrade concurrently. -1 to specify all remaining.  
`completionThreshold` _integer_ | Percent success for considering this group of node pools as completed.  
  
### UpgradeStepStatus

_Appears in:_ \- UserClusterUpgradeRequestStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observed status of the upgrade step.  
`phase` _integer_ | Phase tracks the index of the current phase.  
`phaseBatchNames` _string array_ | PhaseBatchNames lists NodeUpgrade CR names being processed or completed.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | StartTime represents the start time of the upgrade step.  
  
### UserClusterUpgradeRequest

Represents the configuration of a user cluster upgrade request, such as the cluster reference and the target Kubernetes version.

_Appears in:_ \- UserClusterUpgradeRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `cluster.gdc.goog/v1`  
`kind` _string_ | `UserClusterUpgradeRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _UserClusterUpgradeRequestSpec_ |   
`status` _UserClusterUpgradeRequestStatus_ |   
  
### UserClusterUpgradeRequestList

Represents a collection of `UserClusterUpgradeRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `cluster.gdc.goog/v1`  
`kind` _string_ | `UserClusterUpgradeRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _UserClusterUpgradeRequest array_ |   
  
### UserClusterUpgradeRequestSpec

Provides the specification, such as the desired state, of a `UserClusterUpgradeRequest` resource.

_Appears in:_ \- UserClusterUpgradeRequest

Field | Description  
---|---  
`clusterRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | A reference to the GDC user cluster object to which the upgrade applies.  
`targetVersion` _string_ | The target Kubernetes user cluster version.  
`nodePoolUpgradePhases` _UpgradePhaseConfig array_ | Schema for parallelization of node upgrades  
`concurrentUpgrades` _boolean_ | Toggle for concurrent worker node pool ABM upgrades True upgrades all worker node pools together, False upgrades one at a time.  
`disruption` _NodeUpgradeDisruption_ | Disruption defines the disruption level for node upgrades. If this field is not set, patch upgrades default to executing without draining workloads (NoDisruption). Setting this field to "RequiresWorkloadDrain" overrides that default behavior, forcing the system to perform a standard drain process on the nodes. Note: This field is ignored for minor version upgrades, which always require workload drain.  
  
### UserClusterUpgradeRequestStatus

_Appears in:_ \- UserClusterUpgradeRequest

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The current upgrade state. Known condition types: Succeeded.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The observed start time for the current upgrade.  
`cluster` _UpgradeStepStatus_ | Cluster represents the observed cluster upgrade status.  
`node` _UpgradeStepStatus_ | Node represents the observed Node upgrade status for cluster nodes.  
  
### VersionStatus

Defines the installed version information of the cluster.

_Appears in:_ \- ClusterStatus

Field | Description  
---|---  
`componentVersion` _string_ | The component version of the cluster.  
`kubernetesVersion` _string_ | The Kubernetes version of the cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
